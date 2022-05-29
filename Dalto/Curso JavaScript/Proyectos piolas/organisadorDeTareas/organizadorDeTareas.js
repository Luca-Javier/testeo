console.time()
/* const tiempoTotal = 14; dias / 2 semanas */

/* let horaTotal = 112; */ /* tmb es el tiempo para gastar */
/* let horaPorDia = 8; */
/* let horaTrabajo = 56; */

let horaEstudio = ["estudio",24];
let horaTps = ["tps",24];
let horaCasa = ["casa",8]; 

let tareas = [horaEstudio, horaTps, horaCasa];



let estudiado = 0;
let tpf = 0;
let casado = 0;


function numero(){
    numerinho:
    for(let i = 0; i == 0; i++){
    let num = Math.random()*3
    let select = Math.trunc(num)
    
    if(tareas[select][1] != 0 && select != undefined){
        /* document.write(select) */ /* los numero que salen bien */
        return select;
    }else{
        /* document.write("---"+select+"---") */ /* los que no */
        i--;
        continue numerinho;
    }
    }
    
}

for(let dias = 0; dias != 14; dias++){


    let nume = dias;
    nume++;
    let dia = "Día "+nume+":";

    forinho:
    for(let horas = 4; horas != 0; --horas){
        
        select = numero()
        /* if(select == undefined){
            horas++;
            continue forinho;
            
        } */
        

        if(tareas[select][0] == "estudio" && tareas[select][1] != 0){
            
            estudiado++;
            
        }else if( tareas[select][0] == "tps" && tareas[select][1] != 0){
            
            tpf++;
            
        }else if(tareas[select][0] == "casa" && tareas[select][1] != 0){
            
            casado++;
        
        }
        else{
            horas++;
            continue forinho;
        }
        tareas[select][1]--;
    }
    console.group(dia)
    console.log(`
    Horas estudiadas: ${estudiado}
    Horas haciendo tps: ${tpf}
    Horas haciendo cosas de casa: ${casado}
    Horas trabajando: 4`);
    console.groupEnd(dia)
    document.write(`${dia}<br>
        Horas estudiadas: ${estudiado}<br>
        Horas haciendo tps: ${tpf}<br>
        Horas haciendo cosas de casa: ${casado}<br>
        Horas trabajando: 4<br><br>`);
        tpf = 0;
        estudiado = 0;
        casado = 0;

} 
 

console.timeEnd()
