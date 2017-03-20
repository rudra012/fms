'use strict';

jobApp.factory("Job", ['$http',function($http){

    var obj = {};

    obj.getJobList = function(){
        return $http.get('/api/v1/user/');
    }

    obj.addUser = function(data){
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

jobApp.controller('jobApp', function ($cookies,$http,$location,$scope,Flash,$animate,Group,$timeout,$rootScope) {

//            $rootScope.loadMoreGroups =function(){
//                if($scope.has_next && !$scope.loadMoreInitiale){
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
//            }
//            $scope.checkCount=0;
//            $scope.deletingIds=[];



//            $scope.subCheck=function(select,id){
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
//            }


//            $scope.allCheckChange=function(select){
//                $scope.deletingIds=[];
//                angular.forEach($scope.groupData, function (item) {
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


            Group.getJobList().success(function(response){
                $scope.total=response.total;
                $scope.has_next=response.has_next;
                $scope.has_previous=response.has_previous;
                $scope.previous_page_number=response.previous_page_number;
                $scope.pages=response.pages;
                $scope.next_page_number=response.next_page_number;
                $scope.JobData = response.Job;


            }).error(function(e_data, e_status, e_headers, e_config){
            });








});

jobAdd.component('jobAdd', {
        templateUrl: '/djangotemplates/private/jobs/form.html',
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
                $stateParams

            ){





        }
})