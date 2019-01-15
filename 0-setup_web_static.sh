#!/usr/bin/env bash
#installs nginx and sets redirect
apt-get update -y
# Install Nginx if it not already installed
apt-get -y install nginx
# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/
# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
echo "<html><head></head><body>H3110 Holberton School !</body></html>" > ~/temp.html
mv ~/temp.html /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). 
sed -i 's|^server {|server {\n\location /hbnb_static {\n    alias /data/web_static/current/;\n}|' /etc/nginx/sites-enabled/default
# Don’t forget to restart Nginx after updating the configuration:
service nginx restart
