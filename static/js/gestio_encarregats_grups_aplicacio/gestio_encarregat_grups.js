function obrir_modal_modificar_grups_aplicacio(url){
    $('#modalModificarGrups').load(url,function(){
        $(this).modal('show');
    });
}

function obrir_modal_modificar_encarregats_aplicacio(url){
    $('#modalModificarEncarregats').load(url,function(){
        $(this).modal('show');
    });
}