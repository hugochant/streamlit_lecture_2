import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# load data
df = px.data.gapminder()

# Title
st.title('Welcome on streamlit lecture')

# show dataset sample
st.write(df.sample(5))

# create a slider 
year = st.slider('Year', int(df.year.min()), int(df.year.max()), step=5)


# display a chart 
fig = px.scatter(df[df['year']==year], x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)


st.plotly_chart(fig)        