#!/usr/bin/python3




"""Fabric script is equipped with a module that generates a.tgz"""
import os
from fabric.api import local, runs_once
from datetime import datetime



@runs_once
def do_pack():
    """to archive files """
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    da_ti = datetime.now()
    op = "versions/web_static_{}{}{}{}{}{}.tgz".format(
         da_ti.year,
         da_ti.month,
         da_ti.day,
         da_ti.hour,
         da_ti.minute,
         da_ti.second
    )
    try:
        print("Packing web_static to {}".format(op))
        local("tar -cvzf {} web_static".format(op))
        s = os.stat(op).st_size
        print("web_static packed: {} -> {} Bytes".format(op, s))
    except Exception:
        output = None
    return output
    
