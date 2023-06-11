import os
import json
profile = { 
    'first_name': 'David', 
    'last_name': 'Ebert', 
    'professional': 'Full-Stack Development | Blockchain Development | Amazon Web Services', 
    'overview': 
"""A web3 developer with a passion in building experience in web3, metaverse and NFT.
Have strength in integrating web3 & backend and providing higher performance using indexing protocols and third-party APIs like Moralis API, the Graph,  QuckNode and Geyser.
A dedicated full stack developer with 7+ years of total experience in AWS/backend/frontend development, architectural design, and database administration.
Good sense in the responsive and the better UX.
Strong creative and analytical skills.""", 
    'country': 'Canada', 
    'hourRate': '50', 
    'workXP': [
        ('Full Stack Blockchain Developer', 'Improbable Company', 'London', 'United Kingdom', '2021.3', '2023.5',
"""Full Stack Blockchain Developer
Improbable Company
Improbable is a technology company that provides a metaverse platform designed to offer virtual gaming experiences.
Worked on NFT minting/staking platforms on Ethereum, Solana, and Polygon networks.
Build NFT marketplaces on both Ethereum and Solana networks.
Improved performance by integrating the Moralis API, Graph protocol, and QuickNode APIs.
With the fast development of landing/minting pages and NFT contracts and deployment and hosting of the platforms onto the cloud, could bring the platforms into the booming NFT market in a short time and bring the good sales to distributors.
Used python, FastAPI and SQLAlchemy also to build the backend APIs.
Implemented staking/breeding/airdrop with ERC20 tokens and SPL tokens as rewards."""), 
        ('Blockchain Developer', 'Figment Company', 'Toronto', 'Canada', '2019.1', '2021.2',
"""Blockchain Developer
Figment Company
Figment supports the adoption, growth and long term success of the Web3 ecosystem.
Developed token and DEX platform on Ethereum network.
Extended the DEX platform onto Polygon.
Developed a bridge to cross-operate the token on multiple networks.
Integrated contract using web3.js.
Developed wrapped token and DEX platform using project-serum on Solana network."""),
        ('Full Stack Developer', 'UniClinic Company', 'London', 'United Kingdom', '2017.2', '2019.11',
"""Full Stack Developer
UniClinic Company
UniClinic is a medical clinic that offers physiotherapy, gynecology, heart problem treatment, health diagnostics, and digestive treatment.
Developed an integrated social network platform.
Built integrated dashboard for the different social networks.
Enabled switching of multiple social accounts.
Boosted the sales by 20% by developing a scheduled post feature that posts content onto different social platforms regularly.
Upgraded the legacy website into the modern web app using MERN stack.
Integrated third-party APIs including Facebook, Twitter, Linkedin, and Instagram.""")
    ], 
    'education': [
        ('University of Toronto', 'Bachelor of Computer Science (BCompSc)', 'Computer science', '2013', '2017')
    ], 
    'languages': [
        ('Cantonese', '4')
    ], 
    'skills': [
        'MERN Stack', 
        'Full-Stack Development', 
        'LAMP Stack', 
        'MEAN Stack',
        'Ecommerce Website', 
        'Back-End Development',
        'Django Stack', 
        'Amazon Web Services', 
        'Rust', 
        'Python',
        'Web3',
        'Blockchain Development',
        'Smart Contract', 
        'Web Development', 
        'Cryptocurrency'
    ], 
    'services': [
        'Database Management & Administration',
        'Desktop Application Development',
        'DevOps & Solution Architecture',
        'Web Development',
        'Web & Mobile Design',
        'Network & System Administration',
        'Blockchain, NFT & Cryptocurrency',
        'Ecommerce Development',
    ], 
    'street': '131 Bremner Blvd', 
    'zipcode': 'M5J 3A7', 
    'city': 'Toronto', 
    'state':'Ontario',
    'location': 'Canada', 
    'phone': '6473525252'
}

