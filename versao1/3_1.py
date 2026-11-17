import matplotlib.pyplot as plt
import numpy as np

# Parâmetros
f = 100  # 100 Hz
T = 1 / f
t = np.linspace(0, 3 * T, 1000)
Vi = 5 * np.sin(2 * np.pi * f * t)

V_sat = 14.0
Vo = np.zeros_like(Vi)
state = V_sat
vt_up = 1.0
vt_down = -1.0

for i in range(len(Vi)):
  if state == V_sat and Vi[i] > vt_up:
    state = -V_sat
  elif state == -V_sat and Vi[i] < vt_down:
    state = V_sat
  Vo[i] = state

# Encontrar pontos de comutação para as linhas verticais
switch_indices = []
for i in range(1, len(Vi)):
  if (Vi[i - 1] <= vt_up and Vi[i] > vt_up) or (
      Vi[i - 1] >= vt_down and Vi[i] < vt_down
  ):
    switch_indices.append(i)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle(
    "Prática 3.1 - Amplificador Comparador / Schmitt Trigger",
    fontsize=12,
    weight="bold",
)

# Plot Vi
ax1.plot(t * 1e3, Vi, label="Vi (Entrada Senoidal 10 Vpp)", color="blue")
ax1.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax1.set_ylabel("Tensão (V)")
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right")

# Anotações de Pico Vi
ax1.annotate(
    "Pico: +5V",
    xy=(T * 1000 * 0.25, 5),
    xytext=(T * 1000 * 0.25, 5.8),
    ha="center",
    arrowprops=dict(facecolor="blue", shrink=0.05, width=1, headwidth=4),
    fontsize=9,
    color="blue",
    weight="bold",
)
ax1.annotate(
    "Pico: -5V",
    xy=(T * 1000 * 0.75, -5),
    xytext=(T * 1000 * 0.75, -6.5),
    ha="center",
    arrowprops=dict(facecolor="blue", shrink=0.05, width=1, headwidth=4),
    fontsize=9,
    color="blue",
    weight="bold",
)

# Plot Vo
ax2.plot(t * 1e3, Vo, label="Vo (Saída Quadrada)", color="red")
ax2.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right")

# Anotações de Pico Vo
ax2.annotate(
    "+14V",
    xy=(0.5, 14),
    xytext=(1.5, 14),
    fontsize=9,
    color="red",
    weight="bold",
)
ax2.annotate(
    "-14V",
    xy=(0.5, -14),
    xytext=(1.5, -14),
    fontsize=9,
    color="red",
    weight="bold",
)

# Linhas verticais verdes de referência
for idx in switch_indices:
  t_val = t[idx] * 1e3
  ax1.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)
  ax2.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.show()