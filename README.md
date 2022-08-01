# web-crawler-Discord-auto-order-
Discord 自動點歌爬蟲

簡單的自動爬蟲 (須配合點歌bot)

# 推薦點歌機器人 Neeko
- [Neeko](https://discord.bots.gg/bots/543771182936358912)

# 用法

1. 根據 `requirements.txt` 安裝環境
2. 修改 `env.txt` 內容改成自己discord 帳號密碼
3. 將 `env.txt` 檔名改成 `.env`
4. 在 `song list` 資料夾自己選擇或建立喜歡的音樂類型與歌單
5. 執行 `auto_song.py` 若有增加新的歌單請自己依照程式增加新模塊

# auto_song 設定

```
with open("./song_list/EDM_EN.txt") as song_file_EDM_EN:
    for song_EDM_EN in song_file_EDM_EN:
        list_EDM_EN.append(song_EDM_EN)
        song_number_EDM_EN = len(list_EDM_EN)
    shuffle(list_EDM_EN)
        
if args.style == 'JP':
  for n in list_JP:
    driver.find_element("xpath",
                            '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys('!p ' + n + '\n')
    sleep(5)
  driver.find_element("xpath",
                            '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys('總共點了:' +  str(song_number_JP) + '首 JP\n')

```

