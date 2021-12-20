#!/usr/bin/python

import os
import time
import pipes
import sys, subprocess

#required packages mysql client, mysqldump, gzip

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'password'
DB_NAMES = ["database01", "database02"]
BACKUP_PATH = '/backup/mysql_backup'

DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

PACKAGES = ["mysql", "gzip"]

def check_package():
    for PACKAGE in PACKAGES:
        rc = subprocess.call(['which', PACKAGE])
        if rc == 0:
            print(f'{PACKAGE} installed!')
        else:
            print(f'{PACKAGE} missing in path!')
            sys.exit(1)

def main():

    check_package()
    
    if os.stat(TODAYBACKUPPATH):
        print("Backup folder already created!")
    else:
        os.mkdir(TODAYBACKUPPATH)
        print("Backup folder has been created!")

    if DB_NAMES:
        print ("List Database names: ", DB_NAMES)
    else:
        print ("Database list is not found...")
        sys.exit()

    for DB_NAME in DB_NAMES:
        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + DB_NAME + ".sql"
        os.system(dumpcmd)
        gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + DB_NAME + ".sql"
        os.system(gzipcmd)

    print ("----------------------------")
    print ("Backup script completed")
    print ("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")

if __name__== "__main__":
    main()