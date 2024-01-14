#!/usr/bin/python3
"""
The distribution of an is done by the fabric script that is based on file 1-pack_web_static.py.
transfer to the web servers
"""
from os.path import exists
from fabric.api import put, run, env

env.hosts = ['100.25.183.90', '54.209.80.28']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        fn = archive_path.split("/")[-1]
        n_ex = fn.split(".")[0]
        pat = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(pat, n_ex))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fn, pat, n_ex))
        run('rm /tmp/{}'.format(fn))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(pat, n_ex))
        run('rm -rf {}{}/web_static'.format(pat, n_ex))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(pat, n_ex))
        return True
    except:
        return False
