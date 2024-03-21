# Extract to IMPRESSION and FINDING section
# files : 121,241
import re
import os
import csv

# Extract to IMPRESSION and FINDINGS section in REPORT
def report_extract_section(content):
    # dictionary "impression" and "findings" 
    sections = {}
    
    # search for IMPRESSION section
    impression_match = re.search(r'FINAL REPORT.*?IMPRESSION:(.*?)(?=NOTIFICATION:|$)', content, re.DOTALL)
    # search for FINDINGS section
    findings_match = re.search(r'FINAL REPORT.*?FINDINGS:(.*?)(?=IMPRESSION:|$)', content, re.DOTALL)

    if impression_match:
        impression_section = impression_match.group(1).strip().replace('\n',' ')
        
        # extract to content of IMPRESSION section 
        sections['impression'] = impression_section
    else:
        sections['impression'] = None

    if findings_match:
        findings_section = findings_match.group(1).strip().replace('\n',' ')
        
        # extract to content of FINDINGS section
        sections['findings'] = findings_section
    else:
        sections['findings'] = None
    
    return sections

# list file has only FINDINGS and IMPRESSION section
file_list_path = "pure_both_findings_and_impression_list.txt"
with open(file_list_path, "r") as file:
    file_names = file.readlines()
    file_names = [f.strip() for f in file_names]

# IMPRESSION section save to './both_impression/'
impression_dir = './both_impression/'
# FINDINGS section svae to './both_finding/'
findings_dir = './both_findings/'

# Check directories exist
if not os.path.exists(impression_dir):
    os.makedirs(impression_dir)
if not os.path.exists(findings_dir):
    os.makedirs(findings_dir)

# Process each file
for file_name in file_names:
    # Original report file in "./collection/"
    file_path = os.path.join("./collection/",file_name+'.txt')
    try:
        # Read the content of the current file
        with open(file_path, "r") as file:
            content = file.read()
        
        # Extract content in REPORT
        sections = report_extract_section(content)

        # Check and save FINDING section to CSV
        if sections['finding'] == "":
            print(f"Finding section is missing in {file_name}")
        else:
            csv_finding_file_name = os.path.join(findings_dir, file_name.split('.')[0] + "_finding.csv")
            with open(csv_finding_file_name, "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Report Finding"])
                csv_writer.writerow([sections['finding']])

        # Check and save IMPRESSION section to CSV
        if sections['impression'] == "":
            print(f"Impression section is missing in {file_name}")
        else:
            csv_impression_file_name = os.path.join(impression_dir, file_name.split('.')[0] + "_impression.csv")
            with open(csv_impression_file_name, "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Report Impression"])
                csv_writer.writerow([sections['impression']])
                
    # If not found File, avoid to ERROR
    except FileNotFoundError:
        print(f"File {file_name} not found.")
