# Fleet location map

The basemap now draws embedded Natural Earth country boundaries using Leaflet. It makes **no map-tile requests**, needs no map API key and does not rely on HTTP Referer headers, which Power BI's embedded browser may omit. Fleet markers and filters use the existing embedded fleet data.

Use the updated, complete `index.html` in your existing Power BI HTML visual or hosting workflow. If the report stores the HTML in a measure or another copy, replace that content too; a repository edit does not automatically refresh a stored report copy.

The dark background shows country outlines and southern African country labels, not roads or street-level detail. The initial view fits all fleet locations. Zoom is limited to 10 because these boundaries are generalised.

The basemap itself requires no network connection. Leaflet and fonts still load externally; the full page is not completely offline. The Power BI visual must allow JavaScript and the existing Leaflet CDN.

## Boundary source and maintenance

- Dataset: Natural Earth 1:110m Admin 0 Countries, Africa subset, downloaded 18 November 2026.
- [Original GeoJSON](https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_admin_0_countries.geojson) and [public-domain terms](https://www.naturalearthdata.com/about/terms-of-use/).
- `assets/africa-countries.geojson` retains the original geometry and label coordinates with only the necessary properties. This is geographic reference data, not generated fleet data.
- An identical compact copy is embedded in the HTML's `africa-basemap` JSON block. No relative asset fetch is required in Power BI.

After changing the reviewed asset, run `python location-webpage/embed_basemap.py` from the repository root. The root `_update_fleet_data.py` preserves this map when updating fleet records.

## Standalone preview

From the repository root, start a local server:

```powershell
python -m http.server --bind 127.0.0.1 8000
```

Open http://localhost:8000/location-webpage/. For a hosted deployment, serve the page over HTTPS.

The previous CARTO endpoint required an API key, and standard OpenStreetMap tiles were blocked in Power BI. Neither service is used by this version. No fleet data was changed.
