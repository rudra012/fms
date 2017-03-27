'use strict';

//var vehicleApp=angular.module('vehicles');


vehicleApp.factory("Vehicle", ['$http',function($http){
    var obj = {};

    obj.getVehicleList = function(){
        return $http.get('/api/v1/vehicle/');
    }

    obj.getVehicleStatusList = function(){
        return $http.get('/api/v1/vehiclestatus/');
    }

    obj.addVehicle = function(data){
         var req = {
             method: 'POST',
             url: '/api/v1/vehicle/',
             data: data
        }

        return $http(req);
    }


    obj.getVehicleDetail = function(data){
         var req = {
             method: 'GET',
             url: '/api/v1/vehicle/',
             params: {
                id: data,
              }
        }
        return $http(req);
    }

    obj.updateVehicles=function(data){
        var req = {
             method: 'PUT',
             url: '/api/v1/vehicle/',
             data: data
        }
        return $http(req);
    }





 return obj;
}]);

vehicleApp.
    component('vehicles', {
        templateUrl: '/djangotemplates/private/vehicle/list.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                Vehicle
            ){



            $scope.checkCount=0;
            $scope.deletingIds=[];
            $scope.subCheck=function(select,id){

                if(select){
                    $scope.deletingIds.push(id);
                    $scope.checkCount += 1
                }else{
                    $scope.deletingIds.pop(id);
                    $scope.checkCount -=1
                }
                if($scope.checkCount==$scope.vehicleData.length)
                    $scope.selectedAllVehicle=true
                else
                    $scope.selectedAllVehicle=false

            }
            $scope.allCheckChange=function(select){
                 $scope.deletingIds=[];
                 angular.forEach($scope.vehicleData, function (item) {
                     item.select = select;
                     if(select)
                     {
                        $scope.deletingIds.push(item.id)
                        $scope.checkCount=$scope.vehicleData.length;
                     }
                     else
                        $scope.checkCount=0;
                });
            }


            Vehicle.getVehicleStatusList().success(function(response){
                $scope.vehicleStatusData = response.vehicle_status;
            }).error(function(e_data, e_status, e_headers, e_config){
            });

            Vehicle.getVehicleList().success(function(response){
                $scope.total=response.total;
                $scope.has_next=response.has_next;
                $scope.has_previous=response.has_previous;
                $scope.previous_page_number=response.previous_page_number;
                $scope.pages=response.pages;
                $scope.next_page_number=response.next_page_number;
                $scope.vehicleData = response.Vehicle;
            }).error(function(e_data, e_status, e_headers, e_config){
            });


            $scope.deletVehicle=function(vehicle,index){
                    vehicle.is_deleted=true;
                Vehicle.updateVehicles(vehicle).success(function(response){
                    if(response.code==200)
                        $scope.vehicleData.splice(index, 1);
                }).error(function(e_data, e_status, e_headers, e_config){
                   Flash.create("error",e_data.message,0);
                });
            }

        }
})


vehicleAdd.component('vehicleAdd', {
        templateUrl: '/djangotemplates/private/vehicle/form.html',
        controller: function(
                $cookies,$http,$location,$rootScope,$scope,
                Flash,$animate,Vehicle,Group,$stateParams
            ){


            Vehicle.getVehicleStatusList().success(function(response){
                $scope.vehicleStatusData = response.vehicle_status;
            }).error(function(e_data, e_status, e_headers, e_config){
            });

            Group.getGroupList().success(function(response){
                $scope.groupData = response.Group;
            }).error(function(e_data, e_status, e_headers, e_config){
            });

            if(!$stateParams.id)
            {
                $scope.vehicle={};
            }
            else
            {
                $scope.updateVehicle=true;
                Vehicle.getVehicleDetail($stateParams.id).success(function(response){
                    $scope.vehicle=response.Vehicle[0];

                }).error(function(e_data, e_status, e_headers, e_config){
                    Flash.create("error",e_data.message,0);
                });

            }




            $scope.doAddVehicle=function(vehicle,valid)
            {
                console.log(vehicle)
                if(valid)
                {
                    if(!vehicle.id){
                        Vehicle.addVehicle(vehicle).success(function(response){
                            console.log(response.code)
                            $location.path("/vehicles")
                        }).error(function(e_data, e_status, e_headers, e_config){
                            //Flash.create("error",e_data.message,0);
                        });
                    }else{
                        Vehicle.updateVehicles(vehicle).success(function(response){
                            $location.path("/vehicles")
                        }).error(function(e_data, e_status, e_headers, e_config){
                           Flash.create("error",e_data.message,0);
                        });
                    }


                }
            }





        }
})