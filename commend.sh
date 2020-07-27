#!/bin/bash
git add .
commit="automatic commit"
if [ $1 ]; then commit=$1; fi
git commit -m "$commit pull"
git pull origin master
git add .
git commit -m "$commit push"
git push origin master