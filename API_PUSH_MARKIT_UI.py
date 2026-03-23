# User interface for Markit API push
# Developed by: Thierry Letendre 
# On behalf of: Scholars Portal/Odesi/Borealis/MarkIt group



#----------------------IMPORTING LIBRARIES

# Importing GUI tools
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog

#Importing libraries for systems set-up and info
from datetime import datetime
import sys
import time

# importing libraries for XML/HTML manipulation
import xml.etree.ElementTree as ET
import re
import io

# Importing libraries for dataverse API
# Documentation found here: https://pydataverse.readthedocs.io/en/latest/
import requests
import pyDataverse.utils as utils
from pyDataverse.api import NativeApi, DataAccessApi

# Importing libraries for file reading and manipulation
import pyreadstat
import json
import pandas as pd


#--------------------USER INTERFACE PARAMETERS

# Background and Font Colours
uni_col = '#FDD44D'
font_col = 'black'
box_col = '#F3F0E6'


# Setting up tkinter window
root = Tk()
root.title('XML UPLOAD VIA API')
root.minsize(1000, 700)
root.resizable(False, False)
root.geometry("1000x700+500+300")
root.configure(bg = uni_col)


# Font Setup
font_setting_1 = ('Baskerville', 20, "bold")
font_setting_2 = ('Baskerville', 14, 'bold')
font_setting_3 = ('Baskerville', 15, 'italic')
font_setting_4 = ('Baskerville', 12, 'bold')
font_setting_5 = ('Baskerville', 20, 'bold')


#----------------------------TEXT VALUES

# Setting up window text values
text_val_1 = "Welcome to the XML upload User Interface!"
text_val_2 = "This UI is used to facilitate the usage of Thierry's code."
text_val_3 = "Please fill ALL fields below to successfully import XML files in Data Explorer!"

text_val_4 = "1) Enter your API key here;"
text_val_5 = "2) Enter the dataset DOI here;"
text_val_6 = "3) Browse for the XML file you wish to upload;"

text_val_7 = 'Currently: No chosen file!'
text_val_8 = "4) Browse for the SPSS file (local .sav file uploaded as a tabular in Borealis)"
text_val_10 = "5) Enter weight variable name;"

text_val_11 = "6) Enter ID variable name;"


#---------------------------LABEL PARAMETERS

# Configurating labels with font, text, and background settings
label_1 = Label(root, text = text_val_1, fg = font_col, bg = uni_col, font = font_setting_1)
label_2 = Label(root, text = text_val_2, fg = font_col, bg = uni_col, font = font_setting_2)
label_3 = Label(root, text = text_val_3, fg = font_col, bg = uni_col, font = font_setting_2)

label_4 = Label(root, text = text_val_4, fg = font_col, bg = uni_col, font = font_setting_2)
label_5 = Label(root, text = text_val_5, fg = font_col, bg = uni_col, font = font_setting_2)
label_6 = Label(root, text = text_val_6, fg = font_col, bg = uni_col, font = font_setting_2)

label_7 = Label(root, text = text_val_7, fg = font_col, bg = uni_col, font = font_setting_4)
label_8 = Label(root, text = text_val_8, fg = font_col, bg = uni_col, font = font_setting_2)
label_9 = Label(root, text = text_val_7, fg = font_col, bg = uni_col, font = font_setting_4)

label_10 = Label(root, text = text_val_10, fg = font_col, bg = uni_col, font = font_setting_2)
label_11 = Label(root, text = text_val_11, fg = font_col, bg = uni_col, font = font_setting_2)


# Placing labels on root window
label_1.place(relx = 0.5, rely = 0.01, anchor = "n")
label_2.place(relx = 0.02, rely = 0.13, anchor = 'w')
label_3.place(relx = 0.02, rely = 0.166, anchor = 'w')

label_4.place(relx = 0.09, rely = 0.24, anchor = 'w')
label_5.place(relx = 0.09, rely = 0.39, anchor = 'w')
label_6.place(relx = 0.09, rely = 0.54, anchor = 'w')

label_7.place(relx = 0.1, rely = 0.64, anchor = 'w')
label_8.place(relx = 0.09, rely = 0.72, anchor = 'w')
label_9.place(relx = 0.1, rely = 0.82, anchor = 'w')

label_10.place(relx = 0.05, rely = 0.89, anchor = 'w')
label_11.place(relx = 0.4, rely = 0.89, anchor = 'w')


#--------------TEXTBOX PARAMETERS AND PLACEHOLDER ENTRIES

