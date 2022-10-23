#!/bin/sh

#~ rsync -avzhd --exclude '.git' --exclude '--pycache--'  ./  gerald@192.168.1.111:/media/gerald/Projects/Remote_sites\weather-141\gsb-wx-code

eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519

git add -A
git commit -m "Generated this file on `date +'%Y-%m-%d %H:%M:%S'`";
git push

