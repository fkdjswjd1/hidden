import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import plotly.express as px
from streamlit_folium import st_folium
import json
import folium
from PIL import Image


#페이지 설정
st.set_page_config(
   layout='wide', # wide,centered
   page_icon=':bar_chart:'
)
# header
st.subheader(':pushpin: 숨은명소란 ??')
st.markdown("☞ 수도권을 제외한 **내국인 대비 외국인 관광 비중이 적은 지역**이라 정의")
st.markdown("( 기준 : 관광방문객, 관광명소, 관광지출액 )")
st.subheader(':pushpin: 관광인프라 ??')
st.markdown("☞ 외국인들이 한국 여행 시 주로 방문하는 **관광지 및 고려 요인**을 나타냄")
st.markdown("(선정 기준 : 문화체육관광부와 한국 관광공사의 “외래관광객조사”를 참고)")
st.markdown("# ")

# tab 설정
tab1, tab2= st.tabs(["Where 숨은명소","숨은명소 관광인프라 In Map"])

# Where 숨은명소 tab
with tab1:
   # tab안에서 header
   st.header("	:grey_question: Where 숨은명소 ")
   st.markdown('# ')

   # 1. 관광방문객
   st.markdown('1. 내국인 방문객 대비 외국인 방문객이 **적은 지역** 순위')
   st.latex(r'\dfrac{행정구역별 외국인 방문객수}{행정구역별 내국인 방문객수}을 계산한 순위 => RankVisit')
   # 확장탭설정
   with st.expander(":date: 데이터 확인하기"):
      col1, col2 = st.columns([1, 1])
      with col1: # 왼쪽에는 표
         visit=pd.read_csv('data/EDA관광방문객.csv',index_col='Unnamed: 0')
         visit.iloc[:, -1] = visit.iloc[:, -1] * 100
         visit.rename(columns={'외국인/내국인': '외국인/내국인*100'}, inplace=True)
         visit.index = str(visit.index+1)+'순위'
         st.table(visit.head(10))

      with col2: #오른쪽에는 막대그래프
         fig1=px.bar(visit.head(10),x='행정구역', y='외국인/내국인*100',width=500)
         st.plotly_chart(fig1)

   # 2. 관광명소
   st.write('')
   st.markdown('2. 면적당 관광명소가 **많은 지역** 순위')
   st.latex(r'\dfrac{행정구역별 관광명소}{행정구역별 면적}을 계산한 순위 => RankPlace')
   # 확장탭설정
   with st.expander(":date: 데이터 확인하기"):
      col1, col2 = st.columns([1, 1])
      with col1: # 왼쪽에는 표
         place=pd.read_csv('data/EDA관광명소.csv',index_col='Unnamed: 0')
         place.iloc[:, -1] = place.iloc[:, -1] * 10000
         place.rename(columns={'관광명소/면적': '관광명소/면적*10000'}, inplace=True)
         place.index = str(place.index+1)+'순위'
         st.table(place[['행정구역', '관광명소', '면적', '관광명소/면적*10000']].head(10))
         st.text('관광명소 수와 면적의 단위가 크게 상이하여 100 대신 10000을 곱함')
      with col2: #오른쪽에는 막대그래프
         fig1=px.bar(place.head(10),x='행정구역', y='관광명소/면적*10000',width=500)
         st.plotly_chart(fig1)

   # 3. 관광지출액
   st.write('')
   st.markdown('3. 내국인 관광지출액 대비 외국인 관광지출액이 **적은 지역** 순위')
   st.latex(r'\dfrac{행정구역별 외국인 관광지출액}{행정구역별 내국인 관광지출액}을 계산한 순위 => RankMoney')
   # 확장탭설정
   with st.expander(":date: 데이터 확인하기"):
      col1, col2 = st.columns([1, 1])
      with col1: # 왼쪽에는 표
         money=pd.read_csv('data/EDA관광지출액.csv',index_col='Unnamed: 0')
         money.iloc[:, -1] = money.iloc[:, -1] * 100
         money.rename(columns={'평균': '외국인/내국인지출액평균*100'}, inplace=True)
         money.index = str(money.index+1)+'순위'
         st.table(money.head(10))
      with col2: #오른쪽에는 막대그래프
         fig1=px.bar(money.head(10),x='행정구역', y='외국인/내국인지출액평균*100',width=500)
         st.plotly_chart(fig1)


   st.write('')
   st.markdown(':arrow_forward:  각 기준의 순위를 매겨 **순위평균**으로 정함.')
   st.latex(r'\dfrac{RankVisit + RankPlace + RankMoney}{3}')

   st.markdown("---")
   # 레이아웃설정
   col1,col2=st.columns([1,1])
   with col1:# 왼쪽에는 단계구분도
      st.markdown("#### :world_map: 숨은명소 순위평균 단계구분도")
      code_sort_total = pd.read_csv('data/숨은명소전체요소순위.csv', index_col='Unnamed: 0')

      # 방법1) folium을 이용한 단계구분도
      with open('data/TL_SCCO_SIG.json', encoding='utf-8') as f:
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


      # 방법2) html을 이용한 단계구분도
      # m = open('../data/2-3/숨은명소순위.html', 'r', encoding='utf-8')
      # source_code = m.read()
      # components.html(source_code, height=600,width=500)
      st.caption('색이 진할수록 숨은명소에 가깝다')

   with col2: # 오른쪽에는 표
      st.markdown("#### :date: 숨은명소 순위평균")
      st.text('전체 172 중')
      rank=code_sort_total[['행정구역','visit_rank','place_rank','money_rank','순위평균']].head(5)
      rank.index=['1순위','2순위','3순위','4순위','5순위']
      st.dataframe(data=rank)

# 숨은명소 관광인프라 In Map
with tab2:
   # tab 안의 header
   st.header(":grey_exclamation: How many 숨은명소 인프라")

   # 레이아웃 설정
   col1,col2,col3=st.columns([2,1,5])


   with col1:
      st.markdown('# ')

      # 숨은명소 선택
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

   # 관광인프라 선택
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

   # 버튼
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
      if button: # 버튼이 눌리면 지도 출력
         m_path = 'data/숨은명소 ' + item + ' ' + hiddenplace + '.html'
         m = open(m_path, 'r', encoding='utf-8')
         source_code = m.read()
         components.html(source_code,height=500,width=800)

   st.markdown("# ")
   st.markdown("# ")
   st.subheader(':thumbsup: 기획자가 추천하는 숨은명소 관광지') # 관광지 추천
   st.write("어느 지역의 유명한 관광지가 궁금하니?")
   option = st.selectbox(
      'Which hidden area are you curious about?',
      ('부산광역시 북구', '대구광역시 서구', '광주광역시 남구', '광주광역시 북구', '전라남도 장흥군'))
   st.write('You selected:', option)
   # 레이아웃 설정
   famous_col1, famous_col2, famous_col3 = st.columns([1, 1, 1])

   # selectbox 선택에 따른 결과 출력
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
         st.write('우치공원 패밀리랜드')
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
