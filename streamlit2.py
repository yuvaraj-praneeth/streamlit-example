import streamlit as st
st.title('Streamlit Example 2')
st.header('Different Games That you have played in your childhood')
st.write("**Open the sidebar on your left top corner to select the device **")
genre = st.sidebar.selectbox(
     "Device:",
     ('None','PC','Romance','Sports'))
st.write('**You selected:**', genre)
if genre == 'PC':
  st.subheader('Device: - PC')
  st.image('https://worldofpcgames.co/wp-content/uploads/2016/11/Road-Rash-PC-Game-Download-By-Worldofpcgames.net_.png.webp')
  S1=st.slider('Road Rash',0.0,5.0,step=0.5)
  st.image('https://gepig.com/game_cover_460w/297.jpg')
  S2=st.slider('Need for Speed Most Wanted',0.0,5.0,step=0.5)
  st.image('https://images-na.ssl-images-amazon.com/images/I/51-IGGUe5ZL.png')
  S3=st.slider('GTA: Vice City',0.0,5.0,step=0.5)
  st.image('https://i.ytimg.com/vi/detvL9SECGQ/maxresdefault.jpg')
  S4=st.slider('Mortal Kombat',0.0,5.0,step=0.5)
  st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S4=st.slider('Tekken',0.0,5.0,step=0.5)

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
