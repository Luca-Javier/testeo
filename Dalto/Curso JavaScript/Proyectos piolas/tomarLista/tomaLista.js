let cantidad = 0;
let presentes = 0;
let ausentes = 0;
let alumnos= [];

function lista(){
    ausencia = prompt("x está?");
    return ausencia;
}
lista();

for(cantidad; cantidad <= 2; cantidad++){


if(ausencia == "presente" || ausencia == "ausente"){
    if(ausencia == "presente"){
        alumnos[presentes] = prompt("tu apellido?");
        presentes++
    }
    else{
        ausentes++
    }
}
else{
    alert("habla bien boludo");
    cantidad--
}

lista();
}
/* while(cantidad <=5){
    alert(cantidad);
    lista();
} */
alert(`de ${cantidad} alumnos hay ${presentes} presentes y ${ausentes} ausentes`);
for(i of alumnos/* let i; i != presentes; i++  */){
alert(`los alumnos presentes son ${i}`);
}
