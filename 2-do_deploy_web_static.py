#!/usr/bin/python3
"""
deploy content
"""
from fabric.api import *
from datetime import datetime
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['52.73.254.165', '100.25.23.236']
env.key = '~/.ssh/id_alx'


def do_pack():
    """ create archive for web_static content """
    local("mkdir -p versions")
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(time)
    archive = local('tar -cvzf {} web_static'.format(name))
    if archive.succeeded:
        return name
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers """
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, '/tmp/')
        run('sudo mkdir -p /data/web_static/releases/{}'.format(file_name))
        #uncompress archive
        run('sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.
            format(file_name, file_name))
        #remove archive
        run('sudo rm -rf /tmp/{}.tgz'.format(file_name))
        run('sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.
            format(file_name, file_name))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'.format(file_name))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current'.format(file_name))
        return True
    except:
        return False

