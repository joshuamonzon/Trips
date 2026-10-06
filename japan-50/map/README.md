# Japan 50 · trip map

Pins and travel times for Mom's 50th trip (Nov 27 – Dec 14, 2026). Companion to the itinerary at https://japan-50-joshmzn.vercel.app/.

- `index.html` — interactive map: one tab per stop, pins to scale around the hotel, numbered in visit order, with ≈ travel time from the previous stop and from the hotel. Every chip opens live Google Maps directions.
- `japan50.kml` — all 102 pins for Google My Maps (mymaps.google.com → Create a new map → Import). Red = sleep, blue = numbered stops, grey = stations/airports, one folder per city, plus the route line.
- `build_trip_map.py` + `map_template.html` — the source. Edit the itinerary data at the top of the script and run `python3 build_trip_map.py` to regenerate both files.

Times marked ≈ are estimates (itinerary figures where stated, typical transit otherwise). Intercity legs are the itinerary's own numbers.

## Bench layer

- Saved spots from chat are now slotted into the itinerary days in `build_trip_map.py` (Tsukiji food tour, Nishikawa pillows, Zauo, MixTHINKS, Momotaro, Zuicho, Sagano train, Taiga Takahashi, B.B. Garage).
- `ideas.kml` / `ideas.csv` — the 8 that didn't fit (Coco Nemaru, Yoroniku, SG Club, Sushi Punch, Uonami, Good Wood Terrace, KUOE, Doguyasuji), each with the reason. Yellow stars. Import as a second layer in the same My Map.
- `build_ideas.py` — source for that layer.
