'use strict';
mainApp.factory("Fuel", ['$http',function($http){

    var obj = {};

    obj.getFuelList = function(){
         var req = {
             method: 'GET',
             url: '/api/v1/fuel/',
         }
        return $http(req);
    }

    obj.addFuel = function(data){
         var req = {
             method: 'POST',
             url: '/api/v1/fuel/',
             data: data
        }
        return $http(req);
    }
    obj.updateFuel = function(data){
         var req = {
             method: 'PUT',
             url: '/api/v1/fuel/',
             data: data
        }
        return $http(req);
    }

    return obj;

}]);

angular.module('fuel', []).
    component('fuel', {
        templateUrl: '/djangotemplates/private/fuel/list.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $scope,
                Flash,
                $animate,
                $timeout,
                $rootScope,
                Fuel
            ){



//            $scope.checkCount=0;
//            $scope.deletingIds=[];
//
//            $scope.subCheck=function(select,id)
//            {
//
//                if(select){
//                    $scope.deletingIds.push(id);
//                    $scope.checkCount += 1
//                }else{
//                    $scope.deletingIds.pop(id);
//                    $scope.checkCount -=1
//                }
//                if($scope.checkCount==$scope.groupData.length)
//                    $scope.selectedAllGroup=true
//                else
//                    $scope.selectedAllGroup=false
//            }
//            $scope.allCheckChange=function(select)
//            {
//                 $scope.deletingIds=[];
//                 angular.forEach($scope.groupData, function (item) {
//                     item.select = select;
//                     if(select)
//                     {
//                        $scope.deletingIds.push(item.id)
//                        $scope.checkCount=$scope.groupData.length;
//                     }
//                     else
//                        $scope.checkCount=0;
//                });
//            }


            Fuel.getFuelList().success(function(response){

                $scope.total=response.total;
                $scope.has_next=response.has_next;
                $scope.has_previous=response.has_previous;
                $scope.previous_page_number=response.previous_page_number;
                $scope.pages=response.pages;
                $scope.next_page_number=response.next_page_number;
                $scope.fuelData = response.Fuel;
            }).error(function(e_data, e_status, e_headers, e_config){
            });



//            $scope.doAddGroup=function(group)
//            {
//
//                $scope.GroupForm.$setPristine();
//
//                var addElement=angular.copy(group);
//
//                Group.addGroup(group).success(function(response){
//                if(response.Group)
//                    response.Group.new=true
//
//                if(response.Group)
//                    $scope.groupData.splice(0, 0, response.Group);
//
//                }).error(function(e_data, e_status, e_headers, e_config){
//                });
//                $scope.group=null;
//            }




        }
})


angular.module('fuelAdd').component('fuelAdd', {
        templateUrl: '/djangotemplates/private/fuel/form.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                $tooltip,
                $stateParams,
                Fuel,
                Vehicle

            ){



            Vehicle.getVehicleList().success(function(response){
                $scope.vehicleData = response.Vehicle;
            }).error(function(e_data, e_status, e_headers, e_config){
            });




            if(!$stateParams.id)
                $scope.job={};
            else
            {
                $scope.updateJob=true;
                Job.getJobDetail($stateParams.id).success(function(response){
                    console.log(response);
                    console.log(response);
                    if(response && response.Job && response.Job[0])
                        $scope.job=response.Job[0];

                }).error(function(e_data, e_status, e_headers, e_config){
                   Flash.create("error",e_data.message,0);
                });


            }


            $scope.doAddFule=function(fuel,valid){

                if(valid)
                    console.log(fuel);

            }


//            $scope.doAddJob =function(job,valid){
//                Flash.clear();
//                if(valid){
//                    if(!job.id){
//
//                        Job.addJob(job).success(function(response){
//                            $location.path("/jobs")
//                        }).error(function(e_data, e_status, e_headers, e_config){
//                           Flash.create("error",e_data.message,0);
//                        });
//                    }else{
//
//                        Job.updateJob(job).success(function(response){
//                            $location.path("/jobs")
//                        }).error(function(e_data, e_status, e_headers, e_config){
//                           Flash.create("error",e_data.message,0);
//                        });
//                    }
//                }
//
//
//            }



        }
})