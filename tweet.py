import tweepy
import requests
import time
import config

# Autenticar o bot com o Twitter
client = tweepy.Client(consumer_key=config.API_KEY, consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(consumer_key=config.API_KEY, consumer_secret=config.API_SECRET, access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Variáveis para armazenar a última temperatura twittada
last_temperature = None

# Função para twittar usando a API do Twitter
def tweet(text):
    response = client.create_tweet(text=text)
    print(response)

while True:
    try:
        # Obter a temperatura atual de Belo Horizonte usando a API OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Belo%20Horizonte,BR&appid={config.OPENWEATHER_API}&units=metric"
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
                    tweet_text = f"A temperatura atual em Belo Horizonte é de {temperature}°C."
                    tweet(tweet_text)
                    last_temperature = temperature
            else:
                print("Erro: Dados não encontrados na resposta da API.")
        else:
            print("Erro ao fazer a requisição à API OpenWeatherMap.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    # Aguardar 30 minutos antes de verificar novamente a temperatura
    time.sleep(1800)
