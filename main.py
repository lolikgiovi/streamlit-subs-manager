import streamlit as st
from subscription_manager import SubscriptionManager, Application

# Initialize session state to store our subscription manager
if 'subscription_manager' not in st.session_state:
    st.session_state.subscription_manager = SubscriptionManager()
subs = st.session_state.subscription_manager

st.title("Subscription Manager")

all_subs, add_subs = st.tabs(["All Subscriptions", "Add Subscription"])

with all_subs:
    active_subs_data = subs.list_applications("all")
    if active_subs_data:
        subs_name, subs_price, due_days = st.columns(3)
        with subs_name:
            st.write("Subscription")
            for sub in active_subs_data:
                st.write(sub['name'])

        with subs_price:
            st.write("Price")
            for sub in active_subs_data:
                st.write(f"Rp {sub['price']:,}".replace(',', '.'))
        
        with due_days:
            st.write("Due Days")
            for sub in active_subs_data:
                st.write(f"{sub['due_days']}")

        st.subheader("Subscription Action")
        name, action = st.columns(2)
        with name:
            selected_sub = st.selectbox("Select Subscription", [sub["name"] for sub in active_subs_data])

        with action:
            selected_action = st.selectbox("Action", ["Pay Subscription", "Cancel Subscription"])
        
        if st.button("Confirm Action"):
            for sub in subs.applications:
                if sub.name == selected_sub and selected_action == "Pay Subscription":
                    subs.pay_subscription(sub)
                    st.rerun()
                elif sub.name == selected_sub and selected_action == "Cancel Subscription":
                    subs.remove_application(sub)
                    st.rerun()

    else:
        st.write("No active subscriptions")

with add_subs:
    name = st.text_input("Name")
    price = st.number_input("Price", step=1000, min_value=1000, value=10000, format="%d")
    due_date = st.number_input("Due Date", step=1, min_value=1, value=1, format="%d")

    submit_btn = st.button("Add new subscription")

    if submit_btn:
        new_application = Application(name, price, due_date)
        subs.add_application(new_application)
        
        st.rerun()

