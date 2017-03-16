'use strict';


userApp.factory("User", ['$http',function($http){
    var obj = {};

    obj.getUserList = function(){
        return $http.get('/api/v1/user/');
    }

    obj.addUser = function(data){
         var req = {
             method: 'POST',
             url: '/api/v1/user/',
             data: data
        }

        return $http(req);
    }

    obj.updateUser = function(data){
         var req = {
             method: 'PUT',
             url: '/api/v1/user/',
             data: data
        }
        return $http(req);
    }

    obj.getUserDetail = function(data){
         var req = {
             method: 'GET',
             url: '/api/v1/user/',
             params: {
                id: data,
              }

        }
        return $http(req);
    }


 return obj;
}]);

userApp.
    component('users', {
        templateUrl: '/djangotemplates/private/users/list.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                User,
                $timeout,
                Group,
                $tooltip
            ){

            User.getUserList().success(function(response){
                $scope.userData = response.User;
            }).error(function(e_data, e_status, e_headers, e_config){
            });


        }
})



userAdd.component('usersAdd', {
        templateUrl: '/djangotemplates/private/users/form.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                User,
                Group,
                $tooltip,
                ngToast,
                $stateParams

            ){

            $scope.tooltip = {title: 'Hello Tooltip<br />This is a multiline message!', checked: false};

            Group.getGroupList().success(function(response){
                $scope.groupData = response.Group;
            }).error(function(e_data, e_status, e_headers, e_config){
            });

            if(!$stateParams.id)
            {
                $scope.user={};
            }
            else
            {
                $scope.updateContact=true;
                User.getUserDetail($stateParams.id).success(function(response){
                console.log(response.User)
                $scope.user=response.User[0];
                }).error(function(e_data, e_status, e_headers, e_config){
                   Flash.create("error",e_data.message,0);
                });

            }


            $scope.doAddUser=function(user,valid)
            {

                console.log(user.id);

                if(valid)
                {
                    if(!user.id)
                    {
                        User.addUser(user).success(function(response){
                        $location.path("/contacts")
                        }).error(function(e_data, e_status, e_headers, e_config){
                           Flash.create("error",e_data.message,0);
                        });
                    }
                    else
                    {
                        User.updateUser(user).success(function(response){
                            $location.path("/contacts")
                        }).error(function(e_data, e_status, e_headers, e_config){
                           Flash.create("error",e_data.message,0);
                        });
                    }

                }

            }


        }
})