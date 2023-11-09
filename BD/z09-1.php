<html>
<header>
    <a href = "index.php">HOME<br/></a>
</header>
</html>

<?php
    $connect = mysqli_connect("localhost", "root", ""); // конект к аккаунту
    if ($connect==false) {
        die("Connection failed");
    }
    mysqli_select_db($connect, "localhost"); // конект к бд

    $sql = 'DROP TABLE IF EXISTS notebook_br01'; // удаление существующей бд
    $result = mysqli_query($connect, $sql);
    if($result) {
        echo "Удалена существовавшая таблица notebook_br01 <br>";
    }
    else {
        echo "Ошибка";
    }

    $sql = 'CREATE TABLE notebook_br01 ( 
        `id` INT NOT NULL AUTO_INCREMENT , 
        `name` VARCHAR(100) NOT NULL , 
        `city` VARCHAR(100) NOT NULL , 
        `address` VARCHAR(100) NOT NULL , 
        `bithday` DATE NOT NULL , 
        `mail` VARCHAR(100) NOT NULL , 
        PRIMARY KEY (`id`)
    );';
    $result = mysqli_query($connect, $sql);
    
    if($result) {
        echo "Создана таблица notebook_br01";
    }
    else {
        echo "Ошибка";
    }
?>
