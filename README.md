Please select a language: 

<details>
  <summary> English  </summary>

# Twitter-Bot-Temperature

[Twitter-Bot-Temperature](https://twitter.com/temperaturabh)
 is a Python application that automatically tweets the current temperature in Belo Horizonte, Minas Gerais - Brasil. 

The bot uses the OpenWeatherMap API to obtain the temperature and the Tweepy library to interact with the Twitter API. It periodically checks the temperature and, if there is a difference from the last tweeted temperature, it updates the Twitter status with the new temperature. The code is written to run in a loop, checking the temperature every 30 minutes. **The Twitter access keys and the OpenWeatherMap API key must be configured before execution.

### Configuring the keys
- Create a config.py file
- Add the following code, updating the value of the variables with their keys.
``` 
# Configure Twitter's access keys
API_KEY = 'ENTER_YOUR_KEY_HERE'
API_SECRET = 'ENTER_YOUR_KEY_HERE'
BEARER_TOKEN = 'ENTER_YOUR_KEY_HERE'
ACCESS_TOKEN = 'ENTER_YOUR_KEY_HERE'
ACCESS_TOKEN_SECRET = 'ENTER_YOUR_KEY_HERE'

# Configure the Open Weather access key
OPENWEATHER_API = 'ENTER_YOUR_KEY_HERE'
```

</details>

<details>
  <summary> Português  </summary>
  
# Bot-Temperatura-Twitter

O [Bot-Temperatura-Twitter](https://twitter.com/temperaturabh) é um aplicativo em Python que twitta automaticamente a temperatura atual de Belo Horizonte. 

O bot usa a API OpenWeatherMap para obter a temperatura e a biblioteca Tweepy para interagir com a API do Twitter. Ele verifica periodicamente a temperatura e, se houver uma diferença em relação à última temperatura twittada, ele atualiza o status do Twitter com a nova temperatura. O código é escrito para ser executado em um loop, verificando a temperatura a cada 30 minutos. **As chaves de acesso do Twitter e a chave de API do OpenWeatherMap devem ser configuradas antes da execução.**

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
</details>