############################################################
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from time import sleep
from datetime import datetime
import sys
from selenium.webdriver.chrome.options import Options
############################################################

with open(sys.argv[1], 'r') as f:
    profile = json.load(f)

global expFlag, photoDir
expFlag = True
photoDir = 'C:\\Users\\Administrator\\Pictures\\'

curr_year = datetime.now().year

def debug():
    cmd = input('>>>')
    try:
        if cmd=='exit':
            print('<<<exited!')
        else:
            exec(cmd)
            print("------------------success")
            debug()
    except:
        print("__________________failed, error")
        debug()
        pass

############################################################
def waitInfinite(callback, debug = False):
    sleep(0.5)
    yet = True
    while yet:
        try:
            callback()
            yet = False
        except NoSuchElementException as e:
            print("{} on line {}".format(str(e).split('\n')[0], sys.exc_info()[-1].tb_lineno))
            sleep(0.5)
            pass
        except JavascriptException as e:
            print("{} on line {}".format(str(e).split('\n')[0], sys.exc_info()[-1].tb_lineno))
            sleep(0.5)
            pass
        except StaleElementReferenceException as e:
            print("{} on line {}".format(str(e).split('\n')[0], sys.exc_info()[-1].tb_lineno))
            sleep(0.5)
            pass
        except ElementClickInterceptedException as e:
            print("{} on line {}".format(str(e).split('\n')[0], sys.exc_info()[-1].tb_lineno))
            sleep(0.5)
            pass
        except ElementNotInteractableException as e:
            print("{} on line {}".format(str(e).split('\n')[0], sys.exc_info()[-1].tb_lineno))
            sleep(0.5)
            pass
        except Exception as e:
            print("{} on line {}".format(str(e).split('\n')[0], sys.exc_info()[-1].tb_lineno))
            driver.quit()
            exit()

def waitUntil(callback, driver, selector):
    sleep(0.5)
    yet = True
    while yet:
        try:
            callback(driver.execute_script("x=document.querySelectorAll('{}').length;return document.querySelectorAll('{}')[x-1]".format(selector, selector)))
            yet = False
        except Exception as e:
            print(str(e).split('\n')[0])
            sleep(0.1)
            pass

################################################################
def clickByMouse(element):
    ActionChains(driver).click(element)\
                        .perform()

def selectDropDown(itemSelector, country):
    nations = driver.find_elements(By.CSS_SELECTOR, itemSelector)

    if str(type(country)) == "<class 'int'>":
        driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(country)}].click()')
    else:
        for i in range(len(nations)):
            try:
                if nations[i].text.find(country) >= 0:
                    driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(i)}].click()')
                    break
            except:
                pass

def selectDateDropDown(dropdownId, itemSelector, country):
    tmp = dropdownId.split('##')

    if len(tmp) == 2:
        dropdownId = tmp[0]
        driver.execute_script(f'document.querySelectorAll(\'div[aria-labelledby^="{dropdownId}"]\')[{tmp[1]}].click()')
    else:
        driver.execute_script(f'document.querySelector(\'div[aria-labelledby^="{dropdownId}"]\').click()')
    sleep(0.5)
    nations = driver.find_elements(By.CSS_SELECTOR, itemSelector)
    if str(type(country)) == "<class 'int'>":
        driver.execute_script(f'x=document.querySelectorAll("{itemSelector}")[{str(country)}];console.log(x);x.click()')
    else:
        for i in range(len(nations)):
            try:
                if nations[i].text.find(country) >= 0:
                    driver.execute_script(f'document.querySelectorAll("{itemSelector}")[{str(i)}].click()')
                    break
            except:
                pass

## Get Temp URL
chrome_options = Options()
chrome_options.add_argument("--headless")
emailGetter = webdriver.Chrome(options=chrome_options)
emailGetter.get("https://www.minuteinbox.com")
tempURL = emailGetter.find_element(By.ID, "email").text

