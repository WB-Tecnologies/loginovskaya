$(document).ready(function (){
    var $inquire_form = $('#inquire-form'),
        $socials_link = $('.c-socials-link'),
        $inquire_result = $('#inquire_result'),
        current_step = $inquire_form.data('step'),
        cookie_name = 'inquire';

    $.cookie.json = true;

    if ($inquire_form.length){
        form_initial();
    } else {
        display_result();
    }

    $('.c-step-previous, .c-submit-form').on('click', function (ev) {
        ev.preventDefault();
        form_save();
        var $this = $(this);
        if ($this.attr('id') === 'lastBtn'){
            $.removeCookie(cookie_name);
        }
        location.href = $this.data('url');
    });

    $socials_link.on('click', function (ev) {
        ev.preventDefault();
        var $this = $(this);
        var $socials_block = $inquire_form.find('#id_1-socials');
        var $checkbox = $socials_block.find('input[type=checkbox][data-name="'+$this.data('name')+'"]');
        $checkbox.prop('checked', !$checkbox.prop('checked'));
        $this.find('img').toggleClass('btn-active');
    });

    function form_initial() {
        var values = ($.cookie(cookie_name) || {})[current_step] || {};
        for (var name in values){
            var $input = $inquire_form.find('input[data-name='+name+']');
            $input.prop('checked', true);
            if ($input.attr('name') === '1-socials'){
                $socials_link.filter('[data-name="'+name+'"]').find('img').addClass('btn-active');
            }
        }
    }

    function number_with_thousand_separator(num) {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    }

    function display_result() {
        var steps = ($.cookie(cookie_name) || {});
        var summary = 0;
        for (var step in steps){
            var values = steps[step];
            for (var name in values){
                summary += Number(values[name]);
            }
        }
        $inquire_result.text(number_with_thousand_separator(summary));
    }

    function form_save() {
        var input_values = {};
        $inquire_form.find('input:checked').each(function() {
            var $this = $(this);
            input_values[$this.attr('data-name')] = $this.val();
        });
        var steps_values = $.cookie(cookie_name) || {};
        steps_values[current_step] = input_values;
        $.cookie(cookie_name, steps_values);
    }
});
