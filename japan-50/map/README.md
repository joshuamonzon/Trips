# Japan 50 · trip map

Pins and travel times for Mom's 50th trip (Nov 27 – Dec 14, 2026). Companion to the itinerary at https://japan-50-joshmzn.vercel.app/.

- `index.html` — interactive map: one tab per stop, pins to scale around the hotel, numbered in visit order, with ≈ travel time from the previous stop and from the hotel. Every chip opens live Google Maps directions.
- `japan50.kml` — all 102 pins for Google My Maps (mymaps.google.com → Create a new map → Import). Red = sleep, blue = numbered stops, grey = stations/airports, one folder per city, plus the route line.
- `build_trip_map.py` + `map_template.html` — the source. Edit the itinerary data at the top of the script and run `python3 build_trip_map.py` to regenerate both files.

Times marked ≈ are estimates (itinerary figures where stated, typical transit otherwise). Intercity legs are the itinerary's own numbers.

## Bench layer

- `ideas.kml` / `ideas.csv` — saved spots that didn't make the schedule (Coco Nemaru, Yoroniku, SG Club, Sushi Punch, Uonami, Good Wood Terrace), each pin says why. Yellow stars. Import as a second layer in the same My Map.
- `build_ideas.py` — source for that layer.

## Changelog

- **Oct 6** — Route reworked: snow monkeys and Kinosaki cut; Kanazawa night 2 moved to Motoyu Ishiya ryokan (onsen + crab kaiseki); Kyoto now 5 nights with a shopping day, Hyotei (3*) dinner and Kikunoi lunch; Osaka 2 nights (Kuromon, Doguyasuji, Shinsaibashi, Amemura/B.B. Garage, Yamazaki, Umeda, Shinsekai); Seoul rebuilt around Gangnam clinics (IV, HBOT, Reberry, Myshopper, Park Jun, Amore Seongsu, Inwangsan hike) at Andaz Gangnam; go-karts, Meiji Jingu, Kenroku-en, Saiho-ji, Shunkoin and the Kurama hike cut.
