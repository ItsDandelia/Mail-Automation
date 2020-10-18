"""
Author:Raj Rajan Talashilkar
Date:17th October 2020
About: This code is made to automate the sign-in process followed by the key pressings
       that are necessary like 'compose','Clicking-on-buttons' to focus on them and 'Send' it also accesses the subject and 'To: emails' section.
       All we need to provide is receiver's mails, subject and content along with date and time.
       The scheduling part is also automated with the time and date that we provide.
       delivering at time is done by GMail itself.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException as ENIE
from selenium.common.exceptions import TimeoutException as TE
import Passwords

maximize = webdriver.ChromeOptions()
maximize.add_argument('start-maximized')

PATH = 'C:\Chromedriver&stockfish\chromedriver.exe'
driver = webdriver.Chrome(PATH, options=maximize)
WEBSITE = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
driver.get(WEBSITE)

"""
Function Name:username
Function call:username()
Use: username function access you email address and waits for 2 seconds
     to click on the next button
"""
def username():
    username = driver.find_element_by_xpath('//*[@id="identifierId"]')
    username.send_keys('2018.raj.talashilkar@ves.ac.in')
    time.sleep(2)
    next1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    next1.click()
    return 0

"""
Function Name:password
Function call:password()
Use: password function access you password and waits for 2 seconds
     to click on the next button.
     Note:Password must be hidden so you can use any encryption method or just create another python file
     containing your password and import it here as I have done it here
"""
def password():
    time.sleep(2)
    password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys(Passwords.email())
    time.sleep(2)
    next2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
    next2.click()
    return 0

"""
Function Name:compose
Function call:compose()
Use: compose function checks if the element is clickable using the Xpath 
     and clicks it as soon as it is.
"""
def compose():
    Xpath = '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div'
    compose = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, Xpath))
    )
    compose.click()
    return 0

"""
Function Name:To_emails
Function call:To_emails()
Use: To_emails functions accesses a list of all the receiver's mails    
     as in this case I have passed only one string.
"""
def To_emails():
    try:
        time.sleep(1)
        To1 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID,':o8'))
        )
        a = '2018.raj.talashilkar@ves.ac.in'
        To1.send_keys(a)
        return 0

    except ENIE:
        time.sleep(1)
        To1 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID,':o9'))
        )
        a = '2018.raj.talashilkar@ves.ac.in'
        print("o9 with ENIE")
        To1.send_keys(a)
        return 0

    except TE:
        time.sleep(1)
        To1 = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID,':o9'))
        )
        a = '2018.raj.talashilkar@ves.ac.in'
        To1.send_keys(a)
        print("o9 with TE")
        return 0

"""
Function Name:subject
Function call:subject()
Use: As the name suggests, it takes the input as the subject or you can just pass a string of the subject
     without prompting it in the console.
"""
def subject():
    try:
        time.sleep(1)
        Subject = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.ID, ':nr'))
        )
        Subject.send_keys("Greetings")
        return 0

    except ENIE:
        time.sleep(1)
        Subject = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.ID, ':nq'))
        )
        print("nq with ENIE")
        Subject.send_keys('Greetings')
        return 0

    except TE:
        time.sleep(1)
        Subject = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.ID, ':nq'))
        )
        print("nq with TE")
        Subject.send_keys('Greetings')
        return 0

"""
Function Name:content
Function call:content()
Use: Content method reads content.txt file which has the content that needs to be sent
     and writes the data in the content section of your mail.
"""
def content():
    try:
        time.sleep(1)
        Content = WebDriverWait(driver, 21).until(
            EC.presence_of_element_located((By.ID, ':ov'))
        )
        Content.send_keys(open("content.txt","r").read())

    except ENIE:
        time.sleep(1)
        Content = WebDriverWait(driver, 21).until(
            EC.presence_of_element_located((By.ID, ':ou'))
        )
        print("ou with ENIE")
        Content.send_keys(open("content.txt","r").read())

    except TE:
        time.sleep(1)
        Content = WebDriverWait(driver, 21).until(
            EC.presence_of_element_located((By.ID, ':ou'))
        )
        print("ou with TE")
        Content.send_keys(open("content.txt","r").read())

"""
Function Name:arrowkey
Function call:arrowkey()
Use: arrowkey is a small button which when pressed,opens the schedule time button
"""
def arrowkey():
    try:
        time.sleep(1)
        ArrowKey = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.ID,':nd'))
        )
        ArrowKey.click()
        return 0

    except ENIE:
        time.sleep(1)
        ArrowKey = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.ID,':nc'))
        )
        print("nc with ENIE")
        ArrowKey.click()
        return 0

    except TE:
        time.sleep(1)
        ArrowKey = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.ID,':nc'))
        )
        print("nc with TE")
        ArrowKey.click()
        return 0

"""
Function Name:schedule_time
Function call:schedule_time()
Use: schedule_time is a button on the Email webpage which opens after arrowkey is pressed,
     and after pressing it it opens another dialog box to set time and date
"""
def schedule_time():
    try:
        time.sleep(1)
        scheduled_time = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, ':q6'))
        )
        scheduled_time.click()

    except ENIE:
        time.sleep(1)
        scheduled_time = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, ':q5'))
        )
        print("q5 with ENIE")
        scheduled_time.click()

    except TE:
        time.sleep(1)
        scheduled_time = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, ':q5'))
        )
        print("q5 with TE")
        scheduled_time.click()

    time.sleep(2)
    Time0 = WebDriverWait(driver, 11).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.Kj-JD.Ac > div.Kj-JD-Jz > div.ZkmAeb > div.Az.AM'))
    )
    Time0.click()

    time.sleep(2)
    date1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div.Kj-JD.hr > div.Kj-JD-Jz > div.hF > div > div.kz.ki > input')))

    time.sleep(2)
    date1.send_keys(Passwords.backspaces())
    date1.send_keys('Oct 18, 2020')

    time.sleep(2)
    time1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div.Kj-JD.hr > div.Kj-JD-Jz > div.hF > div > div.kz.hv > input')))
    time1.send_keys(Passwords.backspaces())
    time1.send_keys('04:00 PM')

"""
Function Name:send
Function call:send()
Use: Send function provokes the send button and the process is done after sending the mail.
"""
def send():
    time.sleep(2)
    schedule_send = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.Kj-JD.hr > div.Kj-JD-Jl > button.J-at1-auR')))
    schedule_send.click()


username()
password()
compose()
To_emails()
subject()
content()
arrowkey()
schedule_time()
send()

