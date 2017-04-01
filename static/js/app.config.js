//var mainApp=angular.module("fms",['ngAnimate',]);

mainApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/home');
    $stateProvider
        .state('public', {
          url: '',
          abstract: true,
          views: {
            'header': {},
            'left':{},

            'footer':{}
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
              controller:'leftController'
            },
            'footer': {
              templateUrl: 'djangotemplates/layout/footer.html',
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
          display:"Home",
        })

        .state('private.home2', {
          url: '/home2',
          views: {
            'container@': {
              templateUrl: 'djangotemplates/private/home2.html'
            }
          },
          authenticate:true,
          display:"Home2",
        })

        .state('private.vehicles', {
          url: '/vehicles',
          views: {
            'container@': {
              template: '<vehicles></vehicles>'
            }
          },
          authenticate:true,
          display:"Vehicles",
        })

        .state('private.group', {
          url: '/groups',
          views: {
            'container@': {
              template: '<group></group>',

            }
          },
          authenticate:true,
          display:"Groups",
        })

        .state('private.jobs', {
          url: '/jobs',
          views: {
            'container@': {
              template: '<jobs></jobs>',

            }
          },
          authenticate:true,
          display:"Jobs",
        })

        .state('private.fuel-type', {
          url: '/fuel-type',
          views: {
            'container@': {
              template: '<fuel></fuel>',
            }
          },
          authenticate:true,
          display:"Jobs",
        })


        .state('private.fuel-add', {
          url: '/fuel-add',
          views: {
            'container@': {
              template: '<fuel-add></fuel-add>',
            }
          },
          authenticate:true,
          display:"Fuel",
        })


        .state('private.fuel-update', {
          url: '/fuel-update~index~:id',
          views: {
            'container@': {
                template: '<fuel-add></fuel-add>',
            }
          },
          authenticate:true,
          display:"Jobs",
        })




        .state('private.chat', {
          url: '/chat',
          views: {
            'container@': {
              templateUrl: "/static/templates/chatView.html",
              templateUrl: 'djangotemplates/private/chat/list.html',
              controller: "ChatCtrl",
              controllerAs: "ctrl"
            }
          },
          authenticate:true,
          display:"Chat",
        })






        .state('private.assigned-jobs', {
          url: '/assigned-jobs',
          views: {
            'container@': {
                template: '<assigned-jobs></assigned-jobs>',
            }
          },
          authenticate:true,
          display:"Jobs",
        })

        .state('private.pending-jobs', {
          url: '/pending-jobs',
          views: {
            'container@': {
                template: '<pending-jobs></pending-jobs>',
            }
          },
          authenticate:true,
          display:"Jobs",
        })

        .state('private.job-add', {
          url: '/job-add',
          views: {
            'container@': {
                template: '<job-add></job-add>',
            }
          },
          authenticate:true,
          display:"Jobs",
        })


        .state('private.job-update', {
          url: '/job-update~index~:id',
          views: {
            'container@': {
                template: '<job-add></job-add>',
            }
          },
          authenticate:true,
          display:"Jobs",
        })



        .state('private.users', {
          url: '/users',
          views: {
            'container@': {
              template: '<users></users>'
            }
          },
          authenticate:true,
          display:"Users",
        })

        .state('private.users-update', {
          url: '/user-update~index~:id',
          views: {
            'container@': {
              template: '<users-add></users-add>'
            }
          },
          authenticate:true,
          display:"Users",
        })

        .state('private.vendors', {
          url: '/vendors',
          views: {
            'container@': {
              template: '<vendors></vendors>'
            }
          },
          authenticate:true,
          display:"Vendors",
        })


        .state('private.vendor-add', {
          url: '/vendor-add',
          views: {
            'container@': {
              template: '<vendor-add></vendor-add>'
            }
          },
          authenticate:true,
          display:"Users",
        })

        .state('private.vendor-update', {
          url: '/vendor-update~index~:id',
          views: {
            'container@': {
              template: '<vendor-add></vendor-add>'
            }
          },
          authenticate:true,
          display:"Users",
        })


        .state('private.vehicle-update', {
          url: '/vehicle-update~index~:id',
          views: {
            'container@': {
              template: '<vehicle-add></vehicle-add>'
            }
          },
          authenticate:true,
          display:"Vehicle",
        })

        .state('private.users-add', {
          url: '/user-add',
          views: {
            'container@': {
              template: '<users-add></users-add>'
            }
          },
          authenticate:true,
          display:"Users",
        })


         .state('private.vehicles-add', {
          url: '/vehicles-add',
          views: {
            'container@': {
              template: '<vehicle-add></vehicle-add>'
            }
          },
          authenticate:true,
          display:"Vehicle",
        })

        .state('public.login', {
          url: '/login',
          views: {
            'container@': {
              template: '<login-detail></login-detail>'
            }
          },
          authenticate:false,
          display:"Login",

        })

        .state('public.signup', {
          url: '/signup',
          views: {
            'container@': {
              template: '<register-detail></register-detail>'
            }
          },
          authenticate:false,
          display:"Signup",

        })

});

mainApp.run(['$state', '$rootScope','$location','Auth','$http','$cookies', function($state, $rootScope,$location,Auth,$http,$cookies) {

    //$http.defaults.headers.common['Authorization'] ="JWT "+$cookies.get('token');

    $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {

            $rootScope.currentState=toState;
            $http.defaults.headers.common['Authorization'] ="";
            Auth.init();
            stateType=toState.name.split('.');
            $rootScope.bodyClass="hold-transition login-page";
            if(stateType && stateType[0]=='private' && toState.authenticate){

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

        $rootScope.currentState=toState;

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


 mainApp.controller('leftController', function($scope) {

    $scope.getClass=function(item,current){
        if(item.activeWhen.indexOf(current.name)>=0)
            return 'active';
        else
            return '';
    }

        $scope.leftmenuItem=[

                {
                   'name':'home',
                   'display':'Home',
                   'url':'home',
                   'activeWhen':[
                    'private.home',
                   ],
                   'faClass':'fa fa-desktop',

                },
                {
                   'name':'vehicle',
                   'display':'Vehicles',
                   'url':'vehicles',
                   'activeWhen':[
                    'private.vehicles',
                    'private.vehicles-add',
                   ],
                   'faClass':'fa fa-car',
                },

                {
                   'name':'group',
                   'display':'Group',
                   'url':'groups',
                   'activeWhen':[
                    'private.group',
                   ],
                   'faClass':'fa fa-group',
                },
                {
                   'name':'users',
                   'display':'Users',
                   'url':'users',
                   'activeWhen':[
                    'private.users',
                    'private.users-update',
                   ],
                   'faClass':'fa fa-user',
                },

                 {
                   'name':'vendors',
                   'display':'Vendors',
                   'url':'vendors',
                   'activeWhen':[
                    'private.vendors',
                    //'private.vendors-update',
                   ],
                   'faClass':'fa fa-user',
                },
                {
                   'name':'jobs',
                   'display':'Jobs',
                   'url':'jobs',
                   'activeWhen':[
                    'private.jobs',
                    //'private.vendors-update',
                   ],
                   'faClass':'fa fa-suitcase',
                },

                {
                   'name':'fuel-type',
                   'display':'Fuel Type',
                   'url':'fuel-type',
                   'activeWhen':[
                    'private.fuel-type',
                    'private.fuel-type-add',
                   ],
                   'faClass':'fa fa-user',
                },

            ];

});
