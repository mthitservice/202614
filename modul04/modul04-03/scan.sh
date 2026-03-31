#!/bin/bash
# ============================================
# Trivy Scan Script
# ============================================

IMAGE_NAME="${1:-trivy-demo}"

echo "=== Building Image ==="
docker build -t $IMAGE_NAME .

echo ""
echo "=== Trivy Image Scan ==="
trivy image $IMAGE_NAME

echo ""
echo "=== Critical/High Only ==="
trivy image --severity CRITICAL,HIGH $IMAGE_NAME

echo ""
echo "=== Dockerfile Config Check ==="
trivy config --file-patterns "dockerfile:dockerfile" .

echo ""
echo "=== Filesystem Scan ==="
trivy fs --scanners vuln .

echo ""
echo "=== SBOM Generation ==="
trivy image --format cyclonedx -o sbom.json $IMAGE_NAME
echo "SBOM saved to sbom.json"
