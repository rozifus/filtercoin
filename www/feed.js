$(document)
  .ready(function() {

    $('.filter.menu .item')
      .tab()
    ;

    $('.ui.sidebar')
      .sidebar('attach events', '.launch.button')
    ;

    $('.ui.filter-modal')
      .modal()
    ;

    $('.ui.accordion')
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
