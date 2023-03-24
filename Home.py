import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(
    page_title='숨은명소 찾아보기 ',
    page_icon=':bar_chart:',
    layout='wide', # wide,centered
    menu_items={
        'Get Help':'https://lc.multicampus.com/k-digital/#/login',   # 페이지로 이동하기
        'About':'### *난나나나솨*의 주간프로젝트 대시보드 입니다.'
    },
    initial_sidebar_state='expanded'
)



# header
st.title(": HiddenPlace Analysis")
st.markdown("##")

st.markdown(':wave: 인사말')
st.write(" 한국의 다양한 아름다운 자연경관과 역사, 문화를 만나보세요. 외국인을 위한 최적의 여행 정보를 제공하는 한국 관광 추천 사이트입니다")
st.markdown(':wave: hello!')
st.write("Discover the diverse and beautiful natural scenery, history, and culture of Korea. Our website provides optimal travel information and recommendations for foreign tourists")
st.markdown("##")
st.subheader(':pushpin: 배경')
st.write(" 대한민국은 방한여행시 외국인 재방문율이 낮은 편에 속하고, 여행수지는 2000년 이후 지금까지 한번도 적자를 벗어나지 못하였다. "
         " 또한 코로나로 인해 관광산업에 큰 타격을 맞았고 현재 코로나 회복 단계로 관광산업 또한 회복 단계에 있다. "
         "이에 정부는 제 6차 관광진흥 기본계획 (2023~2027)을 통해 국내 관광 생태계를 회복하고 관광산업을 혁신하려고 한다. ")

st.markdown("---")
df=pd.read_csv('data/연도별 외래관광객 입국 수 추이 결과.csv',index_col='Unnamed: 0')

# 레이아웃 설정
cols=st.columns((1,2))

# 왼쪽에는 표
cols[0].markdown('#### :date:연도별 외래관광객 입국 수 추이 표')
cols[0].markdown('출처 : 한국문화관광연구원')
cols[0].table(data=df)

# 오른쪽에는 선그래프
cols[1].markdown('#')
cols[1].markdown('#### :chart_with_downwards_trend:연도별 외래관광객 입국 수 추이 그래프')
# 선그래프
fig = px.line(df, x=df.index, y='인원(명)',markers=True,height=500)
fig.update_layout(
    plot_bgcolor = "rgba(200, 150, 10, 0.3)",
)
cols[1].plotly_chart(fig, use_container_width = True)
