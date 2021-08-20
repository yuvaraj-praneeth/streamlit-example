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
  st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fabandonwaregames.net%2Fgame%2Froad-rash&psig=AOvVaw1M3I5hIBJ8Lg3mroFOVRMN&ust=1629556341858000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNif7tPov_ICFQAAAAAdAAAAABAJ')
  S1=st.slider('Road Rash',0.0,5.0,step=0.5)
  st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fgamesystemrequirements.com%2Fgame%2Fneed-for-speed-most-wanted&psig=AOvVaw0Nbn7v0sSqTTCSdweUWkVX&ust=1629559041750000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOCJ29Dyv_ICFQAAAAAdAAAAABAD')
  S2=st.slider('Need for Speed Most Wanted',0.0,5.0,step=0.5)
  st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2FGrand-Theft-Auto-Vice-City%2Fdp%2FB00CF354UG&psig=AOvVaw0wfC6ZVEhWUYiCHGyM2zza&ust=1629559091687000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPDgh-vyv_ICFQAAAAAdAAAAABAJ')
  S3=st.slider('GTA: Vice City',0.0,5.0,step=0.5)
  st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdetvL9SECGQ&psig=AOvVaw3cJeHHduFYJ1XMEPQbfYfa&ust=1629559193036000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLCAqZvzv_ICFQAAAAAdAAAAABAS')
  S4=st.slider('Mortal Kombat',0.0,5.0,step=0.5)
  st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Ftekken.fandom.com%2Fwiki%2FTekken_6&psig=AOvVaw3KySyRRflR0T8RcncDiUSG&ust=1629559371098000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIjJm_Hzv_ICFQAAAAAdAAAAABAI')
  S4=st.slider('Tekken',0.0,5.0,step=0.5)

elif genre == 'Romance':
  st.subheader('Genre:- Romance)
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
