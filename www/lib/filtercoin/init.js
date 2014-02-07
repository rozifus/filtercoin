
$(document)
  .ready(function() {
        $('.filter.menu .item')
      .tab()
    ;

    $('.ui.sidebar')
      .sidebar('attach events', '.launch.button')
    ;

    inter.init();
    console.log('INIT')
  })
;
