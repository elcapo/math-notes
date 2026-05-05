# Notebooks

Cuadernos [Marimo](https://marimo.io/) para experimentar interactivamente con los conceptos del repositorio. Es un proyecto `uv` independiente con su propio `pyproject.toml` y `uv.lock`, igual que `scripts/`.

## Prerrequisitos

- [`uv`](https://docs.astral.sh/uv/) — gestiona el entorno virtual y las dependencias.

## Ejecutar un cuaderno

Marimo tiene dos modos principales:

```bash
# Edición reactiva (lo habitual durante el estudio)
uv run --directory notebooks/ marimo edit notebooks/expression-plotter.py

# Modo "app" sólo lectura (oculta el código)
uv run --directory notebooks/ marimo run notebooks/expression-plotter.py
```

Equivalente desde dentro del directorio:

```bash
cd notebooks && uv run marimo edit expression-plotter.py
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
