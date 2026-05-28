mysql -u root -p
use webapp_db;
SELECT * FROM sensitive_info;
SHOW DATABASES;
SHOW TABLES;
DESCRIBE sensitive_info;
cp /var/lib/mysql/confidential_data.sql /tmp/.backup_data
ls -la /tmp/
cat /tmp/.backup_data
rm /tmp/.backup_data
history -c
