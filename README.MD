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
   git clone https://github.com/k8sexperiment/applab
   cd applab
   task --list-all
   # setup full environment
   task create_everything 
   # do some testing
   task test_apps 
   # delete everything
   task delete_everything 
   ```

## Output - task create_everything
=================

```bash
task create_everything
task: [prerequisites] command -v helm >/dev/null 2>&1 || { echo >&2 "helm is required but it's not installed.  Aborting."; exit 1; }
task: [prerequisites] command -v kubectl >/dev/null 2>&1 || { echo >&2 "kubectl is required but it's not installed.  Aborting."; exit 1; }
task: [prerequisites] command -v k6 >/dev/null 2>&1 || { echo >&2 "k6 is required but it's not installed.  Aborting."; exit 1; }
task: [prerequisites] command -v kind >/dev/null 2>&1 || { echo >&2 "kind is required but it's not installed.  Aborting."; exit 1; }
task: [prerequisites] command -v docker >/dev/null 2>&1 || { echo >&2 "docker and docker compose is required but it's not installed.  Aborting."; exit 1; }
task: [build_and_test_images] docker compose -f source-test/docker-compose.yaml up -d
[+] Running 5/6
 ⠋ Network source-test_default     Created                                                                                                                                                                                                                                                                             1.0s
 ✔ Container prometheus            Started                                                                                                                                                                                                                                                                             0.6s
 ✔ Container grafana               Started                                                                                                                                                                                                                                                                             0.7s
 ✔ Container source-test-db-1      Started                                                                                                                                                                                                                                                                             0.7s
 ✔ Container source-test-reader-1  Started                                                                                                                                                                                                                                                                             0.9s
 ✔ Container source-test-writer-1  Started                                                                                                                                                                                                                                                                             0.9s
task: [build_and_test_images] docker compose -f source-test/docker-compose.yaml down
[+] Running 6/5
 ✔ Container grafana               Removed                                                                                                                                                                                                                                                                             0.2s
 ✔ Container prometheus            Removed                                                                                                                                                                                                                                                                             0.2s
 ✔ Container source-test-writer-1  Removed                                                                                                                                                                                                                                                                            10.2s
 ✔ Container source-test-reader-1  Removed                                                                                                                                                                                                                                                                            10.2s
 ✔ Container source-test-db-1      Removed                                                                                                                                                                                                                                                                             1.2s
 ✔ Network source-test_default     Removed                                                                                                                                                                                                                                                                             0.0s
