#!/usr/bin/env python

import subprocess


def main():
    # Install system dependencies
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "upgrade"])
    subprocess.call(["apt-get", "-y", "--force-yes", "install", "upstart"])
    subprocess.call(["apt-get", "-y", "install", "python-dev"])
    subprocess.call(["apt-get", "-y", "install", "python-pip"])
    subprocess.call(["apt-get", "-y", "install", "avahi-daemon"])
    subprocess.call(["pip", "install", "virtualenv"])

    # Copy Upstart script
    subprocess.call(["cp", "./install/motion-detector.conf", "/etc/init"])

    # TODO: This needs to set the cron job using the crontab.txt file

    # Copy Cron job script
    subprocess.call(["mkdir", "/home/pi/cron_jobs"])
    subprocess.call(["cp", "./install/environmental_sensors_cron.sh", "/home/pi/cron_jobs"])



if __name__ == '__main__':
    main()
