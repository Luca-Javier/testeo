let alumnos = [];

const listado = ()=>{
    for(let i = 0; i < 2; i++)
    alumnos[i] = [prompt("Nombre alumno"),0]
    
}

const presentismo = ()=>{
    for(let i = 0; i < 2; i++){
        for(let j = 0; j < 6; j++){
           let p = prompt(`${alumnos[i][0]} está presente?(p or nothing)`)
           if(p == "p"){
               alumnos[i][1]++;
           }
        }
        
    }
}
listado();
presentismo();
for(let alumno in alumnos){
    document.write(`El alumno ${alumnos[alumno][0]} tiene ${alumnos[alumno][1]} asistencias`);
    if(alumnos[alumno][1] < (6*50/100)){
        document.write(`<a style= "color : red"> este alumno reprobo por no cumplir con la mitad de asistencias </a><br>`);
    }else{
    document.write("<br>")
    }
}

/* sum = [];
sum[0] = [42,33,55];
document.write(sum[0][1]+ "<br>");
if(sum[0][1] > 20){
    document.write("h")
}
else{
    document.write("f")
} */
