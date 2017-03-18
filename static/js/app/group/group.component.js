'use strict';

//var groupApp=angular.module('vehicles');


mainApp.factory("Group", ['$http',function($http){
    var obj = {};

    obj.getGroupList = function(){
        return $http.get('/api/v1/group/');
    }

    obj.getCompanyList = function(){
        return $http.get('/api/v1/company/');
    }

    obj.addGroup = function(data){
         var req = {
             method: 'POST',
             url: '/api/v1/group/',
             data: data
        }

        return $http(req);
    }

    obj.updateGroup = function(data){
         var req = {
             method: 'PUT',
             url: '/api/v1/group/',
             data: data
        }

        return $http(req);
    }

 return obj;
}]);


angular.module('group', []).
    component('group', {
        templateUrl: '/djangotemplates/private/group/list.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $scope,
                Flash,
                $animate,
                Group,
                $timeout,
                $rootScope
            ){


            $scope.checkCount=0;

            $scope.subCheck=function(select)
            {

                if(select)
                  $scope.checkCount += 1
                else
                    $scope.checkCount -=1

                if($scope.checkCount==$scope.groupData.length)
                    $scope.selectedAllGroup=true
                else
                    $scope.selectedAllGroup=false

            }

            $scope.allCheckChange=function(select)
            {

                angular.forEach($scope.groupData, function (item) {
                     item.select = select;
                });

            }


            Group.getGroupList().success(function(response){
                $scope.groupData = response.Group;
            }).error(function(e_data, e_status, e_headers, e_config){
            });

            $scope.updateClick=function(data,index){
                data.edit=true;
            }

            $scope.done=function(data,index){

                if(data.group_name)
                {
                    data.edit=false;
                    data.new=true;
                    Group.updateGroup(data).success(function(response){
                    }).error(function(e_data, e_status, e_headers, e_config){
                    });

                    $timeout(function(){
                        data.new=false;
                     } ,1000);

                }
            }

            $scope.doAddGroup=function(group)
            {

                $scope.GroupForm.$setPristine();

                var addElement=angular.copy(group);

                Group.addGroup(group).success(function(response){
                if(response.Group)
                    response.Group.new=true

                if(response.Group)
                    $scope.groupData.splice(0, 0, response.Group);

                }).error(function(e_data, e_status, e_headers, e_config){
                });
                $scope.group=null;
            }

            $scope.addOpen=function()
            {

                $scope.GroupForm.$setPristine();

                if(!$scope.open)
                    $scope.open=true;
                else
                    $scope.open=false;
            }
            $scope.deletGroup=function(group,index)
            {
                var delGroup=angular.copy(group);
                delGroup.is_deleted="Y";
                Group.updateGroup(delGroup).success(function(response){
                    if(response.code==200)
                        $scope.groupData.splice(index, 1);
                }).error(function(e_data, e_status, e_headers, e_config){
                });
            }

        }
})






groupAdd.component('groupAdd', {
        templateUrl: '/djangotemplates/private/group/form.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                Group

            ){


            $scope.vehicle={};

            $scope.doAddVehicle=function(group){

                Vehicle.addGroup(group).success(function(response){
                }).error(function(e_data, e_status, e_headers, e_config){
                });
            }




        }
})