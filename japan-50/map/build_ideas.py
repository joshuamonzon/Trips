from xml.sax.saxutils import escape as e
P=[
("Tokyo — Food & Drink",[
("Yakiniku Coco Nemaru Ginza",35.6717064,139.7612311,"Wagyu yakiniku (grill at table). Swap candidate for the Dec 13 Sushi Yuu night if you want wagyu over a second omakase. Private rooms. 1 min from Ginza Stn Exit C3."),
("The SG Club",35.6642434,139.69923140000003,"Top cocktail bar, Shibuya. Opens 6 PM. Nightcap spot."),
("Sushi Punch",35.653654599999996,139.7357535,"Omakase sushi, Azabujuban 7F. Book ahead. Closed Sundays."),
("Yoroniku Ebisu",35.646357099999996,139.71180569999999,"Wagyu yakiniku omakase. Reservation-only, book ~1 month out. Overlaps w/ Coco Nemaru — pick one."),
("Uonami Fish Bar",35.726608899999995,139.6952222,"Retro izakaya, Toshima. Out of the way + seafood overlap — low priority. Closed Mondays."),
("Good Wood Terrace",35.6578,139.6935,"Caribbean jerk chicken, Shibuya (viral after Kanye). Novelty pick. 2-19-3 Dogenzaka."),
]),
("Tokyo — Shopping",[
]),
("Kyoto",[
]),
("Osaka",[
]),
]
out=['<?xml version="1.0" encoding="UTF-8"?>','<kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Japan 50 · Bench (saved, not slotted)</name><Style id="idea"><IconStyle><color>ff00d7ff</color><Icon><href>https://maps.google.com/mapfiles/kml/paddle/ylw-stars.png</href></Icon></IconStyle></Style>']
csv=["folder,name,lat,lng,notes"]
for f,items in [x for x in P if x[1]]:
  out.append(f"<Folder><name>{e(f)}</name>")
  for n,la,lo,d in items:
    out.append(f"<Placemark><styleUrl>#idea</styleUrl><name>{e(n)}</name><description>{e(d)}</description><Point><coordinates>{lo},{la},0</coordinates></Point></Placemark>")
    csv.append(",".join('"'+str(x).replace('"','""')+'"' for x in (f,n,la,lo,d)))
  out.append("</Folder>")
out.append("</Document></kml>")
open("ideas.kml","w").write("\n".join(out)); open("ideas.csv","w").write("\n".join(csv)+"\n")
