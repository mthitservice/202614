# Modul 16: Rootless Container - Security Hardening

## Ziel
Container ohne Root-Rechte ausführen für maximale Sicherheit.

## Warum Non-Root?

| Risiko | Mit Root | Non-Root |
|--------|----------|----------|
| Container Escape | Host-Root-Zugriff | Eingeschränkt |
| CVE-Exploitation | Volle Kontrolle | Minimale Rechte |
| Filesystem-Zugriff | Alles beschreibbar | Nur erlaubte Pfade |
| Compliance | ❌ Nicht konform | ✅ Best Practice |

## Übung

### 1. Root vs Non-Root vergleichen
```bash
cd modul16

# Unsicheres Image (root)
docker build -t app-root -f dockerfile.root .
docker run --rm app-root whoami
# Ausgabe: root

# Sicheres Image (non-root)
docker build -t app-nonroot -f dockerfile .
docker run --rm app-nonroot whoami
# Ausgabe: appuser
```

### 2. Sicherheitstest durchführen
```bash
# Als root: Kann Systemdateien lesen
docker run --rm app-root cat /etc/shadow
# Funktioniert!

# Als non-root: Kein Zugriff
docker run --rm app-nonroot cat /etc/shadow
# Permission denied
```

### 3. Mit Docker Scout/Trivy prüfen
```bash
docker scout cves app-nonroot
trivy image --severity CRITICAL,HIGH app-nonroot
```

### 4. Read-Only Filesystem
```bash
# Container mit read-only Filesystem starten
docker run --rm --read-only -p 5000:5000 app-nonroot

# Mit tmpfs für temporäre Dateien
docker run --rm --read-only --tmpfs /tmp -p 5000:5000 app-nonroot
```

## Dockerfile Best Practices für Non-Root

```dockerfile
# 1. User erstellen
RUN useradd -r -s /bin/false -u 1001 appuser

# 2. Verzeichnisse mit korrekten Rechten
WORKDIR /app
RUN chown -R appuser:appuser /app

# 3. User wechseln (NACH allen Root-Operationen)
USER appuser

# 4. Ports > 1024 verwenden (non-privileged)
EXPOSE 8080
```

## Kubernetes Security Context

```yaml
apiVersion: v1
kind: Pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    fsGroup: 1001
  containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
```

## Docker Compose Security

```yaml
services:
  app:
    image: app-nonroot
    user: "1001:1001"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    tmpfs:
      - /tmp
```

## Häufige Probleme & Lösungen

| Problem | Lösung |
|---------|--------|
| Permission denied beim Schreiben | `chown` für benötigte Verzeichnisse |
| Port < 1024 nicht möglich | Ports > 1024 verwenden, z.B. 8080 |
| npm/pip Cache-Fehler | Cache-Verzeichnisse anlegen und `chown` |
| Logs nicht beschreibbar | Log nach stdout/stderr |

## Kommandos

```bash
# User im Container prüfen
docker run --rm <image> whoami
docker run --rm <image> id

# Capabilities anzeigen
docker run --rm <image> cat /proc/1/status | grep Cap

# SecurityContext erzwingen
docker run --rm --user 1001:1001 <image>
```
