import matplotlib.pyplot as plt
import numpy as np

# Parâmetros do circuito
R = 10e3
C = 100e-9
R1 = 100e3     # pino 3 -> GND
Rf = 10e3      # saída -> pino 3
V_sat = 14.0   # ajuste com o valor medido

beta = R1 / (R1 + Rf)
V_lim = beta * V_sat
t_H = R * C * np.log((1 + beta) / (1 - beta))
T = 2 * t_H
f = 1 / T

# Simulação: dVc/dt = (Vo - Vc) / RC, comutando em ±beta*Vsat
dt = 1e-6
t = np.arange(0, 3 * T, dt)
Vc = np.zeros_like(t)
Vo = np.zeros_like(t)
Vo[0] = V_sat
Vc[0] = -V_lim

for i in range(1, len(t)):
    Vo[i] = Vo[i - 1]
    if Vo[i] == V_sat and Vc[i - 1] >= V_lim:
        Vo[i] = -V_sat
    elif Vo[i] == -V_sat and Vc[i - 1] <= -V_lim:
        Vo[i] = V_sat
    Vc[i] = Vc[i - 1] + (Vo[i] - Vc[i - 1]) / (R * C) * dt

# Conferência: período da simulação = período teórico
edges = t[np.flatnonzero(np.diff(Vo)) + 1]
assert abs((edges[2] - edges[0]) - T) / T < 0.01, "período simulado diverge"

print(f"beta = {beta:.4f}")
print(f"Vc pico = ±{V_lim:.2f} V")
print(f"tH = tL = {t_H * 1e3:.2f} ms")
print(f"T = {T * 1e3:.2f} ms  ->  f = {f:.1f} Hz")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle("Prática 3.2 - Oscilador com Amplificador Operacional",
             fontsize=12, weight="bold")

ax1.plot(t * 1e3, Vc, color="purple", label="Vc (Canal 1 - capacitor)")
ax1.axhline(V_lim, color="gray", linestyle="--",
            label=f"+βVsat = {V_lim:+.2f} V")
ax1.axhline(-V_lim, color="gray", linestyle=":",
            label=f"−βVsat = {-V_lim:+.2f} V")
ax1.set_ylabel("Tensão (V)")
ax1.set_ylim(-16, 16)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right", fontsize=8)

ax2.plot(t * 1e3, Vo, color="darkorange",
         label=f"Vo (Canal 2 - saída)  f ≈ {f:.1f} Hz")
ax2.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.set_ylim(-17, 17)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right", fontsize=8)

for te in edges:
    for ax in (ax1, ax2):
        ax.axvline(te * 1e3, color="green", linestyle="--",
                   alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.savefig(__file__.replace(".py", ".png"), dpi=120)
plt.show()
