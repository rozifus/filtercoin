
$(document)
  .ready(function() {
    $('.filter.menu .item')
      .tab()
    ;

    $('.ui.sidebar')
      .sidebar('attach events', '.launch.button')
    ;

    $('.ui.accordion').first()
      .accordion()
    ;

    inter.init();
    console.log('INIT')
  })
;
