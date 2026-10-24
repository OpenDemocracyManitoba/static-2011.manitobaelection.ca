"""Phase B (owner decision, 2026-10-24): drop the Rails ActiveAdmin assets from the 2011 static archive.
Usage: python3 -I drop_admin_assets.py [--apply]   (from the repo root; dry run by default)
The archive has no admin pages; these compiled admin assets aren't referenced by any public file. Refuses to run if one is."""
import os, re, sys

APPLY = '--apply' in sys.argv[1:]
ADMIN = re.compile(r'^(images/active_admin/.*|javascripts/active_admin(_vendor)?\.js|stylesheets/active_admin\.css|stylesheets/admin/.*)$')
files = sorted(os.path.relpath(os.path.join(r, f), 'site') for r, _, fs in os.walk('site') for f in fs)
drop = [f for f in files if ADMIN.match(f)]
names = re.compile(rb'active_admin|stylesheets/admin/')
users = [f for f in files if f not in drop and names.search(open(os.path.join('site', f), 'rb').read())]
print(f'{"APPLY" if APPLY else "dry run"}: {len(drop)} ActiveAdmin files')
for f in drop:
    print('  ', f)
if users:
    sys.exit(f'refusing: public files reference them: {users[:10]}')
if APPLY:
    for f in drop:
        os.remove(os.path.join('site', f))
    for d in ('site/images/active_admin', 'site/stylesheets/admin'):
        if os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)
    section = ('## ActiveAdmin assets removed\n\n'
               'Owner decision (Phase B, 2026-10-24): the archive doesn\'t host the Rails admin. The site never had admin pages in `site/`, '
               f'but the compiled ActiveAdmin assets were there. `python3 -I drop_admin_assets.py --apply` removed these {len(drop)} files, '
               'which no public page references:\n\n' + ''.join(f'* `{f}`\n' for f in drop) +
               '\n**Not admin, left as is:** `pages/13/historical-election-maps.html` loads `/stylesheets/ui-lightness/jquery-ui-1.8.16.custom.css` '
               'and `/javascripts/jquery-ui-1.8.16.custom.min.js` for its slider. Neither file was on the server, so they 404ed on the live site too.\n')
    r = open('README.md').read()
    i = r.find('\n## Hosting\n')
    i = i if i >= 0 else r.find('\n## Secret scan')
    open('README.md', 'w').write(r[:i + 1] + section + '\n' + r[i + 1:])
