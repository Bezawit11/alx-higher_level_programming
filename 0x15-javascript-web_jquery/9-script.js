$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div').append(data.hello);
  });
});
