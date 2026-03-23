# Dataverse-API-Push-UI-MarkIt-Students 🐍🌌
This repository can be used to compute variable weights and create variable groups in Borealis.

### Purpose of the tool 🤔❓
1) Data Explorer sometimes faces issues in which the import of XML files from other datasets of the same series does not import custom groups. This tool, by virtue of pushing groups through the API, circumvents this issue.
2) Some dataset variables can be tempermental (or disfunctional) and cause Data Explorer to crash/fail to save changes when prompted to do so (red failure to save text box). This tool forces weight computation for these troublesome variables and automatically pushes them through the API.

The present tool has the advanatage of allowing users to perform variable level metadata update API pushes without any prior knowledge of CURL commands or Python Requests.

## Python Requirements ⚙️🔧
1) Local python IDE (Jupyter, Wing, PyCharm, etc.). Code will not work with web-based python programs (like Google Colab) due to Borealis restrictions.
2) Minimum required python version: 3.6+.

## File Requirements 📁🗃️
1) API key (generated in Borealis).
2) Dataset DOI (in "https://doi.org/" OR "doi:" format).
3) XML file template (pulled from a different dataset of the same series).
4) Original SPSS (.sav) file for the dataset (the one that was converted in TAB format in Dataverse).
5) The exact tabular file weight variable label (e.g., FINALWT or WEIGHTED).
6) The exact record IDs variable label (e.g., REC_NUM or CASEID)

## User Guide 🔍🛃
⚠️ For successful API push, please make sure to read the steps below! ⚠️

1) Complete your Odesi dataset like you normally would (but don't submit it for revision yet);
2) Export the metadata from a different dataset of the same serie in JSON format (navigate to the "Metadata" tab in Borealis, open the "Export Metadata" scroll down menu, and select "JSON")

<kbd><img width="1140" height="370" alt="image" src="https://github.com/user-attachments/assets/2d5cf726-4f93-4252-aef7-c80e818c0747" /></kbd>
<br><br>

3) Fetch your API key (navigate to your user scroll down menu and select the "API Token" option - from there, you will be able to generate an API token). Remember to never share your API key with anyone.

<kbd><img width="1181" height="217" alt="image" src="https://github.com/user-attachments/assets/f03f1f1d-1889-4d03-8670-bf516a1a2fb4" /></kbd>
<br><br>

4) Download th python file from this GitHub repository (navigate to the [API_PUSH_MARKIT_UI.py](https://github.com/letendrt/Dataverse-API-Push-UI-MarkIt-Students/blob/main/API_PUSH_MARKIT_UI.py) file and select the "Download Raw File" option)

<kbd><img width="1455" height="137" alt="image" src="https://github.com/user-attachments/assets/ab6d2531-d9a7-4a85-98f8-b64b6300554d" /></kbd>
<br><br>

5) Open your python IDE (Jupyter notebook, Wing, PyCharm, etc. - the IDE does not matter as long as it is a local iteration on your device), and import the python file you just downloaded.
6) Run the code by pressing the play button on the IDE. At this point, you should be greeted by the following window:

<kbd><img width="1266" height="775" alt="image" src="https://github.com/user-attachments/assets/129795bc-6f3d-4e6d-b440-d7bdae6229db" /></kbd>
<br><br>

7) For fields 1 and 2, make sure there are no spaces before or after your entries. For field 1, copy your API key and paste it in the box. For field 2, copy the DOI link found on your dataset landing page;

<kbd><img width="861" height="234" alt="image" src="https://github.com/user-attachments/assets/b28c48aa-8837-418f-b513-eb66e248f4be" /></kbd>
<br><br>

8) For fields 3 and 4, simply press their respective button and navigate to the local file on your device. For field 3, select the JSON file donwloaded in step 2. For step 4, simply select the original SPSS file (.sav extension) that was converted to TAB during the ingestion process.
9) For fields 5 and 6, 





