# import module
import streamlit as st
import streamlit_option_menu as opt     # navigation menu adjustment
import pandas as pd
import requests     # json request

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
        icons=["person-lines-fill", "arrow-up-square", "patch-question"],    # optional icon for each options
        menu_icon=["cast"],   # optional icon for menu_title
        default_index=0   # optional, to select default page
    )

# Employee Pay Forecast Page
if selected == "For Individual":
    st.title("Bonus Prediction")
    # st.markdown("Bonus may be awarded by company to act as incentives or reward to good performer.\
    # Company can award them through several ways, such as cash, stock, and stock options.")
    #st.markdown("")
    st.markdown("Please fill in all required information marked with (*) to proceed with personal bonus prediction for \
    upcoming year.")

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
        company = st.selectbox("Company Name*", ["--Please select--", 'Apple', 'Microsoft', 'Google', 'Oracle',
                                                 'Adobe', 'Salesforce', 'IBM', 'SAP', 'Intuit', 'ADP',
                                                 'Schneider Electric', 'ServiceNow', 'VMWare', 'Synopsys',
                                                 'Dassault Systemes', 'Snowflake', 'Cadence Design Systems',
                                                 'Workday', 'Palo Alto Networks', 'Autodesk', 'Fortinet',
                                                 'Atlassian', 'Keysight', 'Wolters Kluwer', 'Veeva Systems',
                                                 'Amadeus', 'CrowdStrike', 'DataDog', 'The Trade Desk', 'Ansys',
                                                 'Zoom', 'EPAM Systems', 'Paycom', 'Zscaler', 'FICO', 'FactSet',
                                                 'leidos', 'PTC', 'Cloudflare', 'Splunk', 'HubSpot', 'Akamai',
                                                 'Tyler Technologies', 'MongoDB', 'SS&C Technologies',
                                                 'Zebra Technologies', 'Palantir', 'NetApp', 'Nice', 'Trimble',
                                                 'Zoominfo', 'Amdocs', 'Dynatrace', 'Unity Technologies',
                                                 'DocuSign', 'Paylocity', 'Okta', 'Zendesk', 'Ceridian', 'Sage',
                                                 'Toast', 'Genpact', 'F5 Networks', 'Twilio', 'Dropbox',
                                                 'OpenText', 'Xero', 'Globant', 'UiPath', 'Trend Micro',
                                                 'GitLab', 'Procore', 'Coupa', 'Confluent', 'Samsara',
                                                 'Nutanix',
                                                 'Qualtrics', 'Clearwater Analytics', 'Telus', 'SmartSheet',
                                                 'HashiCorp', 'KPMG', 'EY', 'PwC', 'Deloitte', 'BCG',
                                                 'Mckinsey & Company', 'Goldman Sachs', 'Facebook', 'Other'],
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
    #basesalary_output = st.write("Base Salary: ", basesalary)
    stockgrantvalue = st.number_input("Stock Grant Value ($)*",
                                min_value=0, max_value=1000000, step=1000,
                                key="stockgrantvalue")
    #stock_grant_output = st.write("Stock Grant: ", stockgrantvalue)
    bonus = st.number_input("Bonus($)*",
                      min_value=0, max_value=1000000, step=1000,
                      key="bonus")
    #bonus_output = st.write("Bonus: ", bonus)
    totalyearlycompensation = int(basesalary) + int(bonus) + int(stockgrantvalue)
    st.metric("Your total yearly compensation is $", totalyearlycompensation)

    # if mandatory fields not all filled in, take no action
    # else, proceed with data submission to backend for data pre-processing after clicking submit button
    # display output from ML model
    if gender and Education and Race and country and company and state and title and yearsofexperience and\
        yearsatcompany and basesalary and totalyearlycompensation is not None:
        if st.button(label="Submit"): #on_click=form_callback())
            # Inputs to ML model
            inputs = {
                "inputs": [
                    {
                        "gender": [
                            'Female',
                            'Male',
                            'Other'
                        ],
                        "Race": [
                            'Asian',
                            'Black',
                            'Hispanic',
                            'Two Or More',
                            'White'
                        ],
                        "Education": [
                            "Bachelor's Degree",
                            'Highschool',
                            "Master's Degree",
                            'PhD',
                            'Some College'
                        ],
                        "country": [
                            'Belarus', 'Belgium', 'Brazil', 'Bulgaria', 'Chile', 'Colombia', 'Costa Rica', 'Czech Republic',
                            'Denmark', 'Egypt', 'Estonia', 'Finland', 'France', 'Ghana', 'Hungary', 'Indonesia', 'Italy',
                            'Japan', 'Kazakhstan', 'Kenya', 'Latvia', 'Lithuania', 'Luxembourg', 'Malaysia', 'Mexico',
                            'Moldova', 'New Zealand', 'Nigeria', 'Norway', 'Peru', 'Philippines', 'Poland', 'Portugal',
                            'Qatar', 'Romania', 'Saudi Arabia', 'Serbia', 'Slovakia', 'South Africa', 'Spain', 'Sweden',
                            'Switzerland', 'Taiwan', 'Thailand', 'Ukraine', 'United Arab Emirates', 'Uzbekistan', 'Vietnam',
                            'Argentina', 'Armenia', 'Australia', 'Austria', 'Canada', 'China', 'Germany', 'Hong Kong (SAR)',
                            'India', 'Ireland', 'Israel', 'Netherlands', 'Russia', 'Singapore', 'South Korea', 'US',
                            'United Kingdom'
                        ],
                        "state": [
                            ' AA', ' AB', ' AC', ' AL', ' AN', ' AP', ' AR', ' AU',
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
                            ' WV', ' WY', ' ZH', ' ZJ'
                        ],
                        "company": [
                            'Apple', 'Microsoft', 'Google', 'Oracle',
                            'Adobe', 'Salesforce', 'IBM', 'SAP', 'Intuit', 'ADP',
                            'Schneider Electric', 'ServiceNow', 'VMWare', 'Synopsys',
                            'Dassault Systemes', 'Snowflake', 'Cadence Design Systems',
                            'Workday', 'Palo Alto Networks', 'Autodesk', 'Fortinet',
                            'Atlassian', 'Keysight', 'Wolters Kluwer', 'Veeva Systems',
                            'Amadeus', 'CrowdStrike', 'DataDog', 'The Trade Desk', 'Ansys',
                            'Zoom', 'EPAM Systems', 'Paycom', 'Zscaler', 'FICO', 'FactSet',
                            'leidos', 'PTC', 'Cloudflare', 'Splunk', 'HubSpot', 'Akamai',
                            'Tyler Technologies', 'MongoDB', 'SS&C Technologies',
                            'Zebra Technologies', 'Palantir', 'NetApp', 'Nice', 'Trimble',
                            'Zoominfo', 'Amdocs', 'Dynatrace', 'Unity Technologies',
                            'DocuSign', 'Paylocity', 'Okta', 'Zendesk', 'Ceridian', 'Sage',
                            'Toast', 'Genpact', 'F5 Networks', 'Twilio', 'Dropbox',
                            'OpenText', 'Xero', 'Globant', 'UiPath', 'Trend Micro',
                            'GitLab', 'Procore', 'Coupa', 'Confluent', 'Samsara',
                            'Nutanix',
                            'Qualtrics', 'Clearwater Analytics', 'Telus', 'SmartSheet',
                            'HashiCorp', 'KPMG', 'EY', 'PwC', 'Deloitte', 'BCG',
                            'Mckinsey & Company', 'Goldman Sachs', 'Facebook', 'Other'
                        ],
                        "title": [
                            'Business Analyst', 'Data Scientist',
                            'Hardware Engineer', 'Human Resources', 'Management Consultant',
                            'Marketing', 'Mechanical Engineer', 'Product Designer',
                            'Product Manager', 'Recruiter', 'Sales', 'Software Engineer',
                            'Software Engineering Manager', 'Solution Architect',
                            'Technical Program Manager'
                        ],
                        "yearsofexperience": yearsofexperience,
                        "yearsatcompany": yearsatcompany,
                        "basesalary": basesalary,
                        "stockgrantvalue": stockgrantvalue,
                        "bonus": bonus,
                        "totalyearlycompensation": totalyearlycompensation
                    }
                ]
            }
            # Posting inputs to ML API
            response = requests.post(f"http://34.200.183.255:5000/predict",
                                     json=inputs,
                                     verify=False)

            if response.status_code == 200:
                # ori code
                # prediction = class_values[json_response.get("predictions")[0]]

                json_response = response.json()

                # modified code
                prediction = json_response.get("predictions")[0]
                prediction = prediction.content.decode()
                st.subheader(f"Your predicted upcoming bonus is **{prediction}!**")
            else:
                # display returned error code if not 200 is returned
                st.error("Error: {}".format(response.status_code))
        else:
            st.stop()
    else:
        st.stop()

# Data Upload Page for Bulk Data Processing
if selected == "Bulk Data Processing":
    st.title("Bulk Bonus Prediction")
    st.markdown("**Step 1**: Please fill in all required information marked with (*) to proceed with file submission.")
    st.markdown("**Step 2**: Kindly review the uploaded file before you click on *Submit* button to prevent receiving unnecessary \
    file submission notification email.")
    # Create form fields
    email = st.text_input("Email Address*", key="email")

    # File Type Configuration
    supported_file_type = ["csv"]

    # create file upload with default dataset
    uploaded_file = st.file_uploader("Select your local CSV file*",
                                     type=supported_file_type,
                                     accept_multiple_files=False,
                                     key="data")
    # if no data file is uploaded, use default df as df
    if email and uploaded_file is not None:
        uploaded_df = pd.read_csv(uploaded_file)
        # Display the top 15 rows of uploaded data
        st.write(uploaded_df.head(10))
        # send POST request to backend when all mandatory fields are filled in
        if st.button(label="Submit"):
            data = {"email": email,
                    "data": uploaded_df.to_csv(index=False)  # TBC whether to add in index=False into bracket
                    }
            headers = {
                # configuration to decide how we transmit the data to backend
                # ref page: https://reqbin.com/req/python/xpcr0cv3/client-request-with-content-type-header
                "Content-Type": "application/json"
            }

            # send a POST request to the backend with the file contents
            r = requests.post("http://34.200.183.255/upload_csv",
                              # "http://localhost:8501/",
                              data=data,
                              headers=headers)
            #  check the response from backend
            if r.status_code == 200:
                st.success("Your file has been successfully uploaded!", icon="✅")
            else:
                # display returned error code if not 200 is returned
                st.error("Error: {}".format(r.status_code))
        else:
            st.stop()


# About Us
if selected == "About Us":
    # Title
    st.title("About Us")

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


