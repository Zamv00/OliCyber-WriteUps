<?php
include 'secrets.php';
?>

<html>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

    <title>Admin's secret - Register</title>
</head>

<body>
    <div class="container justify-content-center">
        <a href="/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Home</a>
        <br>

        <h2>Registrati</h2>

        <form method="POST">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" name="username" placeholder="Inserisci username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="text" class="form-control" id="password" name="password" placeholder="Password">
            </div>
            <button type="submit" class="btn btn-primary">Registrati</button>
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $db = new mysqli($db_host, $db_user, $db_password, $db_schema);

            $username = $_POST['username'];
            $password = $_POST['password'];

            $sql = "INSERT INTO users(username,password,admin) VALUES ('" . $username . "','" . $password . "',false);";

            if ($db->query($sql) === TRUE) {
                echo '<div class="alert alert-success" role="alert">Ti sei registrato! Puoi ora fare login</div>';
            } else {
                echo '<div class="alert alert-danger" role="alert">Error: ' . $sql . "<br>" . $db->error . "</div>";
            }
            $db->close();
        }
        ?>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
    </div>
</body>

</html>