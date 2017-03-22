'use strict';

mainApp.factory("Vender", ['$http',function($http){
    var obj = {};

    obj.getVendorList = function(data){
        var req = {
             method: 'GET',
             url: '/api/v1/user/',
             params: {
                type: data,
             }
        }
        return $http(req);

    }

    obj.addVendor = function(data){
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

vendorApp.
    component('vendors', {
        templateUrl: '/djangotemplates/private/vendor/list.html',
        controller: function(
                $cookies,$http,$location,$rootScope,$scope,
                Flash,$animate,Vender,$timeout,Group,$tooltip
            ){


//            Vender.getVendorList().success(function(response){
//                $scope.venderData = response.User;
//            }).error(function(e_data, e_status, e_headers, e_config){
//            });


            Vender.getVendorList('v').success(function(response){
                $scope.vendorData = response.User;
            }).error(function(e_data, e_status, e_headers, e_config){
               Flash.create("error",e_data.message,0);
            });


            $scope.deletVendor=function(user,index){
                user.is_deleted=true;

                Vender.updateUser(user).success(function(response){

                    if(response.code==200)
                        $scope.vendorData.splice(index, 1);

                }).error(function(e_data, e_status, e_headers, e_config){
                });
            }


        }
})



vendorAdd.component('vendorAdd', {
        templateUrl: '/djangotemplates/private/vendor/form.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                Vender,
                Group,
                $tooltip,
                ngToast,
                $stateParams

            ){

            //$scope.tooltip = {title: 'Hello Tooltip<br />This is a multiline message!', checked: false};
//            Group.getGroupList().success(function(response){
//                $scope.groupData = response.Group;
//            }).error(function(e_data, e_status, e_headers, e_config){
//            });


            if(!$stateParams.id)
            {
                $scope.vendor={
                    'user_type':'v',
                };
            }
            else
            {
                $scope.updateContact=true;
                Vender.getUserDetail($stateParams.id).success(function(response){
                    if(response && response.User && response.User[0])
                        $scope.vendor=response.User[0];
                    else
                        $location.path('/vendors')
                }).error(function(e_data, e_status, e_headers, e_config){
                   Flash.create("error",e_data.message,0);
                });


            }


            $scope.doAddVendor=function(vendor,valid){

                console.log(vendor);
                console.log(valid);

                if(valid){

                    if(!vendor.id){

                        Vender.addVendor(vendor).success(function(response){
                            $location.path("/vendors")
                        }).error(function(e_data, e_status, e_headers, e_config){
                           Flash.create("error",e_data.message);
                        });
                    }else{
                        Vender.updateUser(vendor).success(function(response){
                            $location.path("/vendors")
                        }).error(function(e_data, e_status, e_headers, e_config){
                           Flash.create("error",e_data.message,0);
                        });
                    }
                }
            }




        }
})