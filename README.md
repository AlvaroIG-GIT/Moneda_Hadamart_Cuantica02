# Práctica 2: La Moneda Perfecta con Puerta de Hadamard

Implementación y simulación de un generador cuántico de números aleatorios («la moneda perfecta») utilizando la puerta de Hadamard en **pyQuil** y el simulador **QVM** de Rigetti[cite: 8].

## Contenido del Repositorio

- **Fase 1 (Tirada Simple):** Circuito de 1 cúbit en superposición con puerta $H$, midiendo un único resultado aleatorio equiprobable (0 = Cara, 1 = Cruz)[cite: 8].
- **Fase 2 (Competición Iterativa):** Simulación de 60 lanzamientos entre dos usuarios comparando dos estrategias: bucles de ejecución directa (`wrap_in_numshots_loop`) frente a múltiples llamadas a `qvm.run()`[cite: 9].
- **Fase 3 (Múltiples Monedas):** Escalado del sistema a 6 monedas simultáneas con 25 rondas, implementando lectura mediante registros clásicos individuales y mediante la función `measure_all`[cite: 9].

## Conceptos Clave

- **Superposición Cuántica:** Generación de estados equiprobables partiendo de $|0\rangle$:
  $$H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$
- **Gestión de Memoria Clásica:** Uso de `declare` y lectura con `measure` / `measure_all` en pyQuil[cite: 8, 9].
- **Métricas y Resultados:** Procesamiento de registros cuánticos para resolución de frecuencias y conteos.

## Tecnologías Utilizadas

- Python 3
- pyQuil
- Rigetti Forest SDK (quilc & QVM)