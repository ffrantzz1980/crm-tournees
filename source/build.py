# Construit UNE seule application : dossier dist/crm-tournees/ (PC, clé USB, web et mobile)
import os,shutil,json
from PIL import Image,ImageDraw
L='../libs/';OUT='dist/crm-tournees'
s=open('src.html').read()
x=open(L+'xlsx-0.18.5/package/dist/xlsx.full.min.js').read().replace('</script','<\\/script')
l=open(L+'leaflet-1.9.4/package/dist/leaflet.js').read().replace('</script','<\\/script')
c=open(L+'leaflet-1.9.4/package/dist/leaflet.css').read()
s=s.replace('<style>/*LEAFLETCSS*/</style>','<style>'+c+'</style>').replace('<script>/*LEAFLET*/</script>','<script>'+l+'</script>').replace('<script>/*XLSX*/</script>','<script>'+x+'</script>')
s=s.replace('<!--PWA-->','<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="icon-192.png">\n<link rel="apple-touch-icon" href="icon-192.png">\n<meta name="apple-mobile-web-app-capable" content="yes">')
os.makedirs(OUT,exist_ok=True)
open(OUT+'/crm-tournees.html','w').write(s)
open('crm-tournees.html','w').write(s)
open(OUT+'/index.html','w').write('<!doctype html><meta charset="utf-8"><title>CRM Tournées</title><meta http-equiv="refresh" content="0;url=crm-tournees.html"><a href="crm-tournees.html">Ouvrir CRM Tournées</a>')
json.dump({"name":"CRM Tournées","short_name":"Tournées","start_url":"crm-tournees.html","scope":".","display":"standalone","background_color":"#f6f7f9","theme_color":"#1f6feb","lang":"fr",
 "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any maskable"}]},open(OUT+'/manifest.webmanifest','w'),ensure_ascii=False,indent=1)
for n in (192,512):
  im=Image.new('RGB',(n,n),'#1f6feb');d=ImageDraw.Draw(im);u=n/16
  pts=[(4*u,11*u),(7*u,6*u),(10*u,9*u),(12.5*u,4.5*u)]
  d.line(pts,fill='white',width=int(u*0.9),joint='curve')
  for p in pts:d.ellipse([p[0]-1.1*u,p[1]-1.1*u,p[0]+1.1*u,p[1]+1.1*u],fill='white')
  im.save(f'{OUT}/icon-{n}.png')
shutil.copy('sw.js',OUT+'/sw.js');shutil.copy('LISEZMOI.txt',OUT+'/LISEZMOI.txt')
