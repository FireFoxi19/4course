<html>
<header>
    <a href = "index.php">HOME<br/></a>
</header>
</html>
<?php

    function space($val)
    {
        if(strlen(preg_replace('/\s+/u', '', $val))==0)
        {
            return true;
        }
    }

    if (isset($_POST['name']) && isset($_POST['mail'])) 
    {
        $name = "";
        
        if(empty($_POST['name']))
        {
            print("Нельзя оставлять поле пустым!");
        }
        elseif(!empty($_POST['name']))
        { 
            $name = $_POST['name'];
        }

        ///////////////////////
        if(space($name) == 1)
        {
            print("нельзя ставить пробелы");
        }
        
        else{
        $city = "";
        if(empty($_POST['city']))
        {
            print("Нельзя оставлять поле пустым!");
        }
        elseif(!empty($_POST['city']))
        { 
            $city = $_POST['city'];
        }
       

        $address = "";
        if(empty($_POST['address']))
        {
            print("Нельзя оставлять поле пустым!");
        }
        elseif(!empty($_POST['address']))
        { 
            $address = $_POST['address'];
        }
        
        $bithday = "";
        if(!empty($_POST['bithday'])) {
            $bithday = $_POST['bithday'];
        }

        $mail = "";
        if(!empty($_POST['mail'])) {
            $mail = $_POST['mail'];
        }
        }
        $connect = mysqli_connect("localhost", "root", ""); // конект к аккаунту
        mysqli_select_db($connect, "localhost"); // конект к бд

        $sql = "INSERT INTO notebook_br01 (id, name, city, address, bithday, mail) 
        VALUES (NULL, '$name', '$city', '$address', '$bithday', '$mail');";

        $result = mysqli_query($connect, $sql);
        if($result) {
            echo "Поля добавлены";
        }
        else {
            echo "Ошибка";
        }
    }
?>
    <section>
            <form  action="" method="post">
                <input  type="text" name="name" placeholder="Имя" required="">
                <input  type="text" name="city" placeholder="Город">
                <input  type="text" name="address" placeholder="Адрес">
                <input  type="date" name="bithday" placeholder="Дата рождения">
                <!--<input  type="text" name="bithday" placeholder="Дата рождения">-->
                <input  type="email" name="mail" placeholder="E-mail" required="">
                <button>Ввод</button>
            </form>

    </section>
