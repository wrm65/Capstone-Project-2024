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
    </ol>
    
   <div>
   
      <div>
   
        | Missing Value |  Action taken |
        | --- | --- |
        | FIELD_NumberOfPupils | set to FIELD_NumberOfBoys + FIELD_NumberOfGirls |
        | FIELD_SchoolCapacity | set to FIELD_NumberOfPupils |
    
      </div>

   </div>

   <p>
    <p>
      <ol start="4">
      <li><b>Map raw data columns to database table columns:</b> As a school instance in the raw dataset contained over 300 columns, this was significantly reduced to 20 columns. In addition, some of the column names were abbreviated and somewhat cryptic e.g. EHC, FSM, NUMEAL, therefore the columns were given more meaningful names.</li>
      <li><b>Saving to a PostgreSQL database:</b> The newly formatted school instances were stored into 2 database tables, <b><i>education_establishment</i></b>, <b><i>education_establishment_characteristic</i></b>. By using SQL, this approach allowed further validation and updating of the dataset to be completed in an easier and quicker manner.
<details>
  <summary>Database table: <b><i>education_establishment</i></b> (click to view definition)</summary>
   <pre>
CREATE TABLE education_establishment
(
    unique_reference_number bigint NOT NULL,
    establishment_number integer NOT NULL,
    authority_code integer NOT NULL,
    administrative_code character varying(50) NOT NULL,
    uk_prn character varying(20) NOT NULL,
    establishment_name text NOT NULL,
    establishment_type_code integer NOT NULL,
    statutory_highest_age integer NOT NULL,
    statutory_lowest_age integer NOT NULL,
    sixth_form_exist boolean NOT NULL,
    school_capacity integer NOT NULL,
    pupil_number integer NOT NULL,
    pupil_boys integer NOT NULL,
    pupil_girls integer NOT NULL,
    free_school_meals integer NOT NULL,
    free_school_meals_percentage numeric(5,2) NOT NULL,
    education_phase character varying(80) NOT NULL,
    gender_type integer NOT NULL,
    religious_character_code integer NOT NULL,
    admissions_policy character varying(50) NOT NULL,
    establishment_status character varying(50) NOT NULL,
    opened_reason character varying(50) NOT NULL,
    opening_date date NOT NULL,
    app_image_group integer NOT NULL,
    active_detail boolean NOT NULL,
    created_local_date timestamp with time zone NOT NULL,
    created_date timestamp with time zone NOT NULL,
    created_by integer NOT NULL,
    CONSTRAINT education_establishment_pkey PRIMARY KEY (unique_reference_number)
)
   </pre>
</details>

<details>
  <summary>Database table: <b><i>education_establishment_characteristic</i></b> (click to view definition)</summary>
   <pre>
CREATE TABLE education_establishment_characteristic
(
    unique_reference_number bigint NOT NULL,
    pupil_number integer NOT NULL,
    pupil_boys integer NOT NULL,
    pupil_girls integer NOT NULL,
    pupil_ehc_plan integer NOT NULL,
    pupil_sen_support integer NOT NULL,
    pupil_english_language integer NOT NULL,
    pupil_not_english_language integer NOT NULL,
    pupil_unclassify_language integer NOT NULL,
    pupil_free_school_meals integer NOT NULL,
    percent_pupil_boys numeric(5,2) NOT NULL,
    percent_pupil_girls numeric(5,2) NOT NULL,
    percent_ehc_plan numeric(5,2) NOT NULL,
    percent_sen_support numeric(5,2) NOT NULL,
    percent_english_language numeric(5,2) NOT NULL,
    percent_not_english_language numeric(5,2) NOT NULL,
    percent_unclassify_language numeric(5,2) NOT NULL,
    percent_free_school_meals numeric(5,2) NOT NULL,
    active_detail boolean NOT NULL,
    created_local_date timestamp with time zone NOT NULL,
    created_date timestamp with time zone NOT NULL,
    created_by integer NOT NULL,
    CONSTRAINT education_establishment_characteristic_pkey PRIMARY KEY (unique_reference_number)
)
   </pre>
</details>
      </li>
    </ol>
    </p>
   </p>
   
   <p>
    <p>
      <ol start="6">
      <li><b>Exporting from the database:</b> An SQL Query Statement was used to <i>join</i> the data from both tables to create the dataset. The resultant data was exported directly into a CSV format.
<details>
  <summary>SQL Statement: <b><i>retrieve school details</i></b> (click to view statement)</summary>
  <pre>
    SELECT
      EE.UNIQUE_REFERENCE_NUMBER,
      EE.AUTHORITY_CODE,
      EE.ESTABLISHMENT_TYPE_CODE,
      EE.PUPIL_NUMBER,
      EE.PUPIL_BOYS,
      EE.PUPIL_GIRLS,
      EE.GENDER_TYPE,
      CASE EE.GENDER_TYPE
        WHEN 1 THEN 'Boys'
        WHEN 2 THEN 'Girls'
        ELSE 'Mixed'
      END GENDER_CATEGORY,
      CASE ERC.CLASSIFICATION
        WHEN 'Church of England' THEN 1
        WHEN 'Roman Catholic' THEN 4
        WHEN 'Other religion' THEN 3
        ELSE 2
      END RELIGIOUS_TYPE,
      ERC.CLASSIFICATION AS RELIGIOUS_CLASSIFICATION,
      EEC.PERCENT_PUPIL_BOYS,
      EEC.PERCENT_PUPIL_GIRLS,
      EEC.PERCENT_EHC_PLAN,
      EEC.PERCENT_SEN_SUPPORT,
      EEC.PERCENT_ENGLISH_LANGUAGE,
      EEC.PERCENT_NOT_ENGLISH_LANGUAGE + EEC.PERCENT_UNCLASSIFY_LANGUAGE AS PERCENT_NOT_ENGLISH_LANGUAGE,
      EEC.PERCENT_FREE_SCHOOL_MEALS,
      EOR.RATING
    FROM
      PUBLIC.EDUCATION_ESTABLISHMENT_CHARACTERISTIC EEC,
      PUBLIC.EDUCATION_RELIGIOUS_CHARACTER ERC,
      PUBLIC.EDUCATION_ESTABLISHMENT EE,
      PUBLIC.EDUCATION_OFSTED_REPORT EOR
    WHERE
      EEC.UNIQUE_REFERENCE_NUMBER = EE.UNIQUE_REFERENCE_NUMBER
      AND EOR.UNIQUE_REFERENCE_NUMBER = EE.UNIQUE_REFERENCE_NUMBER
      AND ERC.RELIGIOUS_CHARACTER_CODE = EE.RELIGIOUS_CHARACTER_CODE
      AND EE.ESTABLISHMENT_TYPE_CODE NOT IN (14) -- PRU
      AND EE.GENDER_TYPE NOT IN (9) -- unknown
      AND EOR.RATING IN (
        'Outstanding',
        'Good',
        'Requires improvement',
        'Inadequate'
      ) 
  </pre>
</details>
      </li>
     <div>The final OIS dataset is provided in a CSV format at the following link:</div> 
  https://github.com/wrm65/Capstone-Project-2024/blob//main/dataset/school_ofsted_rating.csv
      </ol>
    </p>
   </p>
  
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

