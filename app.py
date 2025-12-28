
import streamlit as st
st.set_page_config(page_title="Enterprise Billing System", layout="wide")
menu=st.sidebar.radio("Menu",["Customers","Items","Branches","Warehouses","Purchase","Sales","Sales Return","Reports","AI Dashboard","Invoice PDF"])
if menu=="Customers": from pages.customers import show; show()
elif menu=="Items": from pages.items import show; show()
elif menu=="Branches": from pages.branches import show; show()
elif menu=="Warehouses": from pages.warehouses import show; show()
elif menu=="Purchase": from pages.purchase import show; show()
elif menu=="Sales": from pages.sales import show; show()
elif menu=="Sales Return": from pages.returns import show; show()
elif menu=="Reports": from pages.reports import show; show()
elif menu=="AI Dashboard": from ai.dashboard import show; show()
elif menu=="Invoice PDF": from pages.invoice import show; show()
