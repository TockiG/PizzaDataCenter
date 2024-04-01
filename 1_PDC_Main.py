"""
@author: tockig
"""

import streamlit as st
import json
import os
import math
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

logo = Image.open(os.path.join(os.path.dirname(__file__),'pizzailogo.png'))

st.sidebar.image(logo)

dough_time = st.sidebar.select_slider(
    label="How much time till you want to fire up the oven?",
    #options=["3 hours", "24 hours", "48 hours", "72 hours"],
    options=["24 hours", "48 hours", "72 hours"],
    value="24 hours")
st.sidebar.write("72 hours has the best tast, but 24 hours is also good and \
          has a better effort-taste-ratio. A very short one will be added soon.")


yeast_type = st.sidebar.select_slider(
    label="Which kind of yeast will you use?",
    options=["Fresh yeast", "Dry yeast"],
    value="Fresh yeast")
st.sidebar.write("Fresh yest performes best, but dry also works.")

how_many = st.sidebar.number_input(
    label="How many pizza people will there be?",
    min_value=1)


dough_translate_dict = {"3 hours": "3h_dough",
                        "24 hours": "24h_dough",
                        "48 hours": "48h_dough",
                        "72 hours": "72h_dough"
                        }

translated_dough_time = dough_translate_dict[dough_time]

flour_weight = round(dough_dict[translated_dough_time]["Flour"]*how_many, 1)
water_weight = round(dough_dict[translated_dough_time]["Water"]*how_many, 1)
oil_spoons = round(dough_dict[translated_dough_time]["Olive oil"]*how_many, 1)
oil_weight = round(oil_spoons*8*how_many, 1) #8 g/TS olive oil
salt_weight = round(dough_dict[translated_dough_time]["Salt"]*how_many, 1)
yeast_weight = round(dough_dict[translated_dough_time][yeast_type]*how_many, 1)
sugar_weight = round(dough_dict[translated_dough_time]["Sugar"]*how_many, 1)

portion_weight = sum(
    [flour_weight,
     water_weight,
     oil_weight,
     salt_weight,
     yeast_weight,
     sugar_weight]
    ) / how_many

# round up sauce to always show a full can
how_much_sauce = math.ceil(how_many/3)

st.header("What You Need")

st.subheader("For the Dough")

col1, col2, col3 = st.columns(3)
col1.metric(label="Flour",
          value=str(flour_weight)+" g")
col2.metric(label="Cold water",
          value=str(water_weight)+" g")
col3.metric(label="Olive oil",
          value=str(oil_spoons)+" TS")
col1.metric(label="Salt",
          value=str(salt_weight)+" g")
col2.metric(label=yeast_type,
          value=str(yeast_weight)+" g")
col3.metric(label="Sugar",
          value=str(sugar_weight)+" g")
col1.metric(label="Semola",
          value=str(dough_dict[translated_dough_time]["Semola"])+" hand")

st.write("The flour is the most important ingredient and strongly effecting taste and texture. \
          One important parameter is its protein content, which sould be 12.5 to 13 g/100g. \
          Other effecting parameters are the wheat variety, the milling and its particle size. \
          Both effects is a flour should be used for short or long fermentation times. \
          For more than 24 hours Caputo Cuoco is recommend, for less Caputo Nuvola is best. \
          Trust me: it is worth its price!")

st.subheader("For the Sauce")

col1, col2, col3 = st.columns(3)
col1.metric(label="San Marzano tomato",
          value=str(dough_dict["sauce"]["San Marzano Tomato"]*how_much_sauce)+" can")
col2.metric(label="Olive oil",
          value=str(dough_dict["sauce"]["Olive oil"]*how_much_sauce)+" TS")
col3.metric(label="Basil",
          value=str(dough_dict["sauce"]["Basil"]*how_much_sauce)+" hand")
col1.metric(label="Salt",
          value=str(dough_dict["sauce"]["Salt"]))
