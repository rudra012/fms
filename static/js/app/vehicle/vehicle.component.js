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


            Vehicle.getVehicleStatusList().success(function(response){
                $scope.vehicleStatusData = response.vehicle_status;
            }).error(function(e_data, e_status, e_headers, e_config){
            });

            Vehicle.getVehicleList().success(function(response){
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