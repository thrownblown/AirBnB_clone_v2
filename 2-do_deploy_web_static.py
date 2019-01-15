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
def do_deploy(archive_path):
    """
        Uploads the archive to the remote server in the directory /tmp/
        Creates the directory /tmp/holbertonwebapp
        Untars the holbertonwebapp.tar.gz archive in /tmp/holbertonwebapp
    """
    try:
        put(archive_path, '/tmp/')

        fn = archive_path.split('/')[-1].split('.')[0]
        dr = "/data/web_static/releases/"

        run("mkdir -p {}{}/".format(dr, fn))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(fn, dn))

        run("mv {}/web_static/* {}".format(dn, dn))

        run("rm /tmp/{}.tgz".format(fn))
        run("rmdir {}/web_static".format(dn))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dn))
        return True
    except:
        return False


@task
def clean():
    # Deletes the holbertonwebapp.tar.gz on your local machine
    local('rm ./holbertonwebapp.tar.gz')
