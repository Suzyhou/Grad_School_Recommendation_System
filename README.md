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
The ``` scrape_site.py``` file will scripe data in ``` html``` form and store in the folder. Then run the ``` parser.py```file to parse the data from ``` html```pages and eventually save as a ``` csv``` file. During the parsing step, the data was cleaned especially the ``` SchoolName```, ``` Major``` column as there are abbreviation, upper case or small case entries. After parsing, there are ``` 3482``` unique school names, and ``` 7727``` unique maojor names. 

## Data Exploration Analysis
### Top 10 institutions with the most applicant:
```
Columbia University                            3626
Stanford University                            3469
University Of California Berkeley              3429
University Of Michigan (Ann Arbor)             3255
University Of Texas                            2952
Massachusetts Institute Of Technology (MIT)    2677
Carnegie Mellon University                     2675
Cornell University                             2653
New York University                            2577
Harvard University                             2563
```
### Top 5 majors with the most applicant:
```
Computer Science             13928
Economics                    10870
Speech Language Pathology     8481
Clinical Psychology           6985
Physics                       6002
```
### Decision Delivery Season
For different admission decisions, the result start to come out in December, but a small number. This usually apply to programs that are rolling bases or have multiple rounds. Then the decision delivery tends to increase in January, and reaches to a peak in Feburary. The number of decision results start to decrease in March and almost no result come out during spring and summer. 
![image](https://user-images.githubusercontent.com/26268789/154303075-fb3b9620-a707-4535-80c5-9b42a51365dc.png)

### GPA and GRE Distribution for Different Decision 
![image](https://user-images.githubusercontent.com/26268789/154305169-bcb6266d-de34-4815-8f5a-fbbec0a86894.png)
![image](https://user-images.githubusercontent.com/26268789/154308662-ec7a0c4d-9958-4772-93df-af9c28905bc5.png)

### GPA vs GRE for the Top 10 Institution with the Most Applicants
From this plot, it is noticed that Carnegie Mellon University (CMU) and Conell are interested in students with higher GPA instead of higher GRE. UCB, columnbia University, and U of Michigan tends to accpet student that have higher GRE. Stanford and MIT intereted in students have both good GRE and GPA score. Among the top 10 insitutions, Stanford and MIT has the highest requirements. 
![image](https://user-images.githubusercontent.com/26268789/154308890-02faf41a-756f-4e24-ab4c-49ff7e7c6a60.png)

## Grad School Recommendation System
The grad school recommendation system is build based on K Nearest Neighbor with user-user simiarities using Euclidean distance. When input new student's background with their GPA, GRE(if applicable), and research experience, the recommender system will return top k instutions that is suitable for the student. 
```
testSet = [[4, 170, 0]]
```
```
Harvard University
Cornell University
Massachusetts Institute Of Technology (MIT)
University Of Wisconsin
University Of Pennsylvania
```
