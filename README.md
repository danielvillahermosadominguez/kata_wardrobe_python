# Configure your own Wardrobe

Imagine you have just moved into your new apartment, and then you notice that you still need a new wardrobe for your
dressing room. Regrettably, you won’t find a wardrobe that fits exactly to the size of your wall. But fortunately, the
Swedish furniture dealer of your choice offers you the opportunity to build your own, customized wardrobe by combining
individual wardrobe elements.

The wardrobe elements are available in the following sizes: 50cm, 75cm, 100cm, and 120cm. The wall on which the wardrobe
elements are placed has a total length of 250cm. With which combinations of wardrobe elements can you make the most of
the space?

Write a function that returns all combinations of wardrobe elements that exactly fill the wall.

# Additional Task

Here is the price list for the available wardrobe elements:

50cm => 59 USD_
75cm => 62 USD
100cm => 90 USD
120cm => 111 USD
Write a second function that checks which of the resulting combinations is the cheapest one.

# Current job
14-Feb-2023
Lo último que hemos hecho es definir que el usuario tiene un tamaño de armario de 100 y que devuelva dos combinaciones posibles, hemos quedado en el refactor aquí.
No nos han funcionado las clases de test. Investigar.
Nos esta dando muchos problemas la configuración del entorno.

21-02-2023
Hemos usado parametrización en tests y hemos refactorizado
Hemos refactorizado la clase con un while - for y ahora siguientes pasos:
- Meter mas tests 
  - COn las opciones opciones que tenemos, meter casos intermedios: 3, 56, 78
  - Seguir metiendo mas casos -> intentar llegar a lo que dice la kata.
  - Tratar de aplicar calistenia
  - Refactorizacion con patron de diseño

- Posibles reglas a evaluar:
  - ¿Estamos teniendo en cuenta combinación de opciones? Por ejemplo 125 = [[50,50], [75], [50,75]]

27-02-2023
- Meter mas tests
  - aplicar tail recursion
  - Seguir metiendo mas casos -> intentar llegar a lo que dice la kata.
    - ¿Estamos teniendo en cuenta combinación de opciones? Por ejemplo 125 = [[50,50], [75], [50,75]]
  - Tratar de aplicar calistenia
  - Refactorizacion con patron de diseño

- Posibles reglas a evaluar:

28-02-2023
- Estamos en el algoritmo con varias options. Dejamos una primera versión que aun no funciona pero nos da una idea de por donde seguir
- Posibles casos:Tenemos que filtrar los resultados "iguales"? [75.50] y [50, 75] <= quiza ya no se de este caso
- Casos como: 175 = [[50,50,50],[75,50,50], [100,50], [120,50]]
- Tratar de aplicar calistenia
- Refactorizacion con patron de diseño
13-03-2023
  - El caso como: 175 = [[50,50,50],[75,50,50], [100,50], [120,50]] está implementado
  - Requiere una refactorización
  - Tratar de aplicar calistenia
  - Refactorizacion con patron de diseño
