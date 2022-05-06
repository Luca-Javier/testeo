const colorSelec = document.getElementById("color");
const salida = document.querySelector("#contenedor");
const fondo = document.querySelector(".title");

colorSelec.addEventListener("input", ()=>{
  const valor = colorSelec.value;
  salida.setAttribute("value",valor);
/*   salida.innerHTML= valor;  */
  console.log(valor);
  fondo.style.backgroundColor = valor;
});