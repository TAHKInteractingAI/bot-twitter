import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import filedialog

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

global_delay = 3

def follow(): # follow the person only
    driver = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    log('Program started')
    log('Twitter opened')
    time.sleep(90)
    log("Logged in!")
    

    def visit_profiles():
        iloc_start = int(iloc_start_entry.get())
        iloc_end = int(iloc_end_entry.get())
        file = "input.xlsx"
        df = pd.read_excel(file)
        urls = df.iloc[iloc_start-2:iloc_end-1,0].values.tolist()
        #tweets = df.iloc[iloc_start-2:iloc_end-1,1].values.tolist()
        n = len(urls)
        log(f"Visiting {len(urls)} profiles.")
        
        for i in range(n):
            try:
                url = urls[i]
                #tweet = tweets[i]
                driver.get(url)
                time.sleep(5)
                # Perform actions on the profile here
                driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div').click()
                log(f"Followed profile: {url}")
                time.sleep(global_delay)
            except:
                log(f"Failed to follow profile: {url}")
                time.sleep(2)
                continue

    visit_profiles()

def follow_tweet(): #follow and tweet at the person
    driver = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    log('Program started')
    log('Twitter opened')
    time.sleep(90)
    log("Logged in!")
    

    def visit_profiles():
        iloc_start = int(iloc_start_entry.get())
        iloc_end = int(iloc_end_entry.get())
        file = "input.xlsx"
        df = pd.read_excel(file)
        urls = df.iloc[iloc_start-2:iloc_end-1,0].values.tolist()
        ceo_tweets = df.iloc[iloc_start-2:iloc_end-1,1].values.tolist()
        n = len(urls)
        log(f"Visiting {len(urls)} profiles.")
        
        for i in range(n):
            try:
                url = urls[i]
                tweet = ceo_tweets[i]
                driver.get(url)
                time.sleep(5)
                # Perform actions on the profile here
                driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div').click()
                log(f"Visited profile: {url}")
                time.sleep(2)
                driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
                time.sleep(2)
                driver.find_element("xpath",'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div').send_keys(tweet)
                time.sleep(2)
                driver.find_element("xpath",'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
                log(f"Tweeted at profile: {url}")
                time.sleep(global_delay)
            except:
                log(f"Failed to visit profile: {url}")
                time.sleep(2)
                continue

    visit_profiles()

def personal_tweet(): #personal tweet only
    driver = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    log('Program started')
    log('Twitter opened')
    time.sleep(90)
    log("Logged in!")
    

    def tweet():
        iloc_start = int(iloc_start_entry.get())
        iloc_end = int(iloc_end_entry.get())
        file = "input.xlsx"
        df = pd.read_excel(file)
        #urls = df.iloc[iloc_start-2:iloc_end-1,0].values.tolist()
        tweets = df.iloc[iloc_start-2:iloc_end-1,2].values.tolist()
        n = len(tweets)
        log(f"Tweeting")
        
        for i in range(n):
            try:
                #url = urls[i]
                tweet = tweets[i]
                driver.get("https://twitter.com/compose/tweet")
                time.sleep(5)
                # Perform actions on the profile here
                driver.find_element("xpath",'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div').send_keys(tweet)
                time.sleep(2)
                driver.find_element("xpath",'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()
                log(f"Tweeted")
                time.sleep(global_delay)
            except:
                log(f"Failed to tweet")
                time.sleep(2)
                continue
    tweet()


# Create tkinter window
window = tk.Tk()
window.title("Twitter Follow and Tweet Bot")
window.geometry("400x350")

# iloc start entry
iloc_start_label = tk.Label(window, text="Starting Row:")
iloc_start_label.pack()
iloc_start_entry = tk.Entry(window, width=40)
iloc_start_entry.pack()

# iloc end entry
iloc_end_label = tk.Label(window, text="Ending Row:")
iloc_end_label.pack()
iloc_end_entry = tk.Entry(window, width=40)
iloc_end_entry.pack(pady=10)

# follow button
follow_button = tk.Button(window, text="Follow the Twitter user Only", command=follow)
follow_button.pack(pady=10)

# follow and tweet button
follow_tweet_button = tk.Button(window, text="Follow and Tweet at the Twitter user", command=follow_tweet)
follow_tweet_button.pack(pady=10)

# personal tweet button
tweet_button = tk.Button(window, text="Personal Tweets", command=personal_tweet)
tweet_button.pack(pady=10)

window.mainloop()