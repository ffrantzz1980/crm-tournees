// Service worker : l'application fonctionne hors connexion ; les fonds de carte consultés sont gardés en cache.
const APP='crm-app-v2',TILES='crm-tiles-v1',MAXT=3000;
self.addEventListener('install',e=>{e.waitUntil(caches.open(APP).then(c=>c.addAll(['./','index.html','crm-tournees.html','manifest.webmanifest','icon-192.png','icon-512.png'])));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(n=>![APP,TILES].includes(n)).map(n=>caches.delete(n)))));self.clients.claim()});
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET')return;
  if(u.hostname.endsWith('tile.openstreetmap.org')){e.respondWith(caches.open(TILES).then(async c=>{const hit=await c.match(e.request);if(hit)return hit;
    try{const r=await fetch(e.request);if(r.ok){c.put(e.request,r.clone());c.keys().then(k=>{if(k.length>MAXT)c.delete(k[0])})}return r}catch(err){return new Response('',{status:504})}}));return}
  if(u.origin===location.origin){e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(APP).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('crm-tournees.html'))))}
});
