//var mainApp=angular.module("fms",['ngAnimate',]);

mainApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/home');
    $stateProvider
        .state('public', {
          url: '',
          abstract: true,
          views: {
            'header': {
            },
            'left':{
            },
          }
        })
        .state('private', {
          url: '',
          abstract: true,
          views: {
            'header': {
              templateUrl: 'djangotemplates/layout/header.html',
            },
            'left':{
              templateUrl: 'djangotemplates/layout/left.html',
            }
          },
          authenticate:true,
        })

        .state('private.home', {
          url: '/home',
          views: {
            'container@': {
              templateUrl: 'djangotemplates/private/home.html'
            }
          },
          authenticate:true,
        })

        .state('private.home2', {
          url: '/home2',
          views: {
            'container@': {
              templateUrl: 'djangotemplates/private/home2.html'
            }
          },
          authenticate:true,
        })
        .state('private.vehicles', {
          url: '/vehicles',
          views: {
            'container@': {
              template: '<vehicles></vehicles>'
            }
          },
          authenticate:true,
        })


        .state('private.group', {
          url: '/groups',
          views: {
            'container@': {
              template: '<group></group>'
            }
          },
          authenticate:true,
        })

        .state('private.users', {
          url: '/contacts',
          views: {
            'container@': {
              template: '<users></users>'
            }
          },
          authenticate:true,
        })


        .state('private.users-add', {
          url: '/contact-add',
          views: {
            'container@': {
              template: '<users-add></users-add>'
            }
          },
          authenticate:true,
        })


         .state('private.vehicles-add', {
          url: '/vehicles-add',
          views: {
            'container@': {
              template: '<vehicle-add></vehicle-add>'
            }
          },
          authenticate:true,
        })

        .state('public.login', {
          url: '/login',
          views: {
            'container@': {
              template: '<login-detail></login-detail>'
            }
          },
          authenticate:false,
        })

        .state('public.signup', {
          url: '/signup',
          views: {
            'container@': {
              template: '<register-detail></register-detail>'
            }
          },
          authenticate:false,
        })

});

mainApp.run(['$state', '$rootScope','$location','Auth','$http','$cookies', function($state, $rootScope,$location,Auth,$http,$cookies) {

    //$http.defaults.headers.common['Authorization'] ="JWT "+$cookies.get('token');

    $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {

            Auth.init();

            stateType=toState.name.split('.');
            $rootScope.bodyClass="hold-transition login-page";
            if(stateType && stateType[0]=='private' && toState.authenticate)
            {
                $http.defaults.headers.common['Authorization'] ="JWT "+$cookies.get('token');
                if(!Auth.isLoggedIn() && fromState.name!="")
                    event.preventDefault();
                else if(!Auth.isLoggedIn()  && fromState.name == "")
                    $location.path('/login')
                else
                    $rootScope.bodyClass="hold-transition skin-blue sidebar-mini";

            }


    });

    $rootScope.$on("$stateChangeSuccess", function(event, toState, toParams, fromState, fromParams) {
        if(stateType && stateType[0]=='private')
        $rootScope.bodyClass="hold-transition skin-blue sidebar-mini";
    });



}]);


mainApp
.factory('Auth', function($rootScope, $q,$cookies){

    var auth = {};
     auth.isLoggedIn = function(){
            return $cookies.get('username')!="undefined" && $cookies.get('token')!="undefined" && $cookies.get('username')!= null && $cookies.get('token')!=null;
    };


    /**
     *  Saves the current user in the root scope
     *  Call this in the app run() method
     */
    auth.init = function(){
        if (auth.isLoggedIn()){
            $rootScope.user = $cookies.get('username');
        }
    };




//    auth.checkPermissionForView = function(view) {
//        if (!view.requiresAuthentication) {
//            return true;
//        }
//
//        return userHasPermissionForView(view);
//    };


//    var userHasPermissionForView = function(view){
//        if(!auth.isLoggedIn()){
//            return false;
//        }
//
//        if(!view.permissions || !view.permissions.length){
//            return true;
//        }
//
//        return auth.userHasPermission(view.permissions);
//    };
//

//    auth.userHasPermission = function(permissions){
//        if(!auth.isLoggedIn()){
//            return false;
//        }
//
//        var found = false;
//        angular.forEach(permissions, function(permission, index){
//            if ($sessionStorage.user.user_permissions.indexOf(permission) >= 0){
//                found = true;
//                return;
//            }
//        });
//
//        return found;
//    };


    return auth;
});