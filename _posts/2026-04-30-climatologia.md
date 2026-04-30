---
title: "¿Cómo se calcula una climatología?"
date: 2026-04-30
permalink: /posts/2026/04/climatologia/
layout: single
author_profile: true
tags:
  - climate
  - statistics
  - oceanography
---

Calcular una climatología es un procedimiento estándard en las ciencias climáticas. Es la forma de representar el ciclo anual promedio de una variable ambiental. En este artículo vamos a ver que la forma mas usual de computar climatologías tiene sus bemoles. 

La idea central de una climatología es capturar la estacionalidad. Si pensamos en la temperatura del aire, ese ciclo está marcado por las estaciones del año, con amplitudes que varían según la región pero reconocibles en todo el planeta. La razón es directa: el Sol es la fuente de energía radiativa del sistema terrestre, y es él quien impone ese ritmo que luego se transmite al resto del sistema.

Veámoslo gráficamente. Si tomamos una región del mar y seguimos su temperatura superficial durante los últimos 10 años, vemos una estacionalidad marcada (Figura 1). En el Atlántico Sudoccidental, los veranos son en promedio unos 7°C más cálidos que los inviernos, con otoño y primavera como estaciones de transición.

![Evolución de la SST en el Atlántico Sudoccidental (2015-2025)](/images/climatologia/evolucion_sst.png)
*Figura 1. Temperatura superficial del mar diaria en el Atlántico Sudoccidental (310-320°E, 40-35°S) entre 2015 y 2025.*

Es extremadamente útil conocer la climatología de un lugar, porque eso
nos permite tener algo contra qué comparar. Cuando queramos entender si
el 2024 fue un año anómalamente cálido, por ejemplo, vamos a tener que
definir una nueva variable que es la anomalía. Esa anomalía no es más
que una desviación de los datos de un año respecto a los años
climatológicos:

$$X_i - \bar{X}$$

De la definición de anomalías queda claro que aquello que consideremos
anómalo va a depender directamente de cómo hayamos calculado nuestra
media, nuestra climatología. Así que vamos a meter mano en eso.

# Promedios simples

Hay muchas formas de hacer climatologías, pero una de las más comunes es
a través de un promedio simple. Supongamos que tenemos un punto en el
océano con registros diarios de la temperatura en el período 1995-2025.
En este caso, elijo la temperatura por ser la variable más intuitiva, aquella de la
que tenemos alguna noción de cómo funciona, pero también podemos
utilizar otras, como la precipitación, la altura geopotencial, etc. En
ese sitio podemos obtener fácilmente estos datos de algún dataset
satelital, por ejemplo con sensores infrarrojos AVHRR [(Reynolds et al., 2007)](https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html).

Entonces, con los promedios simples construimos el año climatológico
de la siguiente manera: el primero de enero del año promedio es el
promedio de todos los primeros de enero de nuestro registro completo. Y
así seguimos hasta completar todos los días del año (Figura 2). Si recordamos que
tenemos 30 años de datos, entonces cada valor medio lo construimos con
30 valores, excepto los 29 de febrero que quedan un poco más
subrepresentados.

Tomemos nuestro punto en el océano y veamos cómo luce esa climatología:

![Climatologías de SST para distintos períodos base](/images/climatologia/climatologias.png)
*Figura 2. Climatología de promedio simple calculada con períodos base de 10, 15 y 30 años.*

Y comparemos también cómo luce esa climatología cuando achicamos nuestro
"periodo base". Si en lugar de usar 30 años para construir nuestro año
promedio usamos solo 10 o 15 años, vamos a notar que la señal
climatológica se vuelve más irregular y ruidosa (Figura 2). Esto tiene sentido: con
menos datos para promediar, los eventos particulares de años específicos
tienen más peso en el cálculo, y la variabilidad interanual no se
suaviza tanto.

El promedio simple usa 365 parámetros para describir algo que sabemos que es suave y cíclico, lo cual parece excesivo. ¿No habrá una forma más eficiente?

# Método espectral

