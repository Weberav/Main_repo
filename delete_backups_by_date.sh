#!/bin/bash
date > /var/log/delete_backup/log.txt


find /mnt/datastore/Backup_Datastore/vm/100 -mtime +60 -type d -exec rm -rf {} \; > /var/log/delete_backup/log.txt
find /mnt/datastore/Backup_Datastore/vm/102 -mtime +60 -type d -exec rm -rf {} \; > /var/log/delete_backup/log.txt
find /mnt/datastore/Backup_Datastore/vm/103 -mtime +60 -type d -exec rm -rf {} \; > /var/log/delete_backup/log.txt
