#!/usr/bin/python3
"""
This script uses Fabric to create a compressed archive (.tgz) of the web_static
folder in the AirBnB Clone repository.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def create_archive():
    """
    Creates a compressed archive of the web_static folder using the current date
    and time as part of the filename.
    """
    try:
        date_str = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        archive_name = "versions/web_static_{}.tgz".format(date_str)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except:
        return None

