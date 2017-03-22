'use strict';

mainApp.factory("Job", ['$http',function($http){

    var obj = {};

    obj.getJobList = function(){
        return $http.get('/api/v1/jobs/');
    }

    obj.addJob = function(data){
         var req = {
             method: 'POST',
             url: '/api/v1/jobs/',
             data: data
        }

        return $http(req);
    }

    obj.updateJob = function(data){
         var req = {
             method: 'PUT',
             url: '/api/v1/jobs/',
             data: data
        }
        return $http(req);
    }

    obj.getJobDetail = function(data){
         var req = {
             method: 'GET',
             url: '/api/v1/jobs/',
             params: {
                id: data,
              }
        }
        return $http(req);

    }



 return obj;
}]);


angular.module('jobs', []).
    component('jobs', {
        templateUrl: '/djangotemplates/private/jobs/list.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $scope,
                Flash,
                $animate,
                Job,
                $timeout,
                $rootScope
            ){


//            $scope.$on("loadMoreGroups", function(ev) {
//
//            if($scope.has_next && !$scope.loadMoreInitiale){
//                    $scope.loadMoreInitiale=true;
//                    Group.loadMoreGroup($scope.next_page_number).success(function(response){
//                        $timeout(function(){
//                            $scope.total=response.total;
//                            $scope.has_next=response.has_next;
//                            $scope.has_previous=response.has_previous;
//                            $scope.previous_page_number=response.previous_page_number;
//                            $scope.pages=response.pages;
//                            $scope.next_page_number=response.next_page_number;
//                            $scope.groupData = $scope.groupData.concat(response.Group);
//                            $scope.loadMoreInitiale=false;
//
//                        } ,1500)
//                    }).error(function(e_data, e_status, e_headers, e_config){
//                    });
//                }
//
//
//            })



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
//
//
//            }
//
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



            Job.getJobList().success(function(response){
//                $scope.total=response.total;
//                $scope.has_next=response.has_next;
//                $scope.has_previous=response.has_previous;
//                $scope.previous_page_number=response.previous_page_number;
//                $scope.pages=response.pages;
//                $scope.next_page_number=response.next_page_number;


                  $scope.JobData = response.Job;


            }).error(function(e_data, e_status, e_headers, e_config){
            });

        }
})



jobAdd.component('jobAdd', {
        templateUrl: '/djangotemplates/private/jobs/forms.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate,
                Job,
                User,
                $tooltip,
                ngToast,
                $stateParams,
                Vender,
                Vehicle

            ){


            Vender.getVendorList('v').success(function(response){
                console.log(response.User);
                $scope.userData = response.User;
            }).error(function(e_data, e_status, e_headers, e_config){
               Flash.create("error",e_data.message,0);
            });

            Vehicle.getVehicleList().success(function(response){
                console.log(response);
//                console.log(response.Vehicle);

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


            $scope.doAddJob =function(job,valid){

                console.log(job);
                console.log(valid);



                if(valid){
                    if(!job.id){

                        Job.addJob(job).success(function(response){
                            $location.path("/jobs")
                        }).error(function(e_data, e_status, e_headers, e_config){
                           Flash.create("error",e_data.message,0);
                        });

                    }else{

                        Job.updateJob(job).success(function(response){
                            $location.path("/jobs")
                        }).error(function(e_data, e_status, e_headers, e_config){
                           Flash.create("error",e_data.message,0);
                        });
                    }
                }


            }



        }
})