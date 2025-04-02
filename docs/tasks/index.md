---
title: Layers
---

## Layer 1: Pod

- **Same Pod**: Server and client are in the same pod. They communicate using localhost.

## Layer 2: Namespace

- **Same Namespace, Different Pods**: Server and client are in separate pods within the same namespace.
- **Different Namespaces**: Server and client are in separate namespaces but within the same cluster.

## Layer 3: Node

- **Same Node, Same Namespace**: Server and client are in separate pods on the same node, within the same namespace.
- **Different Nodes, Same Namespace**: Server and client are in separate pods on different nodes, within the same namespace.
- **Same Node, Different Namespaces**: Server and client are on the same node but in different namespaces.
- **Different Nodes, Different Namespaces**: Server and client are on different nodes and in different namespaces.

## Layer 4: Cluster

- **Same Cluster, Different Nodes**: Server and client are in different namespaces and located on different nodes in the same cluster.
- **Different Clusters**: Server and client are in separate Kubernetes clusters.

## Layer 5: External to Cluster

- **External Client to Internal Server**: Server is inside Kubernetes (pod), and the client is outside Kubernetes (workstation or another external machine).
- **Internal Client to External Server**: Server is outside Kubernetes, and the client is inside Kubernetes (pod).
- **External to External via Kubernetes**: Server and client are both outside Kubernetes, but communication is routed through Kubernetes (e.g., viaLoadBalancer or Ingress).
