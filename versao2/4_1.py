import matplotlib.pyplot as plt
import numpy as np

# Parâmetros do circuito
Vcc = 10.0
R1 = 47e3
C1 = 100e-6
V_OH = Vcc     # ideal; com LED a saída fica perto de Vcc - 1,5 V

t_pulse = 1.1 * R1 * C1
tau = R1 * C1

t_trigger = 1.0
t_end = t_trigger + t_pulse
t = np.linspace(0, 8, 4000)

on = (t >= t_trigger) & (t < t_end)
Vo = np.where(on, V_OH, 0.0)

# Capacitor carrega por R1 até 2/3 Vcc; depois o pino 7 descarrega C1
Vc = np.zeros_like(t)
Vc[on] = Vcc * (1 - np.exp(-(t[on] - t_trigger) / tau))

print(f"tau = {tau:.2f} s")
print(f"t = 1,1·R1·C1 = {t_pulse:.2f} s")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle("Prática 4.1 - Temporizador Monoestável com 555",
             fontsize=12, weight="bold")

ax1.plot(t, Vo, color="blue", label="Vo (pino 3) - LED aceso em nível alto")
ax1.set_ylabel("Tensão (V)")
ax1.set_ylim(-1, 12)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(loc="upper right", fontsize=8)
ax1.annotate("", xy=(t_trigger, 11), xytext=(t_end, 11),
             arrowprops=dict(arrowstyle="<->", color="black"))
ax1.text((t_trigger + t_end) / 2, 11.2, f"t = {t_pulse:.2f} s",
         ha="center", fontsize=9, weight="bold")

ax2.plot(t, Vc, color="red", label="Vc (capacitor C1)")
ax2.axhline(2 / 3 * Vcc, color="gray", linestyle="--",
            label="2/3 Vcc = 6,67 V")
ax2.set_ylabel("Tensão (V)")
ax2.set_xlabel("Tempo (s)")
ax2.set_ylim(-1, 12)
ax2.grid(True, linestyle="--", alpha=0.6)
ax2.legend(loc="upper right", fontsize=8)

for ax in (ax1, ax2):
    for x in (t_trigger, t_end):
        ax.axvline(x, color="green", linestyle="--", alpha=0.8, linewidth=1.2)

plt.tight_layout()
plt.savefig(__file__.replace(".py", ".png"), dpi=120)
plt.show()
