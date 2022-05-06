const Neurona = new brain.NeuralNetwork(); 
const texto = document.querySelector(".texto");

function iniciar(color){
  console.log(color);
let ColorRGB = {
  r: color.rgb[0]/255,
  g: color.rgb[1]/255,
  b: color.rgb[2]/255
}
};

Neurona.train([
  {input:{r: 0, g: 0, b: 0}, output: {negro: 1 }},
  {input:{r: 1, g: 1, b: 1}, output: {blanco: 1 }}
]);

let rta = brain.likely({})

let Resultado = Neurona.run(ColorRGB);
if(Resultado.blanco > 0.5){
  texto.style.color = "black";
}else if(Resultado.negro > 0.5){
  texto.style.color = "white";
}
/* para mi tendria que sea >= 0.5 porque daria error si da justo */
console.log("hola")


/* window.onload = iniciar(); */







/* let trainedNET;

function encode(arg){
  return arg.split("").map( x=>(x.charCodeAt(0)));

}; */