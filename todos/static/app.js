var phonecatApp = angular.module('phonecatApp', []);

phonecatApp
.config(function($interpolateProvider, setUrlProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    setUrlProvider.setUrl('http://127.0.0.1:8000/todos/api/v1/');
})

.controller('PhoneListCtrl', function ($scope,$http,setUrl,todoData ) {

  todoData.getAllItems().then(function(data){
      $scope.phones = data;
    })


  $scope.addTodo = function(work){
      if(work && work !== 'undefined'){
        var data =  { "name": work.name, "description": work.discription,"created": new Date() };
        $http.post(setUrl.getUrl()+'todo/',data).success(function(data) {
                todoData.getAllItems().then(function(data){
                    $scope.phones = data;
                })
         });
      }
  }

  $scope.remove =function(pk){
    $http.post('http://127.0.0.1:8000/todos/api/v1/deletetodo/',{"pk":pk}).success(function(data) {
                     if (data =='ok'){
                            todoData.getAllItems().then(function(data){
                                    $scope.phones = data;
                                })
                     }

         });
  }

  $scope.update = function(ls
  , pk){

        var data =  { "name": newitem.name, "description": newitem.discription,"created": new Date(),"pk":pk };
        $http.post(setUrl.getUrl()+'updatetodo/',data).success(function(data) {
                todoData.getAllItems().then(function(data){
                    $scope.phones = data;
                })
         });
  }


   $scope.showDetail = function (u) {
    if ($scope.active != u.pk) {
      $scope.active = u.pk;
    }
    else {
      $scope.active = null;
    }
  };

})




//provider style, full blown, configurable version
.provider('setUrl', function() {

    this.name = 'Default';

    this.$get = function() {
        var name = this.name;
        return {
            getUrl: function() {
                return name
            }
        }
    };

    this.setUrl= function(name) {
        this.name = name;
    };
})

  .factory('todoData',function($http, $q, setUrl){
    return{
      apiPath:setUrl.getUrl()+'todo/',
      getAllItems: function(){
        //Creating a deferred object
        var deferred = $q.defer();

        //Calling Web API to fetch shopping cart items
        $http.get(this.apiPath).success(function(data){
          //Passing data to deferred's resolve function on successful completion
          deferred.resolve(data);
      }).error(function(){

        //Sending a friendly error message in case of failure
        deferred.reject("An error occured while fetching items");
      });

      //Returning the promise object
      return deferred.promise;
    }
  }
})

