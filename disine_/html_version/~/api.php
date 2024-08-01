<?php
require_once "db.php";
$time_all = [
    '8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00',
    '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
    '18:00', '18:30', '19:00'
];
$time_busy = [
    "12:00", "13:00", "15:30"
];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
}

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    $datetime = ($_GET['date']);
    //Подключаемся к БД Хост, Имя пользователя MySQL, его пароль, имя нашей базы
    $conn = new mysqli($host_db, $user_db, $pass_db, $name_db);
    //Кодировка данных получаемых из базы
    $conn->query("SET NAMES 'utf8' ");


    $sql = "SELECT * FROM `cust_rec` WHERE DATE(datetime) ='$datetime'";
    $result = mysqli_query($conn, $sql);
    if ($num = mysqli_num_rows($result) > 0) {
        header('Content-Type: application/json');
        echo json_encode(['rows' => 1]);
    } else {
        header('Content-Type: application/json');
        echo json_encode(['rows' => 0]);
    }
    $conn->close();
}//GET