task: [create_kind_cluster] kind create cluster --config=manifests/kind.yaml
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.29.2) 🖼
 ✓ Preparing nodes 📦 📦 📦 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
 ✓ Joining worker nodes 🚜
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
task: [load_images] kind load docker-image writer-image:2
Image: "writer-image:2" with ID "sha256:2774a7474d439917939b7a91f9827d7557a1d86a2325267b6326ca8df753b11f" not yet present on node "kind-control-plane", loading...
Image: "writer-image:2" with ID "sha256:2774a7474d439917939b7a91f9827d7557a1d86a2325267b6326ca8df753b11f" not yet present on node "kind-worker3", loading...
Image: "writer-image:2" with ID "sha256:2774a7474d439917939b7a91f9827d7557a1d86a2325267b6326ca8df753b11f" not yet present on node "kind-worker", loading...
Image: "writer-image:2" with ID "sha256:2774a7474d439917939b7a91f9827d7557a1d86a2325267b6326ca8df753b11f" not yet present on node "kind-worker2", loading...
task: [load_images] kind load docker-image reader-image:2
Image: "reader-image:2" with ID "sha256:34ea42d126c74a340477454c924e876bae743e9b8285f152de87ce7db913e062" not yet present on node "kind-control-plane", loading...
Image: "reader-image:2" with ID "sha256:34ea42d126c74a340477454c924e876bae743e9b8285f152de87ce7db913e062" not yet present on node "kind-worker3", loading...
Image: "reader-image:2" with ID "sha256:34ea42d126c74a340477454c924e876bae743e9b8285f152de87ce7db913e062" not yet present on node "kind-worker", loading...
Image: "reader-image:2" with ID "sha256:34ea42d126c74a340477454c924e876bae743e9b8285f152de87ce7db913e062" not yet present on node "kind-worker2", loading...
task: [deploy_nginx_controller] kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
namespace/ingress-nginx created
serviceaccount/ingress-nginx created
serviceaccount/ingress-nginx-admission created
role.rbac.authorization.k8s.io/ingress-nginx created
role.rbac.authorization.k8s.io/ingress-nginx-admission created
clusterrole.rbac.authorization.k8s.io/ingress-nginx created
clusterrole.rbac.authorization.k8s.io/ingress-nginx-admission created
rolebinding.rbac.authorization.k8s.io/ingress-nginx created
rolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx created
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx-admission created
configmap/ingress-nginx-controller created
service/ingress-nginx-controller created
service/ingress-nginx-controller-admission created
deployment.apps/ingress-nginx-controller created
job.batch/ingress-nginx-admission-create created
job.batch/ingress-nginx-admission-patch created
ingressclass.networking.k8s.io/nginx created
validatingwebhookconfiguration.admissionregistration.k8s.io/ingress-nginx-admission created
task: [deploy_nginx_controller] kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=90s
pod/ingress-nginx-controller-55bbd74b5f-bsppq condition met
task: [create_namespaces_and_deploy_components] kubectl create ns app
namespace/app created
task: [create_namespaces_and_deploy_components] kubectl create ns monitoring
namespace/monitoring created
task: [create_namespaces_and_deploy_components] kubectl create secret generic db-credentials --from-literal=user=testdb --from-literal=password=testdb -n app
secret/db-credentials created
task: [create_namespaces_and_deploy_components] helm upgrade --install mysql oci://registry-1.docker.io/bitnamicharts/mysql -f manifests/mysql.yaml -n app
Release "mysql" does not exist. Installing it now.
Pulled: registry-1.docker.io/bitnamicharts/mysql:10.1.0
Digest: sha256:2077eb83a7e4154213e51fc574031ef541b3c1c1cb2d35196f9de93d976dffb1
NAME: mysql
LAST DEPLOYED: Tue Mar 26 15:24:14 2024
NAMESPACE: app
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: mysql
CHART VERSION: 10.1.0
APP VERSION: 8.0.36

** Please be patient while the chart is being deployed **

Tip:

  Watch the deployment status using the command: kubectl get pods -w --namespace app

Services:

  echo Primary: mysql.app.svc.cluster.local:3306

Execute the following to get the administrator credentials:

  echo Username: root
  MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace app mysql -o jsonpath="{.data.mysql-root-password}" | base64 -d)

To connect to your database:

  1. Run a pod that you can use as a client:

      kubectl run mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.36-debian-12-r8 --namespace app --env MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --command -- bash

  2. To connect to primary service (read/write):

      mysql -h mysql.app.svc.cluster.local -uroot -p"$MYSQL_ROOT_PASSWORD"






WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
  - primary.resources
  - secondary.resources
