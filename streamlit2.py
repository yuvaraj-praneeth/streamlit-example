import streamlit as st
st.title('NutryUS')
st.image('https://image.shutterstock.com/image-photo/best-menu-healthy-body-collage-260nw-1679266360.jpg')
st.header('Your new diet Dormitory Mother')
st.write("**Open the sidebar the type of meal on your left top corner to select **")
genre = st.sidebar.selectbox(
     "Meal:",
     ('None','Breakfast','Lunch','Dinner'))
st.write('**You selected:**', genre)
if genre == 'Breakfast':
  st.subheader('Device:- ',genre)
  st.write('Idly')
  st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
  S1=st.slider('Quantity',0.0,5.0,step=0.5)
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
[URL=http://s05.flagcounter.com/more/mPJQ][IMG]https://s05.flagcounter.com/map/mPJQ/size_m/txt_000000/border_CCCCCC/pageviews_1/viewers_0/flags_0/[/IMG][/URL]
