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
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")
log("Program started")
log("Twitter opened")
try:
    WebDriverWait(driver, 90).until(EC.url_to_be("https://twitter.com/home"))
    log("Logged in!")
except:
    log(f"Failed. Try again")   

def run(command):  # follow the person only
    switch_dict = {
        'follow_only': follow_only,
        'follow_tweet': follow_tweet,
        'personal_tweet': personal_tweet,
    }

    switch_dict.get(command)(driver)

def follow_only(driver):
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


def follow_tweet(driver):
    iloc_start = int(iloc_start_entry.get())
    iloc_end = int(iloc_end_entry.get())
    file = "input.xlsx"
    df = pd.read_excel(file)
    urls = df.iloc[iloc_start - 1 : iloc_end, 0].values.tolist()
    ceo_tweets = df.iloc[iloc_start - 1 : iloc_end, 1].values.tolist()
    imgs = df.iloc[iloc_start - 1 : iloc_end, 2].values.tolist()
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
            
            # Add picture to twitter post
            try:
                xpat1 = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input"
                xpat2 = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input"
                xpat3 = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[4]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input"
                input = find_element_in_list(driver, [xpat1, xpat2, xpat3], 2)
                input.send_keys(fr'{imgs[i]}')
            except Exception as e:
                print(str(e))
                print('can not find image ' + fr'{imgs[i]}')
            time.sleep(3)

            # Add content to twitter post
            driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span[2]/span",
                ).send_keys(tweet)
            time.sleep(2)
            try:
                dropdown = driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[3]",
                )
                driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", dropdown)
            except:
                print('dropdown hidden')
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


def personal_tweet(driver):
    iloc_start = int(iloc_start_entry.get())
    iloc_end = int(iloc_end_entry.get())
    file = "input.xlsx"
    df = pd.read_excel(file)
    tweets = df.iloc[iloc_start - 1 : iloc_end, 3].values.tolist()
    images = df.iloc[iloc_start - 1 : iloc_end, 4].values.tolist()
    n = len(tweets)
    log(f"Tweeting")

    for i in range(n):
        try:
            # url = urls[i]
            tweet = tweets[i]
            driver.get("https://twitter.com/compose/tweet")
            time.sleep(global_delay)
            # Perform actions on the profile here
            
            try:
                xpat1 = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input"
                xpat2 = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input"
                xpat3 = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[4]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input"
                input = find_element_in_list(driver, [xpat1, xpat2, xpat3], 2)
                input.send_keys(fr'{images[i]}')
            except Exception as e:
                print(str(e))
                print('can not find image ' + fr'{images[i]}')
            time.sleep(3)
            
            driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span",
                ).send_keys(tweet)
            time.sleep(2)
            try:
                dropdown = driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div/div/div[1]/div[3]",
                )
                driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", dropdown)
            except:
                print('dropdown hidden')
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

def find_element_in_list(driver, xpath_list, wait=3):
    for xpath in xpath_list:
        try:
            element = WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element not found with XPath: {xpath}")
    print("No element found in the provided XPath list.")
    return None

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
    window, text="Follow the Twitter user Only", command=lambda: run('follow_only')
)
follow_button.pack(pady=10)

# follow and tweet button
follow_tweet_button = tk.Button(
    window, text="Follow and Tweet at the Twitter user", command=lambda: run('follow_tweet')
)
follow_tweet_button.pack(pady=10)

# personal tweet button
tweet_button = tk.Button(window, text="Personal Tweets", command=lambda: run('personal_tweet'))
tweet_button.pack(pady=10)

window.mainloop()
