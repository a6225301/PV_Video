from selenium import webdriver  
import time
import random
import multiprocessing,os
import os,string
import re,signal
#coding=utf-8

# chromedriver = "C:\Program Files\geckodriver.exe"
# os.environ["webdriver.Firefox.driver"] = chromedriver






#start_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))

# os.system('restart.bat')

def open_web(rannum,url):
        #driver=webdriver.Firefox()
        driver=webdriver.Chrome()
        driver.delete_all_cookies()
        driver.get(url)
        # rannum=random.randint(start_interval,end_interval)
        time.sleep(rannum)

        driver.quit()






 
# re rule,to search process PID
rule = re.compile('\s\d+\s')
 
#www.iplaypy.com
 
# Get the Message of the all running process and PID  
 
# Process list to be killed
KillProclist = ['chrome.exe']
 
#Store the process name : PID
table={}

 
def SearchPID(temp):  # To search process PID by Name
    '''Find Proccess Name,Return PID'''
    print 'Proc Name     status     PID'
    ProcMessage = os.popen('tasklist').readlines()
    pids=[]
    for eachline in ProcMessage: # Get a list of running process message to match
        for sub in temp:
            if eachline.find(sub)==0: # if 0 ,Find the process to be killed
                ret = re.search(rule,eachline) # Get the PID
                if ret is not None:
                    print sub,'  running  ',ret.group(0)
                    pids.append(ret.group(0))
                    table.update({sub:ret.group(0)}) # Add {process name:PID} to the Table list
   # print table
    print (pids)
    if table == {}:
        print 'No useless process is running!'
    return pids
 
def KillPID(pids):
    for pid in pids:
        cmd='TaskKill /T /F /PID %s' % (int(pid)) 
        # os.popen(cmd)       # carry out the cmd
        os.kill(int((pid)),signal.SIGTERM)
        print  'Kill process [',pid,'] Successful!' 

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

                start_interval=ad_interval-random.randint(10,15)
                end_interval=ad_interval+random.randint(0,10)
                #ad_interval=70

                real_plays=0
                if (real_plays%5)==0:
                        dur_interval=random.randint(ad_interval-5,ad_interval)
                dur_interval=random.randint(ad_interval+5,ad_interval+10)
                current_play=0
                end=False
                while True:
                        #print (current_play)

                        for i in range(process):
                                real_plays=real_plays+1
                                print ('real_plays:'+(str)(real_plays)+'')
                                if current_play>total_plays:
                                        end=True
                                        break
                                rannum=random.randint(start_interval,end_interval)
                                if rannum>ad_interval:
                                        current_play=current_play+1
                                        print ('URL:'+(str)(url)+'')
                                        print ('current_play:'+(str)(current_play)+'')
                                #print ('dd')
                                mul=multiprocessing.Process(target=open_web,args=(rannum,url,))
                                mul.start()
                        mul.join()
                        SearchRet=SearchPID(KillProclist)
                        KillPID(SearchRet)
                        
                        if end==True:
                                break
                        time.sleep(0.3)
                        # if real_plays%20==0:
                        #         os.system('shutdown.bat')
                        #         time.sleep(7)
                        #         os.system('restart.bat')

                
