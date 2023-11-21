<?php
function vid_structure($connect, $table, $binaryInput)
{
    print "<h4>Структура таблицы $table</h4>";
    $mysql_data_type_hash = array(
        1 => 'tinyint',
        2 => 'smallint',
        3 => 'int',
        4 => 'float',
        5 => 'double',
        7 => 'timestamp',
        8 => 'bigint',
        9 => 'mediumint',
        10 => 'date',
        11 => 'time',
        12 => 'datetime',
        13 => 'year',
        16 => 'bit',
        252 => 'text',
        253 => 'varchar',
        254 => 'char',
        246 => 'decimal'
    );
    $mysql_data_type_flag = array(
        0 => 'NOT_NULL_FLAG',
        1 => 'PRI_KEY_FLAG',
        2 => 'UNIQUE_KEY_FLAG',
        3 => 'BLOB_FLAG',
        4 => 'UNSIGNED_FLAG',
        5 => 'ZEROFILL_FLAG',
        6 => 'BINARY_FLAG',
        7 => 'ENUM_FLAG',
        8 => 'AUTO_INCREMENT_FLAG',
        9 => 'TIMESTAMP_FLAG',
        10 => 'SET_FLAG',
        11 => 'NUM_FLAG',
        12 => 'PART_KEY_FLAG',
        13 => 'GROUP_FLAG',
        14 => 'UNIQUE_FLAG'
    );
    $query = "SELECT * from $table";
    $result = mysqli_query($connect, $query);
    $num_fields = mysqli_num_fields($result);

    for ($x = 0; $x < $num_fields; $x++) {
        $properties = mysqli_fetch_field_direct($result, $x);
        $flag = $properties->flags;
        $binaryFlag = decbin($flag);
        
        
        if ($result) 
        {
            // while ($row = mysqli_fetch_assoc($result)) 
            // {
            //     $arr[] = $row['Field'];
            //     //print($row['Field']);
            // }
            print $mysql_data_type_hash[$properties->type] . " " . ($properties->length) . " " . ($properties->name) . " ";
            // for($i = 0; $i <= count($arr); ++$i)
            // {
                //print($arr[$i]) . " ";
                //print $binaryFlag;
                
                foreach (array_reverse(str_split($binaryFlag, 1)) as $index => $bit) 
                {
                    //print("bit = " . $bit ." ". gettype($bit));
                    //print $mysql_data_type_flag[$index] . " | ";
                    if ($bit == "1") 
                    {
                        print $mysql_data_type_flag[$index] . " | ";
                    }
                    else{continue;}
                }
            //}
        print "</br>";
        }
    }
}
function vid_content($connect, $table)
{
    print "<h4 class = 'title10'>Содержимое таблицы $table</h4>";
    //асоц массив для переназвания столбцов
    $tabname = array(
        "cnum" => "номер покупателя",
        "cname" => "имя покупателя",
        "city" => "город",
        "rating" => "рейтинг покупателя",
        "snum" => "номер продавца",
        "onum" => "номер заказа",
        "amt" => "стоимость заказа",
        "odate" => "дата заказа",
        "sname" => "имя продавца",
        "comm" => "комиссионные"
    );
    $query = "select * from $table";
    $result = mysqli_query($connect, $query);
    $num_fields = mysqli_num_fields($result);
    print "<table border=\"1\" cellpadding=\"5\" cellspacing=\"1\">\n";
    print '<tr class = "table10">';
    for ($x = 0; $x < $num_fields; $x++) //создание заголовков
    {
        $name = mysqli_fetch_field_direct($result, $x)->name;
        print "\t<th>$tabname[$name]</br>$name</th>\n";
    }
    print "</tr>\n";
    while ($a_row = mysqli_fetch_row($result)) //вывод ячеек проходя по строкам таблицы
    {
        print '<tr class = "table10" style="padding:5px 10px">';
        foreach ($a_row as $field)
            print "\t<td class = 'td10'>$field</td>\n";
        print "</tr>\n";
    }
    print "</table>\n";
}
if (isset($_POST['cust'])) {
    $cust = $_POST['cust'];
    $binaryInput = isset($_POST['binaryInput']) ? $_POST['binaryInput'] : 0; // чтение двоичного ввода
    if (isset($cust[0])) {
        vid_structure($connect, 'cust', $binaryInput);
    }
    if (isset($cust[1])) {
        vid_content($connect, 'cust');
    }
}
if (isset($_POST['ord'])) {
    $ord = $_POST['ord'];
    $binaryInput = isset($_POST['binaryInput']) ? $_POST['binaryInput'] : 0;
    if (isset($ord[0])) {
        vid_structure($connect, 'ord', $binaryInput);
    }
    if (isset($ord[1])) {
        vid_content($connect, 'ord');
    }

}
if (isset($_POST['sal'])) {
    $sal = $_POST['sal'];
    $binaryInput = isset($_POST['binaryInput']) ? $_POST['binaryInput'] : 0;
    if (isset($sal[0])) {
        vid_structure($connect, 'sal', $binaryInput);
    }
    if (isset($sal[1])) {
        vid_content($connect, 'sal');
    }

}
?>