entry_1 = Entry(root, font = font_setting_3, fg = font_col, bg = box_col)
entry_1.insert(0, '  e.g.:    caa807d2-c4d3-48fc-a6c3-65f48a1098e9')

entry_2 = Entry(root, font = font_setting_3, fg = font_col, bg = box_col)
entry_2.insert(0, '  e.g.:    doi:10.5683/SP3/MMKTFC    or    https://doi.org/10.5683/SP3/MMKTFC')

entry_3 = Entry(root, font = font_setting_3, fg = font_col, bg = box_col)
entry_3.insert(0, '  e.g.:    FINALWT')

entry_4 = Entry(root, font = font_setting_3, fg = font_col, bg = box_col)
entry_4.insert(0, ' e.g.: CASEID or RECNUM')


# Placing text boxes on root window
entry_1.place(relx = 0.093, rely = 0.29, anchor = 'w', width = 750, height = 40)
entry_2.place(relx = 0.093, rely = 0.44, anchor = 'w', width = 750, height = 40)
entry_3.place(relx = 0.07, rely = 0.945, anchor = 'w', width = 250, height = 40)
entry_4.place(relx = 0.4, rely = 0.945, anchor = 'w', width = 260, height = 40)


#--------------------------BUTTON FUNCTIONS 

# Placeholder filename labels to prevent crashes
filename_1 = ''
filename_2 = ''


# Setting up function called by XML file search button
def browseFiles_1():
    global filename_1
    filename_1 = filedialog.askopenfilename(initialdir = "/", title = "Select an XML File",
                                            filetypes = [("XML files", "*.xml")])
     
    # Change label contents
    label_7.configure(text = filename_1)
    

# Setting up function called by SPSS file search button
def browseFiles_2():
    global filename_2
    filename_2 = filedialog.askopenfilename(initialdir = "/", title = "Select an SPSS File",
                                           filetypes = [("SAV files", "*.sav")])
    
    label_9.configure(text = filename_2)


# Setting up function called by RUN SCRIPT button
def run_script():
    
    api_token_origin = entry_1.get()
    doi = entry_2.get()
    
    if "https://doi.org/" in doi:
        doi = doi.replace("https://doi.org/", "doi:")
    #print(doi)

    xml_template = filename_1
    sav_directory = filename_2
    weight_var = entry_3.get()
    omission = entry_4.get()
    
    row_val = [weight_var, omission, sav_directory, xml_template, api_token_origin]
    print(row_val[0])
    print(row_val[1])
    print(row_val[2])
    print(row_val[3])
    print(row_val[4])
    
    root.destroy()
    backend_processes(doi, row_val)
    
    print("PROCESS DONE!")
    
    
#------------------------------BUTTON PARAMETERS

file_button_1 = Button(root, text = "Upload XML File", font = font_setting_3, 
                       bg = box_col, command = browseFiles_1)

file_button_2 = Button(root, text = "Upload SPSS File", font = font_setting_3, 
                       bg = box_col, command = browseFiles_2)

run_backend = Button(root, text = "RUN SCRIPT", font = font_setting_5,
                     bg = '#C42700', fg = 'white', command = run_script)

# Placing buttons on root window
file_button_1.place(relx = 0.1, rely = 0.59, anchor = 'w', width = 300, height = 40)
file_button_2.place(relx = 0.1, rely = 0.77, anchor = 'w', width = 300, height = 40)
run_backend.place(relx = 0.96, rely = 0.9, anchor = 'e', width = 260, height = 90)


#----------------------- ACTUAL BACKEND

