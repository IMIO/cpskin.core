jQuery(document).ready(function($) {

  var add_line, remove_line, update_clone;

  add_line = function() {
    var container, clone, line;

    container = $(this).parent('div.multiline-widget');
    line = container.find('div.element:last');
    clone = line.clone();
    update_clone(clone);
    clone.insertBefore($(this));
  };

  remove_line = function() {
    var line, latest, container;

    line = $(this).parent('div.element');
    container = line.parent();
    if (container.find('div.element').length === 1) {
      update_clone(line);
    } else {
      line.remove();
    }
  };

  update_clone = function(obj) {
    obj.find('input[type="text"]').attr('value', '');
    obj.find('input.remove').click(remove_line);
  };

  $('div.multiline-widget input.add').click(add_line);
  $('div.multiline-widget input.remove').click(remove_line);
});
