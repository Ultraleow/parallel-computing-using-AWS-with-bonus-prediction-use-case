# import module
import streamlit as st
import streamlit_option_menu as opt  # navigation menu adjustment
from pandas import read_csv
import requests  # handle form-data req and resp
import os  # file path handling

# Page Title
# free favicon web page:
st.set_page_config(page_title="WQD7008 - GP",
                   page_icon=":shark:")

# Side Bar Menu Section
with st.sidebar:
    selected = opt.option_menu(
        menu_title="Main Menu",  # None == no specified naming for menu title
        options=["For Individual", "Bulk Data Processing", "About Us"],  # List of available sidebar option
        # free icons web page: https://icons.getbootstrap.com/
        icons=["person-lines-fill", "arrow-up-square", "patch-question"],  # optional icon for each options
        menu_icon=["cast"],  # optional icon for menu_title
        default_index=0  # optional, to select default page
    )

# Employee Pay Forecast Page
if selected == "For Individual":
    st.title("Bonus Prediction")
    # st.markdown("Bonus may be awarded by company to act as incentives or reward to good performer.\
    # Company can award them through several ways, such as cash, stock, and stock options.")
    # st.markdown("")
    st.markdown("Please fill in all required information marked with (*) to proceed with personal bonus prediction for \
    upcoming year.")

    # Enable this to see session state object
    # "st.session_state object", st.session_state

    st.subheader('Personal Details')
    # segment forms into 2 columns
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender*",
                              ["--Please select--", 'Female', 'Male', 'Other'],
                              index=0,
                              key="gender")
        Education = st.selectbox("Education Level*",
                                 ["--Please select--", "Bachelor's Degree", 'Highschool', "Master's Degree",
                                  'PhD', 'Some College'],
                                 key="Education")
    with col2:
        Race = st.selectbox("Race*",
                            ["--Please select--", 'Asian', 'Black', 'Hispanic', 'Two Or More', 'White'],
                            index=0,
                            key="Race")

    st.subheader('Company Details')
    # segment forms into 2 columns
    col3, col4 = st.columns(2)
    with col3:
        country = st.selectbox("Country*",
                               ["--Please select--", 'Belarus', 'Belgium', 'Brazil', 'Bulgaria', 'Chile',
                                'Colombia',
                                'Costa Rica', 'Czech Republic', 'Denmark', 'Egypt', 'Estonia', 'Finland',
                                'France',
                                'Ghana', 'Hungary', 'Indonesia', 'Italy', 'Japan', 'Kazakhstan', 'Kenya',
                                'Latvia',
                                'Lithuania', 'Luxembourg', 'Malaysia', 'Mexico', 'Moldova', 'New Zealand',
                                'Nigeria',
                                'Norway', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
                                'Saudi Arabia', 'Serbia', 'Slovakia', 'South Africa', 'Spain', 'Sweden',
                                'Switzerland', 'Taiwan', 'Thailand', 'Ukraine', 'United Arab Emirates',
                                'Uzbekistan', 'Vietnam', 'Argentina', 'Armenia', 'Australia', 'Austria',
                                'Canada', 'China', 'Germany', 'Hong Kong (SAR)', 'India', 'Ireland', 'Israel',
                                'Netherlands', 'Russia', 'Singapore', 'South Korea', 'US', 'United Kingdom'],
                               index=0,
                               key="country")
        company = st.selectbox("Company Name*", ["--Please select--", "Apple", "Microsoft", "Google", "Oracle", "Adobe",
                                                 "Salesforce", "IBM", "SAP", "Intuit", "ADP", "Schneider Electric",
                                                 "ServiceNow", "VMWare", "Synopsys", "Dassault Systemes", "Snowflake",
                                                 "Cadence Design Systems", "Workday", "Palo Alto Networks", "Autodesk",
                                                 "Fortinet", "Atlassian", "Keysight", "Wolters Kluwer", "Veeva Systems",
                                                 "Amadeus", "CrowdStrike", "DataDog", "The Trade Desk", "Ansys", "Zoom",
                                                 "EPAM Systems", "Paycom", "Zscaler", "FICO", "FactSet", "leidos",
                                                 "PTC",
                                                 "Cloudflare", "Splunk", "HubSpot", "Akamai", "Tyler Technologies",
                                                 "MongoDB", "SS&C Technologies", "Zebra Technologies", "Palantir",
                                                 "NetApp", "Nice", "Trimble", "Zoominfo", "Amdocs", "Dynatrace",
                                                 "Unity Technologies", "DocuSign", "Paylocity", "Okta", "Zendesk",
                                                 "Ceridian", "Sage", "Toast", "Genpact", "F5 Networks", "Twilio",
                                                 "Dropbox",
                                                 "OpenText", "Xero", "Globant", "UiPath", "Trend Micro", "GitLab",
                                                 "Procore",
                                                 "Coupa", "Confluent", "Samsara", "Nutanix", "Qualtrics",
                                                 "Clearwater Analytics", "Telus", "SmartSheet", "HashiCorp", "KPMG",
                                                 "EY",
                                                 "PwC", "Deloitte", "BCG", "Mckinsey & Company", "Goldman Sachs",
                                                 "Facebook",
                                                 "Other"],
                               index=0,
                               key="company")

    with col4:
        state = st.selectbox("State*",
                             ["--Please select--", ' AA', ' AB', ' AC', ' AL', ' AN', ' AP', ' AR', ' AU',
                              ' AZ', ' BC',
                              ' BE', ' BJ', ' BL', ' BM', ' BR', ' BS', ' BU', ' BW', ' BY', ' CA', ' CE',
                              ' CJ', ' CK',
                              ' CN', ' CO', ' CT', ' CU', ' DA', ' DC', ' DE', ' DF', ' DL', ' DN', ' DS',
                              ' DU', ' EN',
                              ' ER', ' ES', ' FL', ' GA', ' GD', ' GE', ' GJ', ' GT', ' GY', ' HA', ' HB',
                              ' HC', ' HD',
                              ' HE', ' HH', ' HI', ' HK', ' HM', ' HR', ' IA', ' ID', ' IL', ' IN', ' IS',
                              ' JA', ' JH',
                              ' JK', ' JM', ' JS', ' JZ', ' KA', ' KC', ' KD', ' KG', ' KH', ' KK', ' KL',
                              ' KN', ' KS',
                              ' KY', ' LA', ' LD', ' LI', ' LK', ' LO', ' LU', ' LV', ' MA', ' MB', ' MC',
                              ' MD', ' ME',
                              ' MG', ' MH', ' MI', ' MK', ' MM', ' MN', ' MO', ' MS', ' MT', ' MX', ' MY',
                              ' MZ', ' NA',
                              ' NB', ' NC', ' ND', ' NE', ' NH', ' NI', ' NJ', ' NM', ' NS', ' NV', ' NW',
                              ' NY', ' NZ',
                              ' OH', ' OK', ' ON', ' OR', ' OS', ' PA', ' PG', ' PI', ' PM', ' PO', ' PR',
                              ' QC', ' QL',
                              ' RI', ' RM', ' RS', ' SC', ' SF', ' SG', ' SH', ' SJ', ' SK', ' SN', ' SP',
                              ' SR', ' ST',
                              ' SV', ' TA', ' TN', ' TO', ' TP', ' TR', ' TS', ' TT', ' TW', ' TX', ' TY',
                              ' UP', ' UT',
                              ' VA', ' VC', ' VD', ' VE', ' VG', ' VI', ' VL', ' VT', ' WA', ' WB', ' WC',
                              ' WH', ' WI',
                              ' WV', ' WY', ' ZH', ' ZJ'],
                             index=0,
                             key="state")
        title = st.selectbox("Job Title*", ["--Please select--", 'Business Analyst', 'Data Scientist',
                                            'Hardware Engineer', 'Human Resources', 'Management Consultant',
                                            'Marketing', 'Mechanical Engineer', 'Product Designer',
                                            'Product Manager', 'Recruiter', 'Sales', 'Software Engineer',
                                            'Software Engineering Manager', 'Solution Architect',
                                            'Technical Program Manager'],
                             index=0,
                             key="title")
    st.subheader('Working Experience')
    # segment forms into 2 columns
    col5, col6 = st.columns(2)
    with col5:
        yearsofexperience = st.number_input("Total Years of Working Experience*",
                                            min_value=0, max_value=45, step=1,
                                            key="yearsofexperience")

    with col6:
        yearsatcompany = st.number_input("Years at Current Company*",
                                         min_value=0, max_value=45, step=1,
                                         key="yearsatcompany")

    st.subheader('Salary Package')
    basesalary = st.number_input("Base Salary Per Year($)*",
                                 min_value=4000, max_value=900000, step=1000,
                                 key="basesalary")
    totalyearlycompensation = st.number_input("Total Yearly Compensation ($)",
                                              min_value=0, max_value=900000, step=1000,
                                              key = "totalyearlycompensation")

    # if mandatory fields not all filled in, take no action
    # else, proceed with data submission to backend for data pre-processing after clicking submit button
    # display output from ML model
    if gender and Education and Race and country and company and state and title and yearsofexperience and \
            yearsatcompany and basesalary and totalyearlycompensation is not None:
        if st.button(label="Submit"):
            payload = {"company": company,
                       "title": title,
                       "totalyearlycompensation": totalyearlycompensation,
                       "yearsofexperience": yearsofexperience,
                       "yearsatcompany": yearsatcompany,
                       "basesalary": basesalary,
                       "gender": gender,
                       "Race": Race,
                       "Education": Education,
                       "state": state,
                       "country": country}
            #use line right below to print out API content
            #print(st.text(payload))
            files = [

            ]
            headers = {}

            response = requests.request("POST", f"http://34.200.183.255:5000/predict",
                                        headers=headers, data=payload, files=files)

            if response.status_code == 200:
                # modified code
                # 1. define prediction as response returned
                prediction = response.text
                # 2. place prediction amount into output subheader below
                st.text(f"The predicted amount of upcoming bonus is ${prediction}!")
                # clear existing session state
            else:
                # display returned error code if not 200 is returned
                st.error("Error: {}".format(response.status_code))
                print(response.text.encode('utf8'))
        else:
            st.stop()