## Sign up
#chrome_options = Options()
#chrome_options.add_argument("--proxy-server=socks5://localhost:8080")
driver = webdriver.Chrome()
driver.get("https://www.upwork.com/nx/signup/?dest=home")

# Apply as freelancer
driver.find_element(By.ID, "button-box-4").click()
driver.find_element(By.CSS_SELECTOR, "button[data-qa='btn-apply']").click()

# input information
driver.find_element(By.ID, "first-name-input").send_keys(profile['first_name'])
driver.find_element(By.ID, "last-name-input").send_keys(profile['last_name'])
driver.find_element(By.ID, "redesigned-input-email").send_keys(tempURL)
driver.find_element(By.ID, "password-input").send_keys("qwe123!@#")

#! validating email
wait = WebDriverWait(driver, 10)
action = webdriver.ActionChains(driver)
action = webdriver.common.action_chains.ActionChains(driver)

driver.execute_script(f'document.querySelector("#dropdown-label-7").click()')
waitInfinite(lambda: selectDropDown("li.up-menu-item", profile['country']))
driver.execute_script('document.querySelectorAll("span.up-checkbox-replacement-helper")[1].click()')
driver.execute_script('document.getElementById("button-submit-form").click()')

# Verify email
def verifyEmail():
    global emailGetter
    emailGetter.execute_script('x = document.querySelectorAll("td.from")[0];if(x.textContent.includes("Upwork Notifications")) x.click()')
    sleep(5)
    iframe = emailGetter.find_element(By.ID, "iframeMail")
    emailGetter.switch_to.frame(iframe)

waitInfinite(verifyEmail)
verifiedURL = emailGetter.find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')

try:
    emailGetter.quit()
except:
    try:
        emailGetter.close()
    except:
        pass
    

driver.get(verifiedURL)

# Are your Expert, GET_EXPERIENCE, ...
sleep(10)
waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary").click()'))


waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "input[value=\"FREELANCED_BEFORE\"]").click())
waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())


waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "input[value=\"GET_EXPERIENCE\"]").click())
waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())


waitInfinite(lambda: driver.execute_script("x=document.querySelectorAll('input[class=\"air3-btn-box-input\"]').length - 3;document.querySelectorAll('input[class=\"air3-btn-box-input\"]')[x].click()"))
waitInfinite(lambda: driver.execute_script("x = document.querySelector('span[data-test=\"checkbox-input\"]'); x.click()"))
# waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "span[data-test=\"checkbox-input\"]").click())
waitInfinite(lambda: driver.execute_script("document.querySelector('button[data-test=\"next-button\"]').click()"))
# waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())


# Fill out manually
waitInfinite(lambda: driver.execute_script('x=document.querySelectorAll("button.mb-3.air3-btn.air3-btn-secondary").length;document.querySelectorAll("button.mb-3.air3-btn.air3-btn-secondary")[x-1].click()'))

def addExperience(driver, title, comapny, city, country, start, end, description):

    print(title, comapny, city, country, start, end)
    global expFlag
    if expFlag:
        waitInfinite(lambda: driver.execute_script('document.querySelectorAll("button.air3-btn.air3-btn-circle")[0].click()'))
    else:
        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-secondary.air3-btn-circle").click()'))


    if expFlag: waitInfinite(lambda: driver.find_elements(By.CSS_SELECTOR, 'input[aria-labelledby="title-label"]')[1].send_keys(""))
    waitInfinite(lambda: driver.find_elements(By.CSS_SELECTOR, 'input[aria-labelledby="title-label"]')[1].send_keys(title))
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="company-label"]').send_keys(comapny))
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="location-label"]').send_keys(city))
    waitInfinite(lambda: selectDateDropDown("location-label", "span.air3-menu-item-text", country))

    sleep(0.5)

    start_year = eval(start.split('.')[0])
    start_month = eval(start.split('.')[1])
    waitInfinite(lambda: selectDateDropDown("start-date-month", "span.air3-menu-item-text", start_month - 1))
    waitInfinite(lambda: selectDateDropDown("start-date-year", "span.air3-menu-item-text", curr_year - start_year))

    waitInfinite(lambda: driver.find_element(By.TAG_NAME,'textarea').send_keys(description))
    # sleep(3)

    if end == 'current':
        driver.execute_script('document.querySelector(\'span[data-test="checkbox-input"]\').click()')
    else:
        end_year = eval(end.split('.')[0])
        end_month = eval(end.split('.')[1])
        waitInfinite(lambda: selectDateDropDown("end-date-month", "span.air3-menu-item-text", end_month - 1))
        waitInfinite(lambda: selectDateDropDown("end-date-year", "span.air3-menu-item-text", curr_year - end_year))

    # debug()
        
    driver.execute_script('document.querySelector(\'button[data-test="save-btn"]\').click()')

    expFlag = False
    
    
