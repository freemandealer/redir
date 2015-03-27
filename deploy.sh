#!/bin/sh

cp * deploy/
cd deploy/
git add --all
git commit -m 'deploy'
git push
cd ..
