'use strict';

/**
 * @ngdoc function
 * @name yapp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of yapp
 */

app.controller('DashboardCtrl', function($scope, $state, $http) {
    $scope.$state = $state;
    var hello = "hellp";

    console.log("in dashbaord cteel");
    $http({
            method: 'GET',
            url: "/api/get_cofee"
        }).then(function (response) {
            console.log('suman')
        });

    $scope.menuItems = [];
    angular.forEach($state.get(), function (item) {
        if (item.data && item.data.visible) {
            $scope.menuItems.push({name: item.name, text: item.data.text});
        }
    });
});
