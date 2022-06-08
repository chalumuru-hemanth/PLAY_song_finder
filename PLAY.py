from this import s
from time import time
from tkinter import *
from tkinter import simpledialog
import time

from importlib.metadata import distribution
from re import search
from pyparsing import line
from selenium import webdriver
root =Tk()
root.title('PLAY')
e = Entry(root)
e.pack()
def get_me():
    global s
    s = e.get()
    root.after(1000,root.quit)
button =  Button(root,text="submit",command = get_me)
button.pack()
root.geometry("300x300")
root.mainloop()

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
search = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search.click()
search.send_keys(s)
enter = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button').click()
time.sleep(1)
first = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
first.click()
time.sleep(2)
fscreen = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[25]/div[2]/div[2]/button[10]')
fscreen.click()
