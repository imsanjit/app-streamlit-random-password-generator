import streamlit as st
import random
import string
import pandas as pd


def password_Generator(password_Length, number_Of_Password):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    pass_list = []
    for _ in range(0, number_Of_Password):
        char_U = random.choice(string.ascii_uppercase)
        char_L = random.choice(string.ascii_lowercase)
        char_D = random.choice(string.digits)
        char_P = random.choice(string.punctuation)
        main_char = char_D + char_U + char_L + char_P
        password = main_char
        for _ in range(0, password_Length-4):
            pass_char = random.choice(chars)
            password += pass_char
        pass_list.append(password)
    return pass_list
        

def main():
    st.title('Random Password Generator')
    st.subheader('Add password char length and number of password you need...')
    password_Length = st.number_input('Enter password Length', 4, 30)
    # st.write(password_Length)
    number_Of_Pass = st.number_input('Enter number of password you need', 1, 50)
    # st.write(number_Of_Pass)
    if st.button('Generate'):
        random_password = password_Generator(password_Length, number_Of_Pass)
        df = pd.DataFrame(random_password, columns = ['Passwords'])
        st.dataframe(df)
 
    st.write('Password char length min:4 and max:30.')
    st.write('Generates 50 max passwords. ')



if __name__ == '__main__':
    main()