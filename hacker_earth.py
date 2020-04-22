# from selenium import webdriver
# from bs4 import BeautifulSoup

# driver = webdriver.Chrome()
# driver.get("https://www.hackerearth.com/challenges/")
# response = driver.execute_script("return document.documentElement.outerHTML")
# soup = BeautifulSoup(response,"html.parser")
# main_div = soup.find("div",class_="upcoming challenge-list")
# span_tags = main_div.find_all("span",class_="challenge-list-title challenge-card-wrapper")
# div_tag = main_div.find_all("div",class_="inline-block company-image")
# company_name = main_div.find_all("div",class_="company-details ellipsis")
# challenges_links = main_div.find_all("a",class_="challenge-card-wrapper challenge-card-link")
# dict_he = {}
# for i in range(len(span_tags)):
# 	dict_he["challenge_name"]=span_tags[i].text
# 	dict_he["company-name"]=company_name[i].text.strip()
# 	dict_he["company-image"]=div_tag[i]["style"][21:]
# 	dict_he["challenges_link"]=challenges_links[i]["href"].strip()
# 	print(dict_he)


















