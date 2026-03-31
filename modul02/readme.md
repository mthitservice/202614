# Dockerfile (Aufbau eine Images)

| Befehl         | Beschreibung        | Beispiel
|----------------|---------------------|---------
| `FROM` | Basis-Image festlegen | `FROM node:12.04-alpine` |
| `WORKDIR` | Arbeitsverzeichnis setzen | `WORKDIR /app` |
| `COPY` | Dateien kopieren | `COPY . /app` |
| `ADD` | Dateien kopieren (mit Extraktion) | `ADD archive.tar.gz /app` |
| `RUN` | Befehl während Build ausführen | `RUN apt-get update` |
| `RUN` | Befehl während Build ausführen | `RUN apt install xyz` |
| `CMD` | Standard-Befehl (überschreibbar) | `CMD ["npm", "start"]` |
| `ENTRYPOINT` | Haupt-Befehl (nicht überschreibbar) | `ENTRYPOINT ["python"]` |
| `ENV` | Umgebungsvariable setzen | `ENV NODE_ENV=production` |
| `EXPOSE` | Port dokumentieren | `EXPOSE 8080` |
| `VOLUME` | Volume-Mount-Point | `VOLUME /data` |
| `USER` | User für nachfolgende Befehle | `USER node` |
| `ARG` | Build-Argument | `ARG VERSION=1.0` |
| `LABEL` | Metadaten hinzufügen | `LABEL version="1.0"` |


# Docker Build (zum Bauen von Images)

``` bash
docker build .
```

``` bash
docker build -t myapp:1.0.0 .
```