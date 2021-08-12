from selenium import webdriver
import time
import tweepy


driver = webdriver.Chrome()
driver.get('')

time.sleep(2)

pontos = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div/div[3]/div[1]/p')
pontos_content = pontos.text
str(pontos_content)

variacao = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div/div[3]/div[2]/p')
variacao_content = variacao.text

str(variacao_content)

driver.close()

# Abaixo você deve inserir os dados de acesso da sua API do Twitter
consumer_key = "***"
consumer_secret = "***"
access_token = "***"
access_token_secret = "***"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

texto = "Bot de Fechamento IBOV: "+ pontos_content + '. Variação de: '+variacao_content
print(texto)
api.update_status(texto)
print("Tweet enviado corretamente")

