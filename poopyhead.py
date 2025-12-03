st.title("🧠 General Knowledge Quiz")

# Questions, options, and correct answers
questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Mahatma Gandhi"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "answer": "Canberra"
    },
    {
        "question": "Which gas do plants absorb for photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Isaac Newton"
    }
]

# Track current question + score
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "selected" not in st.session_state:
    st.session_state.selected = None

q = questions[st.session_state.q_index]

st.subheader(f"Question {st.session_state.q_index + 1} of {len(questions)}")
st.write(q["question"])

# Options
st.session_state.selected = st.radio("Choose an answer:", q["options"])

# Submit button
if st.button("Submit Answer"):
    if st.session_state.selected == q["answer"]:
        st.success("Correct! 🎉")
        st.session_state.score += 1
    else:
        st.error(f"Wrong! The correct answer is **{q['answer']}**.")

# Next question
if st.button("Next Question"):
    if st.session_state.q_index < len(questions) - 1:
        st.session_state.q_index += 1
        st.session_state.selected = None
        st.experimental_rerun()
    else:
        st.write("### 🎉 Quiz Completed!")
        st.write(f"### Your Final Score: **{st.session_state.score}/{len(questions)}**")

        # Restart button
        if st.button("Restart Quiz"):
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.selected = None
            st.experimental_rerun()
