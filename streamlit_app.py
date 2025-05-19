import streamlit as st
import requests

st.title("📝 장기자랑 심사 점수 입력")

# ▶ 심사위원 10명 리스트로 조정!
judge_names = [
    "김기철", "변재은", "이은", "강민영", 
    "상희원", "임은지", "임철환", "김채울",
    "우현주", "함보현"
]
team_names = [
    "1번 깍두기 카라멜", "2번 등산하러갈래", "3번 패트와 매트", "4번 충치",
    "5번 82 party", "6번 구름이", "7번 유트와 예트", "8번 딜라이트"
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
            "AKfycbz50zQyhF7Rvy4mVGZC2M7kM7htmbRuSV6gPHk6gppqmfIf0uvVhmwkCrTTduTlL5TotA",  # ← 여기에 Apps Script 웹앱 URL (/exec) 입력
            json=payload,
            timeout=5
        )
        if resp.status_code == 200 and resp.json().status == "success":
            st.success("✅ 점수가 성공적으로 전송되었습니다!")
        else:
            st.error(f"❌ 전송 실패: {resp.text}")
    except Exception as e:
        st.error(f"⚠️ 오류 발생: {e}")
