<? php
// cadenas
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
  //comment
}
for ($x = 0; $x <= 10; $x++) {
  echo "The number is: $x <br>";
  //comment
}
for ($x = 0; $x <= 100; $x+=10) {
  echo "The number is: $x <br>";
}

//Varios tipos de creación de arrays
$array1 = array)"foo", "bar", "hello", "world");
$array2 = array("foo" => "bar", "bar" => "foo", 100   => -100, -100  => 100);
$array3 = array(1 => "a", "1" => "b", 1.5 => "c", true => "d");
$array4 = array("foo" => "bar", "bar" => "foo");
$array5 = array("a", "b", 6 => "c", "d");

$cars = array("Volvo", "BMW", "Toyota");
echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";
echo $array5[6];
$suma = $array2[100] + $array5[-100];

/* $arrayerror = array([1,2]=>"foo"); */
$array = array)4=>"foo);

//Booleans
$entradaverdadera = True;
$entradafalsa = False;

//conversion

(bool) 1
(bool) -2
(bool) ""

//functions
function writeMsg() {
  echo "Hello world!";
}

writeMsg(); // call the function

function familyName($fname) {
  echo "$fname Refsnes.<br>";
}

familyName("Jani");
familyName("Hege");
familyName("Stale");
familyName("Kai Jim");
familyName("Borge");


function familyName($fname, $year) {
  echo "$fname Refsnes. Born in $year <br>";
}

familyName("Hege", "1975");
familyName("Stale", "1978");
familyName("Kai Jim", "1983");

//classes
class Fruit {
  public $name;
  function set_name($name) {
    $this->name = $name;
  }
}
$apple = new Fruit();
$apple->set_name("Apple");

echo $apple->name;

$apple_name = $apple-> name;

class Fruit {
  // Properties
  public $name;
  public $color;

  // Methods
  function set_name($name) {
    $this->name = $name;
  }
  function get_name() {
    return $this->name;
  }
  function set_color($color) {
    $this->color = $color;
  }
  function get_color() {
    return $this->color;
  }
}

$apple = new Fruit();
$apple->set_name('Apple');
$apple->set_color('Red');

echo "Name: " . $apple->get_name();
echo "<br>";
echo "Color: " . $apple->get_color();

class Fruit {
  public $name;
  private $color;
  protected $weight;

  function set_name($n) {  // a public function (default)
    $this->name = $n;
  }
  protected function set_color($n) { // a protected function
    $this->color = $n;
  }
  private function set_weight($n) { // a private function
    $this->weight = $n;
  }
}


?>
