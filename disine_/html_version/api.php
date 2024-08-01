<?php
date_default_timezone_set('Europe/Samara'); //+4
$day = 30;
$date_max = date('Y-m-d', time() + ($day * 86400));

require_once "db.php";
$time_all = [
    '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
    '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
    '18:00', '18:30', '19:00'
];
// $time_busy = [
//     "12:00", "13:00", "15:30"
// ];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name_p = $_POST['name'];
    $phone_p = $_POST['phone'];
    $date_p = $_POST['date'];
    $time_p = $_POST['time'];
    $avto_p = $_POST['avto'];
    //Подключаемся к БД Хост, Имя пользователя MySQL, его пароль, имя нашей базы
    $conn = new mysqli($host_db, $user_db, $pass_db, $name_db);
    //Кодировка данных получаемых из базы
    $conn->query("SET NAMES 'utf8' ");
    //делаем проверку на совпадение даты и времени
    $sql = "SELECT * FROM `cust_rec` WHERE datetime ='$date_p $time_p'";
    //echo $sql;
    $result = mysqli_query($conn, $sql);
    if (mysqli_num_rows($result) > 0) {
        //такая запись существует
        //echo "Запись существует";
        $sql1 = "SELECT * FROM `cust_rec` WHERE DATE(datetime) ='$date_p' ORDER BY datetime ASC";
        $result1 = mysqli_query($conn, $sql1);
        if (mysqli_num_rows($result1) > 0) {
            $data = array();
            $client = array();
            while ($row = mysqli_fetch_assoc($result1)) {
                $data[] = date('H:i', strtotime($row['datetime']));
                
            }
        } else {
            $data = 0;
        }
        header('Content-Type: application/json');
        echo json_encode(['name' => $name_p, 'message' => 'is_busy', 'time_all' => $time_all, 'time_busy' => $data]);
    } else {
        // echo "Записи нет, записываем";

        $sql2 = "INSERT INTO `cust_rec` (`id`, `name`, `phone`, `avto`, `datetime`) VALUES (NULL, '$name_p', '$phone_p', '$avto_p', '$date_p $time_p');";
        $result2 = mysqli_query($conn, $sql2);
        if ($result2) {
            //sucseess
            $sql3 = "SELECT * FROM `cust_rec` WHERE DATE(datetime) ='$date_p' ORDER BY datetime ASC";
            $result3 = mysqli_query($conn, $sql3);
            if (mysqli_num_rows($result3) > 0) {
                $data = array();
                while ($row = mysqli_fetch_assoc($result3)) {
                    $data[] = date('H:i', strtotime($row['datetime']));
                    $client[] = array(
                        "id" => $row['id'],
                        "name" => $row['name'],
                        "phone" => $row['phone'],
                        "avto" => $row['avto'],
                        "time" => date('H:i', strtotime($row['datetime']))
                    );
                }
            } else {
                $data = 0;
            }

            header('Content-Type: application/json');
            echo json_encode(['name' => $name_p, 'message' => 'sucsess', 'time_all' => $time_all, 'time_busy' => $data, 'client' => $client]);
        } else {

            $sql4 = "SELECT * FROM `cust_rec` WHERE DATE(datetime) ='$date_p' ORDER BY datetime ASC";
            $result4 = mysqli_query($conn, $sql4);
            if (mysqli_num_rows($result4) > 0) {
                $data = array();
                while ($row = mysqli_fetch_assoc($result3)) {
                    $data[] = date('H:i', strtotime($row['datetime']));
                }
            } else {
                $data = 0;
            }
            header('Content-Type: application/json');
            echo json_encode(['name' => $name_p, 'message' => 'error', 'time_all' => $time_all, 'time_busy' => $data]);
        }
    }

    $conn->close();
}

if ($_SERVER['REQUEST_METHOD'] == 'GET') {

    if (empty($_GET['date'])) {
        $datetime = date('Y-m-d', time());
    } else {
        $datetime = ($_GET['date']);
    }
    $del_ok=0;
    
    //Подключаемся к БД Хост, Имя пользователя MySQL, его пароль, имя нашей базы
    $conn = new mysqli($host_db, $user_db, $pass_db, $name_db);
    //Кодировка данных получаемых из базы
    $conn->query("SET NAMES 'utf8' ");
    //delite client time
    if(!empty($_GET['del'])){
        //$conn->real_escape_string($_POST["id"]);
        $del = ($_GET['del']);
        $sql_del = "DELETE FROM `cust_rec` WHERE `id` = $del;";
        if ($conn->query($sql_del)==TRUE && $conn->affected_rows > 0){    
            $del_ok=1;
        }else{
            $del_ok=0;
        }
    }
    $datetime = date('Y-m-d', strtotime($datetime));
    $sql = "SELECT * FROM `cust_rec` WHERE DATE(datetime) ='$datetime' ORDER BY datetime ASC";
    //echo $sql;
    $result = mysqli_query($conn, $sql);
    if (mysqli_num_rows($result) > 0) {
        $data = array();
        $client = array();
        
        while ($row = mysqli_fetch_assoc($result)) {
            $data[] = date('H:i', strtotime($row['datetime']));
            $client[] = array(
                "id" => $row['id'],
                "name" => $row['name'],
                "phone" => $row['phone'],
                "avto" => $row['avto'],
                "time" => date('H:i', strtotime($row['datetime']))
            );
        }



        header('Content-Type: application/json');
        echo json_encode(['date' => $datetime, 'date_max' => $date_max, 'time_all' => $time_all, 'time_busy' => $data, 'client' => $client, 'del_ok' => $del_ok]);
    } else {
        header('Content-Type: application/json');
        echo json_encode(['date' => $datetime, 'date_max' => $date_max, 'time_all' => $time_all, 'time_busy' => 0, 'client' => 0, 'del_ok' => $del_ok]);
    }
    $conn->close();
}//GET