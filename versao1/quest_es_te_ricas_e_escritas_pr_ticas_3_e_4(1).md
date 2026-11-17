# Respostas e Fundamentação Teórica - Práticas 3 e 4
**Disciplina:** Eletrônica B - ELN76A (Turmas S15 e S16 - 2º Semestre de 2026)  
**Professor:** José Ricardo Alcântara — UTFPR  

---

## PRÁTICA 3: Amplificadores Não Lineares

### 3.1 Amplificadores Comparadores / Schmitt Trigger
* **Explicação do que acontece no circuito:**  
  O circuito utiliza o amplificador operacional LM741 com realimentação positiva. Ao aplicar um sinal senoidal (ou triangular) de $100\text{ Hz}$ com $10\text{ V}_{pp}$ na entrada ($V_i$), a saída ($V_o$) comuta de estado entre os níveis de saturação ($+V_{sat} \approx +14\text{ V}$ e $-V_{sat} \approx -14\text{ V}$) quando $V_i$ atinge os limiares de comutação $Vt\uparrow$ e $Vt\downarrow$.
  * Quando a saída está em $+V_{sat}$ ($+14\text{ V}$), o diodo $1N4148$ fica reversamente polarizado (aberto), e a tensão de comutação superior $Vt\uparrow$ é determinada pelo divisor resistivo entre $22\text{ k}\Omega$ e $10\text{ k}\Omega$.
  * Quando a saída comuta para $-V_{sat}$ ($-14\text{ V}$), o diodo $1N4148$ conduz (queda de $0,7\text{ V}$), colocando o resistor de $4,7\text{ k}\Omega$ no circuito e alterando o valor da tensão de comutação inferior $Vt\downarrow$.

* **Cálculos Teóricos ($Vt\uparrow$ e $Vt\downarrow$):**
  * **Tensão de limiar superior ($Vt\uparrow$):**
    $$\text{Calculado: } Vt\uparrow = +V_{sat} \cdot \left(\frac{10\text{ k}\Omega}{22\text{ k}\Omega + 10\text{ k}\Omega}\right) = 14 \cdot \left(\frac{10}{32}\right) = \mathbf{4,38\text{ V}}$$
  * **Tensão de limiar inferior ($Vt\downarrow$):**
    $$\text{Calculado: } Vt\downarrow \approx \mathbf{-2,38\text{ V}}$$

---

### 3.2 Oscilador
* **Explicação e Sinais Observados:**  
  O circuito opera como um oscilador onde o capacitor $C$ ($100\text{ nF}$) passa por ciclos contínuos de carga e descarga através de $R$ ($10\text{ k}\Omega$), enquanto o divisor resistivo ($R_1 = 100\text{ k}\Omega$ e $R_f = 10\text{ k}\Omega$) define os pontos de comutação da saída $V_o$.
  * **Canal 1 ($V_c$):** Tensão no capacitor.
  * **Canal 2 ($V_o$):** Onda quadrada na saída do LM741C.

* **Cálculos Teóricos (Tensões de pico, $t_H$, $t_L$ e $f$):**
  * **Fator de realimentação ($\beta$):**
    $$\beta = \frac{R_1}{R_1 + R_f} = \frac{100\text{ k}\Omega}{100\text{ k}\Omega + 10\text{ k}\Omega} = \frac{100}{110} \approx \mathbf{0,909}$$
  * **Tensões de pico:**
    $$\text{Calculado: } V_{o(\text{pico})} = \pm V_{sat} \approx \mathbf{\pm 14\text{ V}}$$
    $$\text{Calculado: } V_{c(\text{pico})} = \pm \beta \cdot V_{sat} = \pm 0,909 \cdot 14 = \mathbf{\pm 12,73\text{ V}}$$
  * **Intervalos de tempo ($t_H$ e $t_L$) e Período ($T$):**
    $$\text{Calculado: } t_H = t_L = R \cdot C \cdot \ln\left(\frac{1 + \beta}{1 - \beta}\right) = (10 \times 10^3) \cdot (100 \times 10^{-9}) \cdot \ln\left(\frac{1 + 0,909}{1 - 0,909}\right) = \mathbf{3,04\text{ ms}}$$
    $$\text{Calculado: } T = t_H + t_L = 3,04\text{ ms} + 3,04\text{ ms} = \mathbf{6,08\text{ ms}}$$
  * **Frequência de oscilação ($f$):**
    $$\text{Calculado: } f = \frac{1}{T} = \frac{1}{6,08 \times 10^{-3}} = \mathbf{164,5\text{ Hz}}$$

---

### 3.3 Gerador de Funções (Sinal Quadrado e Triangular)
* **Explicação e Sinais Observados:**  
  * **U1:** Funciona como comparador, gerando a onda quadrada $V_A$ (Canal 1).
  * **U2:** Funciona como integrador, convertendo a onda quadrada de $V_A$ em um sinal triangular $V_B$ (Canal 2).

