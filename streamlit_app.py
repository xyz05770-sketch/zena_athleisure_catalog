# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zena's Amazing Athleisure Catalog")

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE").select(col('COLOR_OR_STYLE'), col('SIZE_LIST'), col('FILE_URL), 'col('UPSELL_PRODUCT_DESC'), col('PRICE'))
st.dataframe(data=my_dataframe, use_container_width=True)
st.stop()

# pd_df = my_dataframe.to_pandas()
