const inps = document.querySelectorAll('form .datosCand');
const cat = document.querySelectorAll('form .catalogo');
let env = document.getElementById('enviar');
env.addEventListener("click", enviar);


function validarInputs() {
    let valido = true;
    for (let x = 0; x < inps.length; x++) {
        if (inps[x].value.trim() == '' || !inps[x].validity.valid) {
            valido = false;
            inps[x].style.background='#FFDDDD';
            //break;
        } /*else {
            inps[x].style.background='#FFFFFF';
        }*/
    }
    return valido;
}

function validarCatalogos() {
    let valid = true;
    for (let y = 0; y < cat.length; y++) {
        if (cat[y].value == 0 || !cat[y].validity.valid) {
            valid = false;
            cat[y].style.background='#FFDDDD';
            //break;
        } /*else {
            cat[y].style.background='#FFFFFF';
        }*/
    }
    return valid;
}

function enviar() {
    event.preventDefault();
    if (validarInputs() && validarCatalogos()) {
        alert("Valores válidos.");
        document.formulario.submit();
    } else {
        alert("Debes llenar correctamente los campos.");
    }
}

document.formulario.addEventListener("input", validacion, false);
function validacion(e) {
    let elemento = e.target;
    if (elemento.validity.valid) {
        elemento.style.background='#FFFFFF';
    } else {
        elemento.style.background='#FFDDDD';
    }
}