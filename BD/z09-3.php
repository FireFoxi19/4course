<html>
<header>
    <a href = "index.php">HOME<br/></a>
</header>
</html>

<?php
            $connect = mysqli_connect("localhost", "root", ""); // конект к аккаунту
            mysqli_select_db($connect, "localhost"); // конект к бд
            
            $sql = "SELECT * FROM notebook_br01";
            $result = mysqli_query($connect, $sql);
                
            while ($element = mysqli_fetch_array($result)) 
            {
                echo $element[0] . " | " . $element[1] . " | " . $element[2] . " | " . $element[3] . " | " . $element[4] . " | " . $element[5] ."<br>";
            }
?>
