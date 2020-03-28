# payment

https://github.com/microservice-base


## how to create project

https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application


## how to run project

```
$  git clone https://github.com/microservice-base/payment.git

$  cd payment

$  python3 payment/paymentApplication.py

$  curl http://localhost:8004
```

## contributing

[Contributing guide](CONTRIBUTING.md).


# docker 
```docker
$  git clone https://github.com/microservice-base/payment.git
$  cd payment
$  docker build -t image-payment  -f container/docker/Dockerfile . 
$  docker run -d --name app-payment -p 8004:8004 image-payment
```
# kubernetes
```
i will add configs
```
