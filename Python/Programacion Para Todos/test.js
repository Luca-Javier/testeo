/* para compara con IF_test */
p1 = prompt("2 + 2 = ");
if (p1 == 4){
  document.write("Correcto")
  p2 = prompt("3 + 3 = ")
  if(p2 == 6){
    document.write("Correcto")
    p3 = prompt("4 + 4 = ")
    if(p3 == 8){
      document.write("Correcto, sos un genio")
    }else{
      alert("Fail")
    }
  }else{
    alert("Fail")
  }
}else{
  alert("Fail")
}