def check_lock(dataset_id, row_val):
    
        api_token_origin = row_val[4]                                            # Enter API key as string
        url_base_origin = 'https://borealisdata.ca'                              # Input base origin url as string
        headers_origin = {'X-Dataverse-key': api_token_origin}                   # Create dictionary and insert API token as the value
        api_origin = NativeApi(url_base_origin, api_token_origin)                # API call using the pyDataverse
        data_api_origin = DataAccessApi(url_base_origin, api_token_origin)        
    
        time_start = datetime.now()                                                     # Set up internal timer
        print("Start check_lock")                                                       # Print start message
	
        try:
            url = f"{url_base_origin}/api/datasets/{dataset_id}/locks"                  # Set up URL for access
            lock = requests.get(url, headers_origin)                                    # Set up lock status
	
            if lock.status_code == 503:                                                 # If URL is unavailable
                    print("503 - Server is unavailable")                                # Print status
                    sys.exit()                                                          # stop running the function

            a = 0
            while len(lock.json()['data']) > 0:
                print(f"Lock {str(a)} times {dataset_id} {lock.json()}")                # API returns jason file of all locked datasets
                print(lock.json())                                                      # Print lock information
                time.sleep(10)                                                          # Start a 10 second timer
                a += 1                                                                  # Update attempt tracker

                lock = requests.get(url, headers_origin)                                # Check lock status
                if lock.status_code == 503:                                             # If URL is unavailable
                    print("503 - Server is unavailable")                                # Print status
                    sys.exit()                                                          # Stop running the function

                if lock.status_code != 200:                                                                 # If URL status code is not 200 (not successful)
                    print(f"check_lock func: lock status {str(lock.status_code)} for {dataset_id}")         # Print lock information
                    return False                                                                            # Return False

        except Exception as e:                                                          # This exception parameter prevents unwanted crashes or errors.
            print(f"check_lock. Error {str(e)}, dataset {dataset_id} ")                 # Print lock information
            return False                                                                # Return False

        time_end = datetime.now()                                                       # Provide date and time
        t = (time_end - time_start)                                                     # Give total time taken to ingest dataset
        print(f"Dataset {str(dataset_id)} was locked {str(t.total_seconds())} sec")     # Provide dataset information
	
        return True      


def backend_processes(doi, row_val):
    
    api_token_origin = row_val[4]                                                 # Enter API key as string
    url_base_origin = 'https://borealisdata.ca'                                   # Input base origin url as string
    headers_origin = {'X-Dataverse-key': api_token_origin}                             # Create dictionary and insert API token as the value
    api_origin = NativeApi(url_base_origin, api_token_origin)                          # API call using the pyDataverse
    data_api_origin = DataAccessApi(url_base_origin, api_token_origin)
    
    
    resp = api_origin.get_dataset(doi)
    
    if resp.status_code == 200:                                               # If API call is successful (marker 200)
        id = resp.json()['data']['id']                                        # old dataset ID is assigned to variable id
        latest_version = resp.json()['data']['latestVersion']                 # Latest old dataset version is set to variable list "latest_version"
    
        files = latest_version['files']                                       # old file latest version is set to variable list 'files'
        dataset_id = latest_version['datasetId']

        
        for file in files:                                                    # For loop running curl commands to create new dataset version?
            dataFile = file['dataFile']                                       # Assigns file name to a variable.
    
            if dataFile['contentType'] == 'text/tab-separated-values':        # If the file name finishes by .tab
                tab_id_old = dataFile['id']                                   # Assign file ID to 'tab_id_old'
                print(dataFile)
                print(tab_id_old)
    
                tab_xml = get_var_metadata_dataverse(id, tab_id_old, row_val)          # Get variable metadata from the dataverse record
                print(tab_xml)

                if tab_xml != False and tab_xml is not None:                  # If the newly created file is NOT empty - meaning it successfully pulled content in get_var_metadata_dataverse()
                    result = re.search(r'{((.*))}', tab_xml.tag)              # Using regex library to capture and group all instances of the html/XML tag <ns:0>
    
                    if result == None:                                        # If 'result' from the above if statement is empty
                        ns_var = ''                                           # Assign an empty string to 'ns_var'
    
                    else:                                                     # Else, if result is populated
                        ns_var = result.group(0)                              # Assign ns:0 to the variable 'ns_var'
    
                    dataDscr = tab_xml.find(f"{ns_var}dataDscr")
                    xml = ET.ElementTree(dataDscr)
    
                    weight_formatter(row_val, ns_var, xml, dataset_id, tab_id_old)        
    



