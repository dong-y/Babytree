# User Post Content

>* $ python crawler.py

>* $ python parser.py

##Input file:

* ID csv file

e.g. babytree_user_id.csv

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