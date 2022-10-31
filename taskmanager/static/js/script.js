// Init Sidenav functionality
$(document).ready(function(){
    $('.sidenav').sidenav();
  });

// datepicker init
$(document).ready(function(){
  $('.datepicker').datepicker(
    format, "mmmm dd, yyyy", 
    i18n, {done: "Select"}
    );
});

// select init 
$(document).ready(function(){
  $('select').formSelect();
});