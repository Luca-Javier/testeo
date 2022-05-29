let numero = document.querySelector(".numero");
let num= 0;
let tiempo = console.time();
document.write(tiempo);
function sumar(){
  num++;
/*   if (num = 1){
    console.time();
  } */
  numero.setAttribute("value",num);
}

while(tiempo <= 60){
numero.addEventListener("click", sumar());
}
console.timeEnd();



