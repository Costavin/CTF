<?php
// Simple admin panel
session_start();

if (!isset($_SESSION['admin'])) {
    echo "Access Denied";
    exit;
}

echo "<h1>Admin Panel</h1>";
echo "<p>Welcome, Admin!</p>";

// Database operations
$conn = new mysqli("localhost", "dbuser", "dbpassword", "webapp_db");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM articles";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<table>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"] . "</td><td>" . $row["title"] . "</td></tr>";
    }
    echo "</table>";
}
$conn->close();
?>
