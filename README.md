# Bot-Temperatura-Twitter

O [Bot-Temperatura-Twitter](https://twitter.com/TemperaturaBH) é um aplicativo em Python que twitta automaticamente a temperatura atual de Belo Horizonte. 

O bot usa a API OpenWeatherMap para obter a temperatura e a biblioteca Tweepy para interagir com a API do Twitter. Ele verifica periodicamente a temperatura e, se houver uma diferença em relação à última temperatura twittada, ele atualiza o status do Twitter com a nova temperatura. O código é escrito para ser executado em um loop infinito, verificando a temperatura a cada 30 minutos. **As chaves de acesso do Twitter e a chave de API do OpenWeatherMap devem ser configuradas antes da execução.**

### Configurando as chaves
- Crie um arquivo config.py
- Adicione o código a seguir, atualizando o valor das variáveis com suas chaves.
``` 
# Configurar as chaves de acesso do Twitter
API_KEY = 'INSIRA_SUA_CHAVE_AQUI'
API_SECRET = 'INSIRA_SUA_CHAVE_AQUI'
BEARER_TOKEN = 'INSIRA_SUA_CHAVE_AQUI'
ACCESS_TOKEN = 'INSIRA_SUA_CHAVE_AQUI'
ACCESS_TOKEN_SECRET = 'INSIRA_SUA_CHAVE_AQUI'

# Configurar a chave de acesso do Open Weather
OPENWEATHER_API = 'INSIRA_SUA_CHAVE_AQUI'
``` 
