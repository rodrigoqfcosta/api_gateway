# API_Gateway
### Repositório exclusivo para API Gateway

O API Gateway ou Gateway de Serviços, é o cara que chama so serviços que podem estar instalados em mais de uma maquina até mesmo com tecnologias diferentes, 
sendo um ponto único de entrada para os sistemas que se comunicam com os serviços.

### INICIALIZANDO API:

Antes de iniciar a API, certifique-se de habilitar o seu ambiente virtual (VENV):
###### MacOS/Linux:
```
$ source venv/bin/activate
```
###### Windows:
```
> venv\Scripts\activate
```

</br>Em seguida efetue a instalação dos requirements:
```
> pip install -r requirements.txt
```

Agora estamos prontos para executar a API Gateway:
```
> python api_gateway.py
```
