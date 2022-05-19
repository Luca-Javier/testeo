const canvas = document.querySelector(".canvas");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let c = canvas.getContext("2d");
c.fillStyle = "steelblue"; /* color. Lo tengo que poner antes de crearlos */
/* universalmente se usa c para llamar al contexto (el otro uso ctx y en MDN tmb se usa) */
c.fillRect(100, 100, 100, 100);/* es una funcion real */ /* se le pasan los parametros que tiene un 2d */
c.fillRect(300, 400, 100, 100); /* rect de rectangulo */
c.fillStyle = "red";
c.fillRect(500, 200, 100, 100); /* x, y, width, height */ /* x e y son left y top */

c.beginPath(); /* inicia el proceso */
c.strokeStyle = "red" /* en español es empezar camino, vamos a trazar una linea */
c.moveTo(250,200); /* si mantengo el click arriba veo que es la ubicacion del path(camino) */
c.lineTo(400,300);
c.strokeStyle = "blue" /* agarra a todos y se aplica por cascada */
c.lineTo(500,600);
c.lineTo(520,200)
c.strokeStyle = "violet" /* no importa donde lo ponga. Es el color */
c.stroke(); /* muetra la linea */ /* termina el proceso */

c.beginPath(); /* empieza un camino, que no hace falta mover las lineas, si comento el path del for hay una linea que sigue a cada objeto porque no se como cerrar este y les afecta xd */
/* c.arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void */ /* a la mierda que es largo este */
c.arc(200,200,50,0,7,false);/* radius = que tan grande el circulo, endAngle: (creo) cuantos radianes recorre el circulo(con 7 basta y sobra), counterclockwise: sentido anti horario (malardo)*/
c.strokeStyle = "green";
c.stroke();
/* no se como cerrar el path xd */

for (let i = 0; i <= 20; i++){ /* pongo 200k y se pone toda la pantalla azul xd */
  c.beginPath(); /* lo pongo para que cada circulo sea un camino y no me genere lineas el path de arriba que no se cerrar */
  /* c.arc(200,200,50,0,7,false); */
  let x = Math.random() * window.innerWidth; /* math.random genera un numero enter 0-1 y si multiplico por la pantalla temrina quedando adentro teniandola de margen entero */
  let y = Math.random() * window.innerHeight;
  c.arc(x,y,50,0,7,false);
  c.strokeStyle = "blue";
  c.stroke();
}
c.str
