# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Welcome to the Data Dashboard! 📊")

# INTRODUCTORY TEXT
st.write("""
This application is designed to collect and visualize data.
You can navigate to the different pages using the sidebar on the left.

### How to use this app:
- **Survey Page**: Go here to input new data into our CSV file.
- **Visuals Page**: Go here to see the data visualized in different graphs.

This project is part of CS 1301's Lab 2.
""")
st.divider()
st.header("List of recognized common names for data entry:")
st.write("- Tree-of-heaven")
st.write("- River birch")
st.write("- Pecan")
st.write("- Eastern redbud")
st.write("- Blue mistflower")
st.write("- Flowering dogwood")
st.write("- Deertongue grass")
st.write("- Annual fleabane")
st.write("- Wild geranium")
st.write("- Wild hydrangea")
st.write("- Winterberry holly")
st.write("- Spicebush")
st.write("- Tulip tree")
st.write("- Sweetbay magnolia")
st.write("- Wax myrtle")
st.write("- Switchgrass")
st.write("- Virginia creeper")
st.write("- Garden phlox")
st.write("- Virginia pine")
st.write("- Plantain")
st.write("- American sycamore")
st.write("- Christmas fern")
st.write("- Pickerelweed")
st.write("- Black cherry")
st.write("- White oak")
st.write("- Cutleaf coneflower")
st.write("- Tall goldenrod")
st.write("- Indiangrass")
st.write("- Common dandelion")
st.write("- American elm")
