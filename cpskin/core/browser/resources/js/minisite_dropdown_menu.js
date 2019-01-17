jQuery(document).ready(function($) {

    "use strict";

    $('.minisite-dropdown-menu > ul > li:has( > ul)').addClass('menu-dropdown-icon');
    //Checks if li has sub (ul) and adds class for toggle icon - just an UI

    $('.minisite-dropdown-menu > ul > li > ul:not(:has(ul))').addClass('normal-sub');
    //Checks if drodown menu's li elements have anothere level (ul), if not the dropdown is shown as regular dropdown, not a mega menu (thanks Luka Kladaric)

    //Mobile menu is hidden if width is more then 616px, but normal menu is displayed
    //Normal menu is hidden if width is below 616px, and jquery adds mobile menu

    //the following hides the menu when a click is registered outside
    $(document).on('click', function(e){
        if($(e.target).parents('.minisite-dropdown-menu').length === 0) {
            $('.minisite-dropdown-menu > ul').removeClass('show-on-mobile');
            $('.minisite-dropdown-menu > ul > li > ul').fadeOut(200);
        }
    });

    $('.minisite-dropdown-menu > ul > li').click(function(e) {
        //Top level click on a menu with children
        if($(e.target).parents('ul').length == 1 && $(this).children('ul').length > 0) e.preventDefault();
        var thisMenu = $(this).children('ul');
        var prevState = thisMenu.css('display');
        $('.minisite-dropdown-menu > ul > li > ul').fadeOut(200);
        if (prevState == 'block') return;

        if ($(window).width() < 600) thisMenu.fadeIn(200);
        else if ($(window).width() >= 600) $(this).children('ul').fadeToggle(200);
    });

    $('.minisite-dropdown-menu-mobile').click(function (e) {
        $('.minisite-dropdown-menu > ul').toggleClass('show-on-mobile');
        e.preventDefault();
    });

});
