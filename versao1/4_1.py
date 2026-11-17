import matplotlib.pyplot as plt
import numpy as np

Vcc = 10.0
t_pulse = 2.0  # ms
t = np.linspace(0, 5, 1000)

Vo = np.where((t >= 1.0) & (t <= 1.0 + t_pulse), Vcc, 0.0)

Vc = np.zeros_like(t)
for i, ti in enumerate(t):
  if ti < 1.0:
    Vc[i] = 0.0
  elif ti <= 1.0 + t_pulse:
    tau = t_pulse / 1.1
    Vc[i] = (2 / 3 * Vcc) * (1 - np.exp(-(ti - 1.0) / (tau * 0.5)))
  else:
    Vc[i] = 0.0

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle(
    "Prática 4.1 - Temporizador Monoestável com 555",
    fontsize=12,
    weight="bold",
)

ax1.plot(t, Vo, label="Vo (Saída do Temporizador - Pino 3)", color="blue")
ax1.set_ylabel("Tensão (V)")
ax1.set_ylim(-1, 12)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right")

ax1.annotate(
    f"Vcc = {Vcc}V",
    xy=(2.0, Vcc),
    xytext=(2.5, Vcc + 0.5),
    arrowprops=dict(facecolor="blue", shrink=0.05, width=1, headwidth=4),
    fontsize=9,
    color="blue",
    weight="bold",
)

ax2.plot(t, Vc, label="Vc (Tensão no Capacitor C1)", color="red")
ax2.axhline(
    (2 / 3) * Vcc,
    color="gray",
    linestyle="--",
    label="2/3 Vcc (6.67V - Limiar)",
)
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.set_ylim(-1, 12)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right")

# Linhas verticais verdes de referência (início e fim do pulso)
ax1.axvline(
    1.0, color="green", linestyle="--", alpha=0.8, linewidth=1.2, label="Início"
)
ax2.axvline(1.0, color="green", linestyle="--", alpha=0.8, linewidth=1.2)
ax1.axvline(
    3.0, color="green", linestyle="--", alpha=0.8, linewidth=1.2, label="Fim"
)
ax2.axvline(3.0, color="green", linestyle="--", alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.show()