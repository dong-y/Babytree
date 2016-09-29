# Brief introduction on the folders

* BasicDatabase

* DeliveryDate

* HandyScripts
	* Contains some useful scripts

* UserPostCrawler
	* crawler.py
	* parser.py
	* input: babytree_user_id.csv
	* output: babytree_user_post_url.csv (user_id; postdummy; board; date; url)
	
* UserPostContent
	* crawler.py
	* parser.py
	* input: babytree_user_post_url.csv
	* output: babytree_user_post_content.csv


--
#User Post Crawler

>* $ python crawler.py

>* $ python parser.py

##Input file:

* ID csv file

e.g. babytree_user_id.csv

##Output file:

* babytree_user_post_url.csv
	* user_id; postdummy; board; date; url 
* AttributeError.txt
* parser_AttributeError.txt

##Note:
* should indicate the **inputdir** and **outputdir** in the **crawler.py** file
* should manually create **Rawdata dir** and **outputdir** in the folder (will automate this step when I am in good mood)

-- 
# User Post Content

>* $ python crawler.py

>* $ python parser.py

##Input file:

* ID + url csv file

e.g. babytree_user_post_url.csv

##Output file:

* babytree_user_post_content.csv
    * user_id; url; title; body
* babytree_user_post_title.csv
    * user_id; url; title  
* babytree_user_post_body.csv
    * user_id; url; body 
* AttributeError.txt
* parser_AttributeError.txt

##Note:
* should manually create **rawdata dir** and **outputdir** in the folder (will automate this step when I have time)
* To be improved: write a function to initiate the output files
