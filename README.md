# maddy-designs

Static site for [Maddy Designs](https://maddy-designs.yurshack.co.uk/), synced from the Namecheap host (`~/subdomains/maddy-designs`).

This tree is the Next.js static export currently deployed on the server (`index.html`, `_next/`, assets, `.htaccess`).

## GitHub Pages

Published at https://sjwross.github.io/maddy-designs/

The deploy workflow rewrites root-absolute asset paths to the `/maddy-designs` project base at publish time, so the Namecheap copy (paths like `/_next/...`) stays unchanged on `main`.

Pages source is **GitHub Actions** (repo Settings → Pages).
