#!/bin/bash
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
echo "volume prune"
sudo docker volume prune
echo "done volume prune"
sudo docker system prune -a
echo "done all"

