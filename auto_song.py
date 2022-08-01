from selenium import webdriver
from time import sleep
from dotenv import load_dotenv
import json
import os, argparse
from random import shuffle

list_EDM_EN = []
list_EN = []
list_JP = []
song_number = 0
load_dotenv()
email = os.getenv('email')
password = os.getenv('password')

parser = argparse.ArgumentParser(description='')
parser.add_argument('--style', type=str, default='EMD_EN') #batch size= 4
args = parser.parse_args()  # 參數 (上面那一堆)

if __name__ == '__main__':

    with open("./song_list/EDM_EN.txt") as song_file_EDM_EN:
        for song_EDM_EN in song_file_EDM_EN:
            list_EDM_EN.append(song_EDM_EN)
            song_number_EDM_EN = len(list_EDM_EN)
        shuffle(list_EDM_EN)
    with open("./song_list/EN.txt") as song_file_EN:
        for song_EN in song_file_EN:
            list_EN.append(song_EN)
            song_number_EN = len(list_EN)
        shuffle(list_EN)
    with open("./song_list/JP.txt") as song_file_JP:
        for song_JP in song_file_JP:
            list_JP.append(song_JP)
            song_number_JP = len(list_JP)
        shuffle(list_JP)


    driver = webdriver.Chrome()
    driver.get(
        'https://discord.com/channels/666975325431005186/972527260374564904')
    sleep(1)

    driver.find_element("xpath",
                        '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/section/div/button[2]/div').click()
    driver.find_element("xpath",
                        '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(email)
    driver.find_element("xpath",
                        '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
    driver.find_element("xpath",
                        '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div').click()
    sleep(4)
    driver.find_element("xpath",
                        '//*[@id="channels"]/ul/li[3]/div/div/a').click()
    sleep(2)
    if args.style == 'EDM_EN':
        for n in list_EDM_EN:
            driver.find_element("xpath",
                                '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys(n+'\n')
            sleep(5)
        driver.find_element("xpath",
                            '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys('總共點了:'+str(song_number_EDM_EN)+'首 EDM_EN\n')

    if args.style == 'EN':
        for n in list_EN:
            driver.find_element("xpath",
                                '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys(n + '\n')
            sleep(5)
        driver.find_element("xpath",
                            '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys('總共點了:' +  str(song_number_EN) + '首 EN\n')
    if args.style == 'JP':

        for n in list_JP:
            driver.find_element("xpath",
                                '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys('!p ' + n + '\n')
            sleep(5)
        driver.find_element("xpath",
                            '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div').send_keys('總共點了:' +  str(song_number_JP) + '首 JP\n')





