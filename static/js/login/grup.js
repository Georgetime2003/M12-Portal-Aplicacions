const forms = document.querySelectorAll('.needs-validation')
const curs = document.getElementById('curs')
const grup = document.getElementById('grup')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
print(csrf)
// Validacio formulari grups
Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
        }else{
            event.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/grup/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'grup': grup.value,
                },
                success: function(response){
                    location.href="/" 
                },
                error: function(error){
                    console.log(error)
                }
            })
        }
        form.classList.add('was-validated')
    }, false)
})
// Mostrar desplegable grups al desplegar cursos
curs.addEventListener('change', e=>{
    $("#grup").find('option').not(':first').remove();
    const cursValue = e.target.value
    $.ajax({
        type: 'GET',
        url: `/grups-json/${cursValue}/`,
        success: function(response){
            const modelsData = response.data
            console.log(modelsData)
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.name
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.id)
                grup.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})
