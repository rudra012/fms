    'use strict';
    angular.module('loginDetail').
        component('loginDetail', {
            templateUrl: '/djangotemplates/public/access/login.html',
            controller: function(
                    $cookies,
                    $http,
                    $location,
                    $rootScope,
                    $scope,
                    Flash,
                    $animate
                ){

                var loginUrl = '/api/v1/login/'
                $scope.loginError = {}

                $scope.user = {
                }

                var tokenExists = $cookies.get("token")
                if (tokenExists) {
                    // verify token
                    $scope.loggedIn = true;
                    $cookies.remove("token");
                    $cookies.remove("username");
                    $scope.user = {
                        username: $cookies.get("username")
                    }
                    //window.location.reload()
                }


                var animate = function(element) {
                      element.removeClass('shake');
                      $animate.addClass(element, 'shake').then(function() {
                        element.removeClass('shake');
                      });
                };

                $scope.doLogin = function(user,valid){

                var myElement =null;
                if(!user.username)
                    myElement= angular.element( document.querySelector( '#Lusername' ) );
                else if(!user.password)
                    myElement= angular.element( document.querySelector( '#Lpassword' ) );

            if(myElement)
                animate (myElement);



                    if(!user.username || !user.password)
                        Flash.create("error","Please Tell us Username & Password");

                    if (user.username && user.password) {
                        var reqConfig = {
                            method: "POST",
                            url: loginUrl,
                            data: {
                                username: user.username,
                                password: user.password
                            },
                            headers: {}
                        }
                        var requestAction = $http(reqConfig)

                        requestAction.success(function(r_data, r_status, r_headers, r_config){
                                 $cookies.put("token", r_data.token)
                                $cookies.put("username", r_data.username)

                                $location.path("/home")

//                                window.location.reload()
                        })
                        requestAction.error(function(e_data, e_status, e_headers, e_config){
                                Flash.create("error",e_data.non_field_errors);

                        })
                    }


                }
                // $http.post()
            }
    })
