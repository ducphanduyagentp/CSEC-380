#!/bin/bash

service mysql start
mysql -u root -e "CREATE DATABASE IF NOT EXISTS armbook;"
mysql -u root armbook < /app/public/armbook.sql
mysqladmin -u root password "imxyubx"
/start.sh
