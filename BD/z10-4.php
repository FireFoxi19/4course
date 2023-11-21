<?php
    $connect = mysqli_connect("localhost", "root", "");
    if ($connect==false) {
        die("Connection failed");
    }
    mysqli_select_db($connect, "localhost");
?>