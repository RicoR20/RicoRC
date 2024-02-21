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

# Fungsi kuadrat
def f(x):
    a = 18
    b = 9
    c = 3
    return a * x ** 2 + b * x - c

x = st.slider('Pilih rentang', -20, 20, (5, 10))
st.write('nilai x:', x)

t = np.linspace(x[0], x[1], 100)
u = f(t)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label=r'$18x^2 + 9x - 3$', color='b')  # Plotting kurva fungsi kuadrat

# Menghitung integral dari fungsi kuadrat dalam rentang yang dipilih
integral_value = np.trapz(u, t)
st.write("Nilai integral fungsi kuadrat dalam rentang yang dipilih:", integral_value)

#FUNGSI TRAPESIUM INTEGRAL
def trapesium (f, a, b, n=100)
  x=np.linspace(a, b, n+1)
  y=f(x)
  h=(b-a)/n
  s=0.5*(y[0]+y[-1])+np.sum([y[1:-1])
  return h*s

# Slider untuk memilih rentang untuk integral fungsi polinomial
integral_range = st.slider('Pilih rentang untuk integral fungsi polinomial', -10.0, 10.0, (1.0, 3.0), key='integral_range')
integral_result = trapz(f(t), t)

# Tambahkan arsiran untuk area di bawah kurva pada rentang integral
t_fill = np.linspace(integral_range[0], integral_range[1], 100)
u_fill = f(t_fill)
ax.fill_between(t_fill, 0, u_fill, color='skyblue', alpha=0.4)

ax.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

st.write(f"Hasil integral dari fungsi polinomial pada rentang {integral_range} adalah: {integral_result}")

# Slider untuk memilih rentang untuk integral fungsi polinomial
integral_range = st.slider('Pilih rentang untuk integral fungsi polinomial', -10.0, 10.0, (1.0, 3.0), key='integral_range')
integral_result = trapz(f(t), t)

# Tambahkan arsiran untuk area di bawah kurva pada rentang integral
t_fill = np.linspace(integral_range[0], integral_range[1], 100)
u_fill = f(t_fill)
ax.fill_between(t_fill, 0, u_fill, color='skyblue', alpha=0.4)

ax.set_xlabel("t")
plt.grid(color='green', linestyle='-.', linewidth=.5)
st.pyplot(fig)

st.write(f"Hasil integral dari fungsi polinomial pada rentang {integral_range} adalah: {integral_result}")
