'use strict';

//var vehicleApp=angular.module('vehicles');


vehicleApp.factory("Vehicle", ['$http',function($http){
    var obj = {};

    obj.getVehicleList = function(){
        return $http.get('/api/v1/vehicle/');
    }

    obj.addVehicle = function(data){
         var req = {
             method: 'POST',
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


            Vehicle.getVehicleList().success(function(response){
                $scope.vehicleData = response.Vehicle;
            }).error(function(e_data, e_status, e_headers, e_config){
            });




        }
})



vehicleAdd.component('vehicleAdd', {
        templateUrl: '/djangotemplates/private/vehicle/form.html',
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


            $scope.vehicle={};

            $scope.doAddVehicle=function(vehicle)
            {

            Vehicle.addVehicle(vehicle).success(function(response){


            }).error(function(e_data, e_status, e_headers, e_config){
            });



            }




        }
})