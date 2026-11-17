import matplotlib.pyplot as plt
import numpy as np

# Parâmetros do circuito
Vcc = 10.0
R1 = 10e3
R2 = 66e3
C1 = 10e-6
V_OH = Vcc     # ideal; com LEDs a saída alta fica abaixo de Vcc

t_H = np.log(2) * (R1 + R2) * C1
t_L = np.log(2) * R2 * C1
T = t_H + t_L
f = 1 / T
duty = 100 * t_H / T

V_low = Vcc / 3
V_high = 2 * Vcc / 3

# Regime permanente: carga por R1+R2 (1/3 -> 2/3 Vcc), descarga por R2
t = np.linspace(0, 3 * T, 3000)
phase = t % T
charging = phase < t_H
Vo = np.where(charging, V_OH, 0.0)
Vc = np.where(
    charging,
    Vcc - (Vcc - V_low) * np.exp(-phase / ((R1 + R2) * C1)),
    V_high * np.exp(-(phase - t_H) / (R2 * C1)),
)

print(f"tH = {t_H * 1e3:.0f} ms  (LED verde aceso)")
print(f"tL = {t_L * 1e3:.0f} ms  (LED vermelho aceso)")
print(f"T = {T * 1e3:.0f} ms  ->  f = {f:.3f} Hz,  duty = {duty:.1f}%")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle("Prática 4.2 - Oscilador Astável com 555",
             fontsize=12, weight="bold")

ax1.plot(t, Vc, color="purple", label="VC1 (Canal 1 - capacitor)")
ax1.axhline(V_high, color="gray", linestyle="--", label="2/3 Vcc = 6,67 V")
ax1.axhline(V_low, color="gray", linestyle=":", label="1/3 Vcc = 3,33 V")
ax1.set_ylabel("Tensão (V)")
ax1.set_ylim(0, 11)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right", fontsize=8)

ax2.plot(t, Vo, color="blue",
         label=f"Vo (Canal 2 - pino 3)  f ≈ {f:.3f} Hz")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (s)")
ax2.set_ylim(-1, 12)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right", fontsize=8)
ax2.text(t_H / 2, 10.5, f"tH = {t_H * 1e3:.0f} ms\n(verde)",
         ha="center", fontsize=8)
ax2.text(t_H + t_L / 2, 0.5, f"tL = {t_L * 1e3:.0f} ms\n(vermelho)",
         ha="center", fontsize=8)

for idx in np.flatnonzero(np.diff(Vo)) + 1:
    for ax in (ax1, ax2):
        ax.axvline(t[idx], color="green", linestyle="--",
                   alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.savefig(__file__.replace(".py", ".png"), dpi=120)
plt.show()