+info https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
task: [create_namespaces_and_deploy_components] kubectl wait --namespace app --for=condition=ready pod --selector=app.kubernetes.io/instance=mysql --timeout=120s
pod/mysql-0 condition met
task: [create_namespaces_and_deploy_components] helm upgrade --install monitoring prometheus-community/kube-prometheus-stack -f manifests/monitoring.yaml -n monitoring
Release "monitoring" does not exist. Installing it now.
NAME: monitoring
LAST DEPLOYED: Tue Mar 26 15:25:00 2024
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1
NOTES:
kube-prometheus-stack has been installed. Check its status by running:
  kubectl --namespace monitoring get pods -l "release=monitoring"

Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.
task: [create_namespaces_and_deploy_components] kubectl apply -f manifests/writer.yaml -n app
deployment.apps/writer-deployment created
service/writer created
servicemonitor.monitoring.coreos.com/writer-monitor created
task: [create_namespaces_and_deploy_components] kubectl apply -f manifests/reader.yaml -n app
deployment.apps/reader-deployment created
servicemonitor.monitoring.coreos.com/reader-monitor created
poddisruptionbudget.policy/reader-pdb created
service/reader created
ingress.networking.k8s.io/reader-ingress created
task: [create_namespaces_and_deploy_components] kubectl wait --namespace app --for=condition=ready pod --selector=app=reader --timeout=90s
pod/reader-deployment-655b44dbb7-7hbsd condition met
pod/reader-deployment-655b44dbb7-m574p condition met
pod/reader-deployment-655b44dbb7-pcwtr condition met
```

## Output - task test_apps
=================

```bash
task test_apps                                                                                                                                                                                                                                                                                     2m 42s
task: [test_apps] k6 run k6-script.js

          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

     execution: local
        script: k6-script.js
        output: -

     scenarios: (100.00%) 1 scenario, 20 max VUs, 40s max duration (incl. graceful stop):
              * default: 20 looping VUs for 10s (gracefulStop: 30s)


     data_received..................: 38 kB 3.4 kB/s
     data_sent......................: 16 kB 1.5 kB/s
     http_req_blocked...............: avg=1.22ms  min=1µs     med=4µs     max=12.94ms  p(90)=1.21ms   p(95)=11.88ms
     http_req_connecting............: avg=67.27µs min=0s      med=0s      max=1.02ms   p(90)=50.4µs   p(95)=690.54µs
     http_req_duration..............: avg=76.36ms min=16.93ms med=43.98ms max=287.78ms p(90)=232.49ms p(95)=246.98ms
       { expected_response:true }...: avg=76.36ms min=16.93ms med=43.98ms max=287.78ms p(90)=232.49ms p(95)=246.98ms
     http_req_failed................: 0.00% ✓ 0        ✗ 200
     http_req_receiving.............: avg=87.72µs min=19µs    med=41µs    max=1.9ms    p(90)=206µs    p(95)=290.34µs
     http_req_sending...............: avg=37.01µs min=5µs     med=16µs    max=386µs    p(90)=65µs     p(95)=236.24µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s
     http_req_waiting...............: avg=76.23ms min=16.88ms med=43.91ms max=287.7ms  p(90)=232.07ms p(95)=246.92ms
     http_reqs......................: 200   18.19892/s
     iteration_duration.............: avg=1.07s   min=1.01s   med=1.04s   max=1.28s    p(90)=1.24s    p(95)=1.26s
     iterations.....................: 200   18.19892/s
     vus............................: 20    min=20     max=20
     vus_max........................: 20    min=20     max=20


