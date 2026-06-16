import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(layout="wide",page_icon = 'Cartoon2.png')

st.markdown("""
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
.stAppDeployButton {visibility:hidden;}
</style>
""", unsafe_allow_html=True)
st.image('Cartoon1.jpg',width=800)
st.subheader("Smart Trip Expense Splitter")

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "expense_ids" not in st.session_state:
    st.session_state.expense_ids = [0]

if "next_expense_id" not in st.session_state:
    st.session_state.next_expense_id = 1

# --------------------------------------------------
# MEMBERS
# --------------------------------------------------

member_count = st.number_input(
    "Number of Members",
    min_value=1,
    step=1
)

members = []

if member_count:

    st.header("Member Details")

    for i in range(member_count):

        name = st.text_input(
            f"Member {i+1} Name",
            key=f"member_{i}"
        )

        if name.strip():
            members.append(name.strip())

# --------------------------------------------------
# EXPENSES
# --------------------------------------------------

if len(members) == member_count:

    st.header("Expenses")

    expenses = []

    # ------------------------------------------
    # EXPENSE LOOP
    # ------------------------------------------

    for idx, expense_id in enumerate(
        st.session_state.expense_ids
    ):

        with st.container(border=True):

            col1, col2 = st.columns([10, 1])

            with col1:
                st.subheader(
                    f"Expense {idx + 1}"
                )

            with col2:

                if len(
                    st.session_state.expense_ids
                ) > 1:

                    if st.button(
                        "🗑",
                        key=f"delete_expense_{expense_id}"
                    ):
                        st.session_state.expense_ids.remove(
                            expense_id
                        )
                        st.rerun()

            expense_name = st.text_input(
                "Expense Name",
                key=f"expense_name_{expense_id}"
            )

            st.markdown("### Contributors")

            contributor_key = (
                f"contributors_count_{expense_id}"
            )

            if contributor_key not in st.session_state:
                st.session_state[
                    contributor_key
                ] = 1

            c1, c2 = st.columns(2)

            with c1:

                if st.button(
                    "➕ Add Contributor",
                    key=f"add_contributor_{expense_id}"
                ):
                    st.session_state[
                        contributor_key
                    ] += 1
                    st.rerun()

            with c2:

                if (
                    st.session_state[
                        contributor_key
                    ] > 1
                ):

                    if st.button(
                        "➖ Remove Contributor",
                        key=f"remove_contributor_{expense_id}"
                    ):
                        st.session_state[
                            contributor_key
                        ] -= 1
                        st.rerun()

            contributors = {}

            total_expense = 0

            for j in range(
                st.session_state[
                    contributor_key
                ]
            ):

                cc1, cc2 = st.columns([2, 1])

                with cc1:

                    contributor = st.selectbox(
                        f"Contributor {j+1}",
                        members,
                        key=f"contributor_person_{expense_id}_{j}"
                    )

                with cc2:

                    amount = st.number_input(
                        f"Amount {j+1}",
                        min_value=0.0,
                        step=1.0,
                        key=f"contributor_amount_{expense_id}_{j}"
                    )

                contributors[contributor] = (
                    contributors.get(
                        contributor,
                        0
                    )
                    + amount
                )

                total_expense += amount

            st.info(
                f"Total Expense Amount: ₹ {round(total_expense,2)}"
            )

            consumers = st.multiselect(
                "Consumed By",
                members,
                default=members,
                key=f"consumers_{expense_id}"
            )

            expenses.append(
                {
                    "name": expense_name,
                    "contributors": contributors,
                    "consumers": consumers,
                }
            )

    # ------------------------------------------
    # ADD EXPENSE BUTTON
    # ------------------------------------------

    st.markdown("###")

    if st.button(
        "➕ Add Expense",
        use_container_width=True
    ):

        st.session_state.expense_ids.append(
            st.session_state.next_expense_id
        )

        st.session_state.next_expense_id += 1

        st.rerun()

    # ------------------------------------------
    # CALCULATE
    # ------------------------------------------

    st.markdown("###")

    if st.button(
        "💰 Calculate Settlement",
        use_container_width=True
    ):

        paid = {
            member: 0
            for member in members
        }

        owed = {
            member: 0
            for member in members
        }

        grand_total = 0

        # -----------------------------
        # PROCESS EXPENSES
        # -----------------------------

        for expense in expenses:

            consumers = expense[
                "consumers"
            ]

            if len(consumers) == 0:
                continue

            expense_total = sum(
                expense[
                    "contributors"
                ].values()
            )

            grand_total += expense_total

            for (
                contributor,
                amount
            ) in expense[
                "contributors"
            ].items():

                paid[
                    contributor
                ] += amount

            share = (
                expense_total
                / len(consumers)
            )

            for consumer in consumers:

                owed[
                    consumer
                ] += share

        # -----------------------------
        # BALANCE
        # -----------------------------

        balance = {}

        for member in members:

            balance[
                member
            ] = round(
                paid[member]
                - owed[member],
                2
            )

        # -----------------------------
        # SUMMARY
        # -----------------------------

        st.header("Trip Summary")

        st.success(
            f"Total Expense : ₹ {round(grand_total,2)}"
        )

        summary = []

        for member in members:

            summary.append(
                {
                    "Member": member,
                    "Paid": round(
                        paid[member],
                        2
                    ),
                    "Consumed": round(
                        owed[member],
                        2
                    ),
                    "Balance": round(
                        balance[member],
                        2
                    ),
                }
            )

        st.dataframe(
            summary,
            use_container_width=True
        )

        # -----------------------------
        # SETTLEMENT
        # -----------------------------

        creditors = []
        debtors = []

        for member, amount in balance.items():

            if amount > 0:
                creditors.append(
                    [member, amount]
                )

            elif amount < 0:
                debtors.append(
                    [
                        member,
                        abs(amount)
                    ]
                )

        creditors.sort(
            key=lambda x: x[1],
            reverse=True
        )

        debtors.sort(
            key=lambda x: x[1],
            reverse=True
        )

        st.header(
            "Final Settlement"
        )

        i = 0
        j = 0

        while (
            i < len(debtors)
            and j < len(creditors)
        ):

            debtor_name = debtors[i][0]
            debtor_amt = debtors[i][1]

            creditor_name = creditors[j][0]
            creditor_amt = creditors[j][1]

            payment = min(
                debtor_amt,
                creditor_amt
            )

            st.success(
                f"💸 {debtor_name} pays ₹{round(payment,2)} to {creditor_name}"
            )

            debtors[i][1] -= payment
            creditors[j][1] -= payment

            if debtors[i][1] < 0.01:
                i += 1

            if creditors[j][1] < 0.01:
                j += 1

        st.markdown("---")
        st.markdown(
            "### Thanks for using Apka Hissa 😀"
        )
