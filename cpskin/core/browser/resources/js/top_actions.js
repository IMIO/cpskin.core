function toggleMenuHandler(event) {
    // swap between activated and deactivated
    // Don't change menu with no submenu
    var menu = jQuery(this).parents('.actionMenu:first');
    if (menu.hasClass('empty')) return true;
    menu.toggleClass('deactivated')
        .toggleClass('activated');
    return false;
}
