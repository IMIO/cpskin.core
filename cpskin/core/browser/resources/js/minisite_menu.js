jQuery(document).ready(function($) {

    if ($("#toggle-minisite-menu").length == 0) {
        // collapse_minisite_menu option is not activated
        return;
    }
    
    if ($("body.in-minisite-in-portal").length == 0) {
        // we are not in a minisite
        $("#toggle-minisite-menu").hide();
        return;
    }

    $(".minisite-collapsable").hide();
    $("#toggle-minisite-menu .hide-menu").hide();
    $("#toggle-minisite-menu a").click(function() {
        $("#toggle-minisite-menu a").toggle();
        $(".minisite-collapsable").slideToggle('slow');
    });
});
