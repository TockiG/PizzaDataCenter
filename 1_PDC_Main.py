
"""
@author: tockig
"""

import streamlit as st
import json
import os
from PIL import Image

# initialize page
# menu_items = {}

# Global page settings
st.set_page_config(
    page_title='PizzaDataCenter',
    page_icon='🍕',
    layout='centered')

# import dough dict
dough_json = open(os.path.join(os.path.dirname(__file__), 'recipes.json'))
dough_dict = json.load(dough_json)


st.header("Welcome to the PizzaDataCenter")

st.write("This page will introduce you to the world of awesome, juicy and \
         friendmaking homemade italian pizza. Just use the recipe calculator \
         and follow the instructions below to become a home oven pizzaiolo. \
         Enjoy!")

logo = Image.open('logo.jpeg')

st.sidebar.image(logo)

dough_time = st.sidebar.select_slider(
    label="How much time till you want fire the oven?",
    options=["3 hours", "24 hours", "72 hours"],
    value="24 hours")

yeast_type = st.sidebar.select_slider(
    label="Which kind of yeast will you use?",
    options=["Fresh yeast", "Dry yeast"],
    value="Fresh yeast")

how_many = st.sidebar.number_input(
    label="How much pizza do you want to make?",
    min_value=1)


dough_translate_dict = {"3 hours": "3h_dough",
                        "24 hours": "24h_dough",
                        "72 hours": "72h_dough"
                        }

# =============================================================================
# st.write(dough_translate_dict[dough_time])
# 
# st.write(type(dough_dict[dough_translate_dict[dough_time]]))
# 
# dough_dict[dough_translate_dict[dough_time]]
# 
# st.write(dough_dict["3h_dough"]["Water"])
# =============================================================================

st.metric(label="Flour",
          value=str(dough_dict[dough_translate_dict[dough_time]]["Flour"]*how_many)+" g")
st.metric(label="Water",
          value=str(dough_dict[dough_translate_dict[dough_time]]["Water"]*how_many)+" g")
st.metric(label="Olive oil",
          value=str(dough_dict[dough_translate_dict[dough_time]]["Olive oil"]*how_many)+" table spoons")
st.metric(label="Salt",
          value=str(dough_dict[dough_translate_dict[dough_time]]["Salt"]*how_many)+" g")
st.metric(label="Sugar",
          value=str(dough_dict[dough_translate_dict[dough_time]]["Sugar"]*how_many)+" g")
st.metric(label=yeast_type,
          value=str(dough_dict[dough_translate_dict[dough_time]][yeast_type]*how_many)+" g")
    
