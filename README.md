# Grad_School_Recommendation_System

For students who are interested in apply for grad school, finding target schools is one of the important steps for grad school application and somethimes students may interesed in past years admission status in order to plan their application well. This project will analyze the admission data submitted by students from previous on GradCafe and provide insighs on the admission trend. Moreover, a grad school recommender system will provide k univeristies that suitable for a student's background. 

## DataSet

The admission data are scraped from ``` GradCafe```. ``` GradCafe``` is a website which allows to submit their admission result for schools all over the world. They can choose to submit the following information on the website: ``` SchoolName```, ``` Major```,``` GRE```,``` GPA```,``` Decision Received```,``` Decision Date```,``` Degree```,``` EntryTime```, as well as any ``` Comments``` they want to make. 
</br></br>

About 144960 rows of entries were scrapped. This data has no maojor, shcool or degree preference, but input request with the desired``` SchoolName```, ``` Major```,``` Degree```, the program will scrape the corrsponding admission data for you. 

```
school = str(input('Enter university name(hit Enter if no preference):'))
major= str(input('Enter major(hit Enter if no preference):'))
degree_type=str(input('Enter degree type(hit Enter if no preference):'))
num_pages=int(input('Enter num pages:')) #3634
```
## Web Scraping

To scrape the admission data, run the ``` scrape_site.py``` file. The program will scrape the corrsponding data based on the preference given in the previous section. 


## Data Parsing
The ``` scrape_site.py``` file will scripe data in ``` html``` form and store in the folder. Then run the ``` parser.py```file to parse the data from ``` html```pages and eventually save as a ``` csv``` file.


