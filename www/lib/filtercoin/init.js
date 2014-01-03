
$(document)
  .ready(function() {

    interface = new Interface();
    interface.init();
    console.log('INIT')

    $('.filter.menu .item')
      .tab()
    ;

    $('.ui.sidebar')
      .sidebar('attach events', '.launch.button')
    ;
  })
;
