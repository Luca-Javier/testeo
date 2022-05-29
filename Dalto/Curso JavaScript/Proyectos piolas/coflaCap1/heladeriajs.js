let palitoDeAgua = 0.6 , palitoDeCrema = 1, bombomHeladix = 1.6 , bombomHlardo= 1.8,
bombomHelardovich = 1.7, potecito = 2.9, pote = 2.9;





let molto = prompt("por favor, ingresar el molto a gastar");

if(molto >= palitoDeAgua && molto < palitoDeCrema){
    alert("comprare del palito de agua");

}
else if(molto >= palitoDeCrema && molto < bombomHeladix){
    alert("comprate el palito de crema");
}
else if(molto >= bombomHeladix && molto < bombomHelardovich){
    alert("comprate el bombom heladix");
}
else if(molto >= bombomHelardovich && molto < bombomHlardo){
    alert("comprate el bombom heladovich");
}
else if(molto >= bombomHlardo && molto < potecito){
    alert("comprate el bombomhelardo");
}
else if(molto >= potecito){
    alert(`comprate el potecito o el pote. Tu vuelto sera ${molto - potecito}`);
}