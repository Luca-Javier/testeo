/* 9:35:05 */
const SelectKey =(eleccion)=>{
    const compraSelect = document.querySelector(".seleccionedKey")
    /* tranformo lo que me llega en texto, sino es un objeto HTML */
    eleccion = eleccion.innerHTML;
    compraSelect.setAttribute("value",eleccion);
}

function CrearLLave(nombre,modelo,precio,img){
    this.nombre = nombre;
    this.modelo = modelo;
    this.precio = precio;
    /* creamos el contenedor en el articulo */
    const article = document.querySelector(".articulo")
    const contenedores = document.createElement("div");
    contenedores.classList.add("contenedorLLave");
    /* mi contenedor main al articulo */
    article.appendChild(contenedores);
    /* elemento imagen */
    const imagen = document.createElement("img");
    imagen.classList.add("imagenLLave");
    imagen.setAttribute("src", img);
    /* crear elemntos se llave */
    const llaveName = document.createElement("h2");
    const llaveModel = document.createElement("h3");
    const llaveCost = document.createElement("p");
    /* asignar valores. No asigne imagen */
    llaveName.innerHTML = this.nombre;
    llaveModel.innerHTML = this.modelo;
    llaveCost.innerHTML = `$${this.precio}`;
    /* agregar todo al articulo */
    contenedores.appendChild(imagen);
    contenedores.appendChild(llaveName);
    contenedores.appendChild(llaveModel);
    contenedores.appendChild(llaveCost);
    /* evento click + funcion flecha para llevar el nombre elegio a un input */
    contenedores.addEventListener("click", ()=>{SelectKey(llaveName)});
}
/* mis llaves */
CrearLLave("LLave amarilla", "Keykey", "100", "miLLave.jpg");
CrearLLave("LLave blanca", "fabricator", "120", "miLLave2.jpg");
CrearLLave("LLave romana", "fabricator", "150", "miLLave.jpg");
CrearLLave("LLave de hierro", "Keykey", "210", "miLLave2.jpg");

