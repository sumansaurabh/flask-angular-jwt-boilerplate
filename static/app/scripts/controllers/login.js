'use strict';

/**
 * @ngdoc function
 * @name yapp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of yapp
 */

app.controller('LoginCtrl', function($scope, $location) {

    $scope.submit = function() {
    	$auth.login({email: $scope.email, password: $scope.password}).then(function (response) {
	        $auth.setToken(response);
	        $state.go('dashboard');
	    }).catch(function (response) {
	        toastr.error(
	          'Email or password not correct!',
	          {closeButton: true}
	        );
	      })
    }

});
