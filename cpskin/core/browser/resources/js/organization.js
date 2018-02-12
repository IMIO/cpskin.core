jQuery(document).ready(function($) {
    $('.dynamic-hover').hover(
        function() {
            var image_hover = $(this).attr('hover-image-url');
            $(this).css('background-image', 'url(' + image_hover + ')');
        },
        function() {
            var image = $(this).attr('image-url');
            $(this).css('background-image', 'url(' + image + ')');
        }
    );

    $('.organization-photo a').fancybox();
});
