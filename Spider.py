
# coding: utf-8

# In[2]:


import urllib
from bs4 import BeautifulSoup
import re

# url='https://lcdh-amsterdam.com/index.php?route=product/product&product_id=521'

def spider_product_urls(main_url):
    product_urls=[]

    html=urllib.urlopen(main_url)
    bsObj=BeautifulSoup(html)
    obj_product_urls=bsObj.findAll({"a"},{"class":{"list-group-item"}})

    for i in range(len(obj_product_urls)):
        product_urls.append(obj_product_urls[i]["href"])

    # product_avaialbity=bsObj.findAll(text=re.compile("https://lcdh-amsterdam.com/index.php?route=product/category&path=59"))
#     print (product_urls)
#     print (len(product_urls))
    del product_urls[0]
    
    return product_urls

# product_urls=spider_product_urls(main_url)

# print (product_urls)


# In[3]:


# product_url='https://lcdh-amsterdam.com/index.php?route=product/category&path=59_144'




# url='https://lcdh-amsterdam.com/index.php?route=product/product&product_id=521'
# product_url='https://lcdh-amsterdam.com/index.php?route=product/category&path=59_64'

def spider_subproduct_urls(product_url):
    sub_product_urls=[]

    html=urllib.urlopen(product_url)
    bsObj=BeautifulSoup(html)
    if bsObj=='':
    	print ('fuck')

    try:
		page = int(bsObj.findAll({"div"},{"class":{"col-sm-6 text-right"}})[0].get_text()[-8:-7])
		#     print (page)

		for p in range(page):
		    time.sleep(0.3)    
		    product_page_url=product_url+'&page='+(str)(p+1)
		#         print (product_page_url)
		    html=urllib.urlopen(product_page_url)
		    bsObj=BeautifulSoup(html)
		    obj_subproduct_hs=bsObj.findAll({"h4"})
		    for obj_subproduct_h in obj_subproduct_hs:
		        obj_subproduct_a=obj_subproduct_h.findAll({"a"})[0]["href"]
		#             print (obj_subproduct_a)
		        sub_product_urls.append(obj_subproduct_a)
    except:
        pass
    
    
#     for i in range(len(obj_product_urls)):
#         sub_product_urls.append(obj_product_urls[i]["href"])

    # product_avaialbity=bsObj.findAll(text=re.compile("https://lcdh-amsterdam.com/index.php?route=product/category&path=59"))
#     print (product_urls)
#     print (len(product_urls))
#     del product_urls[0]
    
    return sub_product_urls

# sub_product_urls= spider_subproduct_urls(product_url)


# In[4]:




# url='https://lcdh-amsterdam.com/index.php?route=product/product&product_id=521'
# sub_product_url='https://lcdh-amsterdam.com/index.php?route=product/product&path=59_91&product_id=100'

def spider_stock_stage(sub_product_url):
    html=urllib.urlopen(sub_product_url)
    bsObj=BeautifulSoup(html)
    product_name=bsObj.findAll({"h1"})[0].get_text()
    product_avaialbity=bsObj.findAll(text=re.compile("Availability"))[0]
#     print (product_avaialbity)
    # print (bsObj)
    product_name =product_name
    # print (product_name)
    return product_name,product_avaialbity[14:],sub_product_url


# product_name,product_avaialbity,sub_product_url=spider_stock_stage(sub_product_url)

# print (product_name,product_avaialbity,sub_product_url)



# In[ ]:

if __name__ == '__main__':

	import time


	main_url='https://lcdh-amsterdam.com/index.php?route=product/category&path=59'

	product_urls=spider_product_urls(main_url)
	sub_product_urls=[]
	for product_url in product_urls[:]:
	    time.sleep(0.8)
	    print (product_url)
	    obj_sub_product_urls= spider_subproduct_urls(product_url)
	    sub_product_urls =sub_product_urls + obj_sub_product_urls

	print(len(sub_product_urls))
	# for sub_product_url in sub_product_urls:
	#     product_name,product_avaialbity,sub_product_url=spider_stock_stage(sub_product_url)
	#     print (product_name,product_avaialbity,sub_product_url)


	# In[ ]:

	import csv
	with open('./Desktop/product.csv', 'wb') as csvfile:
	    writer = csv.writer(csvfile)
	    writer.writerow(['product_name','product_avaialbity','product_url'])
	    for sub_product_url in sub_product_urls[:]:
	        time.sleep(0.5)
	        product_name,product_avaialbity,sub_product_url=spider_stock_stage(sub_product_url)
	        writer.writerow([product_name,product_avaialbity,sub_product_url])
	        print (product_name,product_avaialbity,sub_product_url)



	print ('Finished....')

