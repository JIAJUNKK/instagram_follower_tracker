from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Check_follower:
    def __init__(self, name, password):
        self.name = name
        self.password = password

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")

        self.followingUrl = "https://www.instagram.com/"+name+"/following/"
        self.followerUrl = "https://www.instagram.com/"+name+"/followers/"
        
        self.followingList = []
        self.followerList = []

    def login(self):
        time.sleep(5)
        accept_cookie = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
        accept_cookie.click()

        time.sleep(5)
        user_name = self.driver.find_element(By.NAME, "username")

        for char in self.name:
            user_name.send_keys(char)
            time.sleep(0.05)

        user_password = self.driver.find_element(By.NAME, "password")
        for char in self.password:
            user_password.send_keys(char)
            time.sleep(0.05)

        time.sleep(5)
        logbutton = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        logbutton.click()
        time.sleep(5)

    def check_following(self):
        self.driver.execute_script("window.open('about:blank','secondTab');")
        self.driver.switch_to.window("secondTab")
        self.driver.get(self.followingUrl)
        scroll_box = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

        followerNames = scroll_box.find_elements(By.TAG_NAME, "a")
        self.followerList = [name.text for name in followerNames if name != '']
        time.sleep(10)


    def check_follower(self):
        self.driver.execute_script("window.open('about:blank','thirdTab');")
        self.driver.switch_to.window("thirdTab")
        self.driver.get(self.followerUrl)
        time.sleep(100)
        scroll_box = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

        followerNames = scroll_box.find_elements(By.TAG_NAME, "a")
        self.followerList = [name.text for name in followerNames if name != '']
        time.sleep(10)

    def check_unfollowing(self):
        count = 0
        for names in self.followingList:
            if names not in self.followerList:
                count += 1
                print(f"{count}. {names}")


class File:
    def __init__(self):
        try:
            self.file = open("followerList.txt", "x")
        except FileExistsError:
            pass
        try:
            self.file = open("followingList.txt", "x")
        except FileExistsError:
            pass

    def writeFollowers(self, followerList):
        self.file = open("followerList.txt", "w")
        for names in followerList:
            if names != '':
                self.file.write(names + '\n')
        self.file.close()

    def writeFollowings(self, followingList):
        self.file = open("followingList.txt", "w")
        for names in followingList:
            if names != '':
                self.file.write(names + '\n')
        self.file.close()


InstagramBot = Check_follower("jiajunkk", "kongjiajun123")
writeToFile = File()


InstagramBot.login()
InstagramBot.check_following()
InstagramBot.check_follower()
InstagramBot.check_unfollowing()

writeToFile.writeFollowers(InstagramBot.followerList)
writeToFile.writeFollowings(InstagramBot.followingList)
