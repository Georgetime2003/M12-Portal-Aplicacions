function obrir_modal_modificar_grups_aplicacio(url){
    $('#modalModificarGrups').load(url,function(){
        $(this).modal('show');
    });
}

function obrir_modal_modificar_encarregats_aplicacio(url){
    $('#modalModificarEncarregats').load(url,function(){
        $(this).modal('show');
        $(this).find("input")[1].add
        $(this).find("input")[1].addEventListener('keyup', test);
    });
    
}

function test() {
    let encarregatText = $(this).val();
    let totsLi= $(this).parent().parent().parent().find('li')
    totsLi.each(function(){
        $(this).toggle($(this).children().text().toLowerCase().indexOf(encarregatText) > -1)
    });     
};        
