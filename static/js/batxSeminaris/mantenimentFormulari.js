function obrir_modal_crear_departament(url){
    $('#creacio').load(url,function(){
        $(this).modal('show');
    });
}
