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

## Secret scan

The Phase A §7.2 scan (no `.git`, `.env`, `.ftpconfig`, `.htpasswd`, `debug.log`, `*.php`, `*.sql*`; no `DB_PASSWORD`/`AUTH_KEY`/private keys/`phpinfo()`/`mysql_connect` in any text file) found nothing.

Source: the export tarball `src/2011.manitobaelection.ca.tar.gz`, sha256 `df4eaab0258206d01e03946bec0bc96527ca99513d12713e9c34a1286ca583d0`.
