/* vamos a probar por separado como hacer un circulo con movimiento */
const canvas = document.querySelector(".canvas");

canvas.width = window.innerWidth; /* estos se establecen la primera vez, por lo que si agrandamos la pantalla ya no se ve */
canvas.height = window.innerHeight;
let c = canvas.getContext("2d");

/* anotaciones:
innerWidth agarra la pantalla que usamos al momento, si agrandamos y le pusimos a nuestro circulo ese limite, va a desaparecer */

let x = 200;
let dx = 7; /* dx sería como el estandar de velocidad en eje x */
let radius = 50; /* radio del circulo, si lo sumamos a la posicion x, tenemos que el circulo no sale de pantalla y rebota. Si sale de la pantalla vuelve full igual */
function animate(){
c.beginPath(); 
/* let x = Math.random() * window.innerWidth; 
let y = Math.random() * window.innerHeight; */
c.arc(x,200,radius,0,7,false);
x+=dx;
if(x + radius >= innerWidth || x - radius <= 0){ /* x - radio es igual a rebotar en la pared izq donde x es 0 y el radio sigue en pantalla */
  dx = -dx; /* esto sirve para cambiar a positivo y luego a negativo tmb */
}
/* if(x < innerWidth){
  dx = -1*dx;
} */
c.clearRect(0, 0, innerWidth, innerHeight); /* borra el creado y lo usamos para dar efecto de que se mueve y no de que genera un gusano */ /* entiendo que el margen EJ: x e y que le damos es como el espacio donde va a borrar, si pongo 200 borra la mitad y si pongo 0 no salva nada, o sea borra todo */
c.strokeStyle = "blue";
c.stroke();
requestAnimationFrame(animate);
}
animate();
/* function animate(){
  requestAnimationFrame(animate);  crea un intervalo que sería el de cada frame(60f/1s). No entiendo porque si ejecuto la function animate se sigue ejecutando la linea de abajo
  console.log("hola");
}
animate(); */