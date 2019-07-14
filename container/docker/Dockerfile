FROM python:3-alpine

RUN python --version

#RUN apk update && apk upgrade && \
#    apk add --no-cache bash git

RUN apk add git


RUN git clone https://github.com/microservice-base/payment.git

WORKDIR /payment/payment

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["paymentApplication.py"]
#CMD ["echo","hello"]
