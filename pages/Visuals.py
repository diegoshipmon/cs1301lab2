import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
    page_title="Visualize Data",
    page_icon="🔍",
)

st.title("Plant Data Visualizations 🔍")
st.write("Use this page to visualize the ecological dynamics of your site! CSR strategy and taxonomic family are both strong tools to understand a plant's role in the environment")
st.divider()

st.header("Charts from Current Data in CSV")
data = pd.read_csv("data.csv")
data = data.drop(columns=["Unnamed: 0"], errors="ignore")

st.write("Bar graph showing CSR strategy distribution.")
csr_summary = data.groupby("CSR strategy")["Abundance"].sum().reset_index()

st.bar_chart(csr_summary, x="CSR strategy", y="Abundance", color = "CSR strategy")


st.write("Explore the relationship between family and abundance within one of Grimes' ecological strategies")

if "csr_choice" not in st.session_state:
    st.session_state.csr_choice = "C"

if "minimum_abundance" not in st.session_state:
    st.session_state.minimum_abundance = 0

st.session_state.csr_choice = st.selectbox("Choose CSR strategy", ["C", "S", "R"], index=["C", "S", "R"].index(st.session_state.csr_choice))

max_abundance = int(data["Abundance"].max())

st.session_state.minimum_abundance = st.slider("Minimum abundance", min_value=0,max_value=max_abundance, value=st.session_state.minimum_abundance)

filtered_data = data

filtered_data = filtered_data[filtered_data["CSR strategy"] == st.session_state.csr_choice]
filtered_data = filtered_data[filtered_data["Abundance"] >= st.session_state.minimum_abundance]

st.bar_chart(filtered_data, x="Common Name", y="Abundance")

st.write("Explore diversity metrics within your site!")
if "metric" not in st.session_state:
    st.session_state.metric = "Shannon Index"
if "grouping" not in st.session_state:
    st.session_state.grouping = "Community"
st.session_state.metric = st.radio(
    "Select biodiversity metric",
    ["Shannon Index","Simpson Index","Evenness"],
    index=["Shannon Index","Simpson Index","Evenness"].index(st.session_state.metric)
)

st.session_state.grouping = st.segmented_control(
    "Select grouping", 
    ["Community", "Family", "CSR strategy"],
    default=st.session_state.grouping
)

def shannon_index(abundances):
    proportions = abundances / abundances.sum()
    return -(proportions * np.log(proportions)).sum()


def simpson_index(abundances):
    proportions = abundances / abundances.sum()
    return 1 - (proportions ** 2).sum()


def evenness(abundances):
    species_count = len(abundances)

    if species_count <= 1:
        return 0
    else:
        return shannon_index(abundances) / np.log(species_count)

def calculate_metric(df):

    if st.session_state.metric == "Shannon Index":
        return shannon_index(df["Abundance"])

    elif st.session_state.metric == "Simpson Index":
        return simpson_index(df["Abundance"])

    elif st.session_state.metric == "Evenness":
        return evenness(df["Abundance"])


if st.session_state.grouping == "Community":
    result = pd.DataFrame({"Group": ["Community"], "Value": [calculate_metric(data)]})


elif st.session_state.grouping == "Family":
    results = []
    for family, group in data.groupby("Family"):
        results.append({"Group": family, "Value": calculate_metric(group)})
    result = pd.DataFrame(results)


elif st.session_state.grouping == "CSR strategy":
    results = []
    for csr, group in data.groupby("CSR strategy"):
        results.append({"Group": csr, "Value": calculate_metric(group)})
    result = pd.DataFrame(results)


st.subheader(st.session_state.metric)

st.bar_chart(result, x="Group", y="Value")
