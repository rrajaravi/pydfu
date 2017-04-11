# pydfu
[![Build Status](https://travis-ci.org/rrajaravi/pydfu.svg?branch=master)](https://travis-ci.org/rrajaravi/pydfu)

Python Interface and cli for Disk and Filesystem Utils

### Requirements
Unix/Linux Operating System

### How to Use
#### Installation

        $ git clone https://github.com/rrajaravi/pydfu.git
        $ cd pydfu
        $ python setup.py install

#### Command Line

        $ pydfu --help
        usage: pydfu [-h] [-s] [-d]

        Disk and FileSystem Utils

        optional arguments:
          -h, --help  show this help message and exit
          -s, --scan
          -d, --df
        $ pydfu --df
        FileSystem    1K-blocks     Used          Avail         Use%          Mounted On    
        udev          3780128       0             3780128       0%            /dev          
        tmpfs         760264        17780         742484        3%            /run          
        /dev/sda1     102049120     9684784       87157504      11%           /             
        tmpfs         3801300       436           3800864       1%            /dev/shm      
        tmpfs         5120          4             5116          1%            /run/lock     
        tmpfs         3801300       0             3801300       0%            /sys/fs/cgroup
        vmhgfs-fuse   249414652     134421324     114993328     54%           /mnt/hgfs     
        tmpfs         760264        76            760188        1%            /run/user/1000

#### Library

        import pydfu
        
        df = pydfu.df()
        
        # get list of file system object
        df.query()
        
        # query for a file system based on path and get file system object
        fs = df.query_one(path='/')

        # query all file systems based on size and get matches in list
        fs = df.query(size='>10g')

        # query for a file system based on used size
        fs = df.query_one(use='<100%')
        
        # query for a file system based on multiple conditions
        fs = df.query_one(size='>10g', use='<50%') 
