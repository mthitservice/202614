# Azure ACR DEMO
# Modul 09 – Azure Container Registry (ACR)

## Ziel

Ein Docker-Image lokal bauen und in die **Azure Container Registry** pushen – ohne CI/CD, rein manuell über die Azure CLI.

---

## Voraussetzungen

- [Azure CLI](https://learn.microsoft.com/de-de/cli/azure/install-azure-cli) installiert
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installiert und gestartet
- Ein aktives Azure-Abonnement

---

## Schritt 1 – Bei Azure anmelden

```bash
az login
```

> Wird im Browser ein Anmeldefenster geöffnet. Nach erfolgreicher Anmeldung wird das aktive Abonnement angezeigt.

---

## Schritt 2 – Ressourcengruppe erstellen

```bash
az group create --name rg-container-demo --location westeurope
```

---

## Schritt 3 – Azure Container Registry erstellen

```bash
az acr create \
  --resource-group rg-container-demo \
  --name acrdemokurs2025 \
  --sku Basic \
  --admin-enabled true
```

> **Wichtig:** Der Name der ACR muss global eindeutig sein (nur Kleinbuchstaben und Zahlen, 5–50 Zeichen). Passe `acrdemokurs2025` ggf. an.

### Zugangsdaten anzeigen

```bash
az acr credential show --name acrdemokurs2025
```

Notiere dir **username** und **password** – du brauchst sie für den Docker-Login.

---

## Schritt 4 – Docker-Image lokal bauen

Navigiere in das Verzeichnis `modul09/`:

```bash
cd modul09
docker build -t acr-demo-app:v1 .
```

### Lokaler Test (optional)

```bash
docker run -d -p 5000:5000 --name acr-test acr-demo-app:v1
```

Öffne `http://localhost:5000` im Browser. Danach:

```bash
docker stop acr-test && docker rm acr-test
```

---

## Schritt 5 – Image taggen für ACR

```bash
docker tag acr-demo-app:v1 acrdemokurs2025.azurecr.io/acr-demo-app:v1
```

> Das Tag-Format ist: `<registry-name>.azurecr.io/<image-name>:<tag>`

---

## Schritt 6 – Bei ACR anmelden

### Variante A – Über Azure CLI (empfohlen)

```bash
az acr login --name acrdemokurs2025
```

### Variante B – Über Docker Login

```bash
docker login acrdemokurs2025.azurecr.io \
  --username acrdemokurs2025 \
  --password <PASSWORT_AUS_SCHRITT_3>
```

---

## Schritt 7 – Image in ACR pushen

```bash
docker push acrdemokurs2025.azurecr.io/acr-demo-app:v1
```

---

## Schritt 8 – Image in ACR überprüfen

```bash
az acr repository list --name acrdemokurs2025 --output table
```

```bash
az acr repository show-tags --name acrdemokurs2025 --repository acr-demo-app --output table
```

---

## Schritt 9 – Alternative: Image direkt in ACR bauen (ohne lokales Docker)

Die ACR kann Images auch serverseitig bauen:

```bash
az acr build \
  --registry acrdemokurs2025 \
  --image acr-demo-app:v2 \
  --file dockerfile \
  .
```

> Dabei wird der lokale Build-Kontext hochgeladen und das Image direkt in der Registry gebaut. Docker muss dafür nicht lokal installiert sein.

---

## Aufräumen

```bash
# Einzelnes Image löschen
az acr repository delete --name acrdemokurs2025 --repository acr-demo-app --yes

# Komplette Ressourcengruppe löschen (inkl. ACR)
az group delete --name rg-container-demo --yes --no-wait
```

---

## Zusammenfassung

| Schritt | Befehl |
|---|---|
| RG erstellen | `az group create` |
| ACR erstellen | `az acr create` |
| Image bauen | `docker build` |
| Image taggen | `docker tag` |
| ACR Login | `az acr login` |
| Image pushen | `docker push` |
| Image prüfen | `az acr repository list` |
| Remote Build | `az acr build` |

---

## Weiter

→ **Modul 10**: Container als Azure Container Instance (ACI) deployen
