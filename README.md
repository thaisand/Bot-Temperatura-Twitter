# Bot-Temperatura-Twitter

O Bot-Temperatura-Twitter é um aplicativo em Python que twitta automaticamente a temperatura atual de Belo Horizonte. 

O bot usa a API OpenWeatherMap para obter a temperatura e a biblioteca Tweepy para interagir com a API do Twitter. Ele verifica periodicamente a temperatura e, se houver uma diferença em relação à última temperatura twittada, ele atualiza o status do Twitter com a nova temperatura. O código é escrito para ser executado em um loop infinito, verificando a temperatura a cada 5 minutos. **As chaves de acesso do Twitter e a chave de API do OpenWeatherMap devem ser configuradas antes da execução.**
