/* Funcio color background botons*/ 
$("button").click(function() {
    let trPare = $(this).parent().parent()
    let buttons = trPare.find("button")
    buttons.each(function() {
        $( this ).removeClass( "active" );
    });

    if($(this).parent()[0].tagName=="TD"){
        $(this).addClass("active")
    }
    if($(this).hasClass('collapsed')){
        $( this ).removeClass( "active" );
    }
});
/*Funcio filtrar taula nom*/
$(document).ready(function(){
  $("#alumne").on("keyup", function() {
    let value = $(this).val().toLowerCase();
    $("#taulaSolicituds tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
/*Funcio filtrar taula grup */ 
$('#filter').change(function() {
  let grup = $(this).val()
  $("#taulaSolicituds tr").filter(function() {
    if(grup =="Tots") return $(this).toggle(true)
    $(this).toggle($(this).attr('grup') == grup )
  });
});
