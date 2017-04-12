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
        usage: pydfu [-h] {df,du,scan} ...

        Disk and FileSystem Utils

        positional arguments:
          {df,du,scan}  help for subcommand
            df          df help
            du          du help
            scan        scan help

        optional arguments:
          -h, --help    show this help message and exit
          
          
        $ pydfu df
        FileSystem    1K-blocks     Used          Avail         Use%          Mounted On    
        udev          3780128       0             3780128       0%            /dev          
        tmpfs         760264        17780         742484        3%            /run          
        /dev/sda1     102049120     9684784       87157504      11%           /             
        tmpfs         3801300       436           3800864       1%            /dev/shm      
        tmpfs         5120          4             5116          1%            /run/lock     
        tmpfs         3801300       0             3801300       0%            /sys/fs/cgroup
        vmhgfs-fuse   249414652     134421324     114993328     54%           /mnt/hgfs     
        tmpfs         760264        76            760188        1%            /run/user/1000
        
        $ pydfu du /tmp/suf -h
        258.0 B   /tmp/suf/configure_os_datastage_node.xml
        258.0 B   /tmp/suf/configure_os_db_node.xml
        258.0 B   /tmp/suf/configure_app_datastage_node.xml
        258.0 B   /tmp/suf/configure_app_core_svcs_node.xml
        258.0 B   /tmp/suf/configure_app_db_node.xml
        258.0 B   /tmp/suf/configure_os_web_node.xml
        258.0 B   /tmp/suf/configure_os_core_svcs_node.xml
        258.0 B   /tmp/suf/configure_app_web_node.xml
        258.0 B   /tmp/suf/configure_app_analytics_node.xml
        258.0 B   /tmp/suf/configure_os_analytics_node.xml

        Total Size: 2.52 KB

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
        
        du = pydfu.du()
        
        # get list of file and directory object
        du.query('/tmp')
        du.total_size # get total size of /tmp 
        
        # access a file or directory object
        du.query('/tmp')[0]
        
        # access information of a file or directory object
        >>> du.query('/tmp')[0].name
        '/tmp/.X0-lock'
        >>> du.query('/tmp')[0].size
        11
        >>> du.query('/tmp')[0].size_in_h
        '11.0 B'


### Planned work / work in progress
Track: https://github.com/rrajaravi/pydfu/blob/master/WORK.md
