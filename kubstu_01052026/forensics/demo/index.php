<?php
$servername = "localhost";
$username = "dbuser";
$password = "dbpassword";
$dbname = "webapp_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$id = $_GET['id'];

// Vulnerable SQL query
$sql = "SELECT title, content FROM articles WHERE id = $id";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<h1>" . $row["title"]. "</h1>";
        echo "<p>" . $row["content"]. "</p>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
// Simulate file upload directory
if (!file_exists('uploads')) {
    mkdir('uploads', 0777, true);
}

?>
