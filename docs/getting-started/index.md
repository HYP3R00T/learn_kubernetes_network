---
title: Getting Started
---

## Prerequisite

- Kubernetes
- Docker

### My Setup

I have two machines.

- Workstation:
    - Host OS: Windows 11
    - WSL2: Ubuntu 24.04
    - Tools installed in Host:
        - Docker (with WSL2 integration)
    - Tools installed In WSL2:
        - `kubectl`
        - `k9s`
- Server:
    - Host: Ubuntu 24.04 Server
    - Tools installed:
        - `k3s`: Kubernetes cluster
        - `docker`

Both of these machines are in the same LAN (Local Area Network).

## Hardware Requirements

You don't need two separate machines as I do. But separate machines allow me experiment things without worry too much about the consequences. If anything goes south, you can simply reinstall Ubuntu in the server and start again.
