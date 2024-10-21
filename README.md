# ¿De cuántas formas se puede colorear el mapa de Colombia 🇨🇴? / How many ways to color the map of Colombia 🇨🇴?

Hola a todxs, desde cualquier parte del mundo. He calculado que el número de formas de colorear el mapa de Colombia sin que dos regiones adyacentes compartan color, usando solamente 4 colores, es:
```math
283\ 115\ 520
```

Cabe anotar que he considerado a Bogotá como un departamento aislado, y el archipiélago de San Andrés y Providencia se pinta de un solo color.

¿Cómo lo he hecho? En Wolfram Mathematica hay un comando muy sencillo que permite calcular el polinomio cromático de cualquier grafo planar. Para quienes no sean conocedores del tema, el problema de colorear un mapa se puede traducir en cómo colorear los vértices de un grafo planar sin que dos vértices adyacentes queden coloreados por el mismo color. Esto lo podemos hacer ya que hay una correspondencia entre ambos objetos si a cada departamento le asignamos un vértice en un grafo, y dibujamos una arista en caso de que dos regiones compartan una frontera cuya longitud sea positiva, es decir, no consideraremos como fronteras aquellas regiones que se toquen en esquinas. Como dato curioso, el único cuatrifinio (cuatro esquinas) de Colombia está en las fronteras de Boyacá, Casanare, Cundinamarca y Meta.

![image](https://github.com/user-attachments/assets/2e2cee12-287f-4cfd-9546-9c80d037e079)
_Imagen de fondo recuperada de [Wikipedia](https://es.m.wikipedia.org/wiki/Archivo:Mapa_de_Colombia_(departamentos).svg)_

A decir verdad no he hecho nada novedoso, lo más tedioso fue listar todas los departamentos de Colombia y sus fronteras a mano. Una vez hecho esto, el programa hace el resto del trabajo basándose en un teorema muy conocido, llamado el teorema de eliminación-contracción, que dice que si $\chi(G,t)$ representa el número de formas de colorear un grafo $G$ empleando solamente $t$ colores, y si $e$ es una arista del grafo, entonces $$\chi(G, t)=\chi(G-e, t)-\chi(G / e, t),$$ donde $G-e$ es el grafo obtenido a partir de quitar la arista $e$, y $G/e$ es el grafo que resulta de juntar los vértices que une $e$ en un solo vértice y si quedan aristas dobles considerarlas como una sola. Es gracias a esta recurrencia que $\chi(G,t)$ es de hecho un polinomio, llamado el polinomio cromático de $G$.

![image](https://github.com/user-attachments/assets/9d5d99ac-e16d-4cc8-ad3a-918ac62a7395)

Específicamente, el polinomio cromático de Colombia es

```math
\begin{align*}
    \chi(G_{\text{Col}},t)&=t^{33}-72 t^{32}+2514 t^{31}\\
    &\quad-56703 t^{30}+928416 t^{29}-11757140 t^{28}\\
    &\quad+119803182 t^{27}-1008989839 t^{26}+7159276765 t^{25}\\
    &\quad-43406309014 t^{24}+227281194275 t^{23}-1036142031322 t^{22}\\
    &\quad+4137985048853 t^{21}-14543216293518 t^{20}+45128702300210 t^{19}\\
    &\quad-123904692011141 t^{18}+301323104920452 t^{17}-649111128011288 t^{16}\\
    &\quad+1237494226626151 t^{15}-2083729861163011 t^{14}+3089197236230153 t^{13}\\
    &\quad-4014284821039240 t^{12}+4544515915061124 t^{11}-4446080022163760 t^{10}\\
    &\quad+3719159851081504 t^9-2622562341468416 t^8+1529179876264320 t^7\\
    &\quad-717670769635584 t^6+260520144880896 t^5-68636197988352 t^4\\
    &\quad+11673935115264 t^3-961919815680 t^2.
\end{align*}
```

Todos los detalles formales de $\chi(G,t)$ pueden ser consultados en el artículo [_**'How many ways to color the map of America?'**_](https://arxiv.org/abs/1908.05694) donde prueban varias propiedades del polinomio cromático y cuentan cuántas formas hay de colorear los mapas de Canadá, Francia y EEUU.

Este problema crece de forma exponencial gracias a la recurrencia anterior, así que es computacionalmente complejo calcular el polinomio cromático de un grafo si el número de aristas es muy grande. Es por esto que me gustaría, por puro pasatiempo, calcular el polinomio cromático de Colombia usando los teoremas mencionados en el artículo. La forma que por el momento se me ocurre es separar los 3-ciclos en la parte superior del mapa y separar la 6-rueda que proviene del departamento de Santander. También se puede separar el 3-ciclo de Nariño, y tal vez usar el teorema principal de dicho artículo, que permite reducir el polinomio cromático de la intersección de los dos grafos rueda de Caquetá y Guaviare. Sigo pensándolo, pero si alguien más se anima, adelante.

La razón por la que pensé en este problema fue gracias a una conferencia (buenísima) dada por Federico Ardila en el Congreso Colombiano de Matemáticas de 2023, en la que nos habló del teorema de los cuatro colores y nos motivó a calcular el polinomio cromático de Colombia, nos dijo que le avisáramos una vez lo calculáramos. Pensé que sería muy difícil y por eso lo postergué, pero después de año y medio, aquí está. Avísenle.

Queda a disposición de cualquiera el dataset de las fronteras de Colombia, con esto pueden reconstruir el grafo y calcular otro tipo de objetos interesantes, como su matriz de adyacencia, etc. Solo no olviden citar este sitio.

¡Saludos!
