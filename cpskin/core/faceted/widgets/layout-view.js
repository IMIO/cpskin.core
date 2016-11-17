Faceted.initializeLayoutWidget = function(evt){
  jQuery('div.faceted-layout-widget').each(function(){
    var wid = jQuery(this).attr('id');
    wid = wid.split('_')[0];
    var widget = new Faceted.RadioWidget(wid);
    query = jQuery.param(Faceted.Query, traditional=true);
    jQuery.bbq.pushState(query, 1);
  });
};

jQuery(document).ready(function(){
  jQuery(Faceted.Events).bind(
    Faceted.Events.INITIALIZE,
    Faceted.initializeLayoutWidget);
});
