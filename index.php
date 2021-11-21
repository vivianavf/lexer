<? php
// cadneas
$hola = 'hola';
$saludo = "hola" . " a todos" . 'hoy';
$cadena = 'hola' . $saludo . $saludo;
$cadena .= $cadena ;
$cadena .= $cadena . "hola" ;
$cadena .= "hola que tal";

$flot = +-1.222;
$flot = -+1.222;
$flot = -+-+-+1.222;
$flot = +-+-+-+-1.222;
$a = 3 + $flot * 2;
$b = 2 * 2 + 6 - 6;
$b--;
$a++;
$c = $a+$b/2 + 11;
$d = $a-$b/3;

if($c>$d){
  echo "la variable a es mayor a b";
}elseif($c===$d){
  echo "la variable a es igual a b";
}else{
  echo "la variable a es menor a b";
}

if (!$a != $b and $c >= $d){
  echo "a y b son iguales, c y d son iguales";
}
$x = 1;
while($x <= 5) {
  echo "The number is: $x <br>";
  $x++;
}
$x = 0;

while($x <= 100) {
  echo "The number is: $x <br>";
  $x+=10;
}
for ($x = 0; $x <= 10; $x++) {
  echo "The number is: $x <br>";
}
for ($x = 0; $x <= 100; $x+=10) {
  echo "The number is: $x <br>";
}

//Varios tipos de creación de arrays
array("foo", "bar", "hello", "world");
array("foo" => "bar", "bar" => "foo", 100   => -100, -100  => 100,);
array(1 => "a", "1" => "b", 1.5 => "c", true => "d");
array("foo" => "bar", "bar" => "foo");
array("a", "b", 6 => "c", "d");



?>
