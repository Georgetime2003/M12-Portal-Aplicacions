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
var departament_id
function f1(objButton){  
    departament_id = objButton.value;
}
function obrir_modal_crear_seminari(url){
    $('#modalAfegirSeminari').load(url,function(){
        $(this).modal('show');
        let selectDepartaments =  document.getElementById("departamentId")
        console.log(departament_id)
        for(let i, j = 0; i = selectDepartaments.options[j]; j++) {
            if(i.value == departament_id) {
                selectDepartaments.selectedIndex = j;
                break;
            }
        }
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
