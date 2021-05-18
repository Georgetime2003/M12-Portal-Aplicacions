function obrir_modal_modificar_grups_aplicacio(url){
    $('#modalModificarGrups').load(url,function(){
        $(this).modal('show');
    });
}