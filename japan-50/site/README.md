# Japan 50 · itinerary site

Source for https://japan-50-joshmzn.vercel.app/ (Vercel project `japan-50`, team `joshmzn`). Static: `index.html`, `site.css`, `app.js`, `manifest.json`, two icons. No build step.

Deploy: `vercel deploy --prod` from this folder, or push the six files via the Vercel API with paths at the root (not under `src/`; the dashboard's file tree shows `src/` but that's display only).

Bump `?v=` on the css/js links in `index.html` when they change. The booking checklist persists in localStorage under `bk4*`; bump that key in `app.js` when the list order changes.
