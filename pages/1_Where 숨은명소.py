import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import plotly.express as px
from streamlit_folium import st_folium
import json
import folium
from PIL import Image

st.set_page_config(
   layout='wide', # wide,centered
   page_icon=':bar_chart:'
)
st.subheader(':pushpin: 숨은명소란 ??')
st.markdown("☞ 수도권을 제외한 **내국인 대비 외국인 관광 비중이 적은 지역**이라 정의")
st.markdown("( 기준 : 관광방문객, 관광명소, 관광지출액 )")
st.subheader(':pushpin: 관광인프라 ??')
st.markdown("☞ 외국인들이 한국 여행 시 주로 방문하는 **관광지 및 고려 요인**을 나타냄")
st.markdown("(선정 기준 : 문화체육관광부와 한국 관광공사의 “외래관광객조사”를 참고)")
st.markdown("# ")

tab1, tab2= st.tabs([" Where 숨은명소","숨은명소 관광인프라 In Map"])

with tab1:
   st.header("	:grey_question: Where 숨은명소 ")
   st.write('')
   st.markdown('1. 내국인 방문객 대비 외국인 방문객이 **적은 지역**')
   st.latex(r'\dfrac{행정구역별 외국인 방문객수}{행정구역별 내국인 방문객수} => RankVisit')
   with st.expander(":date: 데이터 확인하기"):
      col1, col2 = st.columns([1, 1])
      with col1:
         visit=pd.read_csv('data/EDA관광방문객.csv',index_col='Unnamed: 0')
         st.dataframe(visit.head(10))
      with col2:
         fig1=px.bar(visit.head(10),x='행정구역', y='외국인/내국인',width=500)
         st.plotly_chart(fig1)
   st.write('')
   st.markdown('2. 면적당 관광명소가 **많은 지역**')
   st.latex(r'\dfrac{행정구역별 관광명소}{행정구역별 면적} => RankPlace')
   with st.expander(":date: 데이터 확인하기"):
      col1, col2 = st.columns([1, 1])
      with col1:
         place=pd.read_csv('data/EDA관광명소.csv',index_col='Unnamed: 0')
         st.dataframe(place.head(10))
         st.text('관광명소/면적컬럼의 수가 0.0001보다 작아서 0으로 출력됨 ')
         st.text('그래프의 숫자 참고')
      with col2:
         fig1=px.bar(place.head(10),x='행정구역', y='관광명소/면적',width=500)
         st.plotly_chart(fig1)
   st.write('')
   st.markdown('3. 내국인 관광지출액 대비 외국인 관광지출액이 **적은 지역**')
   st.latex(r'\dfrac{행정구역별 외국인 관광지출액}{행정구역별 내국인 관광지출액} => RankMoney')
   with st.expander(":date: 데이터 확인하기"):
      col1, col2 = st.columns([1, 1])
      with col1:
         money=pd.read_csv('data/EDA관광지출액.csv',index_col='Unnamed: 0')
         money.rename(columns={'평균':'외국인/내국인지출액평균'},inplace=True)
         st.dataframe(money.head(10))
      with col2:
         fig1=px.bar(money.head(10),x='행정구역', y='외국인/내국인지출액평균',width=500)
         st.plotly_chart(fig1)
   st.write('')
   st.write(':arrow_forward:  각 기준의 순위를 매겨 순위평균으로 정함.')
   st.latex(r'\dfrac{RankVisit + RankPlace + RankMoney}{3}')

   st.markdown("---")
   col1,col2=st.columns([1,1])
   with col1:
      st.markdown("#### :world_map: 숨은명소 순위평균 단계구분도")
      code_sort_total = pd.read_csv('data/숨은명소전체요소순위.csv', index_col='Unnamed: 0')
      with open('./data/TL_SCCO_SIG.json', encoding='utf-8') as f:
         geo = json.loads(f.read())

      m = folium.Map(location=[36.5, 127.5],
                     zoom_start=7)
      folium.Choropleth(geo_data=geo,
                        data=code_sort_total,
                        columns=['코드', '순위평균'],
                        fill_color='YlGn', fill_opacity=0.8,
                        line_opacity=0.3,
                        key_on='feature.properties.SIG_CD',
                        ).add_to(m)
      st_data= st_folium(m,width=400,height=500)


      # m = open('../data/2-3/숨은명소순위.html', 'r', encoding='utf-8')
      # source_code = m.read()
      # components.html(source_code, height=600,width=500)
      st.caption('색이 진할수록 숨은명소에 가깝다')

   with col2:
      st.markdown("#### :date: 숨은명소 순위평균")
      rank=code_sort_total[['행정구역','visit_rank','place_rank','money_rank','순위평균']].head(5)
      rank.index=['1순위','2순위','3순위','4순위','5순위']
      st.dataframe(data=rank)

