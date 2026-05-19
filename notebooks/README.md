# Notebooks

Cuadernos [Marimo](https://marimo.io/) para experimentar interactivamente con los conceptos del repositorio. Es un proyecto `uv` independiente con su propio `pyproject.toml` y `uv.lock`, igual que `scripts/`.

## Prerrequisitos

- [`uv`](https://docs.astral.sh/uv/) — gestiona el entorno virtual y las dependencias.

## Ejecutar un cuaderno

Marimo tiene dos modos principales:

```bash
cd notebooks/

# Edición reactiva (lo habitual durante el estudio)
uv run marimo edit expression-plotter.py

# Modo "app" sólo lectura (oculta el código)
uv run marimo run expression-plotter.py
```

La primera ejecución descarga e instala dependencias en `notebooks/.venv/` (ignorado por git).

## Cuadernos

### `expression-plotter.py`

Escribe una expresión en $x$ (por ejemplo `x**2 - 4`, `sin(x)/x`, `exp(-x**2)`) y se grafica al vuelo. Parámetros expuestos:

- **Expresión** — se analiza con `sympy.sympify`, por lo que se aceptan `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `Abs`, `pi`, `E`, etc. El resultado se renderiza en LaTeX como confirmación.
- **Dominio** $[x_{\min}, x_{\max}]$ — controles numéricos independientes.
- **Eje $y$** — por defecto se autoescala al percentil 2-98 (descarta picos por asíntotas). Marcando *fijar eje $y$* puedes imponer límites manuales.
- **Muestreo** — número de puntos de la rejilla en $x$ (100 a 5000).

Solo se admite la variable `x`; cualquier otro símbolo libre se rechaza con un mensaje.

### `expression-comparer.py`

Igual que el anterior pero con **dos** expresiones $f(x)$ y $g(x)$ representadas en los mismos ejes con colores distintos (`tab:blue` para $f$, `tab:orange` para $g$). Útil para contrastar familias, traslaciones o aproximaciones (p. ej. $\sin x$ frente a su Taylor de orden 3).

Parámetros adicionales sobre `expression-plotter.py`:

- **Mostrar $f-g$** — superpone la diferencia como línea verde discontinua (rápido sanity-check de cuándo dos curvas coinciden).

### `parametric-curves-2d.py`

Define dos curvas paramétricas $\gamma_1(t) = (x_1(t), y_1(t))$ y $\gamma_2(t) = (x_2(t), y_2(t))$ sobre un mismo intervalo $t \in [t_{\min}, t_{\max}]$ y las dibuja superpuestas en el plano. Útil para circunferencias, elipses, espirales, figuras de Lissajous o para contrastar dos trayectorias.

Las cuatro componentes se analizan con `sympy.sympify` y solo se admite la variable `t`; cualquier otro símbolo libre se rechaza con un mensaje. El resultado se renderiza en LaTeX como confirmación antes de plotear.

Parámetros:

- **Dominio en $t$** — controles numéricos $t_{\min}$ y $t_{\max}$ (por defecto $[0, 2\pi]$).
- **Ejes** — por defecto autoescala $x$ e $y$ al percentil 2-98 de los valores muestreados de cada curva. Marcando *fijar ejes* puedes imponer límites manuales para ambos ejes.
- **Aspecto 1:1** — activo por defecto (las circunferencias se ven circulares). Desactívalo si prefieres que la curva llene los ejes.
- **Muestreo** — número de puntos en $t$ (100 a 5000).

Colores: `tab:blue` para $\gamma_1$, `tab:orange` para $\gamma_2$.
