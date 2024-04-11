# Dataset Name: Ofsted Inspected School Dataset

## Motivation

- <b>For what purpose was the dataset created?</b> The Ofsted Inspected School {OIS} Dataset was created to enable the analyse and prediction of the likely grade that a school would receive on its next inspection by Ofsted.
- <b>Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?</b> The dataset was created by the author of this datasheet.
- <b>Who funded the creation of the dataset?</b> Creation of the dataset is freely available. 

 
## Composition

- <b>What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?</b> Each instance within the dataset will represent the information created for the state-funded primary school.
- <b>How many instances of each type are there?</b> The dataset will contain nn,nnn unique schools in total
- <b>Is there any missing data?</b> There is no missing data.
- <b>Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor–patient confidentiality, data that includes the content of individuals’ non-public communications)?</b> There is no confidential data.

## Collection process

- <b>How was the data acquired?</b> The dataset is created from the UK Government website [Get Information about Schools](https://www.get-information-schools.service.gov.uk/). The OIS dataset is created from the online register provided by the Department of Education.
- <b>If the data is a sample of a larger subset, what was the sampling strategy?</b> The school register contains a list of all the state-funded schools. The OIS dataset is a subset of schools which are classed as Primary School. These are schools with pupils between the ages of 4 - 11.
- <b>Over what time frame was the data collected?</b> As the school data is updated daily and can be filtered from the Department of Education's School Register, an "on-demand" service is provided and the dataset is created as and when required. i.e. the data is the most-up-to-date and is collected on the day it is requested.

## Preprocessing/cleaning/labelling

- <b>Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.</b> 
	<div>
    The following steps were taken to process the data:
    <ol start="1">
			<li><b>Collecting the raw data:</b> Data was obtained from the GIAS website and stored locally.</li>
			<li><b>Creating a PHP script:</b> A script was developed to process and clean the dataset.</li>
			<li><b>Correct missing data:</b> Each school instance was validated for missing information. The list of missing data and action taken is shown below.</li>
    </ol>
	<div>
	
| Missing Value |  Action taken |
| --- | --- |
| FIELD_NumberOfPupils | set to FIELD_NumberOfBoys + FIELD_NumberOfGirls |
| FIELD_SchoolCapacity | set to FIELD_NumberOfPupils |

<div>
    
    <ol start="4">
      <li><b>Map raw data columns to database table columns:</b></li>
      <li><b>Saving to a database:</b></li>
      <li><b>Exporting from the database:</b></li>
     <div>The final Ofsted Inspected School dataset is provided in a CSV format at the following link:</div> 
https://github.com/wrm65/Capstone-Project-2024/blob//main/dataset/ofsted_inspected_school.csv
    </ol>
</div>
	
- <b>Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?</b> The raw unprocessed data is saved in its CSV format.
- <b>Is the preprocessing software available?</b> While the PHP script which perform a number of cleaning tasks and save the data to the database is not available, all the software used is open source and has been specified above.
 
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