with tab2:
   st.header(":grey_exclamation: How many 숨은명소 인프라")

   col1,col2,col3=st.columns([2,1,5])
   with col1:
      st.markdown('# ')
      hiddenplace = st.radio(
         " :heavy_check_mark: 숨은명소를 선택해주세요",
         ('부산광역시 북구', '대구광역시 서구', '광주광역시 남구', '광주광역시 북구', '전라남도 장흥군'))
      if hiddenplace == '부산광역시 북구':
         st.write('You selected \'부산광역시 북구\'.')
      elif hiddenplace == '대구광역시 서구':
         st.write('You selected \'대구광역시 서구\'.')
      elif hiddenplace == '광주광역시 남구':
         st.write('You selected \'광주광역시 남구\'.')
      elif hiddenplace == '광주광역시 북구':
         st.write('You selected \'광주광역시 북구\'.')
      elif hiddenplace == '전라남도 장흥군':
         st.write('You selected \'전라남도 장흥군\'.')
      else:
         st.write("지역 하나를 선택하세요")
      st.markdown('# ')
      item = st.radio(
         ":heavy_check_mark: 관광인프라를 선택해주세요",
         ('식당', '쇼핑몰', '역사유적지', '전통문화체험지', '박물관/미술관', '숙박업소'))
      if item == '식당':
         st.write('You selected \'식당\'.')
         item='1'
      elif item == '쇼핑몰':
         st.write("You selected \'쇼핑몰\'.")
         item = '2'
      elif item == '역사유적지':
         st.write("You selected \'역사유적지\'.")
         item = '3'
      elif item == '전통문화체험지':
         st.write("You selected \'전통문화체험지\'.")
         item = '4'
      elif item == '박물관/미술관':
         st.write("You selected \'박물관/미술관\'.")
         item = '5'
      elif item == '숙박업소':
         st.write("You selected \'숙박업소\'.")
         item = '6'
      else:
         st.write("관광인프라 하나를 선택하세요")

   with col2:
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      st.markdown('# ')
      button=st.button('지도보기')

   with col3:
      if button:
         m_path = 'data/숨은명소 ' + item + ' ' + hiddenplace + '.html'
         m = open(m_path, 'r', encoding='utf-8')
         source_code = m.read()
         components.html(source_code,height=500,width=600)

   st.markdown("# ")
   st.markdown("# ")
   st.subheader(':thumbsup: 기획자가 추천하는 숨은명소 관광지')
   st.write("어느 지역의 유명한 관광지가 궁금하니?")
   option = st.selectbox(
      'Which hidden area are you curious about?',
      ('부산광역시 북구', '대구광역시 서구', '광주광역시 남구', '광주광역시 북구', '전라남도 장흥군'))
   st.write('You selected:', option)

   famous_col1, famous_col2, famous_col3 = st.columns([1, 1, 1])
   if option=='부산광역시 북구':
      with famous_col1:
         st.write('낙동강')
         image=Image.open('data/낙동강.png')
         st.image(image)
      with famous_col2:
         st.write('부산어촌민속관')
         image=Image.open('data/부산어촌민속관.png')
         st.image(image)
      with famous_col3:
         st.write('만덕사지')
         image=Image.open('data/만덕사지.png')
         st.image(image)

   elif option=='대구광역시 서구':
      with famous_col1:
         st.write('중리동 곱창골목')
         image=Image.open('data/대구 곱창골목.png')
         st.image(image)
      with famous_col2:
         st.write('서부 오미가미 거리')
         image=Image.open('data/오미가미 거리.png')
         st.image(image)
      with famous_col3:
         st.write('내당동 큰장길 침구류 명물거리')
         image=Image.open('data/침구류 명물거리.png')
         st.image(image)

   elif option=='광주광역시 남구':
      with famous_col1:
         st.write('펭귄마을')
         image=Image.open('data/펭귄마을.png')
         st.image(image)
      with famous_col2:
         st.write('사직공원전망타워')
         image=Image.open('data/사직전망타워.png')
         st.image(image)
      with famous_col3:
         st.write('빛고을농촌테마공원')
         image=Image.open('data/빛고을 농촌 테마 공원.png')
         st.image(image)

   elif option=='광주광역시 북구':
      with famous_col1:
         st.write('북구8경')
         image=Image.open('data/북구8경.png')
         st.image(image)
      with famous_col2:
         st.write('우치공원 페밀리랜드')
         image=Image.open('data/우치공원.png')
         st.image(image)
      with famous_col3:
         st.write('원효사')
         image=Image.open('data/원효사.png')
         st.image(image)

   elif option=='전라남도 장흥군':
      with famous_col1:
         st.write('정남진')
         image=Image.open('data/정남진.png')
         st.image(image)
      with famous_col2:
         st.write('편백숲우드랜드')
         image=Image.open('data/편백숲우드랜드.png')
         st.image(image)
      with famous_col3:
         st.write('소등섬')
         image=Image.open('data/소등섬.png')
         st.image(image)