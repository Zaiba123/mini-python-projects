import streamlit as st
import time


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("pomodoro.css")

st.write("""
# The Pomodoro App 
* Twist of extended time to allow you to watch a show in between
* adapted code from [Data Professor](http://youtube.com/dataprofessor)
""")

# Timer to help you stay focused
# Created by adapting from:
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# https://docs.streamlit.io/en/latest/api.html#lay-out-your-app

button_clicked = st.button("Start") 

study_time = 3000   #3000 seconds, 50 mins
break_time = 1200   #break time (20 minutes )

if button_clicked: 
    with st.empty():
        while study_time:
            mins, secs = divmod(study_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏲ {timer}")
            time.sleep(1)
            study_time = study_time-1
            st.success("🏆 You did awesome! Take some time for  yourself!")

    with st.empty():
        while break_time:
            # Start the break
            mins2, secs2 = divmod(break_time, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            break_time = break_time-1
            st.error("⏰ 5 minute break is over!")