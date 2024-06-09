
import streamlit as st
import numpy as np
import pandas as pd

#dataframe = pd.DataFrame(
#    np.random.randn(10, 20),
#    columns=('col %d' % i for i in range(20))
#)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#st.table(dataframe)

#st.dataframe(dataframe.style.highlight_max(axis=0))

