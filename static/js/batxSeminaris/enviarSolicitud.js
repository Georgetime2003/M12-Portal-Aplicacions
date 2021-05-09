'use strict';
const departamentPrimeraOpcio = document.getElementById("departamentPrimeraOpcio")
const departamentSegonaOpcio = document.getElementById("departamentSegonaOpcio")
const departamentTerceraOpcio = document.getElementById("departamentTerceraOpcio")

const seminariPrimeraOpcio = document.getElementById("seminariPrimeraOpcio")
const seminariSegonaOpcio = document.getElementById("seminariSegonaOpcio")
const seminariTerceraOpcio = document.getElementById("seminariTerceraOpcio")


const segonaOpcioDiv = document.getElementById("segonaOpcio")
const terceraOpcioDiv = document.getElementById("terceraOpcio")

const formulariSolicituds = document.getElementById("formulariSolicituds")
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const botoSubmit = document.getElementById('botoSubmit')

let departamentSelecionatPrimeraOpcio;
let departamentSelecionatSegonaOpcio;

departamentPrimeraOpcio.addEventListener('change', e=>{
    departamentSelecionatPrimeraOpcio = e.target.value
    $("#seminariPrimeraOpcio").find('option').not(':first').remove();
    $("#seminariSegonaOpcio").find('option').not(':first').remove();
    $("#departamentSegonaOpcio").find('option').not(':first').remove();
    $("#seminariTerceraOpcio").find('option').not(':first').remove();
    $("#departamentTerceraOpcio").find('option').not(':first').remove();
    $.ajax({
        type: 'GET',
        url: `seminari-json/${departamentSelecionatPrimeraOpcio}/`,
        success: function(response){
            const modelsData = response.data 
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.nom
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.id)
                seminariPrimeraOpcio.appendChild(option)
            })
            seminariPrimeraOpcio.addEventListener('change', e=>{
                segonaOpcioDiv.classList.remove('d-none')
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})

seminariPrimeraOpcio.addEventListener('change', e=>{
    $.ajax({
        type: 'GET',
        url: `departament-json/${departamentSelecionatPrimeraOpcio}/`,
        success: function(response){
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.nom
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.id)
                departamentSegonaOpcio.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    }) 
})
departamentSegonaOpcio.addEventListener('change', e=>{
    departamentSelecionatSegonaOpcio = e.target.value
    $("#seminariSegonaOpcio").find('option').not(':first').remove();
    $("#departamentTerceraOpcio").find('option').not(':first').remove();
    $.ajax({
        type: 'GET',
        url: `seminari-json/${departamentSelecionatSegonaOpcio}/`,
        success: function(response){
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.nom
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.id)
                seminariSegonaOpcio.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})
seminariSegonaOpcio.addEventListener('change', e=>{
    terceraOpcioDiv.classList.remove('d-none')
    $("#seminariTerceraOpcio").find('option').not(':first').remove();
    $("#departamentTerceraOpcio").find('option').not(':first').remove();
    $.ajax({
        type: 'GET',
        url: `departament-json/${departamentSelecionatPrimeraOpcio}/${departamentSelecionatSegonaOpcio}/`,
        success: function(response){
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.nom
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.id)
                departamentTerceraOpcio.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})

departamentTerceraOpcio.addEventListener('change', e=>{
    const departamentTerceraOpcioValue = e.target.value
    $.ajax({
        type: 'GET',
        url: `seminari-json/${departamentTerceraOpcioValue}/`,
        success: function(response){
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.nom
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.id)
                seminariTerceraOpcio.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
    seminariTerceraOpcio.addEventListener('change', e=>{
        botoSubmit.classList.remove('d-none')
    })
})

Array.prototype.slice.call(formulariSolicituds).forEach(function(form){
    formulariSolicituds.addEventListener('submit', e=>{
        if(!form.checkValidity()){
            e.preventDefault()
            e.stopPropagation()
        }
        form.classList.add("was-validated")
    },false)
})

var forms = document.querySelectorAll('.needs-validation')

// Loop over them and prevent submission
Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener('submit', function (event) {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }else{
        $.ajax({
            type: 'POST',
            url: '/batxilleratProjecte/',
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'departamentPrimeraOpcio': departamentPrimeraOpcio.value,
                'seminariPrimeraOpcio': seminariPrimeraOpcio.value,
                'plantajamentPrimeraOpcio': $('#plantajamentPrimeraOpcio').val(),
                'departamentSegonaOpcio': departamentSegonaOpcio.value,
                'seminariSegonaOpcio': seminariSegonaOpcio.value,
                'plantajamentSegonaOpcio': $('#plantajamentSegonaOpcio').val(),
                'departamentTerceraOpcio': departamentTerceraOpcio.value,
                'seminariTerceraOpcio': seminariTerceraOpcio.value,
                'plantajamentTerceraOpcio': $('#plantajamentTerceraOpcio').val(),
            },
            success: function(response){
                console.log(response)
            },
            error: function(error){
                console.log(error)
            }
        })
      }
      form.classList.add('was-validated')
    }, false)
})