running (11.0s), 00/20 VUs, 200 complete and 0 interrupted iterations
default ✓ [======================================] 20 VUs  10s
task: [test_apps] for ((i=0; i<2; i++)); do curl -s http://localhost/reader; sleep 2; done
{"count":52,"pod":"reader-deployment-655b44dbb7-m574p"}
{"count":54,"pod":"reader-deployment-655b44dbb7-7hbsd"}
task: [test_apps] kubectl rollout restart deployment reader-deployment -n app
deployment.apps/reader-deployment restarted
task: [test_apps] for ((i=0; i<10; i++)); do curl -s http://localhost/reader; sleep 2; done
{"count":56,"pod":"reader-deployment-655b44dbb7-pcwtr"}
{"count":58,"pod":"reader-deployment-655b44dbb7-7hbsd"}
{"count":60,"pod":"reader-deployment-655b44dbb7-m574p"}
{"count":62,"pod":"reader-deployment-7885c56845-c2tdm"}
{"count":64,"pod":"reader-deployment-7885c56845-c2tdm"}
{"count":66,"pod":"reader-deployment-7885c56845-n4nwh"}
{"count":68,"pod":"reader-deployment-7885c56845-c2tdm"}
{"count":70,"pod":"reader-deployment-7885c56845-9d945"}
{"count":72,"pod":"reader-deployment-7885c56845-9d945"}
{"count":74,"pod":"reader-deployment-7885c56845-9d945"}
```

## Output - cluster pods
=================

```bash
kubectl get po -A -o wide
NAMESPACE            NAME                                                     READY   STATUS      RESTARTS   AGE     IP           NODE                 NOMINATED NODE   READINESS GATES
app                  mysql-0                                                  1/1     Running     0          3m34s   10.244.2.4   kind-worker3         <none>           <none>
app                  reader-deployment-7885c56845-9d945                       1/1     Running     0          91s     10.244.3.6   kind-worker          <none>           <none>
app                  reader-deployment-7885c56845-c2tdm                       1/1     Running     0          89s     10.244.2.7   kind-worker3         <none>           <none>
app                  reader-deployment-7885c56845-n4nwh                       1/1     Running     0          90s     10.244.1.8   kind-worker2         <none>           <none>
app                  writer-deployment-7c5c5ddf85-vljzq                       1/1     Running     0          2m30s   10.244.1.6   kind-worker2         <none>           <none>
ingress-nginx        ingress-nginx-admission-create-d9xww                     0/1     Completed   0          4m4s    10.244.1.2   kind-worker2         <none>           <none>
ingress-nginx        ingress-nginx-admission-patch-kt252                      0/1     Completed   2          4m4s    10.244.2.2   kind-worker3         <none>           <none>
ingress-nginx        ingress-nginx-controller-55bbd74b5f-bsppq                1/1     Running     0          4m4s    10.244.0.5   kind-control-plane   <none>           <none>
kube-system          coredns-76f75df574-cdc4q                                 1/1     Running     0          4m30s   10.244.0.4   kind-control-plane   <none>           <none>
kube-system          coredns-76f75df574-sfz9x                                 1/1     Running     0          4m30s   10.244.0.3   kind-control-plane   <none>           <none>
kube-system          etcd-kind-control-plane                                  1/1     Running     0          4m44s   172.19.0.5   kind-control-plane   <none>           <none>
kube-system          kindnet-79hsx                                            1/1     Running     0          4m23s   172.19.0.4   kind-worker3         <none>           <none>
kube-system          kindnet-cf84b                                            1/1     Running     0          4m24s   172.19.0.3   kind-worker2         <none>           <none>
kube-system          kindnet-ggjsb                                            1/1     Running     0          4m30s   172.19.0.5   kind-control-plane   <none>           <none>
kube-system          kindnet-z4b6l                                            1/1     Running     0          4m23s   172.19.0.2   kind-worker          <none>           <none>
kube-system          kube-apiserver-kind-control-plane                        1/1     Running     0          4m44s   172.19.0.5   kind-control-plane   <none>           <none>
kube-system          kube-controller-manager-kind-control-plane               1/1     Running     0          4m44s   172.19.0.5   kind-control-plane   <none>           <none>
kube-system          kube-proxy-2tr9d                                         1/1     Running     0          4m30s   172.19.0.5   kind-control-plane   <none>           <none>
kube-system          kube-proxy-7rw9d                                         1/1     Running     0          4m23s   172.19.0.4   kind-worker3         <none>           <none>
kube-system          kube-proxy-c4qhw                                         1/1     Running     0          4m24s   172.19.0.3   kind-worker2         <none>           <none>
kube-system          kube-proxy-v6mtf                                         1/1     Running     0          4m23s   172.19.0.2   kind-worker          <none>           <none>
kube-system          kube-scheduler-kind-control-plane                        1/1     Running     0          4m44s   172.19.0.5   kind-control-plane   <none>           <none>
local-path-storage   local-path-provisioner-7577fdbbfb-5tdbr                  1/1     Running     0          4m30s   10.244.0.2   kind-control-plane   <none>           <none>
monitoring           alertmanager-monitoring-kube-prometheus-alertmanager-0   2/2     Running     0          2m30s   10.244.1.5   kind-worker2         <none>           <none>
monitoring           monitoring-grafana-8579bfbb94-4twtw                      3/3     Running     0          2m41s   10.244.3.4   kind-worker          <none>           <none>
monitoring           monitoring-kube-prometheus-operator-5bc9ffd764-qz2h9     1/1     Running     0          2m41s   10.244.3.3   kind-worker          <none>           <none>
monitoring           monitoring-kube-state-metrics-6dd6484f-l7ntk             1/1     Running     0          2m41s   10.244.1.3   kind-worker2         <none>           <none>
monitoring           monitoring-prometheus-node-exporter-p7xrt                1/1     Running     0          2m41s   172.19.0.4   kind-worker3         <none>           <none>
monitoring           monitoring-prometheus-node-exporter-pxqz6                1/1     Running     0          2m41s   172.19.0.3   kind-worker2         <none>           <none>
monitoring           monitoring-prometheus-node-exporter-svxc8                1/1     Running     0          2m41s   172.19.0.2   kind-worker          <none>           <none>
monitoring           monitoring-prometheus-node-exporter-xnzg5                1/1     Running     0          2m41s   172.19.0.5   kind-control-plane   <none>           <none>
monitoring           prometheus-monitoring-kube-prometheus-prometheus-0       2/2     Running     0          2m30s   10.244.2.5   kind-worker3         <none>           <none>
---
kubectl get svc -A

