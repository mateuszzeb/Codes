<?php
    $host = ""; 
    $user = ""; 
    $pass = ""; 
    $db_name = ""; 
    
    // (host_name, user_login, password, database_name)
    $connect = new mysqli($host, $user, $pass, $db_name);

    // query
    $sql = "SELECT * FROM table";

    // return false or result
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            // for each row 
        }
    } 
    else {
        // if number of rows is 0
    }

    // close connect
    $connect->close();
?>
