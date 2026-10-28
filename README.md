# TrendScout Board · @ForecastQuant
Tendencias de Bitcoin/macro/quant convertidas en borradores de posts para revisión humana. Nada se publica en X.
Live: https://cemedinan.github.io/trend-scout-board/

## Actualización diaria
1. Detectar tendencias (X news/search + web) y escribir entradas nuevas en un archivo `nuevas.json` (lista).
2. `python3 update.py nuevas.json` → agrega, archiva >72 h en `data/archive.json`, actualiza la fecha.
3. `git commit -am "update" && git push`. La página además oculta en el navegador todo lo que tenga >72 h.

## Esquema `data/suggestions.json`
```
{ "meta": { "generated_at": "ISO-8601 UTC", "note": "texto opcional" },
  "entries": [ {
    "id": "slug-unico",
    "detected_at": "ISO-8601 UTC (fecha de detección)",
    "topic": "tendencia o tema detectado",
    "why": "por qué tiene potencial",
    "post": "borrador del post o hilo (EN INGLÉS; \n para saltos)",
    "cta": ["1 o 2 opciones de CTA suave EN INGLÉS, máx. 1 línea c/u"],
    "image": "assets/img/<id>.jpg (imagen final 1200x675 que se muestra en la tarjeta)",
    "image_note": "origen de la imagen: datos reales (fuente) o tarjeta numérica con cifras de la fuente",
    "visual": "descripción precisa del visual (azul marino #0B0B2B, Bitcoin blanco, lima #C5E523)",
    "format": "post corto | hilo | gráfico | video | meme",
    "priority": "Alta | Media | Baja",
    "window": "ventana sugerida de publicación (opcional)",
    "source": "URL de la fuente (obligatoria)"
  } ] }
```
`data/archive.json`: `{ "entries": [ ...mismo esquema... ] }`.
Cada borrador termina con un CTA suave (campo `cta`, natural, no vendedor). Reglas: no inventar datos, citar siempre la fuente, no copiar posts textualmente, $BTC en posts de noticias.

## Imágenes (`image`)
Cada sugerencia lleva una imagen real en `assets/img/<id>.jpg` (1200x675, JPG optimizado <100 KB), referenciada en el campo `image`. La tarjeta la muestra arriba del borrador, con el brief del visual debajo y un enlace de descarga.
Estilo: azul marino #0B0B2B, Bitcoin blanco, acentos lima #C5E523, logo de `assets/logo-watermark.png` como marca de agua.
Gráficos solo con datos reales (Google Trends vía pytrends, precios Kraken). Si no hay datos, tarjeta numérica con cifras ya citadas en la fuente. Nunca inventar cifras.
`update.py` mueve las imágenes de sugerencias archivadas (>72 h) a `assets/img/archive/` y actualiza su ruta en `data/archive.json`.
Idioma: posts y CTA en inglés; la interfaz y las explicaciones quedan en español.
