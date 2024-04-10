# Dataset Name: Ofsted Inspected School Dataset

## Motivation

- <b>For what purpose was the dataset created?</b> The Ofsted Inspected School {OIS} Dataset was created to enable the analyse and prediction of the likely grade that a school would receive on its next inspection by Ofsted.
- <b>Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?</b> The dataset was created by the author of this datasheet.
- <b>Who funded the creation of the dataset?</b> Creation of the dataset is freely available. 

 
## Composition

- <b>What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?</b> Each instance within the dataset will represent the information created for the state-funded primary school.
- <b>How many instances of each type are there?</b> The dataset will contain nn,nnn unique schools in total
- <b>Is there any missing data?</b>There is no missing data.
- <b>Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor–patient confidentiality, data that includes the content of individuals’ non-public communications)?</b> There is no confidential data.

## Collection process

- <b>How was the data acquired?</b> The dataset is created from the UK Government website [Get Information about Schools](https://www.get-information-schools.service.gov.uk/). The OIS dataset is created from the online register provided by the Department of Education.
- <b>If the data is a sample of a larger subset, what was the sampling strategy?</b> The school register contains a list of all the state-funded schools. The OIS dataset is a subset of schools which are classed as Primary School. These are schools with pupils between the ages of 4 - 11.
- <b>Over what time frame was the data collected?</b> As the school data is updated daily and can be filtered from the Department of Education's School Register, an "on-demand" service is provided and the dataset is created as and when required. i.e. the data is the most-up-to-date and is collected on the day it is requested.

## Preprocessing/cleaning/labelling

- <b>Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.</b> 
    <div>
    The following steps were taken to process the data:
    <ol>
    <li><b>Collecting the raw data:</b></li>
    <li><b>Creating a PHP script:</b></li>
    <li><b>Saving to a database:</b></li>
    <li><b>Exporting from the database:</b></li>
    </ol>
		The final dataset, [Ofsted Inspected School](https://github.com/wrm65/Capstone-Project-2024/blob/main/docs/ofsted_inspected_school.csv) is provided in a CSV format.
    <div>
- <b>Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?</b> The raw unprocessed data is saved in its CSV format.
 
## Uses

- What other tasks could the dataset be used for? 
- Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a dataset consumer might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other risks or harms (e.g., legal risks, financial harms)? If so, please provide a description. Is there anything a dataset consumer could do to mitigate these risks or harms? 
- Are there tasks for which the dataset should not be used? If so, please provide a description.

## Distribution

- How has the dataset already been distributed? 
- Is it subject to any copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?  

## Maintenance

- Who maintains the dataset?

