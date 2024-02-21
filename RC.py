#Rico Rachmad Maulana
#210322607316
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
  
x=st.slider('Pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y=st.slider('Set nilai', 0.0, 10.0, 6.0)
st.write('nilai y:', y)

t=np.linspace(x[0]*np.pi,x[1]*np.pi,100)
u=np.sin(y*t)
#st.write('nilai t:', t)

fig, ax = plt.subplots(figsize=(16,8))
ax.plot(t, u, label='sin(t)', color='b') #Plotting sin(t) curve
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

#FUNGSI kUADRAT 
def f(x):
  a=18
  b=9
  c=3
  return a*x**2 + b*x - c

x=st.slider('Pilih rentang', -20, 20, (5, 10))
st.write('nilai x:', x)

t=np.linspace(x[0],x[1],100)
u=f(t)

fig, ax = plt.subplots(figsize=(16,8))
ax.plot(t, u, label=r'$18x^2 + 9x - 3$', color='b') #Plotting sin(t) curve
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

#INTEGRAL
# Fungsi kuadrat
def f(x):
    a = 18
    b = 9
    c = 3
    return a * x ** 2 + b * x - c

t = np.linspace(x[0], x[1], 100)
u = f(t)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label=r'$18x^2 + 9x - 3$', color='b')  # Plotting kurva fungsi kuadrat

# Menghitung integral dari fungsi kuadrat dalam rentang yang dipilih
integral_value = np.trapz(u, t)
st.write("Nilai integral fungsi kuadrat dalam rentang yang dipilih:", integral_value)

# Plotting arsiran di bawah kurva fungsi kuadrat untuk menandakan integral
ax.fill_between(t, u, color='skyblue', alpha=0.5)

ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)
