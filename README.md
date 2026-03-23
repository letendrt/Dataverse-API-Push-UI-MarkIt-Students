# Dataverse-API-Push-UI-MarkIt-Students 🐍🌌
This repository can be used to compute variable weights and create variable groups in Borealis.

### Purpose of the tool 🤔❓
1) Data Explorer sometimes faces issues in which the import of XML files from other datasets of the same series does not import custom groups. This tool, by virtue of pushing groups through the API, circumvents this issue.
2) Some dataset variables can be tempermental (or disfunctional) and cause Data Explorer to crash/fail to save changes when prompted to do so (red failure to save text box). This tool forces weight computation for these troublesome variables and automatically pushes them through the API.

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

