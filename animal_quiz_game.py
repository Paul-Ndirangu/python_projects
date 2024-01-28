import streamlit as st

score = 0
st.header('Guess the Animal!')

questions = ["Which bear lives at the North Pole? ", 
             "Which is the fastest land animal? ",
             "Which is the largest animal? "]

answers = ['polar bear', 'cheetah', 'blue whale']


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    
    while still_guessing and attempt < len(answers):
        if guess.lower() == answer.lower():
            st.success("Correct answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < (len(answers)):
                st.warning("Sorry wrong answer. Try again")
            attempt = attempt + 1
        
           

guess = st.text_input(questions[0])   

if guess:
    check_guess(guess, answers[0])
    
if (score/len(questions))*100 >= 80:
    st.info("\nCongratulations you have successfully passed the test")
else:
    st.warning("Sorry, you have failed the test")

st.write(f"Your score is: {str(score)}/{str(len(questions))}\nWhich is: {str(score/len(questions)*100)}%")

