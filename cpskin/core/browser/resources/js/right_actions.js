jQuery(document).ready(function($) {

  function hide_all() {
      $('#right-actions-viewlet .right-panel').addClass('hidden-right-panel');
      $('#right-actions-viewlet .right-panel').removeClass('shown-right-panel');
  }

  function toggle_useful_links(show) {
      hide_all();
      if (show) {
          $('#useful-links-container').removeClass('hidden-right-panel');
          $('#useful-links-container').addClass('shown-right-panel');
      }
  }

  function toggle_toc(show) {
      hide_all();
      if (show) {
          $('#table-of-contents-container').removeClass('hidden-right-panel');
          $('#table-of-contents-container').addClass('shown-right-panel');
      }
  }

  $('#useful-links-button').click(function(event) {
      show = $('#useful-links-container').hasClass('hidden-right-panel');
      toggle_useful_links(show);
      event.stopPropagation();
      event.preventDefault();
  });

  $('#table-of-contents-button').click(function(event) {
      show = $('#table-of-contents-container').hasClass('hidden-right-panel');
      toggle_toc(show);
      event.stopPropagation();
      event.preventDefault();
  });

  $('#document-toc a').click(function(event) {
      hide_all();
      event.stopPropagation();
  });


  $(window).click(function() {
      hide_all();
  });
  });

});
