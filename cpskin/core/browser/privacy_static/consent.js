jQuery(function($) {

  var reasons = [];
  var setConsentForm = function() {
    if (reasons.length > 0) {
      $('#gdpr-consent-banner a').prepOverlay({
        subtype: 'ajax',
        filter: '#content',
        cssclass: 'overlay-privacy',
        formselector: '#form',
        closeselector: '[name="form.buttons.cancel"]',
        noform: function(el) {return $.plonepopups.noformerrorshow(el, 'reload');}
      });
    } else {
      $('#gdpr-consent-banner').remove();
    }
  };

  var url = $('#gdpr-consent-banner form').data('json-url');
  $.ajax({
    type: "GET",
    url: url,
    headers: {"Cache-Control": "no-cache"},
  }).done(function(data) {
    reasons = data;
    setConsentForm();
    // Open overaly on page load
    $("#gdpr-consent-banner a").click();
  });
});
