import streamlit as st

st.title("🧪AI 과학 탐구 메이트")

with st.sidebar:
  st.header("프로필")
  age = st.select_slider("연령대", ["중학생", "고1", "고2", "고3", "성인"], value = "고2")
  career_goal = st.text_input("진로 희망")
  field = st.radio("관심 분야", ["물리", "화학", "생명과", "지구과학"])

def page_research():
  st.title("최신 연구&학술 동향")
  st.info("선택하신 분야를바탕으로 최신트렌드와 논문 이슈를 탐색합니다.")
  st.markdown("---")
  if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "당신은 과학 전문 연구원입니다. 사용자가 검색하는 연구 동향에 대해 최근 가장 주목받는 연구 트렌드 ToP3, 핵심 학술 논문 및 주요 기술 키워드, 이 연구가 사회 및 산업에 미치는 영향을 요약 정리해서 알려주세요."}
        ]
        
  for message in st.session_state.messages:
      if message["role"] != "system":
          with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
  question = st.chat_input("검색하기")
  if question:
      st.session_state.messages.append({"role": "user", "content": question})
      with st.chat_message("user"):
          st.markdown(question)
      with st.chat_message("assistant"):
          prompt = st.session_state.messages
          with st.spinner("최신 연구 트렌드와 연구 동향 요약 중...🌐"):
              response = ai_client.chat.completions.create(
                  model="gpt-5.4-mini",
                  messages=prompt)
              ai_response = response.choices[0].message.content
              st.markdown(ai_response)
      st.session_state.messages.append({"role": "assistant", "content": ai_response})

def page_mentoring():
  st.title("나이&진로 맞춤형 탐구 설계 조언"
  st.info("사이드바에 입력하신 프로필을 바탕으로, 학년 수준에 맞는 탐구 로드맵을 제공합니다.")
  st.markdown("---")
  with st.container(border=True):
    st.subheader("프로필")
    st.markdown(f"""
    * **연령대:** {age}
    * **진로 희망:** {career_goal}
    * **관심 분야:** {field}
    st.subheader("탐구 고민 작성")
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "당신은 고등학교 및 대학교 과학 탐구활동 전문 입시/학술 컨설턴트 입니다. 사용자의 학년 수준에서 스스로 수행할 수 있는 구체적인 탐구 주제 3가지를 추천하고, 진로와 직접적으로 연계되는 생활기록부 세특 강조 포인트를 짚어준 다음,
             학교 실험실이나 집(컴퓨터)에서 직접 해볼 수 있는 실험/데이터 분석 방법을 조언해 주세요."}]
        
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
    question = st.chat_input("진로와 과학 탐구와 관련해서 궁금한 점을 입력하세요.")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            status_context = f"사용자의 연령대: {age}, 사용자의 진로: {career_goal}"
            prompt = st.session_state.messages + [{"role": "system", "content": status_context}]
            with st.spinner("AI 코치가 생각 중...🤔"):
                response = ai_client.chat.completions.create(
                    model="gpt-5.4-mini",
                    messages=prompt)
                ai_response = response.choices[0].message.content
                st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

    pg = st.navigation([
      st.Page(page_research, title="자료 탐색"),
      st.Page(page_mentoring, title="조언 구하기")], position="top")
    pg.run()