col2.metric(label="Pepper",
          value=str(dough_dict["sauce"]["Pepper"]))
col3.metric(label="Sugar",
          value=str(dough_dict["sauce"]["Sugar"]))

st.write("It's all about the tomato! Canned tomotes have the best taste, because they \
          are harvested when they are perfectly ripe. San Marzano tomatoes might be expensive, \
          but perfeclty sweet and rich in flavour.")


st.header("How to Dough")

col1, col2, col3 = st.columns(3)
col1.metric(label="Bulk fermentation (cold)", 
            value=dough_dict[translated_dough_time]["Bulk time"])
col2.metric(label="Portion fermentation (cold)",
            value=dough_dict[translated_dough_time]["Portion time cold"])
col3.metric(label="Portion fermentation (warm)",
            value=dough_dict[translated_dough_time]["Portion time warm"])

st.write("Seperate a little bit of the cold water and disolve the yeast. Don't be \
          afraid - you do not need more yeast. Mix the flour, oil, water and yeast \
          water, maybe using a tool. Don't be afraid - it is supposed to be that wet. \
          Cover the dough with a wet towel and let it rest für 30 minutes at room temperature.")
st.write("Add the salt and kneet the dough intense with your hands for 15 minutes. It \
          will be ready, when the dough has a smooth and closed surface.")
if not dough_time == "3 hours":
    st.write("Let the whole dough portion rest in you fridge for {}."
              .format(str(dough_dict[translated_dough_time]["Bulk time"])))
st.write("Portion the dough to {} dough balls. Each ball should have a weight of {} g \
          (if you followed the recipe). Briefly knead and round each dough ball again. \
          Place the balls on a little bit of Semolina in the dough box (or another container) \
          and cover airtight. Let them rest in the fridge for {}. Take them out again {} \
          before usage." \
          .format(how_many,
                  portion_weight,
                  str(dough_dict[translated_dough_time]["Portion time cold"]),
                  str(dough_dict[translated_dough_time]["Portion time cold"])))
st.write("Do not kneet the dough portions again Take them carefully out of the box and \
          place them on a lot of Semola. Strech it with your hands add some Semola to let it\
          slide better. Do not use a rolling pin - trust me. Form a nice crust and a thin bottom.")


st.header("How to Sauce")

st.write("Put a can of whole tomatoes with olive oil in a pot and bring to a simmer. \
          Season with salt and sugar. Add fresh sage and a small amount of rosemary in \
          a tea infuser for easy removal later. After simmering for 10 minutes, crush \
          the tomatoes with a potato masher. Do not blend them since the seats get bitten \
          when they were crushed. Let it simmer for another 15 to 20 minutes. Season \
          with pepper. Remove from heat and and season with pepper. Add a handful of \
          fresh basil, which you crushed a litte bit in your hands. Do not worry if \
          it is too much - it's also perfect for pasta the day afterwards.")


st.header("How to Pizza")

st.write("Put some sauce on the pizza and top it with the stuff you like. There are \
          no rules - pizza is love! For the cheese Mozzarella, buffalo Mozzarella or \
          Scamorza (maybe smoked if you like) are highly recommended.")
         

st.header("How to Bake")

st.write("Preheat the oven to the maximum temperature. Place the pizza stone in the \
          cold oven and heat for approximately 45 to 60 minutes. Transfer the pizza \
          onto the stone using a shovel and bake for about 8 to 10 minutes depending \
          on the temperature. Do not open the oven door to check weather it's good or \
          not - just use the window.)")


st.header("How to Enjoy")

st.write("Just enjoy, but do not burn yourself! 🍕")


st.header("How to Contribute")

st.write("If you have any feedback send me a [mail](mailto:jan.tockloth@gmail.com) \
          - I would be very happy about that! You are also very welcome to contribute \
          to this page on <a href='" + "https://github.com/TockiG/PizzaDataCenter" + \
          "' target='_blank'>GitHub</a>.", unsafe_allow_html=True)

