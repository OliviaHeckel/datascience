import streamlit as st

st.set_page_config(page_title="Award", layout="wide")

st.title("Award")

st.write("📅 Due date: 2026-07-05")

# ... (inside the main function after clicking "Submit All Evaluations")

st.divider()
            res_df = pd.DataFrame(all_final_scores).sort_values(by="Final Score", ascending=False)
            
            # Identify the winner
            winner_name = res_df.iloc[0]['Supplier']
            winner_score = res_df.iloc[0]['Final Score']

            # Celebration Header
            st.balloons()  # Built-in Streamlit animation for "fireworks/celebration" effect
            st.markdown(f"""
                <div style="text-align: center;">
                    <h1 style="color: #FFD700; font-size: 50px;">✨ 🏆 WINNER 🏆 ✨</h1>
                    <h2 style="color: #FFFFFF;">Supplier <b>"{winner_name}"</b> won the award!</h2>
                    <p style="font-size: 24px;">With a winning score of: <b>{winner_score}</b></p>
                    <h1 style="font-size: 60px;">🎆 🎇 🎆 🎇 🎆</h1>
                </div>
            """, unsafe_allow_html=True)

            # Adding "Winning Music" 
            # Note: Browsers often block autoplay. This provides a player for the user.
            st.write("### 🎶 Press Play for Winning Music!")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") 
            
            # Display the full rankings
            st.subheader("Final Rankings")
            st.dataframe(res_df, use_container_width=True)
            st.bar_chart(res_df.set_index("Supplier"))

if st.button("⬅ Home"):
    st.switch_page("main.py")
