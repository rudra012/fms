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

    obj.loadMoreGroup = function(page){
         var req = {
             method: 'GET',
             url: '/api/v1/group/',
            params: {
                page: page,
            }
        }
        return $http(req);
    }

    return obj;
}]);


//angular.module('group', []).controller

angular.module('group', []).controller('group', function ($cookies,$http,$location,$scope,Flash,$animate,Group,$timeout,$rootScope) {
            $rootScope.loadMoreGroups =function(){
                if($scope.has_next && !$scope.loadMoreInitiale){
                    $scope.loadMoreInitiale=true;
                    Group.loadMoreGroup($scope.next_page_number).success(function(response){
                        $timeout(function(){
                            $scope.total=response.total;
                            $scope.has_next=response.has_next;
                            $scope.has_previous=response.has_previous;
                            $scope.previous_page_number=response.previous_page_number;
                            $scope.pages=response.pages;
                            $scope.next_page_number=response.next_page_number;
                            $scope.groupData = $scope.groupData.concat(response.Group);
                            $scope.loadMoreInitiale=false;

                        } ,1500)
                    }).error(function(e_data, e_status, e_headers, e_config){
                    });
                }
            }
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
                if($scope.checkCount==$scope.groupData.length)
                    $scope.selectedAllGroup=true
                else
                    $scope.selectedAllGroup=false

            }

            $scope.allCheckChange=function(select){
                $scope.deletingIds=[];
                angular.forEach($scope.groupData, function (item) {
                     item.select = select;
                     if(select)
                     {
                        $scope.deletingIds.push(item.id)
                        $scope.checkCount=$scope.groupData.length;
                     }
                     else
                        $scope.checkCount=0;
                });
            }

            Group.getGroupList().success(function(response){
                $scope.total=response.total;
                $scope.has_next=response.has_next;
                $scope.has_previous=response.has_previous;
                $scope.previous_page_number=response.previous_page_number;
                $scope.pages=response.pages;
                $scope.next_page_number=response.next_page_number;
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
            $scope.doAddGroup=function(group){

                $scope.GroupForm.$setPristine();
                var addElement=angular.copy(group);
                Group.addGroup(group).success(function(response){
                if(response.Group)
                    response.Group.new=true

                if(response.Group)
                    $scope.groupData.splice(0, 0, response.Group);
                    $scope.total += 1;

                 if($scope.groupData.length>5)
                    $scope.groupData.splice($scope.groupData.length-1, 1);

                }).error(function(e_data, e_status, e_headers, e_config){
                });
                $scope.group=null;
            }

            $scope.addOpen=function(){

                $scope.GroupForm.$setPristine();
                if(!$scope.open)
                    $scope.open=true;
                else
                    $scope.open=false;

            }
            $scope.deletGroup=function(group,index){

                var delGroup=angular.copy(group);
                delGroup.is_deleted="Y";
                Group.updateGroup(delGroup).success(function(response){
                    if(response.code==200)
                        $scope.groupData.splice(index, 1);
                }).error(function(e_data, e_status, e_headers, e_config){
                });
            }

});

//angular.module('group', []).
//    component('group', {
//        templateUrl: '/djangotemplates/private/group/list.html',
//        controller: function(
//                $cookies,
//                $http,
//                $location,
//                $scope,
//                Flash,
//                $animate,
//                Group,
//                $timeout,
//                $rootScope
//            ){
//
//            $rootScope.loadMoreGroups =function()
//            {
//                alert("loadmore");
//            }
//            $scope.checkCount=0;
//            $scope.deletingIds=[];
//
//            $scope.subCheck=function(select,id)
//            {
//
//                console.log(id);
//
//                if(select)
//                {
//                    $scope.deletingIds.push(id);
//                    $scope.checkCount += 1
//                }
//                else
//                {
//                    $scope.deletingIds.pop(id);
//                    $scope.checkCount -=1
//                }
//
//
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
//
//                $scope.deletingIds=[];
//
//                angular.forEach($scope.groupData, function (item) {
//
//                     item.select = select;
//                     if(select)
//                        $scope.deletingIds.push(item.id)
//                });
//
//            }
//
//
//            Group.getGroupList().success(function(response){
//
//                $scope.has_next=response.has_next;
//                $scope.has_previous=response.has_previous;
//                $scope.previous_page_number=response.previous_page_number;
//                $scope.pages=response.pages;
//                $scope.next_page_number=response.next_page_number;
//
//                $scope.groupData = response.Group;
//            }).error(function(e_data, e_status, e_headers, e_config){
//            });
//
//            $scope.updateClick=function(data,index){
//                data.edit=true;
//            }
//
//            $scope.done=function(data,index){
//
//                if(data.group_name)
//                {
//                    data.edit=false;
//                    data.new=true;
//                    Group.updateGroup(data).success(function(response){
//                    }).error(function(e_data, e_status, e_headers, e_config){
//                    });
//
//                    $timeout(function(){
//                        data.new=false;
//                     } ,1000);
//
//                }
//            }
//
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
//
//            $scope.addOpen=function()
//            {
//
//                $scope.GroupForm.$setPristine();
//
//                if(!$scope.open)
//                    $scope.open=true;
//                else
//                    $scope.open=false;
//            }
//            $scope.deletGroup=function(group,index)
//            {
//                var delGroup=angular.copy(group);
//                delGroup.is_deleted="Y";
//                Group.updateGroup(delGroup).success(function(response){
//                    if(response.code==200)
//                        $scope.groupData.splice(index, 1);
//                }).error(function(e_data, e_status, e_headers, e_config){
//                });
//            }
//
//
//        }
//})

//mainApp.directive('scroll', function() {
//    return {
//        restrict: 'A',
//        link: function(rootScope, element, attrs, $window, $scope, $document) {
//            var bind = element.bind('tbody');
//            var raw = element[0];
//            angular.element(bind).on("scroll", function() {
//                //console.log('in scroll');
//                //console.log(raw.scrollTop + raw.offsetHeight);
//                //console.log(raw.scrollHeight);
//                if (raw.scrollTop + raw.offsetHeight >= raw.scrollHeight) {
//
//                    //rootScope.loadMoreGroups();
//
//                }
//            });
//        }
//    };
//});