NAMESPACE       NAME                                                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                        AGE
app             mysql                                                ClusterIP   10.96.130.193   <none>        3306/TCP                       3m49s
app             mysql-headless                                       ClusterIP   None            <none>        3306/TCP                       3m49s
app             reader                                               ClusterIP   10.96.82.50     <none>        8080/TCP,8000/TCP              2m45s
app             writer                                               ClusterIP   10.96.28.27     <none>        8000/TCP                       2m45s
default         kubernetes                                           ClusterIP   10.96.0.1       <none>        443/TCP                        5m1s
ingress-nginx   ingress-nginx-controller                             NodePort    10.96.241.16    <none>        80:30148/TCP,443:32741/TCP     4m19s
ingress-nginx   ingress-nginx-controller-admission                   ClusterIP   10.96.65.114    <none>        443/TCP                        4m19s
kube-system     kube-dns                                             ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP,9153/TCP         4m59s
kube-system     monitoring-kube-prometheus-coredns                   ClusterIP   None            <none>        9153/TCP                       2m56s
kube-system     monitoring-kube-prometheus-kube-controller-manager   ClusterIP   None            <none>        10257/TCP                      2m56s
kube-system     monitoring-kube-prometheus-kube-etcd                 ClusterIP   None            <none>        2381/TCP                       2m56s
kube-system     monitoring-kube-prometheus-kube-proxy                ClusterIP   None            <none>        10249/TCP                      2m56s
kube-system     monitoring-kube-prometheus-kube-scheduler            ClusterIP   None            <none>        10259/TCP                      2m56s
kube-system     monitoring-kube-prometheus-kubelet                   ClusterIP   None            <none>        10250/TCP,10255/TCP,4194/TCP   2m45s
monitoring      alertmanager-operated                                ClusterIP   None            <none>        9093/TCP,9094/TCP,9094/UDP     2m45s
monitoring      monitoring-grafana                                   ClusterIP   10.96.251.216   <none>        80/TCP                         2m56s
monitoring      monitoring-kube-prometheus-alertmanager              ClusterIP   10.96.240.150   <none>        9093/TCP,8080/TCP              2m56s
monitoring      monitoring-kube-prometheus-operator                  ClusterIP   10.96.5.26      <none>        443/TCP                        2m56s
monitoring      monitoring-kube-prometheus-prometheus                ClusterIP   10.96.184.149   <none>        9090/TCP,8080/TCP              2m56s
monitoring      monitoring-kube-state-metrics                        ClusterIP   10.96.118.15    <none>        8080/TCP                       2m56s
monitoring      monitoring-prometheus-node-exporter                  ClusterIP   10.96.201.17    <none>        9100/TCP                       2m56s
monitoring      prometheus-operated                                  ClusterIP   None            <none>        9090/TCP                       2m45s
---
kubectl get ingress -A

NAMESPACE    NAME                 CLASS    HOSTS   ADDRESS     PORTS   AGE
app          reader-ingress       <none>   *       localhost   80      3m26s
monitoring   monitoring-grafana   <none>   *       localhost   80      3m37s

kubectl get servicemonitor -n app

NAME             AGE
reader-monitor   3m46s
writer-monitor   3m46s
```

## Output - check Grafana
=================

![Grafana example](https://github.com/k8sexperiment/applab/blob/main/source-test/grafana/dashboard.png)

## Output - delete everything
=================

```bash
task delete_everything
task: [delete_everything] kind delete cluster
Deleting cluster "kind" ...
Deleted nodes: ["kind-control-plane" "kind-worker3" "kind-worker" "kind-worker2"]
```