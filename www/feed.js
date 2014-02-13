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


    /*
    $('.ui.rating')
      .rating({
        clearable: true
      })
    ;
    $('.ui.dropdown')
      .dropdown()
    ;
    */
  })
;
