# Docker Befehle für Images 
``` bash
docker pull <imagename>:<tag>
docker pull portainer/portainer-ce:alpine-sts
docker images --filter "dangling=true" # Zeigt ungenutzte Images
# Images löschen
docker rmi <image-iD>
docker rmi  nginx:latest
docker rmi $(docker images -q) # Löscht alle Images

# Image verwalten
docker inspect <imagename>
docker history <imagename>

#Image Taggen
docker tag <sourceimage><tag> <repository>/<targetimage><tag>
#Image veröffentlichen
docker push <repository>/<sourceimage><tag> 

