# import module
import streamlit as st
import streamlit_option_menu as opt     # navigation menu adjustment
import pandas as pd
import requests     # form-data request
import time

# Page Title
st.set_page_config(page_title="WQD7008 - GP")

# Side Bar Menu Section
with st.sidebar:
    selected = opt.option_menu(
        menu_title="Main Menu",  # None == no specified naming for menu title
        options=["Home", "About Us"],  # List of available sidebar option
        icons=["house", "box-arrow-down-right"],    # optional icon for each options
        menu_icon=["cast"],   # optional icon for menu_title
        default_index=0   # optional, to select default page
    )

# Home Page that support data upload
if selected == "Home":
    st.title("Upload of Data File")
    st.markdown("Please fill in all required information marked with * for to proceed with file submission.")

    # Create the form
    with st.empty():
        st.form(key="access_timestamp")

    # Create form fields
    name = st.text_input("Name*", key = "name")
    email = st.text_input("Email Address*", key = "email_add")

    # File Type Configuration
    supported_file_type = ["csv"]
    # Create the file uploaded
    uploaded_file = st.file_uploader("Choose a file*",
                                    type=supported_file_type,
                                    accept_multiple_files=False,
                                    key = "data")

    # Load the csv into dataframe
    if uploaded_file is not None:
        # To read file as dataframe:
        df = pd.read_csv(uploaded_file)  # not sure should add in "caption=uploaded_file.name"

        # perform data transformation
        # tbc

        # Display the top 5 rows of uploaded data
        st.write(df.head())

        # Submission Result
        if st.button("Submit", key="submittion_timestamp", disabled=False):
            # Check if all the mandatory fields are filled in
            if name == "" or email == "":
                st.error("Please fill in all the mandatory fields.")
            else:
                # send POST request to backend when all mandatory fields are filled in
                data = {
                    "name": name,
                    "email_add": email,
                    "data": df.to_csv(index=False)  # TBC whether to add in index=False into bracket
                }
                headers = {
                    # configuration to decide how we transmit the data to backend
                    # ref page: https://reqbin.com/req/python/xpcr0cv3/client-request-with-content-type-header
                    "Content-Type": "multipart/form-data"
                }

                # send a POST request to the backend with the file contents
                r = requests.post("http://34.200.183.255/upload_csv",
                    #"http://localhost:8501/",
                    data=data,
                    headers=headers)
                #  check the response from backend
                if r.status_code == 200:
                    st.success("Your file has been successfully uploaded!", icon="✅")
                else:
                    # display returned error code if not 200 is returned
                    st.error("Error: {}".format(r.status_code))
    else:
        st.button(label = "Submit", disabled=True)

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
