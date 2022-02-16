#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import pandas as pd
import sys, re
import datetime, time
import pandas as pd
from bs4 import BeautifulSoup
import pandas

SCHOOL = [('Columbia U', 'Columbia University'),
         ('Stanford','Stanford University'),
         ('Of Michi|Ann Arbor','University Of Michigan (Ann Arbor)'),
         ('UC B|Berkeley|California Berkeley|UCB|Ucb','University Of California Berkeley'),
         ('Of Wash','University Of Washington'),
         ('Massachusetts Institute|MIT','Massachusetts Institute Of Technology (MIT)'),
         ('Cornell W|Cornell U|Weill C|Ithaca','Cornell University'),
         ('Wiscons','University Of Wisconsin'),
         ('Southern Cal|USC','University Of Southern California'),
         ('y Of Chi|Harris','University Of Chicago'),
         ('Toronto|Rotman|OISE|Oise|oise|UofT|UTSC|Scarborough','University Of Toronto'),
         ('Harvard','Harvard University'),
         ('Texas At|Austin|Of Texas|UT Southwestern','University Of Texas'),
         ('Carnegie|CMU','Carnegie Mellon University'),
         ('Northwest','Northwestern University'),
         ('Princeton','Princeton University'),
         ('Yale','Yale University'),
         ('Boston U|BU','Boston University'),
         ('Of Penn|UPenn','University Of Pennsylvania'),
         ('UCLA|Californa Los','University Of California Los Angeles (UCLA)'),
         ('Duke','Duke University'),
         ('New York U|NYU|Nyu','New York University'),
         ('Oxford','University Of Oxford'),
         ('Ohio State|OSU','Ohio State University'),
         ('Minnesota','University Of Minnesota'),
         ('Johns Hopkins|JHU|Hopkins','Johns Hopkins University'),
         ('Georgia In|GT|GTech|Georgia T','Georgia Institute Of Technology'),
         ('Of Colo|Colorado B|Colorado D|Colorado Sp|CU B|CU D','University Of Colorado'),
         ('Of Massachusetts|UMass','University Of Massachusetts'),
         ('Of Maryland|UMD|UMCP|UMBC','University Of Maryland'),
         ('Of California I|UCI|UC Ir','University Of California Irvine'),
         ('TAMU|A&M','Texas A&M University - College Station (TAMU)'),
         ('Brown','Brown University'),
         ('f British C|UBCO|Sauder|Okanagan|UBC','University Of British Columbia'),
         (' San Diego|UCSD','University Of California San Diego'),
         ('Cambridge','University Of Cambridge'),
         ('Emory','Emory University'),
         ('California Davis|UCD','University Of California Davis'),
         ('McGill','McGill University'),
         ('f Virginia|UVA','University Of Virginia'),
         ('Carolina C|Chapel Hill|UNC','UNC Chapel Hill'),
         ('Northeastern|NEU','Northeastern University'),
         ('WashU|WUSTL|n St. Louis|WashU/WUSTL','Washington University In St. Louis (WashU/WUSTL)'),
         ('Arizona S|ASU','Arizona State University'),
         ('f Arizona','University Of Arizona'),
         ('Bloomington|IU Bloomington','Indiana University Bloomington'),
         ('Purdue|West La','Purdue University'),
         ('Penn S|PSU|Pennsylvania St','Penn State University'),
         ('Vanderbilt','Vanderbilt University'),
         ('California Institute Of Te|Caltech|CalTech|Cal Tech','California Institute Of Technology'),
         ('Of New York|CUNY','City University Of New York (CUNY)'),
         ('f Illinois|UIC|UIUC|Champaign','University Of Illinois'),
         ('Pittsburgh','University Of Pittsburgh'),
         ('Waterloo','University Of Waterloo'),
         ("Queens |Queens (Canada)",'Queens University'),
         ('University College London|UCL ','University College London'),
         ('f Missouri|UMSL|Mizzou',''),
         ('UC Santa Barbara|UCSB|Santa Barbara|California Santa Barbara','University Of California Santa Barbara'),
         ('University New York|SUNY','State University New York'),
         ('York University|Schulich','York University'),
         ('NCSU|North Carolina S|NC State','North Carolina State University'),
         ('California State|CSU','California State University'),
         ('f Iowa','University Of Iowa'),
         ('California San F|UCSF','University Of California San Francisco'),
         ('Florida St','Florida State University (FSU)'),
         ('Rice','Rice University'),
         ('Kings College|KCL','Kings College London'),
         ('Riverside|UC R|California R','University Of California Riverside'),
         ('George Washington|GU','George Washington University'),
         ('Rutgers','Rutgers University'),
         ('EPFL|Swiss','Swiss Federal Institute Of Technology')]

