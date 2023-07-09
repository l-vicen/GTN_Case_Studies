""" Mainly stilistic page for software eng.
purposes since Streamlit renders the original app.py (now, Documentation.py)
script in root source, instead of the pages directtly """

# App Dependency
import streamlit as st

# UI-stuff
st.markdown("### Using Evolutionary Game Theory to Understand Behavior Dynamics during the Covid-19 Pandemic")
st.markdown("---")
st.info("On this website we provide an interactive interface to interact Evolutionary Game Theory methods implemented by Domingos et al. (2023) in the open-source library EGTtools. For more information consult our paper.")

# Source of EGTtools
st.warning(r"@misc{Fernandez2020,\
  author = {Fernández Domingos, Elias},\
  title = {EGTTools: Toolbox for Evolutionary Game Theory},\
  year = {2020},\
  publisher = {GitHub},\
  journal = {GitHub repository},\
  howpublished = {\url{https://github.com/Socrats/EGTTools},\
  doi = {10.5281/zenodo.3687125}")