from bs4 import BeautifulSoup as bs
from requests import get
import telebot
import config

#token = "625744069:AAGTXbrysLdWXsapmqhI9SPYpgledYJWPa4"
token = config.token
url_base = 'https://statusblog.locaweb.com.br/'
locaweb = get(url_base).content
locaweb_page = bs(locaweb,'html.parser')
servico = locaweb_page.find_all('span',{'class':'name'})
status = locaweb_page.find_all('span',{'class':'component-status'})
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['locaweb'])
def locaweb_status (message):
    listasrv = []
    for op in servico:
        serv = op.get_text()
        listasrv.append(serv)

    listasts = []
    for stts in status:
        stat = stts.get_text()
        listasts.append(stat)

    s1 = listasrv[0].strip()
    s2 = listasrv[1].strip()
    s3 = listasrv[2].strip()
    s4 = listasrv[3].strip()
    s5 = listasrv[4].strip()
    s6 = listasrv[5].strip()
    s7 = listasrv[6].strip()
    s8 = listasrv[7].strip()
    s9 = listasrv[8].strip()
    s10 = listasrv[9].strip()

    st1 = listasts[0].strip()
    st2 = listasts[1].strip()
    st3 = listasts[2].strip()
    st4 = listasts[3].strip()
    st5 = listasts[4].strip()
    st6 = listasts[5].strip()
    st7 = listasts[6].strip()
    st8 = listasts[7].strip()
    st9 = listasts[8].strip()
    st10 = listasts[9].strip()


    msg = f"""
    Status Produtos Locaweb:

    Produto:                               Status:\n
    {s1}              {st1}\n 
    {s2}               {st2}\n 
    {s3}                  {st3}\n 
    {s4}                                    {st4}\n 
    {s5}                 {st5}\n 
    {s6}                      {st6}\n 
    {s7}                              {st7}\n 
    {s8}                       {st8}\n 
    {s9}                              {st9}\n 
    {s10}      {st10}\n
    """
    #print(msg)
    bot.reply_to(message,msg)

bot.polling()