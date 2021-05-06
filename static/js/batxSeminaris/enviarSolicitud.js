const departamentPrimeraOpcio = document.getElementById("departamentPrimeraOpcio")
const departamentSegonaOpcio = document.getElementById("departamentSegonaOpcio")
const seminariPrimeraOpcio = document.getElementById("seminariPrimeraOpcio")
const seminariSegonaOpcio = document.getElementById("seminariSegonaOpcio")
const segonaOpcioDiv = document.getElementById("segonaOpcio")
const terceraOpcioDiv = document.getElementById("terceraOpcio")
/*Opcio seminari per defecte */ 
const seminariDefaultOpcio = document.createElement('option');
seminariDefaultOpcio.textContent = "Selecciona seminari";
seminariDefaultOpcio.selected = true;
seminariDefaultOpcio.disabled = true; 
/*Opcio departament per defecte */ 
const departamentDefaultOpcio = document.createElement('option');
departamentDefaultOpcio.textContent = "Selecciona Departament";
departamentDefaultOpcio.selected = true;
departamentDefaultOpcio.disabled = true; 

departamentPrimeraOpcio.addEventListener('change', e=>{
    const departamentSelecionat = e.target.value
    seminariPrimeraOpcio.innerHTML = ""
    seminariSegonaOpcio.innerHTML = ""
    $.ajax({
        type: 'GET',
        url: `seminari-json/${departamentSelecionat}/`,
        success: function(response){
            const modelsData = response.data 
            seminariPrimeraOpcio.appendChild(seminariDefaultOpcio)
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

departamentPrimeraOpcio.addEventListener('change', e=>{
    departamentSegonaOpcio.innerHTML = ""
    let departamentPrimeraOpcioValue = departamentPrimeraOpcio.value
    $.ajax({
        type: 'GET',
        url: `departament-json/${departamentPrimeraOpcioValue}/`,
        success: function(response){
            const modelsData = response.data
            departamentSegonaOpcio.appendChild(departamentDefaultOpcio)
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
    const departamentSelecionat = e.target.value
    console.log(departamentSelecionat)
    seminariSegonaOpcio.innerHTML = ""
    $.ajax({
        type: 'GET',
        url: `seminari-json/${departamentSelecionat}/`,
        success: function(response){
            const modelsData = response.data
            seminariSegonaOpcio.appendChild(seminariDefaultOpcio)
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.nom
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.id)
                seminariSegonaOpcio.appendChild(option)
            })

            seminariSegonaOpcio.addEventListener('change', e=>{
                terceraOpcioDiv.classList.remove('d-none')
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})