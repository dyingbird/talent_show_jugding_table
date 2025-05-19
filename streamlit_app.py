import streamlit as st
import requests

st.title("📝 팀 심사 점수 입력")

# • 심사위원 이름과 팀명 리스트를 원하는 대로 수정하세요.
judge_names = [
    "홍길동", "김철수", "이영희", "박민수", "이수진",
    "최준호", "정다은", "오승현", "강다희", "유지훈", "신예린"
]
team_names = [
    "Alpha", "Bravo", "Charlie", "Delta",
    "Echo", "Foxtrot", "Golf", "Hotel"
]

# 1) 심사위원 선택
judge = st.selectbox("당신의 이름을 선택하세요", judge_names)

st.markdown(f"### {judge} 님, 팀별 점수를 입력해 주세요")

# 2) 각 팀별 점수 입력
scores = {}
for team in team_names:
    scores[team] = st.selectbox(f"- {team} 점수", options=list(range(1, 11)), index=4)

# 3) 제출
if st.button("제출"):
    payload = {
        "judge": judge,
        "scores": scores  # { "Alpha":7, "Bravo":5, … }
    }
    try:
        resp = requests.post(
            "<<YOUR_SCRIPT_WEB_APP_URL>>",
            json=payload,
            timeout=5
        )
        if resp.status_code == 200 and resp.json().status == "success":
            st.success("✅ 점수가 성공적으로 전송되었습니다!")
        else:
            st.error(f"❌ 전송 실패: {resp.text}")
    except Exception as e:
        st.error(f"⚠️ 오류 발생: {e}")
