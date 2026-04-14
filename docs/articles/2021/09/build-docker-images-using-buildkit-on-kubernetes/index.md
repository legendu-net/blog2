---
title: Build Docker Images Using BuildKit on Kubernetes
created: 2021-09-15 16:43:40
date: 2026-04-13 23:14:10.776327
authors:
  - bendu
label: build-docker-images-using-buildkit-on-kubernetes
license: CC-BY-4.0
tags:
  - computer science
  - software
  - tools
  - Kubernetes
  - k8s
  - BuildKit
  - Docker
  - image
  - build
  - container
---

[buildkit-cli-for-kubectl](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl)
is a plugin for kubectl
which provides a similar experience building Docker images on Kubernetes
as building Docker images locally using `docker build`.
[buildkit-cli-for-kubectl](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl)
works perfectly in a personal/development Kubernetes cluster (e.g., minikube running locally),
however,
it doesn't work in an enterprise production environment
due to permission related issues
[#68](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl/issues/68),
[#24](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl/issues/24)
and
[#25](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl/issues/25)
.

## References

- [BuildKit](https://github.com/moby/buildkit)

- [Support custom DNS from dockerd config #734](https://github.com/moby/buildkit/issues/734)
