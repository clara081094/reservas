#!/usr/bin/php -q 

<?php 
require 'phpagi.php'; 
$agi    = new AGI(); 
$mensaje = $argv[1]; 
$fecha =  $argv[2];
echo "Numero: ".$no."\n";

$numero = substr($mensaje,30,9);
$monto = (int)substr($mensaje,52,4);

//$numero = '990893138';
//$monto = (int)'5.00';
//$fecha = '2005-12-12 06:06:07';

$sql1="select RES_ID from RESERVA r inner join TARIFA t on r.TARIFA_TAR_ID = t.TAR_ID where r.RES_CUENTADM='".$numero."' AND r.ESTADO_EST_ID=3 AND t.TAR_COSTO=".$monto.";";
//$sql2="insert into poner (campo1,campo2) values ('".$mensaje."',".$fecha.");"; 

//$strToken=strtok($mensaje,";"); 
//$sql=$sql.$strToken."','"; 

//$sender=strtok(";"); 
//$sql=$sql.$sender."',"; 

/*$monto=strtok(";"); 
$sql=$sql.$monto.","; 

$fecha="STR_TO_DATE('".strtok(";")."','%m/%d/%y')"; 
$sql=$sql.$fecha.","; 

$hora="STR_TO_DATE('".strtok(";")."','%H:%i:%s')"; 
$sql=$sql.$hora.")"; 
*/
echo "Script generado: ".$sql1."\n"; 
//echo "El mensaje es ".$mensaje."\n"; 
$db     = 'comercio'; 
$dbuser = 'root'; 
$dbpass = 'root'; 
$dbhost = 'localhost'; 
 
mysql_connect($dbhost,$dbuser,$dbpass); 
mysql_select_db($db) or die("could not open database"); 
$result = mysql_query($sql1);
$row = mysql_fetch_row($result)[0]; 
echo "Resultado de consulta: ".$row."\n";

if(!is_null($row))
{
	$sql2="insert into PAGO (PAGO_CUENTADM, PAGO_MONTO, PAGO_FECHA) values ('".$numero."', ".$monto.", '".$fecha."');";
	echo "Script generado: ".$sql2."\n"; 
	mysql_connect($dbhost,$dbuser,$dbpass); 
	mysql_select_db($db) or die("could not open database"); 
	$result2 = mysql_query($sql2);
	echo "resultado: ".$result2."\n"; 
	$sql3="select PAGO_ID from PAGO where PAGO_FECHA = '".$fecha."';";
	$result3 = mysql_query($sql3);
	$row2 = mysql_fetch_row($result3)[0]; 
	echo "Resultado de consulta: ".$row2."\n";
	$sql4="update RESERVA SET PAGO_PAGO_ID='".$row2."', ESTADO_EST_ID='1' WHERE RES_ID=".$row.";";
	$result4 = mysql_query($sql4);
	echo "resultado: ".$result4."\n";
	$dongle = "dongle sms dongle0 ";
 	$ini = "'";
 	$message = "Su pago se realizo con exito";
 	$runcommand = '/usr/sbin/asterisk -rx'.$ini.$dongle.$numero." ".$message.$ini."";
 	echo $runcommand;
	exec($runcommand);
}
 
?>