import selenium, time, csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep


driver = webdriver.Chrome()
driver.get("https://x.com/login")

subject = "Elon Musk"


sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("carav2412")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('vajha2002')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()


sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

sleep(3)
profile = driver.find_element(By.XPATH,"//span[contains(text(), 'Elon Musk')]")
profile.click()


wait = WebDriverWait(driver, 10)


all_tweets = []
all_usernames = []
all_likes= []

def scroll_and_collect():
    
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  

    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="tweetText"]'))
    )
    
    
    tweets = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')
    usernames = driver.find_elements(By.CSS_SELECTOR, 'div[class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-1udh08x r-3s2u2q"]')
    likes = driver.find_elements(By.CSS_SELECTOR, 'div[class="css-175oi2r r-xoduu5 r-1udh08x"]')
    
    for tweet in tweets:
        all_tweets.append(tweet.text)
    for username in usernames:
        all_usernames.append(username.text)
    for like in likes:
        all_likes.append(like.text)
    


scroll_count = 0
max_scrolls = 400
while scroll_count < max_scrolls:
    scroll_and_collect()
    scroll_count += 1


'''for tweet in all_tweets:
    print("------------------------------------")
    print(tweet)

for like in all_likes:
    print("^_^_^_^_^_^_^_^_^_")
    print(like)'''

with open('tweets_and_usernames.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Tweet', 'Likes']) 

    min_length = min(len(all_tweets), len(all_usernames), len(all_likes))
    for i in range(min_length):
        writer.writerow([all_usernames[i], all_tweets[i], all_likes[i]])
print("Data has been written to tweets_and_usernames.csv")


while(True):
    pass