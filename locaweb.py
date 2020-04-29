from bs4 import BeautifulSoup as bs
from requests import get
import telebot
from datetime import datetime
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

    data_hj = datetime.now()
    data_atual = data_hj.strftime('%d/%m/%Y %H:%M')

    msg = f"""
    *Status Produtos Locaweb:*

    *Produto:*                               *Status:*\n
    *{s1}*              _{st1}_\n 
    *{s2}*               _{st2}_\n 
    *{s3}*                  _{st3}_\n 
    *{s4}*                                    _{st4}_\n 
    *{s5}*                 _{st5}_\n 
    *{s6}*                      _{st6}_\n 
    *{s7}*                              _{st7}_\n 
    *{s8}*                       _{st8}_\n 
    *{s9}*                              _{st9}_\n 
    *{s10}*      _{st10}_\n
    Data da Consulta:  *{data_atual}*\n
    """
    #print(msg)
    bot.reply_to(message,msg,parse_mode="Markdown")

bot.polling()