from selenium import webdriver  
import time
import random
import multiprocessing,os


# chromedriver = "C:\Program Files\geckodriver.exe"
# os.environ["webdriver.Firefox.driver"] = chromedriver






#start_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))

os.system('restart.bat')

def open_web(rannum,url):
        #driver=webdriver.Firefox()
        driver=webdriver.Chrome()
        driver.delete_all_cookies()
        driver.get(url)
        # rannum=random.randint(start_interval,end_interval)
        time.sleep(rannum)

        driver.quit()


if __name__ == '__main__':
        with open('Log.txt','r+') as f:
                lines=f.readlines()
        for line in lines:
                (url,total_plays,process,ad_interval)=line.strip().split(',')
                total_plays=int(total_plays)
                process=int(process)
                ad_interval=int(ad_interval)
                # print (url,total_play,process)

                # total_plays=3

                #start_interval=ad_interval-random.randint(10,15)
                start_interval=ad_interval+20
                end_interval=ad_interval+random.randint(20,25)
                #ad_interval=70

                real_plays=0

                #dur_interval=random.randint(ad_interval+5,ad_interval+10)
                current_play=0
                end=False
                while True:
                        #print (current_play)

                        for i in range(process):
                                rannum=random.randint(start_interval,end_interval)
                                #rannum=random.randint(start_interval,end_interval)
                                if (real_plays%80)==0:
                                        #dur_interval=random.randint(ad_interval-5,ad_interval)
                                        rannum=random.randint(int(ad_interval/2),ad_interval)
                                real_plays=real_plays+1
                                print ('real_plays:'+(str)(real_plays)+'')
                                if current_play>total_plays:
                                        end=True
                                        break
                                
                                if rannum>ad_interval:
                                        current_play=current_play+1
                                        print ('URL:'+(str)(url)+'')
                                        print ('current_play:'+(str)(current_play)+'')
                                #print ('dd')
                                mul=multiprocessing.Process(target=open_web,args=(rannum,url,))
                                mul.start()
                        mul.join()
                        if end==True:
                                break
                        time.sleep(0.3)
                        #if real_plays%20==0:
                        os.system('shutdown.bat')
                        os.system('restart.bat')

                
