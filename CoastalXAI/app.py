import streamlit as st

# ====================================
# CONFIG
# ====================================

st.set_page_config(

    page_title="CoastalXAI",

    layout="wide",

    initial_sidebar_state="expanded"

)



# ====================================
# IMPORTS
# ====================================

from utils.session import (

    init_session_state,

    is_logged_in

)


from styles.theme import (

    get_glass_css

)


from auth.login import (

    show_login

)


from auth.register import (

    show_register

)


from views.land2 import (

    show_landing

)


from views.dashboard import (

    show_dashboard

)


from views.prediction import (

    show_prediction

)


from views.explainability import (

    show_explainability

)


from views.reports import (

    show_reports

)


from views.comparison import (

    show_comparison

)


from views.simulations import (

    show_simulations

)


from views.settings import (

    show_settings

)




# ====================================
# SESSION
# ====================================

init_session_state()



if "show_auth" not in st.session_state:

    st.session_state.show_auth = False




# ====================================
# THEME
# ====================================

st.markdown(

    get_glass_css(),

    unsafe_allow_html=True

)




# ====================================
# LANDING PAGE
# ====================================



if not is_logged_in():
    if not st.session_state.get(
        "show_auth",
        False,
    ):
        show_landing()
        st.stop()



# ====================================
# LOGIN / REGISTER
# ====================================


if not is_logged_in():


    tabs = st.tabs(

        [

            "🔐 Login",

            "📝 Register"

        ]

    )



    with tabs[0]:

        show_login()



    with tabs[1]:

        show_register()



    st.stop()




# ====================================
# MAIN APP
# ====================================


st.sidebar.markdown(

"""

# 🌊 CoastalXAI


AI Climate Intelligence

""")




page = st.sidebar.radio(

    "",

    [

        "Dashboard",

        "Prediction",

        "Explainability",

        "Reports",

        "Simulation",

        "Comparison",

        "Settings"

    ]

)




if page == "Dashboard":

    show_dashboard()




elif page == "Prediction":

    show_prediction()




elif page == "Explainability":

    show_explainability()




elif page == "Reports":

    show_reports()




elif page == "Simulation":

    show_simulations()




elif page == "Comparison":

    show_comparison()




elif page == "Settings":

    show_settings()