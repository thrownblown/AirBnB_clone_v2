#!/usr/bin/python3
# Write a Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pac
from datetime import datetime
from fabric.api import *

env.user = 'ubuntu'


@task
def do_pack():
    """
        Creates a tar gzipped archive of the versions directory,
        the name of the archive created must be
        web_static_<year><month><day><hour><minute><second>.tgz
    """
    local("mkdir -p ./versions")
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local("tar -cvzf ./versions/web_static_{}.tgz web_static".format(now))


@task
def deploy():
    # Uploads the archive to the remote server in the directory /tmp/
    # Creates the directory /tmp/holbertonwebapp
    # Untars the holbertonwebapp.tar.gz archive in /tmp/holbertonwebapp
    run('mkdir -p /tmp/holbertonwebapp')
    with cd('/tmp'):
        put('holbertonwebapp.tar.gz')
    run('tar -C /tmp/holbertonwebapp -xzf /tmp/holbertonwebapp.tar.gz')
    # run('ls -l /tmp/holbertonwebapp')


@task
def clean():
    # Deletes the holbertonwebapp.tar.gz on your local machine
    local('rm ./holbertonwebapp.tar.gz')
