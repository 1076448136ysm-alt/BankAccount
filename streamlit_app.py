import streamlit as st

#next steps
#store the data in a file

# -----------------------
# STARTING ACCOUNT DATA
# -----------------------

passwords = {
    "alice123": "pAssword",
    "bob_smith": "bobpass",
    "charlie_p": "mypass5"
}

starting_balances = {
    "alice123": 1500.00,
    "bob_smith": 3.00,
    "charlie_p": 0.00
}


# -----------------------
# SESSION STATE
# -----------------------

if "balances" not in st.session_state:
    st.session_state["balances"] = starting_balances.copy()

if "passwords" not in st.session_state:
    st.session_state["passwords"] = passwords.copy()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = None

if "mode" not in st.session_state:
    st.session_state["mode"] = None


st.title("My Bank")


# -----------------------
# LOGIN PAGE
# -----------------------

if st.session_state["logged_in"] == False:

    st.subheader("Please log in")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log in"):

        if username in st.session_state["passwords"]:

            if password == st.session_state["passwords"][username]:

                st.session_state["logged_in"] = True
                st.session_state["username"] = username

                st.rerun()

            else:
                st.error("Incorrect password.")

        else:
            st.error("Username not found.")


# -----------------------
# BANK PAGE
# -----------------------

else:

    username = st.session_state["username"]

    st.subheader("Welcome " + username)

    st.write(
        "Current balance: $"
        + str(st.session_state["balances"][username])
    )


    # -----------------------
    # MAIN MENU
    # -----------------------

    if st.session_state["mode"] is None:

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Deposit"):
                st.session_state["mode"] = "deposit"
                st.rerun()

        with col2:
            if st.button("Withdraw"):
                st.session_state["mode"] = "withdraw"
                st.rerun()

        with col3:
            if st.button("Change Password"):
                st.session_state["mode"] = "password"
                st.rerun()



    # -----------------------
    # DEPOSIT
    # -----------------------

    if st.session_state["mode"] == "deposit":

        amount = st.number_input(
            "How much would you like to deposit?",
            min_value=0.0
        )

        if st.button("Confirm Deposit"):

            st.session_state["balances"][username] += amount

            st.session_state["mode"] = None

            st.rerun()


    # -----------------------
    # WITHDRAW
    # -----------------------

    if st.session_state["mode"] == "withdraw":

        amount = st.number_input(
            "How much would you like to withdraw?",
            min_value=0.0
        )

        if st.button("Confirm Withdrawal"):

            if amount <= st.session_state["balances"][username]:

                st.session_state["balances"][username] -= amount

                st.session_state["mode"] = None

                st.rerun()

            else:

                st.warning("You do not have enough money.")


    # -----------------------
    # CHANGE PASSWORD
    # -----------------------

    if st.session_state["mode"] == "password":

        new_password = st.text_input(
            "Enter your new password",
            type="password"
        )

        if st.button("Confirm Password Change"):

            if new_password != "":

                st.session_state["passwords"][username] = new_password

                st.session_state["mode"] = None

                st.rerun()



    # -----------------------
    # LOG OUT
    # -----------------------

    if st.button("Log out"):

        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["mode"] = None

        st.rerun()