function mostrarPres(reqId, presId, resId) {
   var seleccion = document.getElementById(reqId).value;
   var campoPres = document.getElementById(presId);
   var present = campoPres.querySelector('select');
   var campoRes = document.getElementById(resId);
   var resultado = campoRes.querySelector('input');
 
   console.log(`mostrarPres called with reqId=${reqId}, presId=${presId}, resId=${resId}, seleccion=${seleccion}`);
 
   if (seleccion === "1") {
     campoPres.style.display = "block";
     campoRes.style.display = "block";
   } else {
     campoPres.style.display = "none";
     present.children[1].selected = true;
     campoRes.style.display = "none";
     if (resultado) {
       resultado.value = 'NO APLICA/NO PRESENTADA';
       resultado.disabled = true; 
     }
   }
 }
 
 function mostrarRes(presId, campoId) {
   var seleccion = document.getElementById(presId).value;
   var campo = document.getElementById(campoId).querySelector('input'); 
 
   console.log(`mostrarRes called with presId=${presId}, campoId=${campoId}, seleccion=${seleccion}`);
 
   if (seleccion === "1") {
     if (campo) {
       campo.disabled = false;
     }
   } else {
     if (campo) {
       campo.value = 'NO APLICA/NO PRESENTADA';
       campo.disabled = true;
     }
   }
 }
 
