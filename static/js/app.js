var mainApp=angular.module("fms", [
    // external
    //'ngMaterial',
    'ngMessages',
    'ui.router',
    'ngAnimate',
    'ngCookies',
    'ngFlash',
    'ngResource',

    'mgcrea.ngStrap',




    //internal Modules
    'loginDetail',
    'registerDetail',
    'vehicles',

    'vehicleAdd',
    'group',
    'users',
    'usersAdd',



]);


mainApp.controller('TooltipDemoCtrl', function($scope, $q, $sce, $tooltip) {

  $scope.tooltip = {title: 'Hello Tooltip<br />This is a multiline message!', checked: false};


});

