<?php
include 'header.php';
?>

	<form action="z10-2.php" method="POST">
		<fieldset>
			<div>
				<lable>Отобразить таблицы</lable><br>
				<lable> &emsp;&emsp;&emsp;&emsp;&emsp;&ensp;Структура </lable> <lable>&emsp;Содержимое</lable><br><br>
				<label>Продавцы (sal)</label>
				&emsp;<input type="checkbox" id="sal_st" name="sal[0]" value="0">
				&emsp;&emsp;&emsp;&emsp; <input type="checkbox" id="sal_ct" name="sal[1]" value="1"><br>
				<label>Покупатели(cust)</label>
				<input type="checkbox" id="cust_st" name="cust[0]" value="0">&ensp;
				&emsp;&emsp;&emsp;&ensp; <input type="checkbox" id="cust_ct" name="cust[1]" value="1"><br>
				<label>Заказы(ord)</label>
				&emsp;&emsp;  <input type="checkbox" id="ord_st" name="ord[0]" value="0">
				&emsp;&emsp;&emsp;&ensp;&emsp;<input type="checkbox" id="ord_ct" name="ord[1]" value="1">
			</div>

			<div>
				<button type="submit">Вывести!</button>
			</div>
		</fieldset>
	</form>