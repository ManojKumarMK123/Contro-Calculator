import streamlit as st
st.set_page_config(layout="wide",page_icon = 'Cartoon2.png')
st.markdown(
        r"""
        <style> 
        MainMenu {visibility: hidden;}
        .stAppDeployButton {
                visibility: hidden;
            }
        footer{visibility: hidden;}
        </style>
        """, unsafe_allow_html=True
    )
st.image('Cartoon1.jpg',width=None)
default_value_goes_here = 0
user_input = st.number_input("enter the number of members ",default_value_goes_here)

members = []
if user_input:
    # st.info(user_input)
    i=0
    while i<user_input:
        user_input = int(user_input)
        name = st.text_input(f"Enter the name of member {i+1}",key=f"input_text{i+1}")
        contro = st.number_input(f"enter amount of contro of member {i+1}",key=f"input_number{i+1}",value=None)
        members.append((contro, name))
        i+=1
    button1 = st.button('Next')
    if button1:
        # Printing the details
        total = sum(contro for contro, _ in members)
        j=0
        for contro, name in members:
            st.write(f"{name} {contro}",key=f"printing{j}")
            j+=1
        st.info(f"\nThe total expenditure of the trip is {round(total,2)}")
        per_head = total / user_input
        st.info(f"Contro per head: {round(per_head,2)}\n")

        for i in range(user_input):
            diff = per_head - members[i][0]
            members[i] = (diff, members[i][1])  # Update with the difference

        st.subheader("Difference with respect to per head:")
        for contro, name in members:
            if contro > 0:
                st.info(f"{name} spent {round(contro,2)} less than per head on the trip")
            else:
                st.info(f"{name} spent {round(-contro,2)} more than per head on the trip")

        # Sorting the list of tuples
        members.sort(key=lambda x: x[0])

        st.subheader("RESULT")

        fst = 0
        lst = user_input - 1

        while fst < lst:
            positive_first = max(0, -members[fst][0])

            if positive_first == members[lst][0]:
                st.success(f"{members[lst][1]} will give {round(members[fst][0] * -1,2)} to {members[fst][1]}")
                members[fst] = (0, members[fst][1])
                members[lst] = (0, members[lst][1])
                fst += 1
                lst -= 1
            elif positive_first > members[lst][0]:
                st.success(f"{members[lst][1]} will give {round(members[lst][0],2)} to {members[fst][1]}")
                members[fst] = (members[fst][0] + members[lst][0], members[fst][1])
                members[lst] = (0, members[lst][1])
                lst -= 1
            else:
                st.success(f"{members[lst][1]} will give {round(members[fst][0] * -1,2)} to {members[fst][1]}")
                members[lst] = (members[lst][0] + members[fst][0], members[lst][1])
                members[fst] = (0, members[fst][1])
                fst += 1
        st.markdown('### Thanks for using Apka Hissa \U0001F600')
