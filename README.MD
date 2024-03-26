# Lab README

This repository contains resources and instructions for completing the lab exercises. Please follow the guidelines below to set up your environment and get started.

## Prerequisites

Before you begin, ensure you have the following tools installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/)
- [Task](https://taskfile.dev/)
- [k6](https://k6.io/)
- [kind](https://kind.sigs.k8s.io/)

## Setup

**Clone this repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   task create_everything # setup full environment
   task test_apps # do some testing
   task delete_everything # delete everything

## Output
=================

