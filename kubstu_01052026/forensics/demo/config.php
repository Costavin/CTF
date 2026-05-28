<?php
// Database configuration
define('DB_HOST', '192.168.1.50');  // IP address of Victim-DB
define('DB_USER', 'dbuser');
define('DB_PASS', 'dbpassword');
define('DB_NAME', 'webapp_db');

// SSH configuration for dbadmin
define('SSH_HOST', '192.168.1.50');
define('SSH_USER', 'dbadmin');
define('SSH_KEY', '/home/www-data/.ssh_key_key');

// API Keys and sensitive data
define('API_KEY', 'sk_live_51234567890abcdefghijk');
define('SECRET_KEY', 'super_secret_key_12345');
?>
