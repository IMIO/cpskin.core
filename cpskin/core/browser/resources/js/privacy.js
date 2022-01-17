jQuery(function($) {

    // See if we need to delete language selector
    if ($('#portal-languageselector').length > 0) {
      $.ajax({
        type: "GET",
        url: "@@allow_languages",
        headers: {"Cache-Control": "no-cache"},
      }).done(function(data) {
          if (data == false) $('#portal-languageselector').remove();
      });
    }

    // See if we need to un-hide blocked iframes
    if ($('.gdpr-iframe').length > 0) {
      $.ajax({
        type: "GET",
        url: "@@allow_iframes",
        headers: {"Cache-Control": "no-cache"},
      }).done(function(data) {
          if (data == true) {
            $('.gdpr-iframe-message').hide();
            $('.gdpr-iframe').each(function() {
              $(this).attr("src", $(this).attr("gdpr-src"));
              if ($(this).attr("gdpr-height")) {
                  $(this).attr("height", $(this).attr("gdpr-height"));
              }
              else {
                  $(this).removeAttr("height");
              }
              if ($(this).attr("gdpr-width")) {
                  $(this).attr("width", $(this).attr("gdpr-width"));
              }
              else {
                  $(this).removeAttr("width");
              }
            });
          }
      });
    }

    // Prepare consent overlay for iframes link
    $('.consent-link').prepOverlay({
      subtype: 'ajax',
      filter: '#content',
      cssclass: 'overlay-privacy',
      formselector: '#form',
      closeselector: '[name="form.buttons.cancel"]',
      noform: function(el) {return $.plonepopups.noformerrorshow(el, 'reload');}
    });

});
