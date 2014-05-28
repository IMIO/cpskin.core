jQuery(function($){

    if (jQuery.browser.msie && parseInt(jQuery.browser.version, 10) < 7) {
        // it's not realistic to think we can deal with all the bugs
        // of IE 6 and lower. Fortunately, all this is just progressive
        // enhancement.
        return;
    }

    // menutools
    $('.toolbox-menutools a').prepOverlay(
        {
            subtype: 'ajax',
            filter: common_content_filter,
            width:'50%'
        }
    );
})
