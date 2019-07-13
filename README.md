# payment

```python
FLASK_APP=paymentApplication.py flask run
```

```
curl http://localhost:5000
```


# docker 
```
$  git clone https://github.com/microservice-base/payment.git
$  cd payment
$  docker build -t payment-basket  -f container/docker/Dockerfile . 
$  docker run -d --name payment-app -p 8004:8004 payment-basket
```