* **Cálculos Teóricos:**
  * **Tensões de pico:**
    $$\text{Calculado: } V_{A(\text{pico})} = \pm V_{sat} \approx \mathbf{\pm 14\text{ V}}$$
    $$\text{Calculado: } V_{B(\text{pico})} = \pm \left(\frac{R_1}{R_2}\right) \cdot V_{sat} = \pm \left(\frac{10\text{ k}\Omega}{20\text{ k}\Omega}\right) \cdot 14 = \mathbf{\pm 7\text{ V}}$$
  * **Frequência de oscilação ($f$):**
    $$\text{Calculado: } f = \frac{R_2}{4 \cdot R_1 \cdot R \cdot C} = \frac{20 \times 10^3}{4 \cdot (10 \times 10^3) \cdot (10 \times 10^3) \cdot (100 \times 10^{-9})} = \mathbf{500\text{ Hz}}$$

---

## PRÁTICA 4: Temporizadores / Osciladores com 555

### 4.1 Temporizador Monoestável com CI 555
**Dados:** $V_{cc} = 10\text{ V}$, $R_1 = 47\text{ k}\Omega$, $R_2 = 10\text{ k}\Omega$, $C_1 = 100\text{ }\mu\text{F}$ e $C_2 = 10\text{ nF}$.

* **i. Cálculo do tempo $t$:**
  $$\text{Calculado: } t = 1,1 \cdot R_1 \cdot C_1 = 1,1 \cdot (47 \times 10^3) \cdot (100 \times 10^{-6}) = \mathbf{5,17}\text{ (segundos)}$$

* **ii. Sinais no $C_1$ e na saída (pino 3) e Tensão de pico do pulso:**
  * **Saída ($V_o$ - pino 3):** Permanece em $0\text{ V}$ até receber o pulso de disparo negativo (*Negative Trigger Pulse*) no pino 2, subindo para nível alto com tensão de pico próxima de $V_{cc}$ ($\mathbf{10\text{ V}}$) durante $5,17\text{ s}$.
  * **Capacitor ($V_c$ - $C_1$):** Inicia em $0\text{ V}$ e carrega-se exponencialmente até atingir o limiar de $\frac{2}{3}V_{cc}$ ($\frac{2}{3} \cdot 10\text{ V} = \mathbf{6,67\text{ V}}$), instante em que descarrega rapidamente para $0\text{ V}$.

* **iii. O que acontece com o LED:**  
  Antes do disparo, a saída (pino 3) está em $0\text{ V}$ e o LED permanece apagado. Ao acionar o disparo (*start*), a saída vai para nível alto ($V_{cc}$) e o **LED acende**, permanecendo aceso durante o tempo calculado ($5,17\text{ s}$). Ao término da temporização, a saída retorna para $0\text{ V}$ e o LED apaga.

---

### 4.2 Oscilador Astável com CI 555
**Dados:** $V_{cc} = 10\text{ V}$, $R_1 = 10\text{ k}\Omega$, $R_2 = 66\text{ k}\Omega\text{ }(33\text{ k}\Omega + 33\text{ k}\Omega)$, $C_1 = 10\text{ }\mu\text{F}/35\text{ V}$ e $C_2 = 100\text{ nF}$.

* **Sinais Observados:**
  * **Canal 1 ($V_{C1}$):** Curva do capacitor oscilando continuamente entre $\frac{1}{3}V_{cc}$ ($\mathbf{3,33\text{ V}}$) e $\frac{2}{3}V_{cc}$ ($\mathbf{6,67\text{ V}}$).
  * **Canal 2 ($V_o$):** Onda quadrada na saída do temporizador (pino 3) com tensão de pico de $\mathbf{10\text{ V}}$. Os LEDs indicadores conectados à saída piscam alternadamente conforme $V_o$ comuta entre nível alto ($+10\text{ V}$) e nível baixo ($0\text{ V}$).

* **Cálculos Teóricos (Intervalos de tempo $t_H$, $t_L$, Período $T$ e Frequência $f$):**
  * **Tempo em nível alto ($t_H$):**
    $$\text{Calculado: } t_H = 0,693 \cdot (R_1 + R_2) \cdot C_1 = 0,693 \cdot (10 \times 10^3 + 66 \times 10^3) \cdot (10 \times 10^{-6}) = \mathbf{0,527\text{ s}}\text{ (ou }\mathbf{527\text{ ms}}\text{)}$$
  * **Tempo em nível baixo ($t_L$):**
    $$\text{Calculado: } t_L = 0,693 \cdot R_2 \cdot C_1 = 0,693 \cdot (66 \times 10^3) \cdot (10 \times 10^{-6}) = \mathbf{0,457\text{ s}}\text{ (ou }\mathbf{457\text{ ms}}\text{)}$$
  * **Período total ($T$):**
    $$\text{Calculado: } T = t_H + t_L = 0,527 + 0,457 = \mathbf{0,984\text{ s}}\text{ (ou }\mathbf{984\text{ ms}}\text{)}$$
  * **Frequência de oscilação ($f$):**
    $$\text{Calculado: } f = \frac{1}{T} = \frac{1}{0,693 \cdot (R_1 + 2R_2) \cdot C} = \frac{1,44}{(10 \times 10^3 + 2 \cdot 66 \times 10^3) \cdot (10 \times 10^{-6})} = \frac{1,44}{1,42} = \mathbf{1,01\text{ Hz}}$$