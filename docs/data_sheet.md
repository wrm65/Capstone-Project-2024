# Dataset Name: Ofsted Inspected School [OIS] Dataset

## Motivation

- <b>For what purpose was the dataset created?</b> The `OIS Dataset` was created to enable the analysis and prediction of the likely grade that a school would receive on its next inspection by [Ofsted](https://www.gov.uk/government/organisations/ofsted).
- <b>Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?</b> The dataset was created by the author of this datasheet.
- <b>Who funded the creation of the dataset?</b> Creation of the dataset is freely available. 

 
## Composition

- <b>What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?</b> Each instance within the dataset will represent the information created for the state-funded primary school.
- <b>How many instances of each type are there?</b> The dataset will contain nn,nnn unique schools in total
- <b>Is there any missing data?</b> There is no missing data.
- <b>Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor–patient confidentiality, data that includes the content of individuals’ non-public communications)?</b> There is no confidential data.

## Collection process

- <b>How was the data acquired?</b> The dataset is created from the UK Government website [Get Information about Schools](https://www.get-information-schools.service.gov.uk/). The `OIS` dataset is created from the online register provided by the Department of Education.
- <b>If the data is a sample of a larger subset, what was the sampling strategy?</b> The school register contains a list of all the state-funded schools. The `OIS` dataset is a subset of schools which are classed as `Primary` school. These are schools with pupils between the ages of 4 - 11.
- <b>Over what time frame was the data collected?</b> As the school data is updated daily and can be filtered from the `Department of Education's School Register`, an "on-demand" service is provided and the dataset is created as and when required. i.e. the data is the most-up-to-date and is collected on the day it is requested.

## Preprocessing/cleaning/labelling

- <b>Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.</b> 
  <div>
    The following steps were taken to process the data:
    <ol start="1">
      <li><b>Collecting the raw data:</b> Data was obtained from the GIAS website and stored locally. A screenshot of a sample school instance data is shown below.</li>
      <li><b>Creating a PHP script:</b> A script was developed to process and clean the dataset.</li>
      <li><b>Correct missing data:</b> Each school instance was validated for missing information. The list of missing data and action taken is shown below.</li>
  
    <div>
   
    <p>
   
    | Missing Value |  Action taken |
    | --- | --- |
    | FIELD_NumberOfPupils | set to FIELD_NumberOfBoys + FIELD_NumberOfGirls |
    | FIELD_SchoolCapacity | set to FIELD_NumberOfPupils |
    
    </p>

    </div>

    </ol>

   <p>
    <div>
      <ol start="4">
        <li><b>Map raw data columns to database table columns:</b> As a school instance in the raw dataset contained over 300 columns, this was significantly reduced to 20 columns. In addition, some of the column names were abbreviated and somewhat cryptic e.g. EHC, FSM, NUMEAL, therefore the columns were given more meaningful names.</li>
        <li><b>Saving to a PostgreSQL database:</b> The newly formatted school instances were stored into 2 database tables, <b><i>education_establishment</i></b>, <b><i>education_establishment_characteristic</i></b>. By using SQL, this approach allowed further validation and updating of the dataset to be completed in an easier and quicker manner.
        </li>
        <li><b>Exporting from the database:</b> An SQL Query Statement was used to <i>join</i> the data from both tables to create the dataset. The resultant data was exported directly into a CSV format.</li>
   
   <div>
  
    <div>
   
    <p>
   
    <div>
      The final OIS dataset is provided in a CSV format at the following link:
https://github.com/wrm65/Capstone-Project-2024/blob//main/dataset/school_ofsted_rating.csv

   </div>
    
  - <b>Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?</b> The raw unprocessed data is saved in its `CSV` format.
- <b>Is the preprocessing software available?</b> The `PHP` script which performed a number of preprocessing tasks and saved the data to the database, is not available. However, all the software used is open source and has been specified above.

- <i>Sample school instance data</i>
   <div>
    <img style="width:500px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/gias_data_01.png">
   </div>
 
- [Click to view the entire school's GIAS details](https://www.get-information-schools.service.gov.uk/Establishments/Establishment/Details/148025)

## Uses

- <b>Does this dataset achieve the motivation for creating the dataset stated in the first section of this datasheet?</b>
  <div>
    There some limitations in the dataset which will prevent other characteristics (features) of a school to be analyse. The following information would need to be considered to provide a more comprehensive prediction of gradings for schools.
    <ul>
    <li><b>Teacher Quality Metrics:</b> Teacher qualifications, experience, methods and pedagogical approaches, student-teacher ratio, class size</li>
    <li><b>Pupils Outcomes:</b> Exam results, progress and attainment measures, attendance rates</li>
    <li><b>Leadership and management:</b> Leadership effectiveness, staff turnover rates, school governance structure</li>
    <li><b>Safeguarding and Well-being:</b> Safeguarding policies and procedures, student well-being and pastoral care support, incidents of bullying or behavior issues</li>
    <li><b>Demographic and Socioeconomic Factors:</b> Ethnicity and language diversity, socioeconomic deprivation indices, special educational needs (SEN) prevalenc</li>
    <li><b>School Characteristics:</b> Funding levels and resources available, facilities and infrastructure</li>
    <li><b>Community Engagement:</b> Parental involvement and engagement, extra-curricular activities and enrichment programs</li>
    <li><b>Past Performance:</b> Trends in performance over time</li>
    </ul>
  <div>
- <b>What other tasks could the dataset be used for?</b> The dataset could be used to provide a variety of summary statistics such as:
    <ul>
    <li><b>Descriptive Statistics:</b> Mean, median, and mode, standard deviation and variance, range, percentiles</li>
    <li><b>Socioeconomic Context:</b> Percentage of students eligible for free school meals, serving as a proxy for socioeconomic disadvantage</li>
    <li><b>Quality Assurance:</b> Summary statistics on inspection outcomes (example shown below)</li>
   <div>
    <img style="width:200px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/summary_stats.png">
   </div>

## Distribution

- <b>How has the dataset already been distributed?</b> The dataset was created at the start of this project.
- <b>Is it subject to any copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?</b> The data is publicly available and there is no IP license, but if the dataset is used, there is a request to cite the use.

## Maintenance

- <b>Who maintains the dataset?</b> The dataset was up-to-date as of the 15th April 2024 and no further update is envisage. 

## Permitted Use

- The dataset is provided for research, educational, and non-commercial purposes <b><u>only</u></b>. Attribution to the original source is required.

## Citation

- Ofsted Inspected School dataset created by W. Menzies, Imperial College Business School, 2024.

