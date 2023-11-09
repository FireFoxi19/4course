<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Результат</title>
</head>
<header>
    <a href = "index.php">HOME<br/></a>
</header>
<body>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Получаем выбранные значения из формы
        $align = isset($_POST["align"]) ? $_POST["align"] : "left";
        $valign = isset($_POST["valign"]) ? $_POST["valign"] : [];
        
        // Создаем ячейку таблицы с заданными атрибутами
        echo '<table width="300" height="300" border="1" cellpadding="10" >';

        $valignAttribute = implode(" ", $valign);
        if (!empty($valignAttribute)) {
            echo '<tr>';
            echo '<td style="text-align: ' . $align . '; vertical-align: ' . $valignAttribute . ';">Текст в таблице</td>';
            echo '</tr>';
        } else {
            echo '<tr>';
            echo '<td >Текст в таблице</td>';
            echo '</tr>';
        }
        echo '</table>';
        echo '<br><a href="4a.html">Назад</a>';
    }
    ?>
</body>
</html>
