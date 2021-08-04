from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


#with st.echo(code_location='below'):
 #   total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
  #  num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

   # Point = namedtuple('Point', 'x y')
    #data = []

    #points_per_turn = total_points / num_turns

    #for curr_point_num in range(total_points):
     #   curr_turn, i = divmod(curr_point_num, points_per_turn)
     #   angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
      #  radius = curr_point_num / total_points
      #  x = radius * math.cos(angle)
      #  y = radius * math.sin(angle)
      #  data.append(Point(x, y))

    #st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
     #   .mark_circle(color='#0068c9', opacity=0.5)
     #    .encode(x='x:Q', y='y:Q'))
#Writing python code
#Here we can change the code and run any no. of times
#%%writefile app.py
import streamlit as st
st.title('Streamlit Example')
st.header('Rating different animes')
st.write("**Open the sidebar to select genre on your left top corner**")
genre = st.sidebar.selectbox(
     "What's your favorite anime genre",
     ('None','Shounen', 'Romance', 'Sports'))
st.write('**You selected:**', genre)
if genre == 'Shounen':
  st.subheader('Genre:- Shounen')
  st.image('https://d.newsweek.com/en/full/1034569/attack-on-titan-season-3-art-poster-how-to-watch-online-hulu-crunchyroll-funimation-01.jpg?w=1600&h=900&q=88&f=99dce8214a86314128b26cd47296ede6')
  S1=st.slider('Attack on Titans',0.0,5.0,step=0.5)
  st.image('https://wallpapercave.com/wp/wp1894643.jpg')
  S2=st.slider('My Hero Academia',0.0,5.0,step=0.5)
  st.image('https://wallpapercave.com/wp/8fMMJWX.jpg')
  S3=st.slider('Naruto',0.0,5.0,step=0.5)
  st.image('https://image.winudf.com/v2/image1/bWUuYXppYXBwLnZpbmxhbmRzYWdhd2FsbHBhcGVyX3NjcmVlbl8yXzE1NzIwOTM2NzRfMDQ1/screen-2.jpg?fakeurl=1&type=.jpg')
  S4=st.slider('Vinland Saga',0.0,5.0,step=0.5)
  st.write('**Average Rating of Shounen genre** = ', (S1+S2+S3+S4)/4)
elif genre == 'Romance':
  st.subheader('Genre:- Romance')
  st.image('https://www.kolpaper.com/wp-content/uploads/2021/02/Horimiya-Wallpaper-HD.jpg')
  R1=st.slider('Horimiya',0.0,5.0,step=0.5)
  st.image('https://wallpapercave.com/wp/wp8650031.jpg')
  R2=st.slider('Bottom-Tier Character Tomozaki-kun',0.0,5.0,step=0.5)
  st.image('https://c4.wallpaperflare.com/wallpaper/166/158/478/clannad-clannad-after-story-okazaki-nagisa-okazaki-tomoya-wallpaper-preview.jpg')
  R3=st.slider('Clannad',0.0,5.0,step=0.5)
  st.image('https://wallpaperaccess.com/full/619632.jpg')
  R4=st.slider('Kimi no Na Wa',0.0,5.0,step=0.5)
  st.write('**Average Rating of Romace genre** = ', (R1+R2+R3+R4)/4)
elif genre == 'Sports':
  st.subheader('Genre:- Sports')
  st.image('https://c4.wallpaperflare.com/wallpaper/430/354/442/haikyuu-haikyuu-hinata-shouyou-kageyama-tobio-azumane-asahi-hd-wallpaper-preview.jpg')
  SP1=st.slider('Haikyuu!',0.0,5.0,step=0.5)
  st.image('https://wallpaperaccess.com/full/1648578.jpg')
  SP2=st.slider('Diamond no Ace',0.0,5.0,step=0.5)
  st.image('https://images2.alphacoders.com/267/267400.jpg')
  SP3=st.slider('Kuroko no Baske',0.0,5.0,step=0.5)
  st.image('https://wallpapercave.com/wp/wp9165028.jpg')
  SP4=st.slider('Burning Kabaddi',0.0,5.0,step=0.5)
  st.write('**Average Rating of Sports genre** = ', (SP1+SP2+SP3+SP4)/4) 
