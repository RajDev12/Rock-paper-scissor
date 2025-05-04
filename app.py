import streamlit as st
import random

# Function to create a beautiful header
def header():
    st.markdown("## 🎮 Rock-Paper-Scissors Game")
    st.markdown("### Choose your move and see if you can beat the computer!")
    st.markdown("---")  # Separator line for visual clarity

# Function to create a beautiful footer
def footer():
    st.markdown("---")  # Separator line for visual clarity
    st.write("Made with ❤ using Streamlit | © 2025 Your Name")

# Call the header function to display the header
header()

# Define choices and corresponding image paths
choices = {
    "Rock": "assets/rock.png",
    "Paper": "assets/paper.png",
    "Scissors": "assets/scissor.png"
}

# User selection
user_choice = st.selectbox("Choose your move:", list(choices.keys()))

# Button to play the game
if st.button("Play"):
    # Randomly select computer's choice
    computer_choice = random.choice(list(choices.keys()))
    
    # Create a three-column layout
    col1, col2, col3 = st.columns([1, 0.5, 1])  # Adjust column widths as needed
    
    # Render user's choice in the first column
    with col1:
        st.image(choices[user_choice], caption=f"You chose: {user_choice}")
    
    # Render "V/S" in the middle column
    with col2:
        st.markdown("### V/S")  # Display "V/S" text in the middle column
    
    # Render computer's choice in the third column
    with col3:
        st.image(choices[computer_choice], caption=f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        st.markdown("### It's a tie! 🤝")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.markdown("### You win! 🏆")
    else:
        st.markdown("### You lose! 😢")

# # Call the footer function to display the footer
# footer()