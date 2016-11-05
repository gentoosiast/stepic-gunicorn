#!/bin/sh

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart

