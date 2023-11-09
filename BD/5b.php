<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Результат теста</title>
</head>
<body>
    <?php
    // Получаем данные из формы
    $name = $_POST['name'];
    $q1 = $_POST['q1'];
    $q2 = $_POST['q2'];
    $q3 = $_POST['q3'];
    $q4 = $_POST['q4'];
    $q5 = $_POST['q5'];

    // Создаем массив с номерами правильных ответов
    $otv = [1, 2, 1, 1, 1];

    // Подсчитываем количество правильных ответов
    $correctAnswers = 0;
    if ($q1 == $otv[0]) $correctAnswers++;
    if ($q2 == $otv[1]) $correctAnswers++;
    if ($q3 == $otv[2]) $correctAnswers++;
    if ($q4 == $otv[3]) $correctAnswers++;
    if ($q5 == $otv[4]) $correctAnswers++;

    // Выводим результаты
    echo "<h1>Результаты теста</h1>";
    echo "<p>Имя тестируемого: $name</p>";
    echo "<p>Правильных ответов: $correctAnswers из 5</p>";

    // Оценка
    switch ($correctAnswers) {
        case 5:
            echo "<p>Отлично! Вы отлично знаете элементарную теорию музыки.</p>";
            break;
        case 4:
            echo "<p>Хороший результат! Ваши знания впечатляют.</p>";
            break;
        case 3:
            echo "<p>Неплохо, но есть к чему стремиться в изучении теории музыки.</p>";
            break;
        default:
            echo "<p>Вам стоит еще немного поучиться теории музыки.</p>";
            break;
    }
    ?>
    <br>
    <a href="5a.html">Пройти тест еще раз</a>
</body>
</html>
