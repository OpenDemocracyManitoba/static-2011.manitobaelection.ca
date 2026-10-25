# 2011.manitobaelection.ca (static archive)

Static copy of **2011.manitobaelection.ca**, taken from olddroplet (`odm-nginx-ruby-php-2018`, 159.203.24.194) on 2026-10-24, before the server was retired. Static HTML export of the 2011 Manitoba election Rails app.

`site/` is the served web root as it was on disk (2798 files), minus the files listed below. No crawl was needed: this site was already static.

## Serving

Serve `site/` as static files from the domain root.
* Rails page-cache export: links have no extension (`/candidates/foo`) and nginx served them with `try_files $uri $uri.html`.

## Left out of `site/`

* `.env`
* `.ftpconfig`

These were left out because they were not site content: version control, PHP, or (per the archive plan) files that should not be public. The full web root is kept in a private archive repo.

## Links to internal or old hosts

Left as they are (Phase A doesn't rewrite content):

* `http://www.manitobaelection.ca`: 1801 files, e.g. `by-election-2012.html`

## Analytics removed

Google Tag Manager / Google Analytics (and the Google Ads tag that rides on `gtag.js`) were removed in Phase B of the olddroplet migration (owner decision D7, 2026-10-24) by `python3 -I strip_analytics.py 2011.manitobaelection.ca --apply`. Files changed: 1,801 HTML files. IDs: `UA-23791334-1`. Each loader went together with its inline block and the comment around it. Other third-party scripts (fonts, embeds, Jetpack stats) were left as they were.

Snippet shapes removed (IDs and whitespace normalised):

* 1,801 ×

  ```html
  <script async src="https://www.googletagmanager.com/gtag/js?id=<ID>"></script> <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', '<ID>'); </script>
  ```

## ActiveAdmin assets removed

Owner decision (Phase B, 2026-10-24): the archive doesn't host the Rails admin. The site never had admin pages in `site/`, but the compiled ActiveAdmin assets were there. `python3 -I drop_admin_assets.py --apply` removed these 9 files, which no public page references:

* `images/active_admin/admin_notes_icon.png`
* `images/active_admin/loading.gif`
* `images/active_admin/nested_menu_arrow.gif`
* `images/active_admin/nested_menu_arrow_dark.gif`
* `images/active_admin/orderable.png`
* `javascripts/active_admin.js`
* `javascripts/active_admin_vendor.js`
* `stylesheets/active_admin.css`
* `stylesheets/admin/active_admin.css`

**Not admin, left as is:** `pages/13/historical-election-maps.html` loads `/stylesheets/ui-lightness/jquery-ui-1.8.16.custom.css` and `/javascripts/jquery-ui-1.8.16.custom.min.js` for its slider. Neither file was on the server, so they 404ed on the live site too.

## Unrelated files removed

Owner decision (Phase B, 2026-10-25): files that aren't part of the site were removed by `python3 -I drop_unrelated.py 2011.manitobaelection.ca --apply` (23 files). No remaining file references them.

* `uploads/politician_image/1/` (4 files): test upload (the Windows `Koala.jpg` sample photo), not a candidate
* `images/test/` (15 files): unreferenced test copies of the historic maps
* `images/rails.png` (1 file): Rails default `public/` file
* `javascripts/prototype.js` (1 file): Rails default `public/` file, never loaded
* `javascripts/ajax_buttons.js` (1 file): unreferenced script
* `stylesheets/sass/application.sass` (1 file): stylesheet source, not served by the app

## Hosting

Served from **Cloudflare Workers static assets** (Phase B of the olddroplet migration). `wrangler.jsonc`, `.gitignore`, `site/404.html` and this section are written by `hosting.py` (`python3 -I hosting.py 2011.manitobaelection.ca <preview|routed|final>`).

* **Worker:** `static-2011-manitobaelection-ca`, account `Stungeye@gmail.com's Account`.
* **Deploy:** `npx wrangler@4.148.0 deploy` from the repo root. Only `site/` is uploaded.
* **Routes:** `2011.manitobaelection.ca/*` on zone `manitobaelection.ca`, over the existing proxied DNS record.
* **workers.dev:** off (R11). Per-version preview URLs are off (`preview_urls: false`).
* **Serving:** `html_handling: auto-trailing-slash` (`/foo` serves `foo.html`, `/foo/` serves `foo/index.html`; the other forms 307 to those) and `not_found_handling: 404-page` (`site/404.html`, a minimal page added in Phase B).
* **http → https:** the zone setting "Always Use HTTPS" (301 at Cloudflare's edge).
* **Redirect rules:** none.
* **Rollback:** while the old origin is up, remove `routes` from `wrangler.jsonc` and deploy (or delete the route in the dashboard); the origin serves again at once. A bad version can be rolled back with `npx wrangler@4.148.0 rollback`.

## Secret scan

The Phase A §7.2 scan (no `.git`, `.env`, `.ftpconfig`, `.htpasswd`, `debug.log`, `*.php`, `*.sql*`; no `DB_PASSWORD`/`AUTH_KEY`/private keys/`phpinfo()`/`mysql_connect` in any text file) found nothing.

Source: the export tarball `src/2011.manitobaelection.ca.tar.gz`, sha256 `df4eaab0258206d01e03946bec0bc96527ca99513d12713e9c34a1286ca583d0`.
