from selenium import webdriver
import pandas as pd

day = 3
day_to_xpath = {
    3: '//*[@id="post-20928"]/div/div/table[1]/tbody',
    4: '//*[@id="post-20948"]/div/div/div[1]/table[1]/tbody',
    5: '//*[@id="post-20986"]/div/div/table[1]/tbody',
    6: '//*[@id="post-21004"]/div/div/table[1]/tbody',
    8: '//*[@id="post-21053"]/div/div/table[1]/tbody',
    9: '//*[@id="post-21056"]/div/div/table[1]/tbody',
    10: '//*[@id="post-21076"]/div/div/table[1]/tbody',
    11: '//*[@id="post-21085"]/div/div/table[1]/tbody',
    12: '//*[@id="post-21095"]/div/div/table[1]/tbody',
    13: '//*[@id="post-21106"]/div/div/table[1]/tbody',
    14: '//*[@id="post-21113"]/div/div/table[1]/tbody',
    15: '//*[@id="post-21150"]/div/div/table[1]/tbody',
    16: '//*[@id="post-21169"]/div/div/table[1]/tbody',
    18: '//*[@id="post-21193"]/div/div/table[1]/tbody',
    19: '//*[@id="post-21198"]/div/div/table[1]/tbody',
    20: '//*[@id="post-21205"]/div/div/table[1]/tbody',
    21: '//*[@id="post-21210"]/div/div/table[1]/tbody',
    22: '//*[@id="post-21244"]/div/div/table[1]/tbody',
    23: '//*[@id="post-21260"]/div/div/table[1]/tbody',
    24: '//*[@id="post-21267"]/div/div/table[1]/tbody'
}

browser = webdriver.Chrome()
URL = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-" + str(day) + \
      "-aprilie-2020-ora-13-00/"
browser.get(URL)

main_header = ["Nr. crt.", "Judet", "Numar de cazuri confirmate " + str(day) + " Aprilie"]

info = browser.find_element_by_xpath(day_to_xpath[day]).text.split('\n')
info.remove(info[0])

for i in range(len(info)):
    info[i] = info[i].split(" ")
info[41][1] = "Mun. Bucuresti"
info[31][1] = "Satu Mare"
info[41].remove(info[41][2])
info[31].remove(info[31][2])
info[42] = ['', 'TOTAL', info[42][40]]

day += 1
browser.close()

while day < 25:
    if day == 7 or day == 17:
        day += 1

    browser = webdriver.Chrome()
    URL = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-" + str(day) + \
          "-aprilie-2020-ora-13-00/"

    browser.get(URL)
    main_header.append("Numar de cazuri confirmate " + str(day) + " Aprilie")

    data = browser.find_element_by_xpath(day_to_xpath[day]).text.split('\n')
    data.remove(data[0])

    if day == 4 or day == 23 or day == 24:
        data.remove(data[42])

    for i in range(len(data)):
        data[i] = data[i].split(" ")

    data[41][1] = "Mun. Bucuresti"
    data[31][1] = "Satu Mare"
    data[41].remove(data[41][2])
    data[31].remove(data[31][2])
    data[42] = ['', 'TOTAL', data[42][40]]

    cases = []
    for i in range(len(data)):
        cases.append(data[i][2])

    for i in range(len(info)):
        info[i].append(cases[i])

    day += 1
    browser.close()

df = pd.DataFrame(info, columns=main_header)
df.to_excel('Tema.xls', index=0)
