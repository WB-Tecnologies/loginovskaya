$(document).ready(function(){
   var $inquire_form = $('#inquire-form'),
       $sumbit_button = $('.c-submit-form'),
       $previous_button = $('.c-step-previous');

   $sumbit_button.on('click', function () {
       $inquire_form[0].submit();
   });

   $previous_button.on('click', function () {
        location.href = $(this).data('url');
   });
});