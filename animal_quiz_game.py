import streamlit as st


score = 0



st.header('Guess the Animal!')
st.divider()
questions = ["Which bear lives at the North Pole?" ,              
             "Which is the fastest land animal? ",
             "Which is the largest animal?  "
             ]
options =[[" kangaroo", "polar bear", "shark", "panda"],
          ["panther","buffalo", "cheetah", "tiger"],
           ["elephant", "giraffe","rhino","blue whale"]]

assets = ["panda.jpg", "shark.jpg", "polar_bear.jpg", "kangaroo.jpg"]

answers = ['polar bear', 'cheetah', 'blue whale']

def ask(question, options):
    
    st.write(question)
    answer = st.radio("**Select answer:**", options=[option.capitalize() for option in options], horizontal=True)
    return answer

def show_images(imgs):
    c1,c2 = st.columns(2)
    with c1:
        st.image(imgs[0], width=350)
    
        st.image(imgs[1], width=350)
    with c2:
        st.image(imgs[2], width=200)
  
        st.image(imgs[3], width=200)

        

        


def check_guess(guess, answer):
    global score
   
   
    
    if guess.lower() == answer.lower():
        st.success("Correct answer")
        score = score + 1
        
    else:
        st.caption("__That's definetly not the answer__")
        
def play_game(): 
    for answer, question in enumerate(questions):

        guess = ask(question,options[answer] )
        if answer == 0:
            show_images(assets)
        

        if guess:
            check_guess(guess, answers[answer])
    check_results()
    

def check_results():
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
        if st.button(":blue[**Check Leaderboard**]"):
           st.caption("Coming Soon")
            



if __name__ == "__main__":
   
    play_game()
    
    

     
        
    
