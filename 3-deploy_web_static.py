#!/usr/bin/python3
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['100.25.183.90', '54.209.80.28']


def do_pack():
    """archive directory web server"""
    datet = datetime.utcnow()
    fil = "versions/web_static_{}{}{}{}{}{}.tgz".format(datet.year,
                                                         datet.month,
                                                         datet.day,
                                                         datet.hour,
                                                         datet.minute,
                                                         datet.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(fil)).failed is True:
        return None
    return fil


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    fil = archive_path.split("/")[-1]
    nam = fil.split(".")[0]

    if put(archive_path, "/tmp/{}".format(fil)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(nam)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(nam)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(fil, nam)).failed is True:
        return False
    if run("rm /tmp/{}".format(fil)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(nam, nam)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(nam)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(nam)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    fil = do_pack()
    if fil is None:
        return False
    return do_deploy(fil)
