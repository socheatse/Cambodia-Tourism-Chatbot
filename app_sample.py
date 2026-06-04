import streamlit as st

st.title("SimpleRNN Chatbot 🤖")
st.write("Cambodia Tourism Chatbot - Demo")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_input("You:", key="input")

# Send button
if st.button("Send"):
    if user_input.strip() != "":
        # Simple demo response
        demo_responses = {
            "angkor": "Angkor Wat is in Siem Reap, Cambodia",
            "food": "Try Khmer curry and fish amok!",
            "visit": "Best time is November to February",
            "safe": "Yes, Cambodia is generally safe for tourists",
            "phnom penh": "Phnom Penh is the capital city"
        }
        
        # Match keywords for demo
        response = "I'm a SimpleRNN chatbot. Ask about Angkor Wat, food, visit time, safety, or Phnom Penh!"
        for keyword, answer in demo_responses.items():
            if keyword in user_input.lower():
                response = answer
                break
        
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

# Display chat history
st.subheader("Conversation")

for speaker, text in st.session_state.history:
    if speaker == "You":
        st.write(f"🧑 You: {text}")
    else:
        st.write(f"🤖 Bot: {text}")

# Clear & End buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🧹 Clear Chat"):
        st.session_state.history = []
        st.rerun()

with col2:
    if st.button("❌ End Chat"):
        st.session_state.history = []
        st.write("Chat ended. Refresh to start again.")
