# Import python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie! :cup_with_straw:")
st.write(
    """    Choose the fruits you want in your custom Smoothie!
    """
)
cnx =st.connection("snowflake")
session = cnx.session()
# session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options"). select(col('fruit_name'))
# st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Choose up to 5 ingredients:', my_dataframe)
if ingredients_list:
    ingredients_string=''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    # st.write("""insert inti smoothies.public.order(ingredients) 
    # values ('""" + ingredients_string + """')  """)

time_to_insert = st.button('Submit order')
my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

# st.write(my_insert_stmt)
if time_to_insert:
    session.sql(my_insert_stmt).collect();
    st.success('Your Smoothie is order!')



# session.sql(INSERT INTO smoothies.public.orders_list (ingredients)
#   SELECT ARRAY_CONSTRUCT(12, 'twelve', NULL); )

#Contact Method
# option = st.selectbox(
#     'How would you like to be contacted', 
#     ('Email', 'Home Phone', 'Mobile Phone'),
#     index=0, 
#     # format_func=special_internal_function, 
#     # key=None, help=None, on_change=None, args=None, kwargs=None,
#     # placeholder="Choose an option", disabled=False, 
#     label_visibility="visible")


# option = st.selectbox(
#     'What is yuor favorite fruit?', 
#     ('Strawberries', 'Banana', 'Peaches'),
#     index=0, 
#     # format_func=special_internal_function, 
#     # key=None, help=None, on_change=None, args=None, kwargs=None,
#     # placeholder="Choose an option",# disabled=False, 
#     label_visibility="visible")

# st.write('You selected:', option)
