# Respostas e Fundamentação Teórica - Práticas 3 e 4
**Disciplina:** Eletrônica B - ELN76A (Turmas S15 e S16 - 2º Semestre de 2026)  
**Professor:** José Ricardo Alcântara — UTFPR

> Valores calculados considerando $V_{sat} \approx \pm 14\text{ V}$ (LM741 alimentado com ±15 V) e queda de $0,7\text{ V}$ no diodo. Os gráficos teóricos estão nos arquivos `3_1.png` … `4_2.png`.

---

## PRÁTICA 3: Amplificadores Não Lineares

### 3.1 Amplificadores Comparadores / Schmitt Trigger

#### Coloque na folha — "Explique o que acontece no circuito"

> O LM741 está funcionando como comparador Schmitt Trigger (com realimentação positiva pelo resistor de 22 kΩ). A saída Vo fica sempre saturada, em +Vsat (≈ +14 V) ou em −Vsat (≈ −14 V), e por isso tem forma de onda quadrada.
>
> O sinal Vi entra no pino 2 (−) e é comparado com a tensão do pino 3 (+), que vem do divisor de tensão ligado na saída.
>
> Com Vo = +14 V o diodo fica cortado e o pino 3 fica em Vt↑ ≈ +4,38 V. Quando Vi sobe e passa de Vt↑, a saída vai para −14 V.
>
> Com Vo = −14 V o diodo conduz e coloca o resistor de 4,7 kΩ no circuito, e o pino 3 fica em Vt↓ ≈ −2,19 V. Quando Vi desce abaixo de Vt↓, a saída volta para +14 V.
>
> Como Vt↑ e Vt↓ são diferentes, o circuito tem histerese: ele não fica trocando de estado com pequenas variações (ruído) perto do ponto de comutação. O diodo faz os dois limiares ficarem diferentes em módulo (4,38 V e 2,19 V).

#### Detalhamento (para conferência)
* **Saída alta ($V_o = +14\text{ V}$):** o pino 3 fica positivo, o diodo 1N4148 fica cortado e o resistor de 4,7 kΩ não participa. Sobra só o divisor de 22 kΩ e 10 kΩ:
  $$Vt\uparrow = +V_{sat}\cdot\frac{10\text{ k}}{22\text{ k} + 10\text{ k}} = 14\cdot\frac{10}{32} = \mathbf{+4,38\text{ V}}$$
* **Saída baixa ($V_o = -14\text{ V}$):** o pino 3 ficaria negativo, então o diodo conduz (0,7 V) e o resistor de 4,7 kΩ entra em paralelo com o de 10 kΩ. Somando as correntes no pino 3:
  $$\frac{V_n + 14}{22\text{ k}} + \frac{V_n}{10\text{ k}} + \frac{V_n + 0,7}{4,7\text{ k}} = 0 \;\Rightarrow\; Vt\downarrow = \mathbf{-2,19\text{ V}}$$
* **Histerese:** $Vt\uparrow - Vt\downarrow \approx 6,57\text{ V}$.
* **Cuidado na bancada:** $Vt\uparrow = 4,38\text{ V}$ está perto do pico de 5 V da entrada. Se o gerador ficar abaixo de cerca de 8,8 Vpp, Vi não chega a Vt↑ e a saída para de comutar.

---

### 3.2 Oscilador
* **O que acontece:**  
  O circuito é um oscilador com amplificador operacional. A saída $V_o$ fica saturada em +14 V ou −14 V. O capacitor de 100 nF carrega e descarrega pelo resistor $R$ de 10 kΩ, seguindo uma curva exponencial (curva de carga do capacitor). O divisor $R_1 = 100\text{ k}\Omega$ e $R_f = 10\text{ k}\Omega$ coloca no pino 3 uma parte da saída ($\beta \cdot V_o$). Quando a tensão no capacitor alcança essa tensão, a saída troca de estado e o capacitor passa a carregar no sentido contrário. Isso se repete sem precisar de sinal de entrada.
  * **Canal 1 ($V_c$):** curvas de carga e descarga entre +12,73 V e −12,73 V.
  * **Canal 2 ($V_o$):** onda quadrada de ±14 V.

* **Cálculos:**
  $$\beta = \frac{R_1}{R_1 + R_f} = \frac{100}{110} = \mathbf{0,909}$$
  $$V_{o(pico)} = \pm V_{sat} \approx \mathbf{\pm 14\text{ V}} \qquad V_{c(pico)} = \pm\beta V_{sat} = \mathbf{\pm 12,73\text{ V}}$$
  $$t_H = t_L = R\,C\ln\left(\frac{1+\beta}{1-\beta}\right) = 1\text{ ms}\cdot\ln(21) = \mathbf{3,04\text{ ms}}$$
  $$T = t_H + t_L = \mathbf{6,09\text{ ms}} \qquad f = \frac{1}{T} = \mathbf{164,2\text{ Hz}}$$

  *Obs.:* a tensão no capacitor chega perto de ±12,7 V, que é quase o limite que o LM741 aceita nas entradas quando alimentado com ±15 V. Por isso os valores medidos podem ficar um pouco diferentes dos calculados.

---

### 3.3 Gerador de Funções (sinal quadrado e triangular)
* **O que acontece:**
  * **U1:** funciona como comparador (Schmitt Trigger) e gera a onda quadrada $V_A$ de ±14 V (Canal 1).
  * **U2:** funciona como integrador. Ele transforma a onda quadrada $V_A$ na onda triangular $V_B$ (Canal 2). Como o integrador é inversor, quando $V_A$ está positiva, $V_B$ desce em rampa; quando $V_A$ está negativa, $V_B$ sobe em rampa.
  * A onda triangular $V_B$ volta para a entrada do U1 pelo resistor $R_1$. Quando $V_B$ chega a ±7 V, o U1 troca de estado. Por isso a onda quadrada troca de nível exatamente nos picos da onda triangular.

