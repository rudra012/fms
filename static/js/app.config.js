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

mainApp.run(['$state', '$rootScope','$location', function($state, $rootScope,$location) {

    $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {

            stateType=toState.name.split('.');

            $rootScope.bodyClass="hold-transition login-page";
            if(fromState.name!="" && toState.authenticate && stateType && stateType[0]=='private')
            {
                if(false)
                {
                    event.preventDefault();
                }else{
                    $rootScope.bodyClass="hold-transition skin-blue sidebar-mini";
                }
            }
            else if(fromState.name == "")
            {
                $location.path('/login')

            }
            else if (stateType && stateType[0]=="private")
            {
                $rootScope.bodyClass="hold-transition skin-blue sidebar-mini";
            }



    });

}]);