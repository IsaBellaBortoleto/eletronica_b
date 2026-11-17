import matplotlib.pyplot as plt
import numpy as np

# Entrada: senoide de 100 Hz, 10 Vpp
f = 100
T = 1 / f
t = np.linspace(0, 3 * T, 3000)
Vi = 5 * np.sin(2 * np.pi * f * t)

# Ajuste V_sat e V_d com os valores medidos na bancada
V_sat = 14.0   # saturação aproximada do LM741 com ±15 V
V_d = 0.7      # queda no 1N4148

# Vo = +Vsat: diodo cortado -> divisor 22k / 10k
vt_up = V_sat * 10 / (22 + 10)
# Vo = -Vsat: diodo conduz -> análise nodal no pino 3 (22k, 10k, 4,7k + diodo)
vt_down = (-V_sat / 22 - V_d / 4.7) / (1 / 22 + 1 / 10 + 1 / 4.7)

# Comparador inversor com histerese (Vi no pino 2)
Vo = np.zeros_like(Vi)
state = V_sat
for i in range(len(Vi)):
    if state == V_sat and Vi[i] > vt_up:
        state = -V_sat
    elif state == -V_sat and Vi[i] < vt_down:
        state = V_sat
    Vo[i] = state

print(f"Vt_up   = {vt_up:+.3f} V")
print(f"Vt_down = {vt_down:+.3f} V")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle("Prática 3.1 - Comparador com Histerese (Schmitt Trigger)",
             fontsize=12, weight="bold")

ax1.plot(t * 1e3, Vi, color="blue", label="Vi (senoide 100 Hz, 10 Vpp)")
ax1.axhline(vt_up, color="gray", linestyle="--",
            label=f"Vt↑ = {vt_up:+.2f} V")
ax1.axhline(vt_down, color="gray", linestyle=":",
            label=f"Vt↓ = {vt_down:+.2f} V")
ax1.set_ylabel("Tensão (V)")
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right", fontsize=8)

ax2.plot(t * 1e3, Vo, color="red", label=f"Vo (±{V_sat:.0f} V)")
ax2.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.set_ylim(-17, 17)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right", fontsize=8)

# Linhas verticais nos instantes de comutação
for idx in np.flatnonzero(np.diff(Vo)) + 1:
    for ax in (ax1, ax2):
        ax.axvline(t[idx] * 1e3, color="green", linestyle="--",
                   alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.savefig(__file__.replace(".py", ".png"), dpi=120)
plt.show()
