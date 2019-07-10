FROM python:3


RUN git clone https://github.com/microservice-base/payment.git

WORKDIR payment/payment


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]
