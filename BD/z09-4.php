<html>
<header>
    <a href = "index.php">HOME<br/></a>
</header>
</html>
<?


$connect = mysqli_connect("localhost", "root", ""); // конект к аккаунту
mysqli_select_db($connect, "localhost"); // конект к бд

$sql = "SELECT * FROM notebook_br01";
$result = mysqli_query($connect, $sql);
?>
<?

if (mysqli_num_rows($result) > 0) //кол-во строк
{
    while ($row = mysqli_fetch_assoc($result)) // возвр ассоц массив 
    {
        ?><p>
                <div>
                    <table>
                        <tr>
                            <td>id</td>
                            <td>name</td>
                            <td>city</td>
                            <td>address</td>
                            <td>birthday</td>
                            <td>mail</td>
                        </tr>
                        <tr>
                            <td><?=$row['id']?>  </td>
                            <td><?=$row['name']?></td>
                            <td><?=$row['city']?></td>
                            <td><?=$row['address']?></td>
                            <td data-type='date'><?=$row['bithday']?></td>
                            <td><?=$row['mail']?></td>
                        </tr>
                    </table>

                    <form action='z09-4-2.php' method='post'>
                        <input type='hidden' name='id' value='<?=$row['id']?>'>
                        <select name='column_name'>
                            <option value='name'>name</option>
                            <option value='city'>city</option>
                            <option value='address'>address</option>
                            <option value='birthday'>birthday</option>
                            <option value='mail'>mail</option>
                        </select>
                        <input type='text' name='column_value'/>
                        <input type='submit' value='Отправить'/>
                </form> 
            </div>
        </p>
     <?
    }
}
?>
</section>