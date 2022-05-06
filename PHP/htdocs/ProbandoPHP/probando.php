<?php
/* 
$nombre = $_GET["nombre"];
$apellido = $_GET["apellido"];

echo '<a href="http://localhost:8080/ProbandoPHP/index2.php">'.$nombre*$apellido."</a>";

 */
class conection{
  function conexion(){

    $host = 'localhost';
    $dbname = 'test1';
    $username = 'luca';
    $password = 'root';
    $puerto = 1433;

    try{
      $con = new PDO ("sqlsrv:Server=$host,$puerto;Database=$dbname",$username,$password);
      echo "se conecto";
    }
    catch(PDOException $exp){
      echo "error $exp";
    }







  }
  







}
?> 