#!/usr/bin/python3
"""
generates tgz archive
"""
from fabric.api import local
from datetime import datetime


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
