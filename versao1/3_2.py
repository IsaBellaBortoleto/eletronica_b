import matplotlib.pyplot as plt
import numpy as np

f = 200
T = 1 / f
t = np.linspace(0, 3 * T, 1000)

V_sat = 14.0
Vo = V_sat * np.sign(np.sin(2 * np.pi * f * t))
Vc = (
    5
    * np.arcsin(np.sin(2 * np.pi * f * t))
    / (np.pi / 2)
    * (10 / V_sat)
    * 0.7
)

# Encontrar picos de Vc
peak_indices = []
for i in range(1, len(Vc) - 1):
  if (Vc[i] > Vc[i - 1] and Vc[i] > Vc[i + 1]) or (
      Vc[i] < Vc[i - 1] and Vc[i] < Vc[i + 1]
  ):
    peak_indices.append(i)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle(
    "Prática 3.2 - Oscilador com Amplificador Operacional",
    fontsize=12,
    weight="bold",
)

ax1.plot(t * 1e3, Vc, label="Vc (Canal 1 - Tensão no Capacitor)", color="purple")
ax1.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax1.set_ylabel("Tensão (V)")
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right")

max_vc = np.max(Vc)
ax1.annotate(
    f"Pico: +{max_vc:.1f}V",
    xy=(t[peak_indices[0]] * 1e3, max_vc),
    xytext=(t[peak_indices[0]] * 1e3, max_vc + 1.5),
    ha="center",
    arrowprops=dict(facecolor="purple", shrink=0.05, width=1, headwidth=4),
    fontsize=9,
    color="purple",
    weight="bold",
)

ax2.plot(
    t * 1e3, Vo, label="Vo (Canal 2 - Saída Quadrada)", color="darkorange"
)
ax2.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right")

# Linhas verticais pontilhadas verdes nos picos/transições
for idx in peak_indices:
  t_val = t[idx] * 1e3
  ax1.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)
  ax2.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.show()