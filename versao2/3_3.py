import matplotlib.pyplot as plt
import numpy as np

# Parâmetros
R = 10e3
C = 100e-9
R1 = 10e3      # VB -> pino 3 de U1
R2 = 20e3      # VA -> pino 3 de U1
V_sat = 14.0   # ajuste com o valor medido

VB_pk = (R1 / R2) * V_sat
f = R2 / (4 * R1 * R * C)
T = 1 / f
t = np.linspace(0, 3 * T, 3000)

# Integrador inversor: dVB/dt = -VA/RC.
# A quadrada troca exatamente nos picos do triângulo -> VA usa cos, VB usa sin.
VA = V_sat * np.sign(np.cos(2 * np.pi * f * t))
VB = -VB_pk * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * f * t))

# Conferência: com VA > 0 a rampa de VB nunca sobe
pos = (VA[:-1] > 0) & (VA[1:] > 0)
assert not np.any(np.diff(VB)[pos] > 1e-9), "fase VA/VB errada"

print(f"VA pico = ±{V_sat:.1f} V")
print(f"VB pico = ±{VB_pk:.1f} V")
print(f"f = {f:.0f} Hz  (T = {T * 1e3:.1f} ms)")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle("Prática 3.3 - Gerador de Funções (Quadrada e Triangular)",
             fontsize=12, weight="bold")

ax1.plot(t * 1e3, VA, color="green", label="VA (Canal 1 - quadrada, U1)")
ax1.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax1.set_ylabel("Tensão (V)")
ax1.set_ylim(-17, 17)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right", fontsize=8)

ax2.plot(t * 1e3, VB, color="saddlebrown",
         label="VB (Canal 2 - triangular, U2)")
ax2.axhline(VB_pk, color="gray", linestyle="--", label=f"±{VB_pk:.0f} V")
ax2.axhline(-VB_pk, color="gray", linestyle="--")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (ms)")
ax2.set_ylim(-10, 10)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right", fontsize=8)

# Linhas nas comutações de VA (= picos de VB)
for idx in np.flatnonzero(np.diff(VA)) + 1:
    for ax in (ax1, ax2):
        ax.axvline(t[idx] * 1e3, color="green", linestyle="--",
                   alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.savefig(__file__.replace(".py", ".png"), dpi=120)
plt.show()
