import numpy as np
import pandas as pd
from scipy.integrate import odeint

# Parameter PLTMH 100 kW
H = 2.0 # Inersia lebih besar karena generator 100 kW
D = 2.0 # Damping naik
Pm = 100000 # Daya mekanik turbin [W]
f0 = 50.0
dt = 0.01 # 100 Hz
T = 1200 # 20 menit biar dataset lebih kaya = 120.000 baris

def swing_eq(f, t, Pbeban, Pballast):
    Pe = Pbeban + Pballast
    dfdt = (Pm - Pe - D*(f - f0)) / (2*H)
    return dfdt

t = np.arange(0, T, dt)
# Beban dibuat random tapi ada pola harian: pagi rendah, malam tinggi
base = 30000 + 40000*np.sin(2*np.pi*t/(T/2)) # 30-70 kW naik turun
noise = np.random.uniform(-10000, 10000, len(t))
Pbeban_profile = np.clip(base + noise, 0, 100000)
Pbeban_profile = np.convolve(Pbeban_profile, np.ones(200)/200, mode='same')

# Ballast di-random 0-100kW untuk eksplorasi ruang state
Pballast_profile = np.random.uniform(0, 100000, len(t))

f = np.zeros(len(t)); f[0] = 50.0
for i in range(1, len(t)):
    f[i] = odeint(swing_eq, f[i-1], [0, dt], args=(Pbeban_profile[i], Pballast_profile[i]))[-1]

df = pd.DataFrame({'t': t, 'f': f, 'P_beban': Pbeban_profile, 'P_ballast': Pballast_profile})
df.to_csv('data_pltmh_100kW.csv', index=False)
print("Dataset 100kW saved:", df.shape)