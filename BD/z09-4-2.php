<header>
    <a href = "index.php">HOME<br/></a>
</header>
</html>
<?php

function Parsing($name, &$var)
{
    if (isset($_POST[$name]) && $_POST[$name] != '') 
    {
        $var = $_POST[$name];
    }
}

$name = null; // название столбика
$id = null; // ид записи
$value = null; // на что меняем
// для каждого выпад списка свое инпут поле проверить
Parsing('column_name', $name);
Parsing('id', $id);
Parsing('column_value', $value);

if (trim($value) == '') {
    echo "Ошибка: Нельзя изменять поле на пустые пробелы.<br>";
}

elseif ($name === 'mail' && $value !== null && !filter_var($value, FILTER_VALIDATE_EMAIL)) {
    echo "Ошибка: Поле 'mail' должно содержать правильный адрес электронной почты.<br>";
}
else 
{
    echo "${id}| ${name}| ${value} <br/>";

    $connect = mysqli_connect("localhost", "root", ""); // конект к аккаунту
    mysqli_select_db($connect, "localhost"); // конект к бд

    $sql = "update notebook_br01 set $name = '$value' where id = '$id'";

    $result = mysqli_query($connect, $sql);
}


?>