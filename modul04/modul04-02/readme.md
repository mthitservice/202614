# Befehle zum Sicherheitscheck

```bash
# Übersicht der Schwachstellen
docker scout cves vulnerable-app

# Detaillierte Ausgabe
docker scout cves --format markdown vulnerable-app

# Nur kritische und hohe Schwachstellen
docker scout cves --only-severity critical,high vulnerable-app
```

### 3. Quickview - Schnellübersicht
```bash
docker scout quickview vulnerable-app
```

### 4. Empfehlungen anzeigen
```bash
# Upgrade-Empfehlungen
docker scout recommendations vulnerable-app

# Vergleich mit aktuelleren Base-Images
docker scout compare vulnerable-app --to python:3.12-slim
```

## SBOM (Software Bill of Materials)

```bash
# SBOM erstellen
docker scout sbom vulnerable-app

# SBOM als JSON exportieren
docker scout sbom --format spdx-json vulnerable-app > sbom.json
```