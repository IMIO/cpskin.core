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

  function toggle_share_viewlet(show) {
      hide_all();
      if (show) {
          $('#social-share-container').removeClass('hidden-right-panel');
          $('#social-share-container').addClass('shown-right-panel');
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

  $('#social-share').click(function(event) {
      show = $('#social-share-container').hasClass('hidden-right-panel');
      toggle_share_viewlet(show);
      event.stopPropagation();
      event.preventDefault();
  });

  $(window).click(function() {
      hide_all();
  });

  $(window).scroll(function(e) {
      if ($(".scroller_anchor").length == 0) return;
      var scroller_anchor = $(".scroller_anchor").offset().top;

      if ($(this).scrollTop() >= scroller_anchor && $('#right-actions-viewlet-inner').css('position') != 'fixed')
      {   // Fix panel at the top of the screen when users scrolls below anchor.
          top_position = $('#top-navigation-inner').height();
          $('#right-actions-viewlet-inner').css({
              'position': 'fixed',
              'top': top_position + 'px'
          });
      }
      else if (($(this).scrollTop() < scroller_anchor) && $('#right-actions-viewlet-inner').css('position') != 'relative')
      {   // Put it back to its original position when users scrolls back
          $('#right-actions-viewlet-inner').css({
              'position': 'relative'
          });
      }
  });

});
