import streamlit as stm

headerSection=stm.container()
midelSection=stm.container()
leftNav=stm.sidebar


with headerSection:
    stm.title("WebApp")
    stm.markdown("-------------")
    stm.markdown("***This is a test Streamlit Web App***")
    stm.markdown("____________________________")

with midelSection:
    left_col,midel_col,right_col=stm.columns(3)

    with left_col:
        stm.title("Az")
        container=stm.container()
        container.write("This is Out side of container")
        stm.write("ABC")
        
    with midel_col:
        stm.title("B")
        stm.write("D E F")

    with right_col:
        stm.title("D")
        container=stm.container()
        container.write("This is inside Container")
        
        
        
        
with leftNav:
    stm.title("Main Menu")
    stm.button("Home",on_click=lambda:stm.success("Home"))
    stm.button("Profile",on_click=lambda:stm.success("Profile"))
    stm.button("About Us",on_click=lambda:stm.success("About us"))
    stm.button("CDC",on_click=lambda:stm.success("CDC"))







