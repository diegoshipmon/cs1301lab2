# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.
import json
import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

infile = open("data.json")
mydata = json.load(infile)

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Plant Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Plant Observation Data Collection Survey 📝")
st.write("Please fill out the form below with the plants you observed toda to add your data to the dataset.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    Abundance_input = st.number_input("Please enter the number of plants you observed.", min_value = 2, step = 1)
    value_input = st.text_input("Please enter the common name of the plant you observed. Please be aware that this input is **case sensitive**.")

    submitted = st.form_submit_button("Submit Data")

    if submitted:
        if "data" not in st.session_state:
            st.session_state.data = pd.read_csv("data.csv")
            st.session_state.data = st.session_state.data.drop(columns=["Unnamed: 0"], errors="ignore")
    
        common_name = value_input.strip()
        if common_name in mydata:
                scientific_name = mydata[common_name]["scientific_name"]
                family = mydata[common_name]["family"]
                csr = mydata[common_name]["CSR_strategy"]
                
                species_exists = (st.session_state.data["Common Name"] == common_name)    
                if species_exists.any():
                    st.session_state.data.loc[species_exists, "Abundance"] += Abundance_input
                else:
                    new_row = pd.DataFrame({
                        "Species": [scientific_name],
                        "Common Name": [common_name],
                        "Family": [family],
                        "CSR strategy": [csr],
                        "Abundance": [Abundance_input]})

                    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index = True)
                    
                st.session_state.data = st.session_state.data.drop(columns=["Unnamed: 0"], errors="ignore")
                st.session_state.data.to_csv("data.csv", index = False)
                st.success("Your data has been submitted!")
                st.write(f"You entered species name: **{value_input}**. This plant was observed: **{Abundance_input} times**")
        else:
            st.error(f"{common_name} is not available in the species dictionary. Please try another plant!")
        
        


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")

if st.button("Clear All Data"):
    
    st.session_state.data = pd.DataFrame(columns=[
        "Species",
        "Common Name",
        "Family",
        "CSR strategy",
        "Abundance"
    ])

    st.session_state.data.to_csv("data.csv", index=False)

    st.success("Plant data all cleared! Reload the page or submit a new entry to view the new table.")
