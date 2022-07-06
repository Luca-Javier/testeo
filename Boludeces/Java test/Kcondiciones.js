let num = 0;
/* en JS como que le if no necesita una un bool. Solo necesita una accion 
que sea posible */
if(num = 10){
 alert(num);
}
let palabras = ["hola", "hoy", "pepe", "esta", "en", "casa"];
let escritor;

let i = 0;
while (escritor = palabras[i]){
document.write(escritor + "<br>");
i++
}
document.write("FIN <br><br>");

function array(){
  palabras.forEach(h => {
  document.write(h + "<br>");
});
document.write("FIN foreach");
}
/* Tengo que hacer una funcion por que 
palabras.foreach 
es un metodo. CREO
EN VERDAD NO ENTIENDO ESTO */
array();
