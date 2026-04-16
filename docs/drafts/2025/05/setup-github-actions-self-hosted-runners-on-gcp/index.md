---
title: Setup GitHub Actions Self-hosted Runners on GCP
created: 2025-05-08 15:51:58
date: 2026-04-15 19:27:00.580867
authors:
  - bendu
label: setup-github-actions-self-hosted-runners-on-gcp
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - GitHub
  - Actions
  - runner
  - self-hosted
  - GCP
  - cloud
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Tips & Traps

1. You must allow http and https traffic for it to work.
   For more instructions,
   pelase refer to
   [Setup GitHub Actions self-hosted runners on Google Compute Engine Instance](https://www.youtube.com/watch?v=yfMzNVtQsVw)
   .

## GitHub Actions & GCP

- [actions-runner-controller](https://github.com/actions/actions-runner-controller)

- [Optimizing Costs with GitHub Actions: Dynamically Starting and Stopping Self-Hosted Runner VMs](https://nakamasato.medium.com/optimizing-costs-with-github-actions-self-hosted-runner-dynamically-starting-and-stopping-gcp-vms-c04acb69bdee)

## References

- [Connecting GitHub Actions and Google Cloud Deploy](https://cloud.google.com/blog/products/devops-sre/using-github-actions-with-google-cloud-deploy)

- [Deploy to Cloud Run with GitHub Actions](https://cloud.google.com/blog/products/devops-sre/deploy-to-cloud-run-with-github-actions/)
