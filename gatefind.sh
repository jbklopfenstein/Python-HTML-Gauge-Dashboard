#!/bin/bash

for i in 1 2 3 4 5 hold cancel; do grep -r --exclude-dir=.revs "gate: $i" /var/www/html/user/pages | tee -a projectgates; done