def weight_formatter(row_val, ns_var, xml, dataset_id, tab_id_old):
    
    api_token_origin = row_val[4]                                                 # Enter API key as string
    url_base_origin = 'https://borealisdata.ca'                                   # Input base origin url as string
    headers_origin = {'X-Dataverse-key': api_token_origin}                             # Create dictionary and insert API token as the value
    api_origin = NativeApi(url_base_origin, api_token_origin)                          # API call using the pyDataverse
    data_api_origin = DataAccessApi(url_base_origin, api_token_origin)
    
    
    weight_var = row_val[0]                                                         # Assigning CSV file weight variable to the variable weight_var
    omission = row_val[1]                                                           # Assigning CSV file weight omissions to the variable 'omission'

    vars = xml.findall(f'{ns_var}var')                                              # Create a list of variables.

    for var in vars:                                                                # For all variables in the vars list
        var_name = var.attrib.get("name")                                           # Assigning eTree attribute name to var_name
        if var_name == weight_var:                                                  # If the variable name is that of the weight variable
            var.attrib['wgt'] = 'wgt'                                               # Assign it as the weight variable
            weight_id = var.attrib.get('ID')                                        # Assign the variable id to the variable weight_id
    
    for var in vars:                                                                # For all variables in the vars list
        var_name = var.attrib.get('name')                                           # Create list of vars.
        if var_name != omission and var_name != weight_var:                         # If the var name is not a to-be omitted (not-weighted) variable or the weight variable
            var.attrib['wgt-var'] = weight_id                                       # Assign to 'wgt-var' the weight variable ID (e.g. v1432609)

    main_dict = {}                                                                  # Create an empty dictionary
    for var in xml.findall(f'{ns_var}var'):                                         # For every variable in the XML file
        var_name = var.attrib.get('name')                                           # Assign eTree attribute 'name' to the variable var_name
        category_data = {}                                                          # Create a new empty dictionary inside the for loop

        for catgry in var.findall(f'{ns_var}catgry'):                               # For every variable category
            labl_element = catgry.find(f'{ns_var}labl')                             # fetch the label element and assign it to the variable labl_element
            print(f'HERE ARE THE LABEL ELEMENTS: {labl_element}')

            if labl_element is not None:                                            # If the label is not empty
                label = labl_element.text                                           # Assign its name to the variable 'label'
                frequency_value = catgry.find(f'{ns_var}catStat')                   # Extract the frequency value of the category statistic

                if frequency_value is not None:                                     # If the extracted category frequency is not empty/Null
                    frequency = frequency_value.text                                # Assign the frequency value to the variable 'frequency'
                    category_data[label] = [frequency]

        main_dict[var_name] = category_data                                         # Add the variable name as the main dictionary key, and the previously created dictionary as its value

    print(main_dict)                                                                # Print the main dictionary
    updated_dictionary = calculate_weights(row_val, main_dict)                          # Assign the result of the function 'calculate weights' to the variable 'updated_dictionary'
    print(updated_dictionary)                                                       # Print the dictionary returned from the above function

    for var in xml.findall(f'{ns_var}var'):                                                 # For every variable in the XML file
        var_name = var.attrib.get('name')                                           # Assign eTree attribute 'name' to the variable var_name

        if var_name in updated_dictionary:                                          # for variable keys in the updated dictionary
            if updated_dictionary[var_name] != {}:                                  # If the updated dictionary variable is not an empty dictionary

                for catgry in var.findall(f'{ns_var}catgry'):                       # For all the categories in the variable subset
                    labl_element = catgry.find(f'{ns_var}labl')                     # Extract the category label

                    if labl_element is not None:                                    # If the label is not empty
                        label = labl_element.text                                   # Assign the label the variable 'label'
                        print(f'THIS IS THE LABEL: {label}')
                        val = updated_dictionary[var_name][label]                   # Fetches the list value of the category
                        print(f'THIS IS VAL: {val}')
                        new_entry = ET.Element(f'{ns_var}catStat')                  # Create a new element location
                        new_entry.set('type', 'freq')                               # Create necessary attribute documentation for the element
                        new_entry.set('wgtd', 'wgtd')                               # Create necessary attribute documentation for the element
                        new_entry.set('wgt-var', weight_id)

                        if len(val) == 1:                                           # if the length of the list value is 1 in length (meaning the numerical text value is 0)
                            new_entry.text = str(val[0])                            # Reuse value 0
                        else:                                                       # Otherwise
                            new_entry.text = str(val[1])                            # Use index 1 to fetch the weighted frequency

                        catgry.append(new_entry)                                    # Append new element as a subelement of the category


    updated_xml = xml.getroot()                                                     # Return to the XML file root
    newest_xml = new_groups(updated_xml, ns_var, row_val)

    namespace = 'http://www.icpsr.umich.edu/DDI'
    new_parent = ET.Element(f"{{{namespace}}}codeBook", version="2.0")
    new_parent.append(newest_xml)

    xml_string = ET.tostring(new_parent, encoding='utf8', method='xml').decode('utf8')               # Setup xml as a string (must be a string to push to dataverse)
    xml_string = xml_string.replace('ns0:', '')

    var_update_dataset(dataset_id, tab_id_old, xml_string, row_val)