* **Cálculos:**
  $$V_{A(pico)} = \pm V_{sat} \approx \mathbf{\pm 14\text{ V}}$$
  $$V_{B(pico)} = \pm\frac{R_1}{R_2}V_{sat} = \pm\frac{10}{20}\cdot 14 = \mathbf{\pm 7\text{ V}}$$
  $$f = \frac{R_2}{4\,R_1\,R\,C} = \frac{20\text{ k}}{4\cdot 10\text{ k}\cdot 10\text{ k}\cdot 100\text{ n}} = \mathbf{500\text{ Hz}}$$

---

## PRÁTICA 4: Temporizadores / Osciladores com 555

### 4.1 Temporizador Monoestável
**Dados:** $V_{cc} = 10\text{ V}$, $R_1 = 47\text{ k}\Omega$, $R_2 = 10\text{ k}\Omega$, $C_1 = 100\text{ }\mu\text{F}$, $C_2 = 10\text{ nF}$.

* **i. Tempo calculado:**
  $$t = 1,1\cdot R_1\cdot C_1 = 1,1\cdot 47\text{ k}\cdot 100\text{ }\mu\text{F} = \mathbf{5,17\text{ s}}$$
  *Obs.:* o capacitor eletrolítico de 100 µF pode variar uns 20% do valor nominal. Um tempo medido entre 4 s e 6 s ainda está coerente.

* **ii. Sinais no $C_1$ e na saída (pino 3):**
  * **Saída $V_o$ (pino 3):** fica em 0 V até apertar o botão *start*, que manda o pulso de disparo negativo (*trigger pulse*) para o pino 2. Aí a saída vai para nível alto e fica assim por cerca de 5,17 s, depois volta para 0 V. A tensão de pico do pulso deveria ser 10 V ($V_{cc}$), mas com o LED ligado o 555 entrega um pouco menos, por volta de **8,5 V**. Anotar o valor medido.
  * **Capacitor $V_c$:** começa em 0 V e carrega pelo $R_1$ (curva exponencial) até chegar em $\frac{2}{3}V_{cc} = \mathbf{6,67\text{ V}}$. Nesse momento a saída volta para 0 V e o 555 descarrega o capacitor pelo pino 7 (descarga), voltando a 0 V.

* **iii. O que acontece com o LED:**

#### Coloque na folha — "Descrever o que acontece com o Led"

> Antes do disparo a saída (pino 3) está em 0 V e o Led fica apagado.
>
> Ao apertar o botão *start*, o pulso de disparo negativo no pino 2 leva a saída para nível alto e o Led acende.
>
> O Led fica aceso enquanto o capacitor C1 carrega pelo R1 até 2/3 Vcc (6,67 V), o que leva cerca de t = 1,1·R1·C1 ≈ 5,17 s.
>
> Quando o capacitor chega em 2/3 Vcc, a saída volta para 0 V, o capacitor é descarregado pelo pino 7 e o Led apaga sozinho, mesmo que o botão já tenha sido solto. Ele só acende de novo com um novo disparo.

---

### 4.2 Oscilador Astável
**Dados:** $V_{cc} = 10\text{ V}$, $R_1 = 10\text{ k}\Omega$, $R_2 = 66\text{ k}\Omega$ (33 kΩ + 33 kΩ), $C_1 = 10\text{ }\mu\text{F}/35\text{ V}$, $C_2 = 100\text{ nF}$.

* **O que acontece:**  
  No modo astável o 555 oscila sozinho, sem precisar de disparo. O capacitor $C_1$ carrega por $R_1 + R_2$ até $\frac{2}{3}V_{cc}$ (saída em nível alto). Depois descarrega por $R_2$ pelo pino 7 até $\frac{1}{3}V_{cc}$ (saída em nível baixo). Então o ciclo recomeça.
  * **Canal 1 ($V_{C1}$):** curva do capacitor subindo e descendo entre **3,33 V** e **6,67 V**.
  * **Canal 2 ($V_o$):** onda quadrada entre 0 V e nível alto (perto de 10 V, um pouco menos por causa dos LEDs).
  * **LEDs:** o LED **verde** (ligado da saída para o GND) acende quando a saída está em nível alto, por cerca de 527 ms. O LED **vermelho** (ligado do +10 V para a saída) acende quando a saída está em nível baixo, por cerca de 457 ms. Os dois piscam alternadamente, cerca de uma vez por segundo.

* **Cálculos:**
  $$t_H = 0,693\cdot(R_1 + R_2)\cdot C_1 = 0,693\cdot 76\text{ k}\cdot 10\text{ }\mu\text{F} = \mathbf{527\text{ ms}}$$
  $$t_L = 0,693\cdot R_2\cdot C_1 = 0,693\cdot 66\text{ k}\cdot 10\text{ }\mu\text{F} = \mathbf{457\text{ ms}}$$
  $$T = t_H + t_L = \mathbf{984\text{ ms}} \qquad f = \frac{1,44}{(R_1 + 2R_2)\cdot C_1} = \frac{1,44}{1,42} = \mathbf{1,016\text{ Hz}}$$
  *Obs.:* logo que o circuito é ligado, o primeiro nível alto dura mais (cerca de 0,84 s), porque o capacitor começa em 0 V e não em 3,33 V.
