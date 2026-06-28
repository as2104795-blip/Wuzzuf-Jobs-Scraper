from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd 
import time


# activate headless مع إضافة هُوية متصفح حقيقي عشان الموقع ما يشكش
Opt = Options()
Opt.add_argument("--headless")
Opt.add_argument("--window-size=1920,1080")
Opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# activate selenium
driver = webdriver.Chrome(options=Opt)

full_data = []
max_pages = int(input("Enter the number of pages to Extract: "))
current_page = 1

while current_page <= max_pages:
    # 🔥 السحر هنا: بنعدل الرابط مباشرة برقم الصفحة بناءً على نظام وظف (الصفحة الأولى start=0، الثانية start=1...)
    page_start = int(current_page - 1)
    target_url = f"https://wuzzuf.net/search/jobs?q=python&start={page_start}"
    
    print(f"🔄 Going to: {target_url}")
    driver.get(target_url)
    time.sleep(6) # وقت كافي جداً لتحميل الصفحة كاملة

    # عمل سكرول لضمان تحميل العناصر الديناميكية
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    main_card = driver.find_elements(By.XPATH, '//div[@class="css-ghe2tq e1v1l3u10"]')

    for every_card in main_card:
        try:
            job_name = every_card.find_element(By.XPATH, './/h2[@class="css-193uk2c"]').text 
            company_name= every_card.find_element(By.XPATH, './/a[@class="css-ipsyv7"]').text
            work_type=every_card.find_element(By.XPATH, './/span[@class="css-uc9rga eoyjyou0"]').text
            posted = every_card.find_element(By.XPATH, './/div[@class="css-1jldrig"] | .//div[@class="css-eg55jf"]').text
            location = every_card.find_element(By.XPATH, './/span[@class="css-uofntu eoyjyou0"]').text
            link = every_card.find_element(By.CLASS_NAME, 'css-o171kl').get_attribute("href")
           
            
            full_data.append({
                "job_name": job_name,
                "company_name":company_name,
                "posted": posted,
                "work_type":work_type,
                "location": location,
                "link": link
                
            })
        except:
            continue
   
    print(f"✅ page__{current_page} has ended. Total jobs extracted so far: {len(full_data)}")
    current_page += 1

# use pandas to connect with csv
df = pd.DataFrame(full_data)
df.to_excel("Wuzzuf.xlsx", index=False, engine='xlsxwriter')
driver.quit()

print("All Pages were extracted Successfully ")



























































# company_name= every_card.find_element(By.XPATH, './/a[@class="css-ipsyv7"]').text



#             work_type=every_card.find_element(By.XPATH, './/span[@class="css-uc9rga eoyjyou0"]').text









# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import pandas as pd 
# import time

# # activate headless مع إضافة هُوية متصفح حقيقي عشان الموقع ما يشكش
# Opt = Options()
# Opt.add_argument("--headless")
# Opt.add_argument("--window-size=1920,1080")
# Opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# # activate selenium
# driver = webdriver.Chrome(options=Opt)

# full_data = []
# max_pages = int(input("Enter the number of pages to Extract: "))
# current_page = 1

# while current_page <= max_pages:
#     # 🔥 السحر هنا: بنعدل الرابط مباشرة برقم الصفحة بناءً على نظام وظف (الصفحة الأولى start=0، الثانية start=1...)
#     page_start = int(current_page - 1)
#     target_url = f"https://wuzzuf.net/search/jobs?q=python&start={page_start}"
    
#     print(f"🔄 Going to: {target_url}")
#     driver.get(target_url)
#     time.sleep(6) # وقت كافي جداً لتحميل الصفحة كاملة

#     # عمل سكرول لضمان تحميل العناصر الديناميكية
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

#     main_card = driver.find_elements(By.XPATH, '//div[@class="css-ghe2tq e1v1l3u10"]')

#     for every_card in main_card:
#         try:
#             job_name = every_card.find_element(By.XPATH, './/h2[@class="css-193uk2c"]').text 
#             company_name= every_card.find_element(By.XPATH, './/a[@class="css-ipsyv7"]').text
#             work_type=every_card.find_element(By.XPATH, './/span[@class="css-uc9rga eoyjyou0"]').text
#             posted = every_card.find_element(By.XPATH, './/div[@class="css-1jldrig"] | .//div[@class="css-eg55jf"]').text
#             requirements = every_card.find_element(By.XPATH, './/div//a[@class="css-o171kl"] | .//div//a[@class="css-5x9pm1"]').text
#             location = every_card.find_element(By.XPATH, './/span[@class="css-uofntu eoyjyou0"]').text
#             link = every_card.find_element(By.CLASS_NAME, 'css-o171kl').get_attribute("href")
            
#             full_data.append({
#                 "job_name": job_name,
#                 "company_name":company_name,
#                 "work_type":work_type,
#                 "requirements": requirements,
#                 "location": location,
#                 "link": link,
#                 "posted": posted
#             })
#         except:
#             continue
   
#     print(f"✅ page__{current_page} has ended. Total jobs extracted so far: {len(full_data)}")
#     current_page += 1

# # use pandas to connect with csv
# df = pd.DataFrame(full_data)
# df.to_csv("Wuzzuf.csv", index=False, encoding="utf-8-sig")
# driver.quit()

# print(f"🥳 كدا قفلنا اللعبة بجد! تم سحب {len(full_data)} وظيفة من الـ {max_pages} صفحات كاملين!")

