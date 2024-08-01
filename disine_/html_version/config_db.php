<?php

return [
    'host'=>'localhost',
    'dbname'=>'test',
    'username'=>'root',
    'password'=>'',
    'charset'=>'utf8',
    'options'=>[
        PDO::ATTR_DEFAULT_FETCH_MODE =>PDO::FETCH_ASSOC,
        //PDO::ATTR_ERRMODE =>PDO::ERRMODE_EXCEPTION,
    ],
];