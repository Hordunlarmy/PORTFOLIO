#!/usr/bin/env bash
# sets up web server for the deployment
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/PORTFOLIO/
chown -R odun:odun /data/
config_content="
server{
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;

    server_name _;
    location / {
        alias /data/PORTFOLIO/;
        index.html;
    }

    error_page 404 /404.html;
        location /404 {
                root /var/www/html;
                internal;
    }

}"
echo "$config_content" > /etc/nginx/sites-available/default
sudo service nginx restart