def calculate_weights(row_val, main_dict):

    weight_var = row_val[0]                                 # Assigning CSV file weight variable to the variable weight_var
    omission = row_val[1]                                   # Assigning CSV file weight omissions to the variable 'omission'
    print(weight_var)
    print(omission)

    filename = row_val[2]
    print(filename)

    df = pd.read_spss(filename)
    print(df.head())

	
    variable_list = []                                                              # Creating and empty list
    for col in df:                                                                  # For columns in the dataframe
        if col != weight_var and col != omission:                                   # If the column name is not that of the weight variable or omitted variables
            variable_list.append(col)                                               # Add it to variable_list

    x = 1
    for key in main_dict:                                                           # For keys in the main dictionary
        if key in variable_list:                                                    # If the key is in the list of variables
            
            print(f'{x} out of {len(variable_list)}')
            print(key)
            print()
            weighted_df = df.groupby([key], observed = False)[weight_var].sum().reset_index()       # Collapse and sum all FINALWT values as a function of category

            for index, row in weighted_df.iterrows():                               # For columns and rows in the newly created weighted_df dataframe
                label = row[key]                                                    # Category label is fetched by parsing through the dataframe column and finding
                frequency = row[weight_var]                                         # Weighted frequency is extracted from the corresponding category row

                if label in main_dict[key]:                                         # If the label is in the main dictionary category dictionary
                    main_dict[key][label].append(frequency)                         # Append the weighted frequency next to the corresponding non-weighted frequency.
            x += 1

    return main_dict                                                                # Return the updated main_dict



def new_groups(updated_xml, ns_var, row_val):
    
    api_token_origin = row_val[4]                                                 # Enter API key as string
    url_base_origin = 'https://borealisdata.ca'                                   # Input base origin url as string
    headers_origin = {'X-Dataverse-key': api_token_origin}                             # Create dictionary and insert API token as the value
    api_origin = NativeApi(url_base_origin, api_token_origin)                          # API call using the pyDataverse
    data_api_origin = DataAccessApi(url_base_origin, api_token_origin)
    
    template = ET.parse(row_val[3])                                                 # Parsing XML file used as template
    template_root = template.getroot()                                              # Setting up etree root
    namespaces = {'ddi': 'http://www.icpsr.umich.edu/DDI'}                          # Defining the namespace dictionary - this seems to be mandatory when we import an XML proper (not necessary when extracted from dataverse)

    grouping = updated_xml.findall(f'{ns_var}varGrp')                               # Creating list of all variable groups currently existing in the current file xml
    for grp in grouping:                                                            # For every variable group in the list of variable groups
        updated_xml.remove(grp)                                                     # Delete the group from the XML record

    x = 0                                                                                    # Create an index variable ======= Note: x starts 0 - that way var groups appear at the top of the XML record under dataDscr (relevant later)
    vars = updated_xml.findall(f'{ns_var}var')                                               # From the file XML, retrieve and list all variables
    groups_template = template_root.findall('ddi:dataDscr/ddi:varGrp', namespaces)           # From the etree template, retrieve and list all variable groups

    for group in groups_template:
        labl_element = group.find('ddi:labl', namespaces)                           # Retrieve the label of the variable using its ID

        if labl_element is not None:                                                # If the label is not empty (it shouldn't ever be empty to be honest)
            label = labl_element.text                                               # Assign the text value to the variable "label"

        variables_template = group.attrib.get('var')                                # Retrieve the variable IDs (all in a same string) from the variable group
        
        try:
            var_grp_template = variables_template.split(' ')                        # List all variables in the string by delineating them at spaces
        except:
            pass

        group_list_template = []                                                      # Create an empty list
        variable_name = template_root.findall('ddi:dataDscr/ddi:var', namespaces)     # List all variables found in the template

        for ids in var_grp_template:                                                # for variable IDs in the variable groups
            for var in variable_name:                                               # For the variables in the variable name list
                tex_val = var.attrib.get('ID')                                      # Assigns the ID to the variable tex_val
                if ids == tex_val:                                                  # If the ID the loop is parsing through is the same as tex_val
                    group_list_template.append(var.attrib.get('name'))              # Add the variable name to group_list

        new_id_list = []                                                            # Create an empty list that will hold IDs
        for var in vars:                                                            # for all variables pulled from the current dataverse record
            var_name = var.attrib.get('name')                                       # Assign the variable name to var_name
            if var_name in group_list_template:                                     # If the pulled variable name appears in the template group list
                new_id_list.append(var.attrib.get('ID'))                            # Add the ID from the dataverse record to new_id_list


        string_setup = " ".join(new_id_list)                                        # Create a list holding the list items (joined at spaces)
        print(string_setup)                                                         # This is optional - good for comparing to an XML record

        group_entry = ET.Element(f'{ns_var}varGrp')                                 # Here we create the new element to be added in the dataverse XML record
        group_entry.set('ID', group.attrib.get('ID'))                               # Create necessary attribute documentation for the element
        group_entry.set('var', string_setup)                                        # Create necessary attribute documentation for the element
        print(ET.tostring(group_entry))                                             # Print the to-be added varGrp entry

        group_label = ET.SubElement(group_entry, 'labl')                            # Create a subelement for the above group entry, name it labl (this follows DDI standards)
        group_label.text = label                                                    # Label text value is set to the name of the group (pulled from the XML template earlier)
        print(ET.tostring(group_label))                                             # Print the to-be added labl subelement

        updated_xml.insert(x, group_entry)                                          # Insert the created group entry at index x - note that group_label is automatically added as a subelement of the group entry
        x += 1                                                                      # Update index parser by one (otherwise the groups are added in descending order)

    return updated_xml 




