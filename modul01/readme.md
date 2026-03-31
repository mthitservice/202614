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

docker exec -it xxxxxxx bash

# Container Übersichten
docker ps # Listet laufende Container auf
docker ps -a # Listet alle Container auch die gestoppten auf
docker ps -q # Nur IDs
docker ps --filter "status=running" gefiltert nach STatus

# Container Verwaltung
docker stop <container-id>
docker start <container-id>
docker pause <container-id> 
docker unpause <container-id>
docker restart<container-id>
docker rm <container-id> # Container entfernen
docker rm $(docker ps -aq) # Entfern alle gestopen container
docker container prune # lösch alle gestoppten Container

# Container untersuchen
docker inspect <container-id>
docker logs  <container-id> 
docker logs -f <container-id> 
docker logs -f <container-id> --tail 10

# Container Ressourcenverbrauch
docker stats
docker stats <container-id> 
docker top <container-id> # Top Prozesse im Container

docker exec -it <container-id> bash
docker exec -it <container-id> sh
docker exec -it <container-id> ls /app 
docker exec -u root  <container-id> bash # Sitzung al root user

# Volumes
docker volume create <volumename>    /dockerhive/data/volumes/<volumename>
docker volume #ls Listet Laufwerke auf
docker volume ls --filter "dangling=true" # ungenutzte Laufwerke
docker volume inspect <volumename>
docker volume create --driver local --opt type=cifs --opt device=//localhost/docker smb_volume

docker run -v smb_volume:/etc/nginx/config --Name myNginnx nginx:latest

docker volume rm <volumename>
docker volume prune
# Network
Treiber
+++++++++++++++++++++++++++++++++++++++
bridge + NAT-Netzwerk auf Host  + Standard, Entwicklung
---------------------------------------------------------
host  * kein eigenes Netz, Host Stack + Low-Latency
---------------------------------------------------------
none  * kein Netzwerk + Security , Batch
---------------------------------------------------------
overlay * Netz über mehrere Host * Swarm
---------------------------------------------------------
macvlan * Eigne Mac Adresse im Lan + Voip, Nas 
---------------------------------------------------------

docker network ls
docker network create <networkname>
docker network create --driver bridge <networkname>
docker network create --subnet=172.99.0.0/16 <networkname>
docker network inspect <networkname>

# Mit Netzwerk verbinden
docker run --network <networkname> nginx

docker network disconnect  <networkname> <container-id> #vom Netzwerk trennen
docker network connect <networkname> <container-id>


docker network rm <networkname> # Löscht das Netzwerk
docker network prune # Löscht alle Netzwerke
```

