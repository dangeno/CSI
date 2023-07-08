'''
For the Band approximation using Numpy Poly fit

'''


import streamlit as st
import numpy as np 
import pandas as pd
import plotly as plt
import plotly.graph_objects as go

st.image('csi-pacific-logo-reverse.png', width = 150)
st.title("Band Force Fitting")

band_select = st.selectbox("Select Band Brand",
	('-- Select Data Type -- ', 'Rogue','Sorinex'))

if band_select == '-- Select Data Type -- ':
	st.subheader("Please select Band Type")
	st.stop()

if band_select == 'Rogue': 
	col_select = st.selectbox('Select Colour',
		('Orange', 'Blue', 'Red', 'Green'))
	data = pd.DataFrame()
	if col_select == 'Orange':
		data['Force'] = [4.5, 4.9, 5.4, 5.8, 6.1]
		data['Length (cm)'] = [172, 183, 196, 216, 222]
	if col_select == 'Red':
		data['Force'] = [8.3,10.2,11.8,13,15]
		data['Length (cm)'] = [168,196,216,233,255]
	if col_select == 'Green':
		data['Force'] = [16.7,18.6,21.4,22.9,26.4]
		data['Length (cm)'] = [167,179,198,207,227]
	if col_select == 'Blue':
		data['Force'] = [9.2,11.3,12.6,13.7,15.4]
		data['Length (cm)'] = [159,181,194,207,225]
	
	fit = np.polyfit(data['Length (cm)'],data['Force'],2)
	fit = pd.DataFrame(fit)
	length = data['Length (cm)']
	force = data['Force']


if band_select == 'Sorinex': 
	col_select = st.selectbox('Select Colour',
		('Orange', 'Red', 'Purple', 'Green'))

	if col_select == 'Orange':
		data = [0.4186,0.7046,0.8714,1.0882,1.2986,1.57745,1.7966,2.05345,2.2546,2.48945,2.6726,2.88545,3.0506,3.24145,3.3886,3.55745,3.6866,3.83345,3.9446]
	if col_select == 'Red':
		data = [1.7644,2.4249,2.814,3.3244,3.8252,4.498125,5.0352,5.675125,6.1852,6.792125,7.2752,7.849125,8.3052,8.846125,9.2752,9.783125,10.1852,10.660125,11.0352]
	if col_select == 'Purple':
		data = [2.2336,3.6156,4.428,5.4916,6.5328,7.927875,9.0378,10.355875,11.4028,12.643875,13.6278,14.791875,15.7128,16.799875,17.6578,18.667875,19.4628,20.395875,21.1278]
	if col_select == 'Green':
		data = [2.8756,5.3221,6.754,8.6212,10.4404,12.863425,14.7784,17.036425,18.8164,20.909425,22.5544,24.482425,25.9924,27.755425,29.1304,30.728425,31.9684,33.401425,34.5064]

	length = [102,107,110,114,118,123.5,128,133.5,138,143.5,148,153.5,158,163.5,168,173.5,178,183.5,188]
	force = data
	fit = np.polyfit(length,force,2)
	fit = pd.DataFrame(fit)



fit_x = []
for i in range(300):
	fit_x.append(i+1)

fit_x = np.array(fit_x)

fit_y = fit_x**2 *fit[0][0] + fit_x*fit[0][1] + fit[0][2]


col1, col2, col3 = st.columns(3)
with col1:
	band_length = st.number_input("Length Input", min_value = 0)
with col3: 
	if band_length is not 0: 
		st.metric('Force at Given Length (N)', round(fit_y[band_length]*9.81,2))
	else: 
		st.subheader('Enter Length')
		
st.header("Polynomial fit Plot")
fig = go.Figure()
fig.add_trace(go.Scatter(x=length, y=force,
                mode='markers',
                name='Measured Points'))
fig.add_trace(go.Scatter(x=fit_x[100:], y=fit_y[100:],
                mode='lines',
               	marker=dict(
			            color=f'{col_select}',
			            size=3),
                name='Fitted Curve'))
fig.update_layout(title = "Poly Fit Plot", 
						xaxis_title = 'Length (cm)', 
						yaxis_title = 'Relative Force (Kg)')
st.plotly_chart(fig)



