function obrir_modal_crear_departament(url){
    $('#modalAfegirDepartament').load(url,function(){
        $(this).modal('show');
    });
}
function obrir_modal_modificar_departament(url){
    $('#modalModificarDepartament').load(url,function(){
        $(this).modal('show');
    });
}

function obrir_modal_eliminar_departament(url){
    $('#modalEliminarDepartament').load(url,function(){
        $(this).modal('show');
    });
}
