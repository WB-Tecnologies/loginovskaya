$(document).ready(function(){
   var $inquire_form = $('#inquire-form'),
       $sumbit_button = $('.c-submit-form'),
       $previous_button = $('.c-step-previous'),
       $socials_link = $('.c-socials-link');

   $sumbit_button.on('click', function (ev) {
       ev.preventDefault();
       $inquire_form[0].submit();
   });

   $previous_button.on('click', function (ev) {
       ev.preventDefault();
       location.href = $(this).data('url');
   });

   $socials_link.on('click', function (ev) {
       ev.preventDefault();
       var $this = $(this);
       var $socials_block = $inquire_form.find('#id_1-socials');
       var $checkbox = $socials_block.find('input[type=checkbox][value="'+$this.data('value')+'"]');
       $checkbox.prop('checked', !$checkbox.prop('checked'));
       $this.find('img').toggleClass('btn-active');
   });
});