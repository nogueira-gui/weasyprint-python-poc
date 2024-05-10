# Weasyprint Python POC

## Description

This project is a simple test using weasyprint to convert html to pdf

## Requirements

- Python 3.x
- Docker

## Installation

1. Clone the repository
```
git clone https://github.com/nogueira-gui/weasyprint-python-poc
```
2. Run Dockerfile
```
docker build -t my-python-app -f Dockerfile .
```
3. Run docker-compose
```
docker-compose up
```
4. Run the curl to download pdf
```
curl --request POST \
  --url http://localhost:5000/receipt \
  --header 'Content-Type: application/json' \
  --data '{
    "company": {
        "name": "Fazer Orçamento Tecnologia LTDA",
        "cnpj": "12.345.678/0001-10",
        "address": "Av. Paulista, 2005 - São Paulo",
        "phone": "(11) 96786-8752"
    },
    "client": {
        "name": "John Doe",
        "address": "Rua Teste, 0 - São Paulo",
        "phone": "(11) 98888-8888"
    },
    "amount": "R$ 413,00",
    "date": "14/07/2020",
    "payment_method": "pix"
}' --output receipt.pdf
```
5. The generated file will also be available in the generated output folder.