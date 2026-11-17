import matplotlib.pyplot as plt
import numpy as np

f = 500
T = 1 / f
t = np.linspace(0, 3 * T, 1000)

V_sat = 13.5
VA = V_sat * np.sign(np.sin(2 * np.pi * f * t))
VB = (
    (2 * V_sat / np.pi)
    * np.arcsin(np.sin(2 * np.pi * f * t))
    * (10 / V_sat)
    * 0.5
)

peak_indices = []
for i in range(1, len(VB) - 1):
  if (VB[i] > VB[i - 1] and VB[i] > VB[i + 1]) or (
      VB[i] < VB[i - 1] and VB[i] < VB[i + 1]
  ):
    peak_indices.append(i)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle(
    "Prática 3.3 - Gerador de Funções (Sinal Quadrado e Triangular)",
    fontsize=12,
    weight="bold",
)

ax1.plot(t * 1e3, VA, label="VA (Canal 1 - Onda Quadrada)", color="green")
ax1.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax1.set_ylabel("Tensão (V)")
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right")

ax2.plot(t * 1e3, VB, label="VB (Canal 2 - Onda Triangular)", color="saddlebrown")
ax2.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right")

max_vb = np.max(VB)
ax2.annotate(
    f"Pico: +{max_vb:.1f}V",
    xy=(t[peak_indices[0]] * 1e3, max_vb),
    xytext=(t[peak_indices[0]] * 1e3, max_vb + 1.5),
    ha="center",
    arrowprops=dict(facecolor="saddlebrown", shrink=0.05, width=1, headwidth=4),
    fontsize=9,
    color="saddlebrown",
    weight="bold",
)

for idx in peak_indices:
  t_val = t[idx] * 1e3
  ax1.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)
  ax2.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.show()