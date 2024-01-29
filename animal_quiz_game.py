import streamlit as st

score = 0
attempt = 0

st.header('Guess the Animal!')

questions = ["Which bear lives at the North Pole? \
                A) kangaroo B) polar bear C) shark D) panda.", 
             "Which is the fastest land animal? \
                A) panther B) buffalo C) cheetah D) tiger",
             "Which is the largest animal? \
                 A) elephant B) giraffe C) rhino D) blue whale"
             ]

answers = ['polar bear', 'cheetah', 'blue whale']

def check_guess(guess, answer):
    global score
    global attempt
   
    
    if guess.lower() == answer.lower():
        st.success("Correct answer")
        score = score + 1
        
    else:
        st.warning("Sorry wrong answer. Try again")
        attempt = attempt + 1
        
def play_game():        
    for i, question in enumerate(questions):

        guess = st.text_input(question)   

        if guess:
            check_guess(guess, answers[i])
    check_results()

def check_results():
    if st.button("Check Results!"):
        if (score/len(questions))*100 >= 80:
            st.info("\nCongratulations you have successfully passed the test")
        elif ((score/len(questions))*100 < 80) and ((score/len(questions))*100 >= 50):
            st.info("\nYou can do better than that!\nPlease try again!")
        else:
            st.warning("Sorry, you have failed the test")
        st.write(f"Your score is: {str(score)}/{str(len(questions))}")
        st.write(f"Which is: {str(round(score/len(questions)*100, 2))}%")

if __name__ == "__main__":
    play_game()
