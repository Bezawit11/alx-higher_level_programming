window.addEventListener('DOMContentLoaded', (event) => {
    $(document).ready(function(){
  $("#add_item").click(function(){

    $("li").append("<li>Item</li>");
  });

  $("#remove_item").click(function(){
      $('#my_list').remove();
  });

  $("#clear_list").click(function(){

    $("ul").html(" ");
  });
});
});
