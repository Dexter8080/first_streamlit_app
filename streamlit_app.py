import streamlit
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#------------------------------------------------
streamlit.title('My Parents New Healthy Diner')
#------------------------------------------------
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boild Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#------------------------------------------------

# Lets put a pic list here so they can pick the fruit they want to Include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#display the table on the page 
streamlit.dataframe(my_fruit_list)