Si bien los promedios simples son la forma más usual de calcular una climatología, no es la
única. Aquí vamos a implementar el método espectral que se basa en una
descomposición en armónicos de Fourier. Esta combinación lineal de senos y cosenos descompone una señal en ondas de distinta amplitud y
frecuencia. Para un fenómeno recurrente y cíclico como las estaciones, una metodología que identifica modos naturales de oscilación debería funcionar bien.

El enfoque consiste en asumir que la media climatológica
tiene la forma funcional:

$$\bar{y}(t_i) = a_0 + \sum_{j=1}^{H} \left[ a_j \cos(\omega_j t_i) + b_j \sin(\omega_j t_i) \right]$$

donde $i = 1, 2, \ldots, N$, $\omega_j = 2\pi j/P$, $P$ es el período, y $H$ es el
parámetro de truncamiento. Luego determinamos los parámetros $a_j$ y $b_j$
que minimizan la diferencia cuadrática media entre $\bar{y}(t_i)$ e $y(t_i)$.

Es cierto que para calcular el ciclo climatológico a partir de los modos
de Fourier hay que tomar algunas decisiones, principalmente cuántos
modos utilizar ($H$). En esta instancia voy a tomar 4 modos, que es el valor que Narapusetty et al. (2009) identifican
como óptimo para datos globales de SST mediante validación cruzada. Este
número lo voy a imponer por ahora, pero más adelante lo vamos a discutir.

Cuando truncamos $H = 4$ podemos calcular nuestro ciclo anual
climatológico y ver cómo luce (Figura 3). Además podemos compararlo con la
metodología que se basa en promedios simples:

![Comparación entre el promedio simple y el método espectral con H=4](/images/climatologia/comparacion_fourier_vs_simple.png)
*Figura 3. Climatologías calculadas con 30 años de datos usando promedio simple y método espectral (H=4).*

A grandes rasgos se observa que ambas metodologías capturan muy bien el
ciclo estacional: el máximo de temperatura ocurre alrededor del día 50
(mediados de febrero, pleno verano austral) con valores cercanos a los
21-22 °C, y el mínimo se da alrededor del día 250 (finales de julio)
con temperaturas próximas a los 15 °C. La diferencia más notable entre
ambos métodos es la suavidad: la climatología espectral produce una
curva limpia y continua, mientras que el promedio simple presenta
oscilaciones día a día que reflejan la variabilidad residual que no se
cancela al promediar 30 años. En términos de la información que
transmiten sobre el ciclo anual, sin embargo, las diferencias son
mínimas.

# ¿Qué método es mejor?

## Errores

Una forma de comparar las dos metodologías que vimos es evaluar qué tan
bien cada climatología predice datos independientes, es decir,
observaciones que no usamos para construirla. Para entender esto mejor,
pensemos en el problema de aproximar un proceso aleatorio $Y$ con algún
parámetro $\mu$.

El mejor $\mu$ posible va a ser aquel que minimiza el error cuadrático
medio:

$$\varepsilon = \langle (Y - \mu)^2 \rangle$$

donde los corchetes $\langle \cdot \rangle$ representan el valor esperado respecto a la
distribución climatológica. Resulta que este $\mu$ óptimo es simplemente la
media de $Y$, es decir, $\mu = \langle Y \rangle$.

Ahora bien, si la distribución de $Y$ cambia con el tiempo, como ocurre
cuando hay ciclos anuales o diurnos, entonces $\mu$ también va a variar con
el tiempo. Esto es exactamente lo que pasa con la temperatura del
océano: tiene un ciclo estacional marcado, por lo que el valor
"esperado" para el 15 de enero es distinto al del 15 de julio.

Este razonamiento nos da un criterio claro para comparar distintas
climatologías: calculamos el error $\varepsilon$ usando datos independientes para
cada método, y el que produzca el $\varepsilon$ más chico es el mas recomendado. En otras
palabras, la climatología más precisa es aquella que comete los errores
más pequeños cuando la ponemos a prueba con observaciones nuevas que no
vio durante su construcción.

En la Figura 4 aplicamos ese criterio con el cálculo de ambas climatologías para distintas cantidades de años, y evaluamos el error sobre un período de test fijo (2015-2024).

