
$(document)
  .ready(function() {
        $('.filter.menu .item')
      .tab()
    ;

    $('.ui.sidebar')
      .sidebar('attach events', '.launch.button')
    ;

    interface = new Interface();
    interface.init();
    console.log('INIT')
  })
;
