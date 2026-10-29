# TrendScout Board · @ForecastQuant
Tendencias de Bitcoin/macro/quant convertidas en borradores de posts para revisión humana. Nada se publica en X.
Live: https://cemedinan.github.io/trend-scout-board/

## Actualización diaria (22:00 hora Chile) — REEMPLAZA TODO
1. Detectar tendencias actuales (X news/search + web). No repetir temas ya sugeridos salvo que haya un desarrollo materialmente nuevo.
2. Generar las imágenes del set nuevo en `assets/img/` y escribir las entradas (5–8) en `nuevas.json` (lista).
3. `python3 update.py nuevas.json` → BORRA todas las sugerencias anteriores de `data/suggestions.json` y todas sus imágenes en `assets/img/`, y deja solo el set nuevo.
4. `git add -A && git commit -m "update" && git push`. La página muestra todo lo que hay en el JSON (sin filtro por antigüedad).

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
No hay archivo histórico: cada corrida reemplaza el set completo.
Cada borrador termina con un CTA suave (campo `cta`, natural, no vendedor). Reglas: no inventar datos, citar siempre la fuente, no copiar posts textualmente, $BTC en posts de noticias.

## Imágenes (`image`)
Cada sugerencia lleva una imagen real en `assets/img/<id>.jpg` (1200x675, JPG optimizado <100 KB), referenciada en el campo `image`. La tarjeta la muestra arriba del borrador, con el brief del visual debajo y un enlace de descarga.
Estilo: azul marino #0B0B2B, Bitcoin blanco, acentos lima #C5E523, logo de `assets/logo-watermark.png` como marca de agua.
Gráficos solo con datos reales (Google Trends vía pytrends, precios Kraken). Si no hay datos, tarjeta numérica con cifras ya citadas en la fuente. Nunca inventar cifras.
`update.py` borra en cada corrida todas las imágenes de `assets/img/` que no pertenecen al set nuevo.
Idioma: posts y CTA en inglés; la interfaz y las explicaciones quedan en español.

## Botón POST ON X (mantener en todas las corridas)
Cada tarjeta tiene un botón grande lima **POST ON X**: un `<a target="_blank">` a `https://x.com/intent/post?text=<encodeURIComponent(texto)>` que abre el editor de X prellenado. **Nada se publica automáticamente**: tú revisas y presionas Post.
- Texto = post + línea en blanco + primer CTA si cabe en 280 caracteres (URLs cuentan 23). Si no cabe: solo el post y la nota "CTA not added (over 280 chars); add it as a reply".
- Si el post solo ya pasa 280: botón "POST ON X (thread: edit)" y nota para dividirlo en hilo en X.
- El intent de X no puede adjuntar imágenes: al lado está "[image ↓]" con la indicación "download the image, then attach it in X before sending".
- Se mantienen botones chicos: [copiar post], [COPIAR CTA], [COPIAR VISUAL]. Lógica en `xi()`/`withCta()` de `index.html` (fuente de verdad junto a `update.py`); las corridas solo cambian `data/` y `assets/img/`, no tocar este botón.
- Si el texto pasa 280 se muestra "más de 280 caracteres (N)" (el intent no recorta).
- iPhone/iPad: el clic abre la app con `twitter://post?message=...` y, si la página no se oculta en 1,5 s, cae al enlace web. Desktop/Android usan el enlace web. **No probado en un iPhone real.**
- No agregar botones de copiar/compartir imagen (en iPhone X descarta el texto). Para la imagen: descargarla o mantener presionada para copiarla y pegarla en X.
