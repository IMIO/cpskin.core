jQuery(document).ready(function($) {

    "use strict";

    // Checks if li has sub (ul) and adds class for toggle icon - just an UI
    $('.minisite-dropdown-menu > ul > li:has( > ul)').addClass('menu-dropdown-icon');

    // Checks if drodown menu li elements have another level (ul) :
    //  -> if yes, the dropdown is shown as mega-menu dropdown
    $('.minisite-dropdown-menu > ul > li > ul:has(ul)').addClass('mega-sub');
    //  -> if no, the dropdown is shown as regular dropdown
    $('.minisite-dropdown-menu > ul > li > ul:not(:has(ul))').addClass('normal-sub');

    // Hide the menu when a click is registered outside
    $(document).on('click', function(e){
        if($(e.target).parents('.minisite-dropdown-menu').length === 0 || $(e.target).hasClass('navTree')) {
            $('.minisite-dropdown-menu > ul').removeClass('show-on-mobile');
            $('.minisite-dropdown-menu > ul > li').removeClass('activated');
            $('.minisite-dropdown-menu > ul > li > ul').fadeOut(200);
        }
    });

    $('.minisite-dropdown-menu > ul > li').click(function(e) {
        // Top level click on a menu with children has no effect
        if($(e.target).parents('ul').length == 1 && $(this).children('ul').length > 0) e.preventDefault();

        var thisMenu = $(this).children('ul');
        var prevState = thisMenu.css('display');
        $('.minisite-dropdown-menu > ul > li > ul').fadeOut(200);
        $('.minisite-dropdown-menu > ul > li').removeClass('activated');
        if (prevState == 'block') return;
        thisMenu.fadeIn(200);
        $(this).addClass('activated');
    });

    $('.minisite-dropdown-menu-mobile').click(function (e) {
        $('.minisite-dropdown-menu > ul').toggleClass('show-on-mobile');
        e.preventDefault();
    });

});
