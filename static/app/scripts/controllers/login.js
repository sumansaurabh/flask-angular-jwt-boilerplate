'use strict';

/**
 * @ngdoc function
 * @name yapp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of yapp
 */

app.controller('LoginCtrl',['$scope', '$state', '$location', '$auth', function($scope, $state, $location, $auth) {

    $scope.submit = function() {
    	$auth.login({email: $scope.email, password: $scope.password}).then(function (response) {
	        $auth.setToken(response);
	        $state.go('dashboard');
	    }).catch(function (response) {
	        console.log('Invalid password!')

	    })
    }

    $scope.authenticate_by_provider = function(provider) {
    	$auth.authenticate(provider).then(function(response) {
            $auth.setToken(response.token);
            $state.go('dashboard');
        })
        .catch(function(response) {
            console.log(response);
        });
    };

}]);
