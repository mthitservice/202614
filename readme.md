# 201614

Docker Grundlagen

>Trainer: Michael Lindner

## Über Container-Standards

Container-Technologien wie Docker basieren auf offenen Standards, die von der **[Open Container Initiative (OCI)](https://opencontainers.org/)** definiert und verwaltet werden. Die OCI wurde 2015 gegründet und ist ein Projekt der Linux Foundation.

**Die OCI spezifiziert:**

- 📦 **Image Specification** - Format und Aufbau von Container-Images
- 🚀 **Runtime Specification** - Wie Container ausgeführt werden
- 📊 **Distribution Specification** - Verteilung von Container-Images über Registries

Dies gewährleistet Interoperabilität zwischen verschiedenen Container-Plattformen (Docker, Podman, containerd, CRI-O, etc.) und verhindert Vendor Lock-in.

**Weitere Informationen:**

- [OCI Official Website](https://opencontainers.org/)
- [OCI Image Specification](https://github.com/opencontainers/image-spec)
- [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec)
