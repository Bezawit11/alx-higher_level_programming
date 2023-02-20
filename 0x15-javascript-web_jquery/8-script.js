$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status){  
$.each(data, function( index, element ) {
  if (index == 'results'){
    for (let i = 0; i < data['results'].length; i++){
      $("ul").append(data['results'][i]['title']);
        $("ul").append("<br>");
    }
  }
  });
});
