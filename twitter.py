import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import filedialog
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding="utf-8")
    log_file.write(log_text + "\n")
    log_file.close()


global_delay = 3


def follow_only():  # follow the person only
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    log("Program started")
    log("Twitter opened")

    def visit_profiles():
        iloc_start = int(iloc_start_entry.get())
        iloc_end = int(iloc_end_entry.get())
        file = "input.xlsx"
        df = pd.read_excel(file)
        urls = df.iloc[iloc_start - 1 : iloc_end, 0].values.tolist()
        n = len(urls)
        log(f"Visiting {len(urls)} profiles.")

        for i in range(n):
            try:
                url = urls[i]
                driver.get(url)
                time.sleep(global_delay)
                try:
                    # Perform actions on the profile here
                    followed_button = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div"
                    follow_element = driver.find_element("xpath", followed_button)
                    assert follow_element.text == "Follow"
                    follow_element.click()
                    log(f"Followed profile: {url}")
                    time.sleep(2)
                except:
                    log(f"Followed profile: {url}")
            except:
                log(f"Failed to visit profile: {url}")
                time.sleep(global_delay)
                continue

    try:
        WebDriverWait(driver, 90).until(EC.url_to_be("https://twitter.com/home"))
        log("Logged in!")
        visit_profiles()
    except:
        log(f"Failed. Try again")


def follow_tweet():  # follow and tweet at the person
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    log("Program started")
    log("Twitter opened")

    def visit_profiles():
        iloc_start = int(iloc_start_entry.get())
        iloc_end = int(iloc_end_entry.get())
        file = "input.xlsx"
        df = pd.read_excel(file)
        urls = df.iloc[iloc_start - 1 : iloc_end, 0].values.tolist()
        ceo_tweets = df.iloc[iloc_start - 1 : iloc_end, 1].values.tolist()
        n = len(urls)
        log(f"Visiting {len(urls)} profiles.")

        for i in range(n):
            try:
                url = urls[i]
                tweet = ceo_tweets[i]
                driver.get(url)
                time.sleep(global_delay)
                try:
                    # Perform actions on the profile here
                    followed_button = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div"
                    follow_element = driver.find_element("xpath", followed_button)
                    assert follow_element.text == "Follow"
                    follow_element.click()
                    log(f"Followed profile: {url}")
                    time.sleep(2)
                except:
                    log(f"Followed profile: {url}")

                driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div",
                ).click()
                time.sleep(2)
                driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span[2]/span",
                ).send_keys(tweet)
                time.sleep(2)
                driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]",
                ).click()
                log(f"Tweeted at profile: {url} : {tweet}")
                time.sleep(global_delay)
            except:
                log(f"Failed to visit profile: {url}")
                time.sleep(global_delay)
                continue

    try:
        WebDriverWait(driver, 90).until(EC.url_to_be("https://twitter.com/home"))
        log("Logged in!")
        visit_profiles()
    except:
        log(f"Failed. Try again")


def personal_tweet():  # personal tweet only
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    log("Program started")
    log("Twitter opened")

    def tweet():
        iloc_start = int(iloc_start_entry.get())
        iloc_end = int(iloc_end_entry.get())
        file = "input.xlsx"
        df = pd.read_excel(file)
        tweets = df.iloc[iloc_start - 1 : iloc_end, 2].values.tolist()
        n = len(tweets)
        log(f"Tweeting")

        for i in range(n):
            try:
                # url = urls[i]
                tweet = tweets[i]
                driver.get("https://twitter.com/compose/tweet")
                time.sleep(global_delay)
                # Perform actions on the profile here
                driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span",
                ).send_keys(tweet)

                time.sleep(2)
                driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]",
                ).click()
                log(f"Tweeted : {tweet}")
                time.sleep(global_delay)
            except Exception as e:
                print(str(e))
                log(f"Failed to tweet")
                continue

    try:
        WebDriverWait(driver, 90).until(EC.url_to_be("https://twitter.com/home"))
        log("Logged in!")
        tweet()
    except Exception as e:
        print(str(e))
        log(f"Failed. Try again")


# Create tkinter window
window = tk.Tk()
window.title("Twitter Follow and Tweet Bot")
window.geometry("400x350")

# iloc start entry
iloc_start_label = tk.Label(window, text="Starting Row:")
iloc_start_label.pack()
iloc_start_entry = tk.Entry(
    window,
    width=10,
    justify="center",
)
iloc_start_entry.pack()

# iloc end entry
iloc_end_label = tk.Label(window, text="Ending Row:")
iloc_end_label.pack()
iloc_end_entry = tk.Entry(window, width=10, justify="center")
iloc_end_entry.pack(pady=10)

# follow button
follow_button = tk.Button(
    window, text="Follow the Twitter user Only", command=follow_only
)
follow_button.pack(pady=10)

# follow and tweet button
follow_tweet_button = tk.Button(
    window, text="Follow and Tweet at the Twitter user", command=follow_tweet
)
follow_tweet_button.pack(pady=10)

# personal tweet button
tweet_button = tk.Button(window, text="Personal Tweets", command=personal_tweet)
tweet_button.pack(pady=10)

window.mainloop()
