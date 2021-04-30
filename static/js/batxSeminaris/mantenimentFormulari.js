//Funcions per obrir els modals de departament 
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
//Funcions per obrir els modals de Seminari
function obrir_modal_crear_seminari(url){
    $('#modalAfegirSeminari').load(url,function(){
        $(this).modal('show');
    });
}
function obrir_modal_modificar_seminari(url){
    $('#modalModificarSeminari').load(url,function(){
        $(this).modal('show');
    });
}

function obrir_modal_eliminar_seminari(url){
    $('#modalEliminarSeminari').load(url,function(){
        $(this).modal('show');
    });
}