PROG = [('Computer Sci|ComputerSci|Computer Inf', 'Computer Science'),
        ('Data Sci', 'Data Science'),
        ('Electrical And Computer Engineering|ECE|EECS', 'Electrical And Computer Engineering'),
        ('Arch', 'Architecture'),
        ('Material', 'Materials Science And Engineering'),
        ('Econ|Economics', 'Economics'),
        ('Physics', 'Physics'),
        ('Clinical Psychology', 'Clinical Psychology'),
        ('Speech Lang', 'Speech Language Pathology'),
        ('Astronomy','Astronomy'),
        ('English','English'),
        ('Mathematics','Mathematics'),
        ('Linguistics','Linguistics'),
        ('Civil Engineering','Civil Engineering'),
        ('Epidemiology','Epidemiology'),
        ('Public Health','Public Health'),
        ('Civil And Environmental','Civil And Environmental Engineering'),
        ('Public Policy','Public Policy'),
        ('Robotics','Robotics'),
        ('Biomedical Engineering','Biomedical Engineering'),
        ('Neuroscience','Neuroscience'),
        ('Electrical Engineering','Electrical Engineering'),
        ('Aerospace Engineering','Aerospace Engineering'),
        ('Marketing','Marketing'),
        ('Anthropology','Anthropology'),
        ('Developmental Psychology','Developmental Psychology'),
        ('Social Psychology','Social Psychology'),
        ('Epidemiology','Epidemiology'),
        ('Business Analytics','Business Analytics'),
        ('Urban Planning','Urban Planning'),
        ('Information Science','Information Science'),
        ('Social Work|MSW','Social Work'),
        ('English','English'),
        ('Education','Education')]


def process(col):
    gpa_match = re.compile("GPA ((?:[0-9]\.[0-9]{1,2})|(?:n/a))")
    gre_match = re.compile("GRE 1(\d{2})")
    
    inst, major, decision, decmonth, gpa = None,None, None, None, None
    gre, status, entryTime, degree, comments= None, None, None,None,None
    
    lines = []
    for line in col:
        if line != '':
            if line != ' 0':
                lines.append(line)

    progtext = lines[0].strip().split('  ')
    if len(progtext) == 1:
        comments = None
    else:
        comments = progtext[1].strip()
    
    other = lines[1:-1]
    for i, j in enumerate(other): 
        if j.startswith('-'):
            more_comments = other[i]
            more_comments = more_comments.replace('-', '')
            comments += more_comments
            
            
    majorSchool = progtext[0].strip()
    parts2 = majorSchool.split(', ')
    
    major_original = parts2[0].strip()
    for match,major_name in PROG:
        s = re.search(match, major_original)
        if s is not None:
            major = major_name
            break
        else:
            major = major_original
            
            
    inst_original =' '.join(parts2[1:])
    for match,inst_name in SCHOOL:
        s = re.search(match, inst_original)
        if s is not None:
            inst = inst_name
            break
        else:
            inst = inst_original
            

    for i, j in enumerate(lines):
        gpa = None
        if j.startswith('GPA 3') and j[-1].isdigit():
            if "/" not in j:
                gpa_list = lines[i]
                gpa = float(gpa_list.split()[-1])
                break

    gre_list =  ' '.join([str(elem) for elem in list(filter(gre_match.match, lines))])
    if gre_list == '':
        gre = None
    else: 
        gre = float(gre_list.split()[-1])    

    for i, j in enumerate(lines):
        if j == 'Accepted' or j == 'Accepted Other':
            decision = lines[i]
        elif j == 'Interview' or j == 'Interview Other':
            decision = lines[i]
        elif j == 'Rejected' or j == 'Rejected Other':
            decision = lines[i]
        elif j == 'Wait listed' or j == 'Wait listed Other':
            decision = lines[i]
        elif j == 'Other' or j == 'Other Other':
            decision = lines[i]

    for i, j in enumerate(lines):
        if j.startswith('\t\t'):
            decision_date = lines[i]
            decision_date = decision_date.replace('\t', '').replace(' on ', '')
    #decision_date= ' '.join([str(elem) for elem in list(filter(decdate_match.match, lines))])
    #decision_date = decision_date.replace('\t', '').replace(' on ', '')
            if decision_date == '29 Feb':
                decmonth = 'February'
            elif decision_date.startswith(' '):
                decision_date = decision_date.lstrip()
                decdate_date = datetime.datetime.strptime(decision_date, '%d %b')
                decmonth = decdate_date.strftime('%B')
            else:
                decdate_date = datetime.datetime.strptime(decision_date, '%d %b')
                decmonth = decdate_date.strftime('%B')

    for i, j in enumerate(lines):
        if j == 'International':
            status = lines[i]
        elif j == 'American':
            status = lines[i]
        elif j == 'Other':
            status = lines[i]

    for i, j in enumerate(lines):
        if len(j)==9:
            if j.startswith('F') or j.startswith('S'):
                entryTime = lines[i]

    for i, j in enumerate(lines):
        if j == 'PhD' or j == 'Masters' or j == 'MFA' or j == 'MBA' or j == 'JD' :
            degree = lines[i]
        elif j == 'EdD' or j == 'IND' or j == 'PsyD' or j == 'Other':
            degree = lines[i]

    results = [inst, major, decision, decmonth, gpa, gre, status, entryTime, degree, comments]
    return results



def parser(num_pages,school,major):
    DataSet = []  
    for idx in range(1,int(num_pages)): 
        with open('data/{0}.html'.format(idx),'r', encoding="utf8") as html_file:
            content = html_file.read()
            soup = BeautifulSoup(content,'lxml')
            tables = soup.findAll('div', class_='row mb-2')
            for tab in tables:
                rows = tab.text.splitlines()
                if len(rows)!=5:
                    values = process(rows)
                    DataSet.append(values)
            print('parsing page {}...'.format(idx))
    df = pd.DataFrame(DataSet,columns = ['school', 'major', 'decision', 'decision_month', 'gpa', 'gre', 'status', 'entryTime', 'degree', 'comments'])
    #df.to_csv('{}_raw.csv'.format(school+major),mode='w+')
    return df