![RMSE en datos independientes en función de los años de cómputo](/images/climatologia/residuos.png)
*Figura 4. RMSE sobre datos independientes (2015-2024) en función de los años de cómputo para promedio simple y método espectral (panel superior). Diferencia de RMSE entre ambos métodos (panel inferior).*

Con apenas 2 años de cómputo, el promedio simple comete un error casi 0.07 °C mayor que el espectral. A medida que crece el registro la diferencia se achica, pero el método espectral nunca pierde.

## Cantidad de modos

Si el método de Fourier es elegido para representar una climatología ante el promedio simple, queda otra pregunta pendiente: ¿cuántos armónicos $H$ necesitamos?

Con el método del promedio diario necesitamos
calcular 365 valores distintos, uno para cada día del año. Con Fourier,
en cambio, solo necesitamos $2H + 1$ coeficientes: las amplitudes de senos
y cosenos para cada armónico, más una constante. Si usamos, por ejemplo,
menos de 10 armónicos, estamos hablando de muchísimos menos parámetros
que con el promedio simple.

Acá entra en juego algo importante, cuando ajustamos
demasiados parámetros respecto a la cantidad de datos que tenemos,
empezamos a sobreajustar. Y cuando eso pasa, el modelo funciona bárbaro
con los datos que usamos para entrenarlo, pero falla cuando lo aplicamos
a datos nuevos. Por eso un modelo de menos
parámetros suele predecir mejor.

Podemos ver esto directamente en la Figura 5. Con solo 2 años de cómputo, el
promedio simple tiene que estimar 365 parámetros con apenas 2
observaciones por día del año: el resultado es una curva irregular que
refleja más ruido que señal. El método espectral, en cambio, estima 9
coeficientes independientemente de cuántos años tengamos, y produce una
curva suave incluso con registros cortos.

![Climatologías construidas con 2 vs 20 años de cómputo](/images/climatologia/fig_pocos_anios.png)
*Figura 5. Climatologías calculadas con 2 años de cómputo (izquierda) y 20 años (derecha), comparando promedio simple y método espectral (H=4).*

Esto no es un accidente de un año particular: es sistemático (Figura 6). Si
repetimos el ejercicio agregando años de a uno y vemos cómo cambia cada
climatología, el promedio simple salta notoriamente con cada nuevo año
mientras que el espectral casi no se mueve.

![Estabilidad de la climatología al agregar años de datos](/images/climatologia/fig_estabilidad.png)
*Figura 6. Climatologías calculadas con 2, 4, 6, 10 y 20 años de cómputo para promedio simple (izquierda) y método espectral con H=4 (derecha).*

Con 2 años de cómputo la diferencia es llamativa. A medida que
crece el registro, la brecha se achica rápidamente y se vuelve
marginal a partir de los 10 a 15 años. Esto no quiere decir que con muchos
datos los métodos sean idénticos: el espectral sigue siendo más
parsimonioso (9 parámetros vs 365), más robusto frente a datos faltantes
y años bisiestos, y produce una curva suave sin necesidad de ningún
suavizado adicional.

Narapusetty et al. (2009) muestran con experimentos de validación cruzada sobre datos globales de SST que el error mínimo se obtiene con H = 4, lo que implica estimar apenas 9 coeficientes en lugar de los 366 parámetros del promedio simple, 40x menos parámetros.

## Referencias

> DelSole, T., & Tippett, M. K. (2022). *Statistical Methods for Climate Scientists*. Cambridge University Press.

> Narapusetty, B., DelSole, T., & Tippett, M. K. (2009). Optimal Estimation of the Climatological Mean. *Journal of Climate*, 22(18), 4845–4859. https://doi.org/10.1175/2009JCLI2944.1

> Reynolds, R. W., Smith, T. M., Liu, C., Chelton, D. B., Casey, K. S., & Schlax, M. G. (2007). Daily High-Resolution-Blended Analyses for Sea Surface Temperature. *Journal of Climate*, 20(22), 5473–5496. https://doi.org/10.1175/2007JCLI1824.1
