jQuery(document).ready(function($) {
  var modals = 0;

  var focusTrap = function(selector) {
    // Inspired by https://uxdesign.cc
    // add all the elements inside modal which you want to make focusable
    var focusableElements = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
    var modal = document.querySelector(selector); // select the modal by it's id
    var firstFocusableElement = modal.querySelectorAll(focusableElements)[0]; // get first element to be focused inside modal
    var focusableContent = modal.querySelectorAll(focusableElements);
    var lastFocusableElement = focusableContent[focusableContent.length - 1]; // get last element to be focused inside modal


    document.addEventListener('keydown', function(e) {
      let isTabPressed = e.key === 'Tab' || e.keyCode === 9;

      if (!isTabPressed) {
        return;
      }

      if (e.shiftKey) { // if shift key pressed for shift + tab combination
        if (document.activeElement === firstFocusableElement) {
          lastFocusableElement.focus(); // add focus for the last focusable element
          e.preventDefault();
        }
      } else { // if tab key is pressed
        if (document.activeElement === lastFocusableElement) { // if focused has reached to last focusable element then focus first focusable element after pressing tab
          firstFocusableElement.focus(); // add focus for the first focusable element
          e.preventDefault();
        }
      }
    });

  };

  $(document).keydown(function() {
    if($('.overlay:visible').length == 1 && modals == 0) {
      modals = 1;
      focusTrap('#' + $('.overlay:visible').attr('id'));
    } else if($('.overlay:visible').length == 0) {
      modals = 0;
    }
  });

});
