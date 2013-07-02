#!/bin/bash

INSTALL_USER=pma
WORDPRESS_PATH=/var/www

apt-get -y install apache2 php5 php5-mysql mysql-server tofrodos

wget http://wordpress.org/latest.tar.gz

mv latest.tar.gz $WORDPRESS_PATH

rm -rf $WORDPRESS_PATH/wordpress

cd $WORDPRESS_PATH
tar xzf latest.tar.gz

chown -R $INSTALL_USER:users wordpress

rm -rf latest.tar.gz

cd $WORDPRESS_PATH/wordpress

sed s/"define('DB_NAME', 'database_name_here');"/"define('DB_NAME', 'wordpress');"/ wp-config-sample.php > wp-config.php
sed s/"define('DB_USER', 'username_here');"/"define('DB_USER', 'root');"/ wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('DB_PASSWORD', 'password_here');"/"define('DB_PASSWORD', 'root');"/ wp-config.php > tmp
mv tmp wp-config.php

wget https://api.wordpress.org/secret-key/1.1/salt/ -O keys

sed s/"define('AUTH_KEY',         'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('SECURE_AUTH_KEY',  'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('LOGGED_IN_KEY',    'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('NONCE_KEY',        'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('AUTH_SALT',        'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('SECURE_AUTH_SALT', 'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('LOGGED_IN_SALT',   'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php
sed s/"define('NONCE_SALT',       'put your unique phrase here');"// wp-config.php > tmp
mv tmp wp-config.php

fromdos wp-config.php
cat keys wp-config.php > tmp
mv tmp wp-config.php
chown -R $INSTALL_USER:users $WORDPRESS_PATH/wordpress

service apache2 restart
