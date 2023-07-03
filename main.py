import tweepy
import requests
import time

# Configurar as chaves de acesso do Twitter
bearer_token = 'AAAAAAAAAAAAAAAAAAAAABZTogEAAAAANcav5xsdavU3JwHudWGEmhR%2Boz0%3D7bOmeDssNafdHyBsNhMKeov0KDshgR8VekK5SZfsh1bxRnZg8y'
access_token = '1637446359333699585-on06KcLHRXkSQ6r5SvDdRAirf8j1lZ'
access_token_secret = 'XcGOYFf10KvNX9dYtcbbX59iF4e9FfXHXHhheVvCdRB7e'

# Configurar a chave de API do OpenWeatherMap
api_key = 'd5e40bae38cd01caf620c5aa0a9f40a3'

# Autenticar o bot com o Twitter
auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)

# Variáveis para armazenar a última temperatura twittada
last_temperature = None

while True:
    try:
        # Obter a temperatura atual de Belo Horizonte usando a API OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Belo%20Horizonte,BR&appid={api_key}&units=metric"
        response = requests.get(url)

        # Verificar o código de status da resposta
        if response.status_code == 200:
            data = response.json()

            # Verificar se os dados estão presentes
            if 'main' in data:
                temperature = data['main']['temp']
                
                # Comparar com a temperatura anteriormente twittada
                if temperature != last_temperature:
                    # Tweetar a nova temperatura no Twitter
                    tweet = f"A temperatura atual em Belo Horizonte é de {temperature}°C."
                    api.update_status(tweet)
                    last_temperature = temperature
            else:
                print("Erro: Dados não encontrados na resposta da API.")
        else:
            print("Erro ao fazer a requisição à API OpenWeatherMap.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    # Aguardar 5 minutos antes de verificar novamente a temperatura
    time.sleep(300)