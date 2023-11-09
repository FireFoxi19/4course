<html>
<header>
    <a href = "index.php">HOME<br/></a>
</header>
</html>
<?php

echo "ЗАДАЧА 1 <br>";
$treug = [];
for($n = 1; $n <= 10; $n++)
{
    $treug[] = $n * ($n + 1)/2;
}
$treugStr = implode("  ", $treug);
echo "Массив треугольных чисел: " . $treugStr . "<br>";

$kvd = [];
for($i = 1; $i <= 10; $i++)
{
    $kvd[] = $i * $i;
}
$kvdStr = implode("  ", $kvd);
echo "Квадраты чисел: " . $kvdStr . "<br>";

$rez = [];
$rez = array_merge($treug, $kvd);
$rezStr = implode("  ", $rez);
echo "Объединеные массивы: " . $rezStr . "<br>";

sort($rez);
$rezStr = implode("  ", $rez);
echo "Отсортированный массив: " . $rezStr . "<br>";

array_shift($rez);
$rezStr = implode("  ", $rez);
echo "Удалили первый элемент: " . $rezStr . "<br>";

$rez1 = [];
$rez1 = array_unique($rez);
$rez1Str = implode("  ", $rez1);
echo "Удалили повторяющиеся элементы: " . $rez1Str . "<br><br>";

echo "ЗАДАЧА 2<br>";
$treug = [];
$kvd = [];
for($n = 1; $n <= 30; $n++)
{
    $treug[] = $n * ($n + 1)/2;
    $kvd[] = $n * $n;
}

function getColor($val, $treug, $kvd)
{
    if ($val == 1 || $val == 36)
    {
        return 'red'; // и треугольные и квадратные
    }
    elseif(in_array($val, $treug))
    {
        return 'green'; // треугольные
    }
    elseif(in_array($val, $kvd))
    {
        return 'blue'; // квадратные
    }
    else
    {
        return 'white'; // прочие
    }
}

echo '<table border = "1">';
for($i = 1; $i <= 30; $i++)
{
    echo '<tr>';
    for($j = 1; $j <= 30; $j++)
    {
        $val = $i * $j;
        $color = getColor($val, $treug, $kvd);
        echo '<td style="background-color:' . $color . ';width:20px;height:20px;">' . $value . '</td>';
    }
    echo '</tr>';
}
echo '</table>';
$treugStr = implode("  ", $treug);
echo "<br>Массив треугольных чисел: " . $treugStr . "<br>";

echo "<br>ЗАДАЧА 3<br>";
$cust = [
    'cnum' => 2001,
    'cname' => 'Hoffman',
    'city' => 'London',
    'snum' => 1001,
    'rating' => 100
];

foreach($cust as $key => $value)
{
    echo $key . ": " . $value . "<br>";
}

// function sortfunc($a, $b)
// {
//     if ($a == $b) {
//         return 0;
//     }
//     return ($a < $b) ? -1 : 1;
// }

asort($cust);
$custStr = implode ("<br>", $cust);
echo "<br>Oтсортированный по значениям: <br>" . $custStr . "<br>";

ksort($cust);
echo "<br>Сортировка по ключам:<br>";
foreach ($cust as $key => $value) {
    echo $key . ": " . $value . "<br>";
}

arsort($cust);
$custStr = implode("<br>", $cust);
echo "<br>Oтсортированный в обратном порядке ассоциативный: <br>" . $custStr . "<br>";

// rsort($cust);
// $custStr = implode ("<br>", $cust);
// echo "<br>Oтсортированный в обратном порядке индексированныый: <br>" . $custStr . "<br>";

sort($cust);
echo "<br>Результат сортировки с помощью sort():<br>";
foreach ($cust as $key => $value) {
    echo $key . ": " . $value . "<br>";
}
?>
