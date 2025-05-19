import streamlit as st
import requests

st.title("📝 장기자랑 심사 점수 입력")

# ▶ 심사위원 10명 리스트
judge_names = [
    "김기철", "변재은", "이은", "강민영", 
    "상희원", "임은지", "임철환", "김채울",
    "우현주", "함보현"
]

# ▶ 팀명 및 소개 정보
team_info = {
    "1번 깍두기 카라멜":   "2220 장하은, 2508 박아원, 2513 신혜진",
    "2번 등산하러갈래":   "2108 오정민, 2505 김다혜, 2610 이민지, 2616 조민지, 2718 전소영, 2803 김수린, 2821 지윤서",
    "3번 패트와 매트": "2609 윤다인, 2618 지승주",
    "4번 충치":   "2714 이승현, 2720 조한결, 2810 송유민, 2818 이효빈, 2820 임수민",
    "5번 82 party":    "2118 지승현, 2818 이효빈",
    "6번 구름이": "2519 형립정",
    "7번 유트와 예트":    "2606 안예은, 2608 유승연",
    "8번 딜라이트":   "2107 오연주, 2516 이지희, 2519 형립정"
}

team_names = list(team_info.keys())

# 1) 심사위원 선택
judge = st.selectbox("당신의 이름을 선택하세요", judge_names)
st.markdown(f"### {judge}님, 팀별 점수를 입력해 주세요")

# 2) 각 팀별 점수 입력 (라벨에 팀 소개 포함)
scores = {}
for team in team_names:
    label = f"- {team} ({team_info[team]}) 점수"
    scores[team] = st.selectbox(label, options=list(range(1, 11)), index=4)

# 3) 제출
if st.button("제출"):
    payload = {
        "judge": judge,
        "scores": scores
    }
    try:
        resp = requests.post("https://script.google.com/macros/s/AKfycbz50zQyhF7Rvy4mVGZC2M7kM7htmbRuSV6gPHk6gppqmfIf0uvVhmwkCrTTduTlL5TotA/exec", json=payload, timeout=5)
        if resp.status_code == 200:
            result = resp.json()
            if result.get("status") == "success":
                st.success("✅ 점수가 성공적으로 전송되었습니다!")
            else:
                st.error(f"❌ 전송 실패: {result.get('message', resp.text)}")
        else:
            st.error(f"❌ HTTP 오류: 상태 코드 {resp.status_code}")
    except Exception as e:
        st.error(f"⚠️ 오류 발생: {e}")