def addEducation(driver, school, degree, field, start, end):
    start = eval(start)
    end = eval(end)

    print(school, degree, field, start, end)

    global expFlag
    if expFlag:
        waitInfinite(lambda: driver.execute_script('document.querySelectorAll("button.air3-btn.air3-btn-circle")[7].click()'))
    else:
        waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-secondary.air3-btn-circle").click()'))


    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="school-label"]').click())
    sleep(0.5)
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="school-label"]').send_keys(school))
    sleep(1)
    driver.find_element(By.CLASS_NAME, "air3-menu-item-text").click()

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="degree-label"]').click())
    sleep(0.5)
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="degree-label"]').send_keys("Bachelor of Computer Science (BCompSc)"))
    sleep(1)

    action.move_to_element_with_offset(driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="degree-label"]'),50,70)
    action.click()
    action.perform()
    # debug()
    # driver.find_element(By.CLASS_NAME, "is-focused").click()
    # driver.find_element(By.CLASS_NAME, "air3-menu-item-text").click()

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="area-of-study-label"]').click())
    sleep(0.5)
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="area-of-study-label"]').send_keys(field))
    sleep(1)
    action.move_to_element_with_offset(driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="area-of-study-label"]'),50,70)
    action.click()
    action.perform()
    
    waitInfinite(lambda: selectDateDropDown("dates-attended-label##0", "span.air3-menu-item-text", curr_year - start + 1+8))
    waitInfinite(lambda: selectDateDropDown("dates-attended-label##1", "span.air3-menu-item-text", 2030 - end + 1+8))
    sleep(3)
    driver.execute_script('document.querySelector(\'button[data-test="save-btn"]\').click()')

    expFlag = False

def addLanguage(driver, language, pro, count):
    pro = eval(pro)
    print(language, pro, count)

    waitInfinite(lambda: selectDateDropDown(f"dropdown-label-english", "span.air3-menu-item-text", pro-1))

    # driver.execute_script('document.querySelector("button.air3-btn.air3-btn-secondary.air3-btn-sm").click()')
    
    # waitInfinite(lambda: selectDateDropDown(f"dropdown-label-language-{count}", "span.air3-menu-item-text", language))
    # waitInfinite(lambda: selectDateDropDown(f"dropdown-label-proficiency-{count}", "span.air3-menu-item-text", pro-2))

    return count + 1

def addSkill(driver, inp, skill, field = "skills-input"):
    # sleep(3)
    waitUntil(lambda x: x.click(), driver, f'input[aria-labelledby="{field}"]')
    # sleep(1)
    waitUntil(lambda x: x.send_keys(skill), driver, f'input[aria-labelledby="{field}"]')
    # sleep(5)
    
    flag = True
    while flag:
        nations = driver.find_elements(By.CSS_SELECTOR, "span.air3-menu-item-text")
        flag = len(nations) == 0
        sleep(0.5)

    for i in range(len(nations)):
        try:
            if nations[i].text.find(skill) >= 0:
                # sleep(3)
                waitInfinite(lambda:driver.execute_script(f'document.querySelectorAll("span.air3-menu-item-text")[{str(i)}].click()'))
                sleep(1.5)
                break
        except:
            pass
        
    # sleep(1)
    waitUntil(lambda x: x.clear(), driver, f'input[aria-labelledby="{field}"]')

