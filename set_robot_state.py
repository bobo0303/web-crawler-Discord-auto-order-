# 導入Discord.py
import discord

# client是我們與Discord連結的橋樑
client = discord.Client()


# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('啟動了拉廢物')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    # 如果以「說」開頭
    if message.content.startswith('說'):
        # 分割訊息成兩份
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("是要供三小？")
        else:
            await message.channel.send(tmp[1])
    if message.content.startswith('更改狀態'):
        # 切兩刀訊息
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("媽的改三小不會打字逆？")
        else:
            game = discord.Game(tmp[1])
            # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await client.change_presence(status=discord.Status.idle, activity=game)


client.run('MTAwMjUzNjc3NTMwODI4MzkwNA.Gs7bJ3.gXWwbT5WRYorEM-pcVVsjnO-va_zdNR8Y-4oik') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面