$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (value) {
  $('DIV#hello').html(value.hello);
});
