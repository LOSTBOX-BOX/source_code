from selenium import webdriver
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
user_name_list=[]
stream_name_list=[]

cred = credentials.Certificate("./file/lol-cctv-firebase-database.com.json")//database 수정필요
db_url = 'https://database.com.firebaseio.com/'

firebase_admin.initialize_app(cred, {'databaseURL':'https://database.com.firebaseio.com/'})//database 수정필요
ref=db.reference('user/cctv/cctv_user/')
for item in ref.get().keys():
    user_name_list.append(item)

ref=db.reference('user/cctv/steram_user/')
for item in ref.get().keys():
    stream_name_list.append(item)

 

# with open('./file/cctv_user.txt','r',encoding='UTF8') as f:
#     line=f.readlines()
#     for item in line:
#         user_name_list.append(item.split('\n')[0])  
#         ref=db.reference('user/cctv/cctv_user/'+item.split('\n')[0])
#         ref.update({
#             'name':item.split('\n')[0]
#         })
    
# with open('./file/stream_name.txt','r',encoding='UTF8') as f:
#     line=f.readlines()
#     for item in line:
#         stream_name_list.append(item.split('\n')[0]) 
#         ref=db.reference('user/cctv/steram_user/'+item.split('\n')[0])
#         ref.update({
#             'name':item.split('\n')[0]
#         })

    
driver = webdriver.Chrome('./file/chromedriver', options=options)    
for user_name in user_name_list:
    print(user_name)
    
    stream_name='_'
    
    driver.get('https://www.op.gg/summoner/userName='+user_name)
    
    driver.implicitly_wait(1)
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/dl/dd[3]/a').click()
        driver.implicitly_wait(1)
        try:        
            check=driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[7]/div[2]/div/div[1]').text
            search = "커스텀"
            
            if search in check:
				print('커스텀')
                user_all=[]
                red=[]
                blue=[]

                for i in range(1,3):
                    for j in range(1,6):
                        name=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[5]/div[7]/div[2]/div/div[2]/table['+str(i)+']/tbody/tr['+str(j)+']').text.split('\n')[0]
                        for steram in stream_name_list:
                            if name.replace(" ","").lower()==steram.replace(" ","").lower():
                                stream_name=stream_name+name+"_"
                        if i==1:
                            blue.append(name)
                        elif i==2:
                            red.append(name)

                user_all.append(blue)
                user_all.append(red)
                now = time.localtime() 
                now_time=str(now.tm_year)+'-'+str(now.tm_mon)+'-'+str(now.tm_mday)+'_'+str(now.tm_hour)+'-'+str(now.tm_min)+'-'+str(now.tm_sec)
                file_name='./file/lol_cctv/'+now_time+'_'+user_name+stream_name+'.txt'
                ref=db.reference('user/cctv/alert/'+now_time+'_'+user_name+stream_name)
                ref.update({
                    'data':str(user_all)
                })
                
                
                with open(file_name,'w') as f:

                    for item in user_all:

                        f.write(str(item)+'\n')        
                pass
            else:
                pass



        except Exception as e:
            print('not game play')
            pass
            # print(e)
    except:
        print("닉네임변경")
        now = time.localtime() 
        now_time=str(now.tm_year)+'-'+str(now.tm_mon)+'-'+str(now.tm_mday)+'_'+str(now.tm_hour)+'-'+str(now.tm_min)+'-'+str(now.tm_sec)
        file_name='./file/lol_cctv/change_name/'+now_time+'_'+user_name+'_닉네임변경됨.txt'
        with open(file_name,'w') as f:
            f.write("now_time:"+now_time)

            
    
driver.quit()