def addService(driver, services):
    waitUntil(lambda x: x.click(), driver, 'div[data-test="dropdown-toggle"]')
    sleep(1)

    for service in services:
        driver.execute_script(f'''
            // document.querySelectorAll(\'div[data-test="dropdown-toggle"]\')[1].click()
            var services = document.querySelectorAll('span.air3-menu-checkbox-labels');
            var toselect;
            for (let i = 0; i < services.length; i++) {{
                console.log(services[i], '{service}');
                if (services[i].textContent.indexOf('{service}') >= 0) {{
                    toselect = services[i].parentNode.parentNode;
                    break;
                }}
            }}
            if (toselect) {{
                if (toselect.getAttribute("aria-selected") == 'false') {{
                    toselect.parentNode.parentNode.parentNode.click();
                    setTimeout(() => toselect.click(), 300);
                }}
            }}
        ''')
        sleep(0.1)

def configLast(driver, country, street, city,zipcode, phone,  state):
    selectDateDropDown("country-label", "span.air3-menu-item-text", country)
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="street-label"]').send_keys(street))
    
    addSkill(driver, driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="city-label"]'), city, "city-label")

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="postal-code-label"]').send_keys(zipcode))
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby^="dropdown-label-phone-number"]').send_keys(phone))
    # waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby^="state-label"]').send_keys(state))
    sleep(1)
    waitInfinite(lambda: driver.execute_script("document.querySelector('button[data-cy=\"open-loader\"]').click()"))
    sleep(1)

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(os.path.abspath(sys.argv[1][:-5]+'.jpg')))
    waitInfinite(lambda: driver.execute_script("document.querySelectorAll('button.air3-btn.air3-btn-primary')[5].click()"))


if False:
    dz = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    dz.send_keys(profile)
else:
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "input[data-test=\"title\"]").send_keys(profile['professional']))
    
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())
    
    # driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()')
    
    for i in profile['workXP']:
        addExperience(driver, *i)

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())

    expFlag = True
    sleep(1)
    for i in profile['education']:
        addEducation(driver, *i)
    # debug()
    

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())

    sleep(6)
    # sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, "button[data-test=\"skip-button\"]").click()
    except:
        pass
    
   
    expFlag = True
    sleep(1)
    waitInfinite(lambda: selectDateDropDown("dropdown-label-english", "span.air3-menu-item-text", 2))
    

    count = 0
    for i in profile['languages']:
        count = addLanguage(driver, *i, count)

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())

    sleep(1)
    inp_skills = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="skills-input"]')
    
    for i in profile['skills']:
        addSkill(driver, inp_skills, i)

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())

    sleep(1)
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'textarea[aria-labelledby="overview-label"]').send_keys(profile['overview']))
    sleep(0.5)
    clickByMouse(driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]"))
    # waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.air3-btn-primary.mb-0").click()'))

    sleep(3)
    addService(driver, profile['services'])
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())

    sleep(1)
    
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[data-test="currency-input"]').clear())
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, 'input[data-test="currency-input"]').send_keys(str(profile['hourRate'])))
        
    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())
    
    sleep(1)
    configLast(
        driver,
        profile['location'],
        profile['street'],
        profile['city'],
        profile['zipcode'],
        profile['phone'],
        profile['state']
    )

    waitInfinite(lambda: driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]").click())
    waitInfinite(lambda: driver.execute_script('document.querySelector("button.air3-btn.width-md.m-0.air3-btn-primary").click()'))

    try:
        open('email.txt', 'a', encoding='utf-8').write(f'{tempURL}\n')
    except FileNotFoundError:
        open('email.txt', 'w', encoding='utf-8').write(f'{tempURL}\n')
    driver.close()
