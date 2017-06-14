jQuery(document).ready(function($) {

  $('#useful-links-button').click(function() {
      $('#useful-links-container').toggleClass('hidden-right-panel');
      $('#useful-links-container').toggleClass('shown-right-panel');
  });
  $('#table-of-contents-button').click(function() {
      $('#table-of-contents-container').toggleClass('hidden-right-panel');
      $('#table-of-contents-container').toggleClass('shown-right-panel');
  });

});
