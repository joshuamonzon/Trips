from xml.sax.saxutils import escape as e
P=[
("Tokyo — Food & Drink",[
("Tsukiji Food Tour w/ Ali (meet point)",35.666553,139.7712317,"Airbnb Experience 6919404 — ~2hr, from $32/pp, food not included, bring cash. Book 7 AM slot early in trip. Itinerary already hits Tsukiji (Tokyo #5). https://www.airbnb.com/experiences/6919404"),
("Zauo Shibuya",35.6624737,139.6998545,"Catch-your-own-fish restaurant. Reserve ahead for evenings. Space apart from Tsukiji."),
("Yakiniku Coco Nemaru Ginza",35.6717064,139.7612311,"Wagyu yakiniku (grill at table). Ask for a private room. 1 min from Ginza Stn Exit C3."),
("Katsudon-ya Zuicho",35.662703,139.6953601,"One-dish katsudon spot, ~8 seats, expect a line. Closed Sundays."),
("Omoide Yokocho (Memory Lane)",35.692703699999996,139.6995778,"Yakitori alley by Shinjuku Stn. Already on the itinerary (Tokyo #11)."),
("The SG Club",35.6642434,139.69923140000003,"Top cocktail bar, Shibuya. Opens 6 PM. Nightcap spot."),
("Sushi Punch",35.653654599999996,139.7357535,"Omakase sushi, Azabujuban 7F. Book ahead. Closed Sundays."),
("Yoroniku Ebisu",35.646357099999996,139.71180569999999,"Wagyu yakiniku omakase. Reservation-only, book ~1 month out. Overlaps w/ Coco Nemaru — pick one."),
("Uonami Fish Bar",35.726608899999995,139.6952222,"Retro izakaya, Toshima. Out of the way + seafood overlap — low priority. Closed Mondays."),
("Good Wood Terrace",35.6578,139.6935,"Caribbean jerk chicken, Shibuya (viral after Kanye). Novelty pick. 2-19-3 Dogenzaka."),
]),
("Tokyo — Shopping",[
("MixTHINKS Harajuku",35.6671291,139.7038071,"Vintage designer bags. Ask condition grade (N/S/A/AB/B). Bring passport for tax-free."),
("Momotaro Jeans Aoyama",35.663737000000005,139.71055719999998,"Japanese selvedge denim. Free hemming; can be a wait. Ask about shrinkage."),
("Nishikawa Sleep Navi — Matsuya Ginza",35.6723299,139.7667615,"Custom-fit pillow. Walk-ins OK; ~20-30 min fitting + ~40 min make. Gift idea for mom."),
("Nishikawa — Nihonbashi (alt)",35.6823657,139.7748403,"Alt custom pillow location. Reservations available online."),
]),
("Kyoto",[
("Sagano Romantic Train — Saga Torokko Stn",35.018568,135.6807823,"Peak fall leaves late Nov. Book exactly 1 month out; Car No. 5 open-air; right side (AB seats). Pair w/ Arashiyama."),
("Taiga Takahashi (T.T)",35.0019692,135.7743322,"Vintage-inspired workwear in a Gion machiya. 12-7 PM daily."),
("KUOE Kyoto (optional)",35.00851,135.76682,"Build-your-own watch. Optional — B.B. Garage is the priority watch stop. Closed Tue."),
]),
("Osaka",[
("B.B. Garage (Amerikamura)",34.6703075,135.4985753,"Vintage watches + Americana. 12-8 PM, closed Wed. Ask about overhaul/warranty + original parts."),
("Sennichimae Doguyasuji",34.664014099999996,135.5035063,"Kitchenware street — knives (engraving), fake food. 10 AM-6 PM. Go before Amemura opens."),
]),
]
out=['<?xml version="1.0" encoding="UTF-8"?>','<kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Japan 50 · Ideas from chat</name><Style id="idea"><IconStyle><color>ff00d7ff</color><Icon><href>https://maps.google.com/mapfiles/kml/paddle/ylw-stars.png</href></Icon></IconStyle></Style>']
csv=["folder,name,lat,lng,notes"]
for f,items in P:
  out.append(f"<Folder><name>{e(f)}</name>")
  for n,la,lo,d in items:
    out.append(f"<Placemark><styleUrl>#idea</styleUrl><name>{e(n)}</name><description>{e(d)}</description><Point><coordinates>{lo},{la},0</coordinates></Point></Placemark>")
    csv.append(",".join('"'+str(x).replace('"','""')+'"' for x in (f,n,la,lo,d)))
  out.append("</Folder>")
out.append("</Document></kml>")
open("ideas.kml","w").write("\n".join(out)); open("ideas.csv","w").write("\n".join(csv)+"\n")
