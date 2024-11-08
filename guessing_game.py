import streamlit as st
import random

st.title("Guessing Game & Portfolio App")

nav = st.sidebar.radio("Navigation", ["Portfolio", "User Guessing Game", "Machine Guessing Game"])

if nav == "Portfolio":
    st.header("My Portfolio")

    st.write("Welcome to my portfolio! Here are some details about me.")
    st.write("*Name:* Angelin Kirubawahi T")
    st.write("*Skills:* Python, Html")
    st.write("*Hobbies:* Traveling")

    st.write("*Projects:*")
    st.write("1. Web Application using Streamlit")
elif nav == "User Guessing Game":
    st.header("User Guessing Game")

    st.write("In this mode, the computer will generate a random number, and you need to guess it.")
    st.write("Rules: The range is dynamically set. You have a limited number of attempts!")

    min_val = st.number_input("Enter minimum range value:", value=1, step=1)
    max_val = st.number_input("Enter maximum range value:", value=100, step=1)
    if min_val >= max_val:
        st.error("Minimum value should be less than maximum value.")
    else:
        target = random.randint(min_val, max_val)
        max_attempts = int(st.number_input("Enter the number of attempts:", value=7, step=1))

        if "user_attempts" not in st.session_state:
            st.session_state.user_attempts = 0
            st.session_state.user_success = False

        guess = st.number_input("Enter your guess:", min_value=min_val, max_value=max_val, step=1)

        if st.button("Submit Guess"):
            st.session_state.user_attempts += 1
            if guess < target:
                st.write("Too low! Try again.")
            elif guess > target:
                st.write("Too high! Try again.")
            else:
                st.session_state.user_success = True
                st.write("Congratulations! You guessed it!")
            
            if st.session_state.user_attempts >= max_attempts and not st.session_state.user_success:
                st.write("Game Over! You've used all attempts.")
                st.write(f"The correct number was {target}.")

elif nav == "Machine Guessing Game":
    st.header("Machine Guessing Game")

    st.write("In this mode, you think of a number, and the computer will try to guess it.")
    st.write("Rules: Set a range, and the computer will try to find your number using binary search.")

    min_val = st.number_input("Enter minimum range value:", value=1, step=1)
    max_val = st.number_input("Enter maximum range value:", value=100, step=1)
    if min_val >= max_val:
        st.error("Minimum value should be less than maximum value.")
    else:
         if "low" not in st.session_state:
            st.session_state.low = min_val
            st.session_state.high = max_val
            st.session_state.mid = (min_val + max_val) // 2
            st.session_state.found = False

         if not st.session_state.found:
            st.write(f"Is your number {st.session_state.mid}?")
            feedback = st.radio("Choose:", ["Too low", "Too high", "Correct"])

            if feedback == "Too low":
                st.session_state.low = st.session_state.mid + 1
            elif feedback == "Too high":
                st.session_state.high = st.session_state.mid - 1
            else:
                st.session_state.found = True
                st.write("The computer guessed your number!")

            if not st.session_state.found:
                st.session_state.mid = (st.session_state.low + st.session_state.high) // 2

         if st.session_state.low > st.session_state.high:
            st.write("Seems like something went wrong. Are you sure the number is within the range?")