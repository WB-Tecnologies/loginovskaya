$(document).ready(function(){
   var $inquire_form = $('#inquire-form'),
       $sumbit_button = $('button.c-submit-form');

   $sumbit_button.on('click', function (ev) {
       $inquire_form[0].submit();
   })
});