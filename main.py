#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        await message.channel.send('pong')

client.run('MTAwMjUzNjc3NTMwODI4MzkwNA.Gs7bJ3.gXWwbT5WRYorEM-pcVVsjnO-va_zdNR8Y-4oik') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面