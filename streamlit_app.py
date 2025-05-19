import streamlit as st
import requests

st.title("팀별 심사 점수 입력")

teams = [f"팀{i}" for i in range(1, 9)]  # 팀1 ~ 팀8
with st.form("score_form"):
    selected_team = st.selectbox("점수를 입력할 팀을 선택하세요", teams)
    # 1번~11번 심사위원의 점수를 각각 입력받기 위한 드롭다운
    scores = {}
    for judge in range(1, 12):
        scores[judge] = st.selectbox(f"심사위원 {judge}의 점수:", list(range(1, 11)), index=0)
    submit_button = st.form_submit_button("제출")

if submit_button:
    # 전송할 데이터 구성 (팀명과 11명의 점수 목록)
    data = {
        "team": selected_team,
        "scores": [scores[j] for j in range(1, 12)]
    }
    try:
        # Apps Script 웹앱 엔드포인트로 POST 요청 전송 (JSON 형식)
        response = requests.post("<<YOUR_SCRIPT_WEB_APP_URL>>", json=data)
        if response.status_code == 200:
            st.success(f"{selected_team}의 점수가 성공적으로 전송되었습니다!")
        else:
            st.error(f"점수 전송 실패 (상태 코드: {response.status_code})")
    except Exception as e:
        st.error(f"오류 발생: {e}")
