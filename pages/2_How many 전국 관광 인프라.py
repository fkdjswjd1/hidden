import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


st.set_page_config(
   layout='wide', # wide,centered
   page_icon=':bar_chart:'
)
st.title('전국 관광명소 map')

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['식당', '쇼핑몰', '역사유적지', '전통문화체험', '박물관/미술관', '유명 촬영지', '숙박업소'])

# 각 지역별 folium 지도의 중심 위치(location)를 딕셔너리에 저장
top_area = {'제주특별자치도 제주시': [33.4304632, 126.557837],
            '서울특별시 강남구': [37.4996051, 127.065900],
            '부산광역시 중구': [35.1062760, 129.033287],
            '대구광역시 중구': [35.8664829, 128.594690],
            '서울특별시 중구': [37.5605029, 126.997965],
            '부산광역시 해운대구': [35.1953764, 129.161179],
            '경기도 성남시 분당구': [37.3777546, 127.111759],
            '경상북도 경주시': [35.8310318, 129.273589],
            '서울특별시 종로구': [37.5976497, 126.985303],
            '제주특별자치도 서귀포시': [33.3396851, 126.585206],
            '강원도 평창군': [37.5603081, 128.489204],
            '부산광역시 북구': [35.230425, 129.026475],
            '대구광역시 서구': [35.87194054, 128.5591601],
            '광주광역시 남구': [35.091235, 126.854079],
            '광주광역시 북구': [35.1931988, 126.935766],
            '전라남도 장흥군': [34.6695994, 126.933706]
        }

