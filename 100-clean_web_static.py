#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.19.204', '54.157.159.85']


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number : The number of archives to keep.

    Only the most recent archive is kept if the number is 0 or 1. If
    Number 2 has the archives that are the most and second-most recent.
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archi = sorted(os.listdir("versions"))
    [archi.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archi]

    with cd("/data/web_static/releases"):
        archi = run("ls -tr").split()
        archi = [a for a in archives if "web_static_" in a]
        [archi.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archi]