# Data Upload Page for Bulk Data Processing
if selected == "Bulk Data Processing":

    #"st.session_state object", st.session_state

    st.title("Bulk Bonus Prediction")
    st.markdown("**Step 1**: Please fill in all required information marked with (*) to proceed with file submission.")
    st.markdown("**Step 2**: Kindly review the uploaded file before you click on *Submit* button to prevent receiving \
                unnecessary file submission notification email.")
    # Create form fields
    email = st.text_input("Email Address*", key="email")

    # File Type Configuration
    supported_file_type = ["csv"]
    # Default Path Configuration
    default_path = r"\\home\\ubuntu\\uploaded_file"

    # create file upload with default dataset
    uploaded_file = st.file_uploader("Select your local CSV file*",
                                     type=supported_file_type,
                                     accept_multiple_files=False,
                                     key="data")#,
                                     #on_change=file_converter)

    if email and uploaded_file is not None:
        # write file into project folder
        st.write(os.path.join("tempDir", uploaded_file.name))
        with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        uploaded_df = read_csv(uploaded_file)
        # Display the top 10 rows of uploaded data
        st.write(uploaded_df.head(10))

        # Archive code: upload drive from local directly to backend server
        # failed ~ can't find solution
        # def file_selector(folder_path=default_path):
        #    selected_filename = uploaded_file.name
        #    return os.path.join(folder_path, selected_filename)
        # filename = file_selector()
        # st.write('You selected `%s`' % filename)

        # pass uploaded file via form-data in POST req to backend
        if st.button(label="Submit"):
            # To read file as byte
            # ref link: https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
            #bytes_data = uploaded_file.getvalue()
            #st.write(bytes_data)

            #file = (open(uploaded_file, 'rb'), 'text/csv')

            # POST Req content
            url = "http://34.200.183.255:5000/upload_csv"
            payload = {'email': email}
            # files = [(field_name, (file_name, file_object, content type))]
            files = [
                ('csv_file', (uploaded_file.name, open(os.path.join("tempDir", uploaded_file.name), 'rb'), 'text/csv'))
            ]

            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            print(response.text)
            # close the uploaded file
            uploaded_file.close()
            if response.status_code == 200:
                st.success("Your file has been successfully uploaded!", icon="✅")
                for key in st.session_state.keys():
                    del st.session_state[key]
            else:
                # display returned error code if not 200 is returned
                st.error("Error: {}".format(response.status_code))
                print(response.text.encode('utf8'))
    else:
        st.stop()

# About Us
if selected == "About Us":
    # Title
    st.title("About Us")
    #"st.session_state object", st.session_state

    # Group Member Listing
    st.markdown("Our group is made up of students as below:")

    # create list of name with details
    team_members = [
        {"Name": "Leow Jun Shou", "Matric No": "17123313"},
        {"Name": "Sim Lin Zheng", "Matric No": "S2102170"},
        {"Name": "Rose Tiong", "Matric No": "S2123103"},
        {"Name": "Tang JingFa", "Matric No": "S2141959"},
        {"Name": "Thoo Pooi Luen", "Matric No": "17218141"}
    ]

    # Display the list of names
    st.table(team_members)