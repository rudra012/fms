'use strict';

mainApp.factory("Job", ['$http',function($http){

    var obj = {};

    obj.getJobList = function(type){

         var req = {
             method: 'GET',
             url: '/api/v1/jobs/',
             params: {
                type: type,
             }
         }
        return $http(req);

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

            $scope.currentState=$rootScope.currentState;


            $scope.checkCount=0;
            $scope.deletingIds=[];
            $scope.subCheck=function(select,id)
            {
                if(select){
                    $scope.deletingIds.push(id);
                    $scope.checkCount += 1
                }else{
                    $scope.deletingIds.pop(id);
                    $scope.checkCount -=1
                }
                if($scope.checkCount==$scope.JobData.length)
                    $scope.selectedAllJob=true
                else
                    $scope.selectedAllJob=false
            }
            $scope.allCheckChange=function(select)
            {
                 $scope.deletingIds=[];
                 angular.forEach($scope.JobData, function (item) {
                     item.select = select;
                     if(select)
                     {
                        $scope.deletingIds.push(item.id)
                        $scope.checkCount=$scope.JobData.length;
                     }
                     else
                        $scope.checkCount=0;
                });
            }



            Job.getJobList(null).success(function(response){
                $scope.total=response.total;
                $scope.has_next=response.has_next;
                $scope.has_previous=response.has_previous;
                $scope.previous_page_number=response.previous_page_number;
                $scope.pages=response.pages;
                $scope.next_page_number=response.next_page_number;

                $scope.JobData = response.Job;


            }).error(function(e_data, e_status, e_headers, e_config){
            });

            $scope.deletJob=function(job,index){

                var delGroup=angular.copy(job);
                delGroup.is_deleted="Y";
                Job.updateJob(delGroup).success(function(response){
                    if(response.code==200)
                        $scope.JobData.splice(index, 1);
                }).error(function(e_data, e_status, e_headers, e_config){
                });
            }
        }
})



angular.module('assignedJobs', []).
    component('assignedJobs', {
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


            $scope.currentState=$rootScope.currentState;

            $scope.checkCount=0;
            $scope.deletingIds=[];
            $scope.subCheck=function(select,id)
            {
                if(select){
                    $scope.deletingIds.push(id);
                    $scope.checkCount += 1
                }else{
                    $scope.deletingIds.pop(id);
                    $scope.checkCount -=1
                }
                if($scope.checkCount==$scope.JobData.length)
                    $scope.selectedAllJob=true
                else
                    $scope.selectedAllJob=false
            }
            $scope.allCheckChange=function(select)
            {
                 $scope.deletingIds=[];
                 angular.forEach($scope.JobData, function (item) {
                     item.select = select;
                     if(select)
                     {
                        $scope.deletingIds.push(item.id)
                        $scope.checkCount=$scope.JobData.length;
                     }
                     else
                        $scope.checkCount=0;
                });
            }



            Job.getJobList('a').success(function(response){
                $scope.total=response.total;
                $scope.has_next=response.has_next;
                $scope.has_previous=response.has_previous;
                $scope.previous_page_number=response.previous_page_number;
                $scope.pages=response.pages;
                $scope.next_page_number=response.next_page_number;

                $scope.JobData = response.Job;


            }).error(function(e_data, e_status, e_headers, e_config){
            });

            $scope.deletJob=function(job,index){

                var delGroup=angular.copy(job);
                delGroup.is_deleted="Y";
                Job.updateJob(delGroup).success(function(response){
                    if(response.code==200)
                        $scope.JobData.splice(index, 1);
                }).error(function(e_data, e_status, e_headers, e_config){
                });
            }
        }
})


angular.module('pendingJobs', []).
    component('pendingJobs', {
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

            $scope.currentState=$rootScope.currentState;


            $scope.checkCount=0;
            $scope.deletingIds=[];
            $scope.subCheck=function(select,id)
            {
                if(select){
                    $scope.deletingIds.push(id);
                    $scope.checkCount += 1
                }else{
                    $scope.deletingIds.pop(id);
                    $scope.checkCount -=1
                }
                if($scope.checkCount==$scope.JobData.length)
                    $scope.selectedAllJob=true
                else
                    $scope.selectedAllJob=false
            }
            $scope.allCheckChange=function(select)
            {
                 $scope.deletingIds=[];
                 angular.forEach($scope.JobData, function (item) {
                     item.select = select;
                     if(select)
                     {
                        $scope.deletingIds.push(item.id)
                        $scope.checkCount=$scope.JobData.length;
                     }
                     else
                        $scope.checkCount=0;
                });
            }



            Job.getJobList('p').success(function(response){
                $scope.total=response.total;
                $scope.has_next=response.has_next;
                $scope.has_previous=response.has_previous;
                $scope.previous_page_number=response.previous_page_number;
                $scope.pages=response.pages;
                $scope.next_page_number=response.next_page_number;

                $scope.JobData = response.Job;


            }).error(function(e_data, e_status, e_headers, e_config){
            });

            $scope.deletJob=function(job,index){

                var delGroup=angular.copy(job);
                delGroup.is_deleted="Y";
                Job.updateJob(delGroup).success(function(response){
                    if(response.code==200)
                        $scope.JobData.splice(index, 1);
                }).error(function(e_data, e_status, e_headers, e_config){
                });
            }
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
                Flash.clear();
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