# Japan 50 · itinerary site

Source for https://japan-50-joshmzn.vercel.app/ (Vercel project `japan-50`, team `joshmzn`). Static: `index.html`, `site.css`, `app.js`, `manifest.json`, two icons. No build step.

Deploy: the Vercel project is linked to this repo (`joshuamonzon/Trips`, root directory `japan-50/site`), so pushing to `main` deploys production. Manual fallback: `vercel deploy --prod` from this folder.

Bump `?v=` on the css/js links in `index.html` when they change. The booking checklist persists in localStorage under `bk4*`; bump that key in `app.js` when the list order changes.
