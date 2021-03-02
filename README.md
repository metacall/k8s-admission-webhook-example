# Dynamic validator

## Building

```bash
$ docker build -t server:metacall .
```

## Testing

```bash
kind create cluster
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.1.1/cert-manager.crds.yaml
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.1.1/cert-manager.yaml
kind load docker-image server:metacall
kubectl apply -f deploy/
```

### Test it

```bash
$ kubectl apply -f nginx-demo-ko.yaml
Error from server: admission webhook "validating.metacall.io" denied the request: THIS IS A FUCKING DEMO
$ kubectl apply -f nginx-demo-ok.yaml
pod/nginx created
```

