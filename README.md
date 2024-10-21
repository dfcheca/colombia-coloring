# ¿De cuántas formas se puede colorear el mapa de Colombia 🇨🇴? / How many ways to color the map of Colombia 🇨🇴?

Hola a todxs, desde cualquier parte del mundo. He calculado que el número de formas de colorear el mapa de Colombia sin que dos regiones adyacentes compartan color, usando solamente 4 colores, es
$$283 115 520.$$
Cabe anotar que he considerado a Bogotá como un departamento aislado, y el archipiélago de San Andrés y Providencia se pinta de un solo color.

¿Cómo lo he hecho? En Wolfram Mathematica hay un comando muy sencillo que te permite calcular el polinomio cromático de cualquier grafo planar. Para quienes no sean conocedores del tema, el problema de colorear un mapa se puede traducir en cómo colorear los vértices de un grafo planar sin que dos vértices adyacentes queden coloreados por el mismo color. Esto lo podemos hacer ya que hay una correspondencia entre ambos objetos si a cada departamento le asignamos un vértice en un grafo, y dibujamos una arista en caso de que dos regiones compartan una frontera cuya longitud sea positiva, es decir, no consideraremos como fronteras aquellas regiones que se toquen en esquinas. Como dato curioso, el único cuatrifinio (cuatro esquinas) de Colombia está en las fronteras de Boyacá, Casanare, Cundinamarca y Meta.

A decir verdad no he hecho nada novedoso, lo más tedioso fue listar todas los departamentos de Colombia y sus fronteras a mano. Una vez hecho esto, el programa hace el resto del trabajo basándose en un teorema muy conocido, llamado el teorema de eliminación-contracción, que dice que si $\chi(G,t)$ representa el número de formas de colorear un grafo $G$ empleando solamente $t$ colores, y si $e$ es una arista del grafo, entonces $$\chi(G, t)=\chi(G-e, t)-\chi(G / e, t),$$ donde $G-e$ es el grafo obtenido a partir de quitar la arista $e$, y $G/e$ es el grafo que resulta de juntar los vértices que une $e$ en un solo vértice y si quedan aristas dobles considerarlas como una sola. Es gracias a esta recurrencia que $\chi(G,t)$ es de hecho un polinomio, llamado el polinomio cromático de $G$.

Específicamente, el polinomio cromático de Colombia es

Todos los detalles formales de $\chi(G,t)$ pueden ser consultados en el artículo [_**'How many ways to color the map of America?'**_](https://arxiv.org/abs/1908.05694) donde prueban varias propiedades del polinomio cromático y cuentan cuántas formas hay de colorear los mapas de Canadá, Francia y EEUU.

Este problema crece de forma exponencial gracias a la recurrencia anterior, así que es computacionalmente complejo calcular el polinomio cromático de un grafo si el número de aristas es muy grande. Es por esto que me gustaría, por puro pasatiempo, calcular el polinomio cromático de Colombia usando los teoremas mencionados en el artículo. La forma que por el momento se me ocurre es separar los 3-ciclos en la parte superior del mapa y separar la 6-rueda que proviene del departamento de Santander. También se puede separar el 3-ciclo de Nariño, y tal vez usar el teorema principal de dicho artículo, que permite reducir el polinomio cromático de la intersección de los dos grafos rueda de Caquetá y Guaviare. Sigo pensándolo, pero si alguien más se anima, adelante.

La razón por la que pensé en este problema fue gracias a una conferencia (buenísima) dada por Federico Ardila en el Congreso Colombiano de Matemáticas de 2023, en la que nos habló del teorema de los cuatro colores y nos motivó a calcular el polinomio cromático de Colombia, nos dijo que le avisáramos una vez lo calculáramos. Pensé que sería muy difícil y por eso lo postergué, pero después de año y medio, aquí está. Avísenle.

Queda a disposición de cualquiera el dataset de las fronteras de Colombia, con esto pueden reconstruir el grafo y calcular otro tipo de objetos interesantes, como su matriz de adyacencia, etc. Solo no olviden citar este sitio.

¡Saludos!
