#!/usr/bin/python3.8
import os
import stat
import time

def main():
    
    filePath = 'E:\\samir\\devops\\python\\scripts\\kube.sh'
    print("**** Get File Last Access time using os.stat() ****")
    # get the the stat_result object
    fileStatsObj = os.stat ( filePath )
    
    # Get last access time
    accessTime = time.ctime ( fileStatsObj [ stat.ST_ATIME ] )
    print("File Last Access Time : " + accessTime)
    print("**** Get File Creation time using os.stat() *******")
    
    # get the the stat_result object
    fileStatsObj = os.stat ( filePath )
    
    # Get the file creation time
    creationTime = time.ctime ( fileStatsObj [ stat.ST_CTIME ] )
    print("File Creation Time : " + creationTime)
    print("**** Get File Last Access time using os.path.getatime() ****")
    
    # Get last access time of file in seconds since epoch
    accessTimesinceEpoc = os.path.getatime(filePath)
    
    # convert time sinch epoch to readable format
    accessTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(accessTimesinceEpoc))
    print("File Last Access Time : " + accessTime)
    print("**** Get File Last Access time using os.path.getatime() in UTC Timezone****")
    accessTime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(accessTimesinceEpoc))
    print("File Last Access Time : " + accessTime + ' UTC'  )
    print("**** Get File creation time using os.path.getctime() ****")
    
    # Get file creation time of file in seconds since epoch
    creationTimesinceEpoc = os.path.getctime(filePath)
    
    # convert time sinch epoch to readable format
    creationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(creationTimesinceEpoc))
    print("File Creation Time : " + creationTime )
    print("**** Get File creation time using os.path.getctime() in UTC Timezone ****")
    creationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(creationTimesinceEpoc))
    print("File Creation Time : ", creationTime , ' UTC'  )

if __name__ == '__main__':
    main()