def var_update_dataset(dataset_id, datafile_id, xml, row_val):
    
    api_token_origin = row_val[4]                                                 # Enter API key as string
    url_base_origin = 'https://borealisdata.ca'                                   # Input base origin url as string
    headers_origin = {'X-Dataverse-key': api_token_origin}                             # Create dictionary and insert API token as the value
    api_origin = NativeApi(url_base_origin, api_token_origin)                          # API call using the pyDataverse
    data_api_origin = DataAccessApi(url_base_origin, api_token_origin)    
    
    
    print("Start var_update_dataset")
    url = f'{url_base_origin}/api/edit/{str(datafile_id)}'                          
    check = check_lock(dataset_id, row_val)                                         # Assign check_lock function return to the variable 'check'
    if check == False:                                                              # If check_lock returns False
        return check                                                                # Return False (?)

    try:
        resp = requests.put(url, headers=headers_origin, data = xml)                # Fetch request information, assign to the variable 'resp'
        #print(resp.status_code())
        if resp.status_code != 200:                                                 # If access is unsuccessful
            print(resp.json())                                                      # Print failure information
            return False                                                            # Return False
        else:                                                                       # If access is successful
            print("Updated")                                                        # Print status

    except Exception as e:                                                          # In the event of an exception (not sure when this actually happens)
        print(f"var_update_dataset: {str(e)} {url}")                                # print url related to the exception
        return False                                                                # Return False

    return True   



def get_var_metadata_dataverse(dataset_id, datafile_id, row_val):
    
    api_token_origin = row_val[4]                                                 # Enter API key as string
    url_base_origin = 'https://borealisdata.ca'                                   # Input base origin url as string
    headers_origin = {'X-Dataverse-key': api_token_origin}                             # Create dictionary and insert API token as the value
    api_origin = NativeApi(url_base_origin, api_token_origin)                          # API call using the pyDataverse
    data_api_origin = DataAccessApi(url_base_origin, api_token_origin)        

	
    print("Start get_var_metadata_dataverse")
    lock = check_lock(dataset_id, row_val)                                          # Checks if dataset is locked with the function 'check_lock()'
    url = url_base_origin                                                           # Assigns previously defined url origin to the variable 'url'

    if lock:                                                                        # if able to access the url -------------------- Dataset must not be in draft prior to this, it kept crashing for me if it was
        url = f"{url}/api/access/datafile/{datafile_id}/metadata"                   # assign new url to the 'url' variable
        resp = requests.get(url, headers=headers_origin)                            # Assign access information to the variable 'resp'

        if resp.status_code == 200:                                                 # If access is successful
            tree = ET.fromstring(resp.content)                                      # Assign string json() data to tree (creates a new json?)
            return tree

        else:                                                                                                            # If access code is not 200
            print(f"get_var_metadata_dataverse: dataset_id = {dataset_id} datafile_id = {datafile_id} url = {url}")      # Print assigned variables
            return False

    else:                                                                                                                          # If the url is locked (this could be for various different reasons)
        print(f"get_var_metadata_dataverse: dataset_id = {dataset_id} datafile_id = {datafile_id} url ={url} locking problem")     # Print an error message
        return False


#-------------------- RUNNING STUFF

root.mainloop()
