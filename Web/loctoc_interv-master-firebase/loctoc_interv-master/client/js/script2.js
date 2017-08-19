// script.js
var myApp = angular.module('webapp', ['ngRoute', 'firebase']);
var map;
var config = {
    apiKey: "AIzaSyBEqJOrKFDs2lsePbl0530O4qrVrKg0qDw",
    authDomain: "botcentric-f8019.firebaseapp.com",
    databaseURL: "https://botcentric-f8019.firebaseio.com",
    projectId: "botcentric-f8019",
    storageBucket: "botcentric-f8019.appspot.com",
    messagingSenderId: "703960303999"
};
firebase.initializeApp(config);

//map key
//AIzaSyC3AFp66yHrTS5OzC1KogV88iklAAcYF5Q
myApp.config(function ($routeProvider, $sceDelegateProvider) {

    $routeProvider
        .when('/', {
            templateUrl: 'html/detailview.html',
            controller: 'cntrl'
        })
        .when('/NewBot', {
            templateUrl: 'html/category.html',
            controller: 'cntrl'
        });
});

myApp.controller('cntrl', function ($scope, $http, $interval, $timeout, $compile, $firebaseObject) {

    $scope.sidelane = 0;
    $scope.maplane = 12;

    $scope.selected_driver = null;

    $scope.optionList = ["Neural-Net", "Spec2", "Spec3"];
    
    $scope.activeBotList = [];
    
    $scope.selectedBot = {};

    $scope.create = function () {
        
        var ref = firebase.database().ref("botcentric-f8019").child('UserBots').child('Paddy').child('Bots').push();

        var BotID = ref.key;
        console.log(BotID);
        
        if($scope.botName == undefined){
            $scope.botName = "BOT "+ BotID;
        }
        
        if($scope.botType == undefined){
            $scope.botType = "Neural-Net";
        }
        var request = $firebaseObject(ref);
        request.$loaded().then(function () {
            request.BotName = $scope.botName;
            request.BotType = $scope.botType;
            request.BotID = BotID;
            
            var save = request.$save();
            console.log(save);
             $scope.populateBotList();
            
            $scope.botName = undefined;
            $scope.botType = undefined;
        });

    }
    
    $scope.populateBotList = function(){
        var ref = firebase.database().ref("botcentric-f8019").child('UserBots').child('Paddy').child('Bots');
        var request = $firebaseObject(ref);
        var res_arr = [];
        request.$loaded().then(function (data) {
//            console.log(data);
            for(var key in data){
                
                if(key.startsWith("-")){
                    console.log(key);
                   res_arr.push(data[key]); 
                }
            }
            
            console.log(res_arr);
            $scope.activeBotList = res_arr;
        });
        
    }
    
    $scope.selectBot = function(bot){
        $scope.selectedBot = bot;
        //change to diff view
    }

    
    $scope.populateBotList();
});