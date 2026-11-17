import matplotlib.pyplot as plt
import numpy as np

f = 200
T = 1 / f
t = np.linspace(0, 3 * T, 1000)
Vcc = 10.0

Vo = np.where(np.sin(2 * np.pi * f * t) >= 0, Vcc, 0)
Vc = (Vcc / 2) + (Vcc / 6) * np.sin(2 * np.pi * f * t - np.pi / 2)

peak_indices = []
for i in range(1, len(Vc) - 1):
  if (Vc[i] > Vc[i - 1] and Vc[i] > Vc[i + 1]) or (
      Vc[i] < Vc[i - 1] and Vc[i] < Vc[i + 1]
  ):
    peak_indices.append(i)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle(
    "Prática 4.2 - Oscilador Astável com 555", fontsize=12, weight="bold"
)

ax1.plot(
    t * 1e3, Vc, label="VC1 (Canal 1 - Tensão no Capacitor)", color="purple"
)
ax1.axhline(
    (2 / 3) * Vcc, color="gray", linestyle="--", label="2/3 Vcc (6.67V)"
)
ax1.axhline(
    (1 / 3) * Vcc, color="gray", linestyle=":", label="1/3 Vcc (3.33V)"
)
ax1.set_ylabel("Tensão (V)")
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right")

ax2.plot(
    t * 1e3, Vo, label="Vo (Canal 2 - Saída do Temporizador)", color="blue"
)
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.set_ylim(-1, 12)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right")

for idx in peak_indices:
  t_val = t[idx] * 1e3
  ax1.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)
  ax2.axvline(t_val, color="green", linestyle="--", alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.show()