# payment

```
$  git clone https://github.com/microservice-base/payment.git
$  cd payment
$  python3 payment/paymentApplication.py
$  curl http://localhost:8004
```


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
