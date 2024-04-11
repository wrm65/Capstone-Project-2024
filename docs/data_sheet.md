# Dataset Name: Ofsted Inspected School [OIS] Dataset

## Motivation

- <b>For what purpose was the dataset created?</b> The `OIS Dataset` was created to enable the analyse and prediction of the likely grade that a school would receive on its next inspection by [Ofsted](https://www.gov.uk/government/organisations/ofsted).
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
	
| Missing Value |  Action taken |
| --- | --- |
| FIELD_NumberOfPupils | set to FIELD_NumberOfBoys + FIELD_NumberOfGirls |
| FIELD_SchoolCapacity | set to FIELD_NumberOfPupils |

 <p>
		<p>
			<ol start="4">
			<li><b>Map raw data columns to database table columns:</b> As a school instance in the raw dataset contained over 300 columns, this was significantly reduced to 20 columns. In addition, the column names were abbreviated and somewhat cryptic, therefore the columns were given more meaningful names.</li>
			<li><b>Saving to a PostgreSQL database:</b> The newly formatted school instances were stored into a database table, <b><i>education_establishment</i></b>. By using SQL, this approach allowed further validation and updating of the dataset to be completed in an easier and quicker manner.
				<details>
					<summary>Database table: <b><i>education_establishment</i></b> (click to view table definition)</summary>
					<pre>
CREATE TABLE education_establishment
(
    unique_reference_number bigint NOT NULL,
    establishment_number integer NOT NULL,
    authority_code integer NOT NULL,
    administrative_code character varying(50) COLLATE pg_catalog."default" NOT NULL,
    uk_prn character varying(20) COLLATE pg_catalog."default" NOT NULL,
    establishment_name text COLLATE pg_catalog."default" NOT NULL,
    establishment_type character varying(80) COLLATE pg_catalog."default" NOT NULL,
    statutory_highest_age integer NOT NULL,
    statutory_lowest_age integer NOT NULL,
    sixth_form_exist boolean NOT NULL,
    school_capacity integer NOT NULL,
    pupil_number integer NOT NULL,
    pupil_boys integer NOT NULL,
    pupil_girls integer NOT NULL,
    free_school_meals integer NOT NULL,
    free_school_meals_percentage numeric(5,2) NOT NULL,
    education_phase character varying(80) COLLATE pg_catalog."default" NOT NULL,
    gender_type integer NOT NULL,
    religious_character character varying(80) COLLATE pg_catalog."default" NOT NULL,
    religious_ethos character varying(80) COLLATE pg_catalog."default" NOT NULL,
    admissions_policy character varying(50) COLLATE pg_catalog."default" NOT NULL,
    establishment_status character varying(50) COLLATE pg_catalog."default" NOT NULL,
    opened_reason character varying(50) COLLATE pg_catalog."default" NOT NULL,
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
			</li>
			<li><b>Exporting from the database:</b> The dataset to be used for the modelling was exported directly into a CSV format.</li>
		 <div>The final OIS dataset is provided in a CSV format at the following link:</div> 
	https://github.com/wrm65/Capstone-Project-2024/blob//main/dataset/ofsted_inspected_school.csv
			</ol>
		</p>
  </p>
	
- <b>Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?</b> The raw unprocessed data is saved in its `CSV` format.
- <b>Is the preprocessing software available?</b> While the `PHP` script which perform a number of cleaning tasks and save the data to the database is not available, all the software used is open source and has been specified above.
 
 <div>
	<img style="width:500px" src="https://github.com/wrm65/Capstone-Project-2024/blob/main/images/gias_data_01.png">
 </div>
 
- [View GIAS  details...](https://www.get-information-schools.service.gov.uk/Establishments/Establishment/Details/148025#school-dashboard)

## Uses

- <b>Does this dataset achieve the motivation for creating the dataset stated in the first section of this datasheet?</b>
	<div>
    There some limitations in the dataset:
    <ul>
    <li><b>Lack of features:</b></li>
    </ul>
	<div>
- <b>What other tasks could the dataset be used for?</b> 
- <b>Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a dataset consumer might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other risks or harms (e.g., legal risks, financial harms)? If so, please provide a description. Is there anything a dataset consumer could do to mitigate these risks or harms?</b>
- <b>Are there tasks for which the dataset should not be used? If so, please provide a description.</b>

## Distribution

- <b>How has the dataset already been distributed?</b> The dataset was created at the start of this project.
- <b>Is it subject to any copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?</b> There is no license, but if the dataset is used, there is a request to cite the use.

## Maintenance

- <b>Who maintains the dataset?</b> The dataset was up-to-date as of the 15th April 2024 and will not be updated. 

## Permitted Use

- The dataset is provided for research, educational, and non-commercial purposes only. Attribution to the original source is required.

## Citation

- Ofsted Inspected School dataset created by W. Menzies, Imperial College Business School, 2024.

