'use strict';

//var vehicleApp=angular.module('vehicles');


vehicleApp.factory("Group", ['$http',function($http){
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

vehicleApp.
    component('group', {
        templateUrl: '/djangotemplates/private/group/list.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                Group,
                $timeout
            ){


            Group.getCompanyList().success(function(response){
                $scope.companyData = response.Company;
            }).error(function(e_data, e_status, e_headers, e_config){
            });

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



vehicleAdd.component('groupAdd', {
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

            $scope.doAddVehicle=function(group)
            {

            Vehicle.addGroup(group).success(function(response){


            }).error(function(e_data, e_status, e_headers, e_config){
            });



            }




        }
})