# Práctica de Laboratorio Integrado de Física  
## Medición, Incertidumbre y Análisis de Datos

---

## Objetivo

El objetivo de esta práctica es comprender el proceso de medición física, el tratamiento de incertidumbres y la validación de modelos teóricos mediante el análisis estadístico de datos experimentales. Se busca aplicar estos conceptos en la determinación del volumen y la densidad de distintos objetos sólidos con formas geométricas regulares, utilizando instrumentos de precisión.

---

## Instrumentos Utilizados

- Pie de rey (precisión: ± 0.05 mm)  
- Tornillo micrométrico (precisión: ± 0.01 mm)  
- Balanza digital (precisión: ± 0.01 g)

---

## Metodología

1. **Medición de dimensiones y masa:**
   - Se usó el pie de rey para medir largo, ancho y alto de objetos como cubos, cilindros y tuercas.
   - La esfera fue medida con el tornillo micrométrico debido a su pequeño tamaño.
   - Las masas fueron obtenidas con una balanza digital.

2. **Cálculo del volumen:**
   Se aplicaron fórmulas geométricas específicas para cada figura:

   - Cubo:  
     $$
     V = L \cdot A \cdot H
     $$

   - Cilindro:  
     $$
     V = \pi r^2 h
     $$

   - Esfera:  
     $$
     V = \frac{4}{3} \pi r^3
     $$

   - Tuerca (hexágono con hueco cilíndrico):  
     $$
     V = \left( \frac{3\sqrt{3}}{2} \cdot b^2 \cdot h \right) - \left( \pi r^2 h \right)
     $$

3. **Cálculo de la densidad y su incertidumbre:**  
   $$
   \rho = \frac{m}{V}, \quad \delta \rho = \rho \cdot \left( \frac{\delta m}{m} + \frac{\delta V}{V} \right)
   $$

4. **Propagación de la incertidumbre:**  
   Se aplicaron fórmulas de propagación para obtener la incertidumbre de los volúmenes calculados:

   - Volumen del prisma hexagonal:  
     $$
     \frac{\delta V_{hex}}{V_{hex}} = 2 \cdot \frac{\delta b}{b} + \frac{\delta h}{h}
     $$

   - Volumen del cilindro interior:  
     $$
     \frac{\delta V_{cil}}{V_{cil}} = 2 \cdot \frac{\delta r}{r} + \frac{\delta h}{h}
     $$

   - Volumen neto:  
     $$
     \delta V = \sqrt{(\delta V_{hex})^2 + (\delta V_{cil})^2}
     $$

---

## Ejemplo de Resultados: Tuerca

- **Volumen del hexágono sin hueco:**  
  $$
  V_{hex} = 1.735 \pm 0.030\ \text{cm}^3
  $$

- **Volumen del hueco cilíndrico:**  
  $$
  V_{cil} = 0.353 \pm 0.007\ \text{cm}^3
  $$

- **Volumen neto de la tuerca:**  
  $$
  V = 1.382 \pm 0.031\ \text{cm}^3
  $$

- **Densidad calculada:**  
  $$
  \rho = 6.25 \pm 0.15\ \text{g/cm}^3
  $$

---

## Conclusiones

- Las mediciones realizadas fueron consistentes con los modelos geométricos teóricos.
- Las incertidumbres se propagaron adecuadamente y mostraron el efecto del instrumento sobre la precisión final.
- La densidad obtenida coincide con valores esperados dentro del margen de error.
- Se destaca la importancia del análisis de errores en la validación experimental.

---

## Créditos

Práctica realizada por:  
**[Tu Nombre Aquí]**  
**Laboratorio Integrado de Física – 2025**