# 식당
with tab1:
    # 상위 숨은명소 리스트 생성
    top_area_name = ['제주특별자치도 제주시',
                     '서울특별시 강남구',
                     '부산광역시 중구',
                     '대구광역시 중구']
    i = '1'

    # 데이터 로드
    df_map1 = pd.read_csv('../data/3/전처리_완료/지역별 식당 위치정보.csv', encoding='utf-8', index_col=0)

    # 레이아웃 구성
    con1, con2, sb = st.columns([2, 2, 1])

    with con1:
        st.subheader('전국 단계구분도')
        m = open('data/' + i + ' 전국 단계구분도.html', 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

    with sb:
        option = st.selectbox('지역 선택', top_area_name)
        st.caption('지역 선정 기준')
        st.caption('- 지역별 관광 인프라 수')
        st.caption('- 면적')

    with con2:
        st.subheader('지역별 지도')
        m_path = 'data/' + i + ' ' + option + '.html'
        m = open(m_path, 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

# 쇼핑몰
with tab2:
    # 상위 숨은명소 리스트 생성
    top_area_name = ['서울특별시 중구',
                     '부산광역시 해운대구',
                     '경기도 성남시 분당구',
                     '부산광역시 중구']
    i = '2'

    # 데이터 로드
    df_map1 = pd.read_csv('data/지역별 쇼핑몰 위치정보.csv', encoding='utf-8', index_col=0)

    # 레이아웃 구성
    con1, con2, sb = st.columns([2, 2, 1])

    with con1:
        st.subheader('전국 단계구분도')
        m = open('data/' + i + ' 전국 단계구분도.html', 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

    with sb:
        option = st.selectbox('지역 선택', top_area_name)
        st.caption('지역 선정 기준')
        st.caption('- 지역별 관광 인프라 수')
        st.caption('- 면적')

    with con2:
        st.subheader('지역별 지도')
        m_path = 'data/' + i + ' ' + option + '.html'
        m = open(m_path, 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

# 역사유적지
with tab3:
    # 상위 숨은명소 리스트 생성
    top_area_name = ['경상북도 경주시',
                     '제주특별자치도 제주시',
                     '서울특별시 종로구',
                     '부산광역시 중구']
    i = '3'

    # 데이터 로드
    df_map1 = pd.read_csv('data/지역별 역사유적지 위치정보.csv', encoding='utf-8', index_col=0)

    # 레이아웃 구성
    con1, con2, sb = st.columns([2, 2, 1])

    with con1:
        st.subheader('전국 단계구분도')
        m = open('data/' + i + ' 전국 단계구분도.html', 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

    with sb:
        option = st.selectbox('지역 선택', top_area_name)
        st.caption('지역 선정 기준')
        st.caption('- 지역별 관광 인프라 수')
        st.caption('- 면적')

    with con2:
        st.subheader('지역별 지도')
        m_path = 'data/' + i + ' ' + option + '.html'
        m = open(m_path, 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

# 전통문화체험지
with tab4:
    # 상위 숨은명소 리스트 생성
    top_area_name = ['서울특별시 종로구',
                     '제주특별자치도 제주시',
                     '대구광역시 중구',
                     '부산광역시 중구']
    i = '4'

    # 데이터 로드
    df_map1 = pd.read_csv('data/지역별 전통체험 위치정보.csv', encoding='utf-8', index_col=0)

    # 레이아웃 구성
    con1, con2, sb = st.columns([2, 2, 1])

    with con1:
        st.subheader('전국 단계구분도')
        m = open('data/' + i + ' 전국 단계구분도.html', 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

    with sb:
        option = st.selectbox('지역 선택', top_area_name)
        st.caption('지역 선정 기준')
        st.caption('- 지역별 관광 인프라 수')
        st.caption('- 면적')

    with con2:
        st.subheader('지역별 지도')
        m_path = 'data/' + i + ' ' + option + '.html'
        m = open(m_path, 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)


# 박물관/미술관
with tab5:
    # 상위 숨은명소 리스트 생성
    top_area_name = ['제주특별자치도 서귀포시',
                     '제주특별자치도 제주시',
                     '부산광역시 중구',
                     '대구광역시 중구']
    i = '5'

    # 데이터 로드
    df_map1 = pd.read_csv('data/지역별 박물관+미술관 위치정보.csv', encoding='utf-8', index_col=0)

    # 레이아웃 구성
    con1, con2, sb = st.columns([2, 2, 1])

    with con1:
        st.subheader('전국 단계구분도')
        m = open('data/' + i + ' 전국 단계구분도.html', 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

    with sb:
        option = st.selectbox('지역 선택', top_area_name)
        st.caption('지역 선정 기준')
        st.caption('- 지역별 관광 인프라 수')
        st.caption('- 면적')

    with con2:
        st.subheader('지역별 지도')
        m_path = 'data/' + i + ' ' + option + '.html'
        m = open(m_path, 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

# 유명 촬영지
with tab6:
    # 상위 숨은명소 리스트 생성
    top_area_name = ['강원도 평창군',
                     '제주특별자치도 서귀포시',
                     '부산광역시 중구',
                     '서울특별시 종로구']
    i = '6'

    # 데이터 로드
    df_map1 = pd.read_csv('data/지역별 촬영지 위치정보.csv', encoding='utf-8', index_col=0)

    # 레이아웃 구성
    con1, con2, sb = st.columns([2, 2, 1])

    with con1:
        st.subheader('전국 단계구분도')
        m = open('data/' + i + ' 전국 단계구분도.html', 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

    with sb:
        option = st.selectbox('지역 선택', top_area_name)
        st.caption('지역 선정 기준')
        st.caption('- 지역별 관광 인프라 수')
        st.caption('- 면적')

    with con2:
        st.subheader('지역별 지도')
        m_path = 'data/' + i + ' ' + option + '.html'
        m = open(m_path, 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

# 숙박업소
with tab7:
    # 상위 숨은명소 리스트 생성
    top_area_name = ['제주특별자치도 제주시',
                     '제주특별자치도 서귀포시',
                     '서울특별시 중구',
                     '부산광역시 중구']
    i = '7'

    # 데이터 로드
    df_map1 = pd.read_csv('data/지역별 숙박업소 위치정보.csv', encoding='utf-8', index_col=0)

    # 레이아웃 구성
    con1, con2, sb = st.columns([2, 2, 1])

    with con1:
        st.subheader('전국 단계구분도')
        m = open('data/' + i + ' 전국 단계구분도.html', 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)

    with sb:
        option = st.selectbox('지역 선택', top_area_name)
        st.caption('지역 선정 기준')
        st.caption('- 지역별 관광 인프라 수')
        st.caption('- 면적')

    with con2:
        st.subheader('지역별 지도')
        m_path = 'data/' + i + ' ' + option + '.html'
        m = open(m_path, 'r', encoding='utf-8')
        source_code = m.read()
        components.html(source_code, height=700)