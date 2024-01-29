import streamlit as st


score = 0
attempt = 0
reset = False


st.header('Guess the Animal!')

questions = ["Which bear lives at the North Pole?" ,              
             "Which is the fastest land animal? ",
             "Which is the largest animal?  "
             ]
options =[[" kangaroo", "polar bear", "shark", "panda."],
          ["panther","buffalo", "cheetah", "tiger"],
           ["elephant", "giraffe","rhino","blue whale"]]


answers = ['polar bear', 'cheetah', 'blue whale']

def ask(question, options):
    
    st.write(question)
    answer = st.radio("Select answer", options=options)
    return answer

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
    for answer, question in enumerate(questions):

        guess = ask(questions[answer],options[answer] )
        

    if guess:
        check_guess(guess, answers[answer])
    check_results()

def check_results():
    global reset
    column1, column2 = st.columns([.8, .2])
    with column1:
      
        with st.expander("Check Your Score!"):
            if (score/len(questions))*100 >= 80:
                st.info("\nCongratulations you have successfully passed the test")
            elif ((score/len(questions))*100 < 80) and ((score/len(questions))*100 >= 50):
                st.info("\nYou can do better than that!\nPlease try again!")
            else:
                st.warning("Sorry, you have failed the test")
            st.write(f"Your score is: **{str(score)}/{str(len(questions))}** ")
            st.write(f"Which is: **{str(round(score/len(questions)*100, 2))}%**")
    with column2:
        if st.button("Reset"):
            reset = True
            



if __name__ == "__main__":
   
    play_game()
    
    

     
        
    
