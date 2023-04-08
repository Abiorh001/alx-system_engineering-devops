#!/usr/bin/python3
from fabric.api import run, env
env.hosts = ["54.172.57.51", "34.232.78.100"]
env.user = "ubuntu"
env.key = "~/.ssh/school"

def deploy():
    run("echo 'Holberton School' | sudo tee /var/www/html/index.html")
    return True
