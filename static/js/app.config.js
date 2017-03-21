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

        .state('private.hannan', {
          url: '/list',
          views: {
            'container@': {
              templateUrl: '/djangotemplates/private/hannan/list.html',
            }
          },
          authenticate:true,
          display:"Vendors",
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

        $rootScope.currentState=toState;

        console.log($rootScope.currentState.display);


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
                   'faClass':'fa fa-desktop text-yellow',

                },
                {
                   'name':'vehicle',
                   'display':'Vehicles',
                   'url':'vehicles',
                   'activeWhen':[
                    'private.vehicles',
                    'private.vehicles-add',
                   ],
                   'faClass':'fa fa-car text-red',
                },
                {
                   'name':'group',
                   'display':'Group',
                   'url':'groups',
                   'activeWhen':[
                    'private.group',
                   ],
                   'faClass':'fa fa-group text-aqua',
                },
                {
                   'name':'users',
                   'display':'Users',
                   'url':'users',
                   'activeWhen':[
                    'private.users',
                    'private.users-update',
                   ],
                   'faClass':'fa fa-user text-green',
                },

                 {
                   'name':'vendors',
                   'display':'Vendors',
                   'url':'vendors',
                   'activeWhen':[
                    'private.vendors',
                    //'private.vendors-update',
                   ],
                   'faClass':'fa fa-user text-orange',
                },
                {
                   'name':'hannan',
                   'display':'A.Hannan',
                   'url':'list',
                   'activeWhen':[
                    'private.hannan',
                    //'private.vendors-update',
                   ],
                   'faClass':'fa fa-user text-orange',
                },




            ];


});

//mainApp.filter()

//mainApp.directive("scroll", function () {
//    return function(scope, element, attrs) {
//
//        var height=angular.element(element).bind("tbody")[0].offsetHeight;
//        console.log(height);
//
//        angular.element(element).bind("scroll", function() {
//            if(this.scrollTop >= height + 20 ) {
//                alert();
//            } else {
//                console.log("Less then 50");
//            }
//        });
//
//
//
//
//    };
//});


//mainApp.directive('scroll', function($window) {
//    return {
//        scope: {
//          offset: "@offset",
//          scrollClass: '='
//        },
//        link: function (scope, element, attr) {
//            angular.element($window).bind("scroll", function(event) {
//                if (element.pageYOffset >= scope.offset) {
//                    //this will change the parent scope variable value to true
//                  //  scope.scrollClass = true;
//                    alert();
//                }
//                //scope.$apply(); //need full to run digest cycle
//            });
//        }
//    }
//});


