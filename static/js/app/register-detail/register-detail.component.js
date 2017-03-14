'use strict';

angular.module('registerDetail').
    component('registerDetail', {
        templateUrl: '/djangotemplates/public/access/signup.html',
        controller: function(
                $cookies,
                $http,
                $location,
                $rootScope,
                $scope,
                Flash,
                $animate
            ){

            var registerUrl = '/api/v1/register/'
            $scope.registerError = {}
            $scope.user = {

            }

            var animate = function(element) {
              $animate.addClass(element, 'shake').then(function() {
                element.removeClass('shake');
              });
            };

            $scope.doRegister = function(user){

            var myElement =null;
            if(!user.username)
                myElement= angular.element( document.querySelector( '#Rusername' ) );
            else if(!user.email)
                myElement= angular.element( document.querySelector( '#Remail' ) );
            else if(!user.password)
                myElement= angular.element( document.querySelector( '#Rpassword' ) );
            else if(!user.password2)
                myElement= angular.element( document.querySelector( '#Rpassword2' ) );
            else if(user.password!=user.password2)
                myElement= angular.element( document.querySelector( '#Rpassword2' ) );

            if(myElement)
                animate (myElement);


            if(!user.username && !user.email && !user.email2 && !user.password)
                Flash.create("error","Please Fill in all required field");
            else if(user.password!=user.password2)
                Flash.create("error","Re entered password should be same");


                if (user.username && user.email && user.password && user.password==user.password2) {
                    var reqConfig = {
                        method: "POST",
                        url: registerUrl,
                        data: {
                            username: user.username,
                            email: user.email,
                            email2: user.email,
                            password: user.password
                        },
                            headers: {}
                    }
                    var requestAction = $http(reqConfig)

                    requestAction.success(function(r_data, r_status, r_headers, r_config){
                            // console.log(r_data) // token
                            $cookies.put("token", r_data.token)
                            $cookies.put("username", r_data.username)
                            $location.path("/home")
                            //window.location.reload()
                    })
                    requestAction.error(function(e_data, e_status, e_headers, e_config){
                        Flash.create("error",e_data.email);
                        Flash.create("error",e_data.username);


//                            $scope.registerError = e_data

                    })
                }


            }

        }
})
