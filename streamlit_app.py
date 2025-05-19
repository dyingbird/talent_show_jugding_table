import streamlit as st
import requests

st.title("장기 자랑 점수 입력")

# 1) 심사위원 번호 선택
judge_number = st.selectbox("심사위원 번호를 선택하세요", list(range(1,12)))

st.write(f"심사위원 {judge_number}님, 점수를 입력해주세요.")

teams = [f"팀{i}" for i in range(1,9)]
scores = {}

# 2) 각 팀별 드롭다운으로 1~10점 입력
for team in teams:
    scores[team] = st.selectbox(f"{team} 점수", options=list(range(1,11)), index=4)

if st.button("제출"):
    payload = {
        "judge": judge_number,
        "scores": [scores[t] for t in teams]  # [팀1 점수, 팀2 점수, …, 팀8 점수]
    }
    try:
        resp = requests.post("<<YOUR_SCRIPT_WEB_APP_URL>>", json=payload)
        if resp.status_code == 200:
            st.success("점수가 성공적으로 전송되었습니다! 🎉")
        else:
            st.error(f"전송 실패: 상태 코드 {resp.status_code}")
    except Exception as err:
        st.error(f"오류 발생: {err}")
