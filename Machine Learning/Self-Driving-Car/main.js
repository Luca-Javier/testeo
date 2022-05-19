const canvas = document.getElementById("myCanvas");
/* canvas.height = window.innerHeight;
canvas.width = 200; */

/* tenemos que asignarle un valor al canvas, un contexto */
const ctx  = canvas.getContext("2d"); 
/* ctx = contexto */
/* mi futuro objeto/car */
const car = new car(100,100,50,50) /* ubicacion x, = y, width, height. Both px */
car.draw(ctx);

/* tengo que ver un tutorial de canvas html */