# Docker Compose
### Build-Befehle
```bash
docker-compose build              # Alle Services builden
docker-compose build --no-cache   # Ohne Cache
docker-compose build <service-name>  # Nur einen Service
```


### Konfiguration validieren
```bash
docker-compose config             # Konfiguration anzeigen
docker-compose config --services  # Alle Services auflisten
```

### Services starten
```bash
docker-compose up
docker-compose up -d              # Im Hintergrund
docker-compose up --build         # Mit rebuild
docker-compose up --force-recreate  # Container neu erstellen
docker-compose up <service-name>  # Nur bestimmten Service
```
### Services stoppen
```bash
docker-compose stop
docker-compose down               # Stoppen und löschen
docker-compose down -v            # Inkl. Volumes löschen
docker-compose down --rmi all     # Inkl. Images löschen
```

### Services verwalten
```bash
docker-compose ps                 # Status anzeigen
docker-compose logs               # Logs anzeigen
docker-compose logs -f            # Logs live verfolgen
docker-compose logs <service-name>  # Logs für Service
docker-compose exec <service-name> bash  # In Service einloggen
docker-compose restart            # Neu starten
docker-compose pause              # Pausieren
docker-compose unpause            # Fortsetzen
```

### Skalierung
```bash
docker-compose up --scale <service-name>=3  # Service auf 3 Instanzen skalieren
```
