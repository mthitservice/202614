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

### Container Start
docker run <imagename>
docker run -d nginx # STartet im Hintergrunt d=detatched
docker run -it ubuntu bash  # Interaktiver Zugriff (-it)
docker run --name mycontainer nginx
docker run -p 8080:80  nginx # Port  -p Host:Container
docker run -v /host/path:/container/path nginx # Pathmount 
docker run -v volume:/container/path nginx # Volume 
docker run -e ENV_VAR=value nginx # Umgebungsvariable
docker run --rm nginx #Autoremove nach Stop
