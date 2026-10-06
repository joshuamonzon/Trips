#!/usr/bin/env python3
"""Builds japan50.kml (Google My Maps import) and japan50-map.html (artifact) from one data set."""
import json, math, html as H

# ---------------- pins: id -> (name, lat, lng, type, place_id, short) ----------------
P = {}
def pin(id, name, lat, lng, typ="stop", pid=None, short=None):
    P[id] = dict(id=id, name=name, lat=lat, lng=lng, type=typ, pid=pid, short=short or name)

# Tokyo
pin("narita","Narita Airport (NRT)",35.7647,140.3864,"transit",None,"Narita")
pin("gracery","Hotel Gracery Shinjuku",35.6953583,139.7020345,"sleep","ChIJF-U1JdiMGGARaay7KIrrtZ0","Gracery")
pin("shinjuku","Shinjuku Station",35.6896067,139.7005713,"transit","ChIJH7qx1tCMGGAR1f2s7PGhMhw","Shinjuku Sta")
pin("shibuya","Shibuya Scramble Crossing",35.659482,139.7005596,"stop","ChIJK9EM68qLGGARacmu4KJj5SA","Shibuya Crossing")
pin("sensoji","Senso-ji",35.7147651,139.7966553,"stop","ChIJ8T1GpMGOGGARDYGSgpooDWw")
pin("kappabashi","Kappabashi Kitchen Town",35.7105797,139.7879645,"stop","ChIJXYV-6JWOGGAR85vIZbM1RCE","Kappabashi")
pin("tsukiji","Tsukiji Outer Market",35.6647703,139.7702515,"stop","ChIJW2cLzSGLGGARXAKXv6EkbqI","Tsukiji")
pin("ginza","Ginza (Uniqlo flagship)",35.6702448,139.7634686,"stop","ChIJb9MHbuaLGGAR0xi-noU25UU","Ginza")
pin("teamlab","teamLab Planets",35.6491207,139.7897739,"stop","ChIJSeco5wiJGGARItbTS8lQ5G0","teamLab")
pin("meiji","Meiji Jingu",35.6763976,139.6993259,"stop","ChIJ5SZMmreMGGARcz8QSTiJyo8","Meiji Shrine")
pin("solakzade","Solakzade (vintage eyewear)",35.6683005,139.7063472,"stop","ChIJ07gjeKSMGGARXVe4hKptEMA","Solakzade")
pin("kart","Street Kart Shibuya",35.6578204,139.6942086,"stop","ChIJAegY-QaNGGAR0t2U3IVjyyE","Street Kart")
pin("omoide","Omoide Yokocho",35.6927037,139.6995778,"stop","ChIJP9eKBdeMGGAR0zzBXJNVj5A")
pin("goldengai","Golden Gai",35.6941118,139.7047611,"stop","ChIJr7mGZdmMGGARjxoMFeHApXE")
pin("zoetrope","Bar Zoetrope",35.6944997,139.6984625,"stop","ChIJA9cRNtaMGGARrZO3HTmHkXs")
pin("kawaguchiko","Kawaguchiko Station",35.4982362,138.7688409,"transit","ChIJV3dIuoJgGWAR7bQ0vq8DlE0","Kawaguchiko Sta")
pin("tenjo","Mt. Tenjo / Fuji Panoramic Ropeway",35.5038024,138.7743776,"stop","ChIJMZmgjCZeGWAR6wB5-jDP5Tk","Mt. Tenjo")
pin("hoto","Hoto Fudo",35.4988609,138.7686546,"stop","ChIJD9e0oIJgGWARjCiXDS-GJmA")
pin("oishi","Oishi Park",35.522904,138.7457522,"stop","ChIJlSsLjKZfGWARBCllOgtTLqI")
pin("kyubey","Kyubey Ginza",35.6684684,139.7612701,"stop","ChIJu3eG8uiLGGAR14kVvD_YrHI","Kyubey")
pin("nishikawa","Nishikawa custom pillow (Matsuya Ginza)",35.6723299,139.7667615,"stop","ChIJG8GsGImLGGAR1PfGCC2k-ok","Nishikawa pillow")
pin("zauo","Zauo Shibuya",35.6624737,139.6998545,"stop","ChIJa3cs7aiMGGAR8weY287qaJE","Zauo")
pin("mixthinks","MixTHINKS Harajuku (vintage designer bags)",35.6671291,139.7038071,"stop","ChIJd5DukxmNGGAR0dK6sam4DIs","MixTHINKS")
pin("momotaro","Momotaro Jeans Aoyama",35.663737,139.7105572,"stop","ChIJLcQt9l-LGGAR0dWhLQOnX-Y","Momotaro Jeans")
pin("zuicho","Katsudon-ya Zuicho",35.662703,139.6953601,"stop","ChIJCZkGEqyMGGAR72gGFgeNxEE","Zuicho")
pin("shimokita","Shimokitazawa (vintage town)",35.660272,139.6672633,"stop","ChIJ3dW4JQDzGGARRqcRBSeCqv0","Shimokitazawa")
pin("tokyosta","Tokyo Station",35.6812996,139.7670658,"transit","ChIJC3Cf2PuLGGAROO00ukl8JwA","Tokyo Sta")
# Nagano
pin("nagano","Nagano Station",36.6431243,138.1886437,"transit","ChIJh0bai5KGHWARO9I7pK11KTU","Nagano Sta")
pin("monkey","Jigokudani Monkey Park",36.7326856,138.4621364,"stop","ChIJzyCiTOzzHWARH9aN73OLTfY","Monkey Park")
pin("shibuhotel","Shibu Hotel (Shibu Onsen)",36.7344059,138.4312715,"sleep","ChIJz292noP0HWARDlUe5KLy9nY","Shibu Hotel")
pin("kanaguya","Kanaguya (Spirited Away inn)",36.734713,138.4329137,"stop","ChIJb0YSwoP0HWARoFR4EcLeZPM","Kanaguya")
pin("yudanaka","Yudanaka Station",36.7400,138.4106,"transit",None,"Yudanaka Sta")
# Kanazawa
pin("kanazawasta","Kanazawa Station",36.5780443,136.6481714,"transit","ChIJBYa7A0Iz-F8R6qe7HgH2XV0","Kanazawa Sta")
pin("intergate","Hotel Intergate Kanazawa",36.5682402,136.6535862,"sleep","ChIJ7UkqBf0z-F8Rf332F5I3XzM","Intergate")
pin("nagamachi","Nagamachi Samurai District",36.5637517,136.6510146,"stop","ChIJhycOJtYz-F8RO54LaTG6_p0","Nagamachi")
pin("nomura","Nomura-ke Samurai House",36.5642058,136.6500324,"stop","ChIJF_AqPH4z-F8Rmtm1IKiShVQ","Nomura house")
pin("kenrokuen","Kenroku-en",36.5621278,136.6626515,"stop","ChIJBVmy-YMz-F8R5PID8D17Cpc")
pin("fukumitsuya","Fukumitsuya Sake Brewery",36.5537054,136.6723403,"stop","ChIJp8mGw4oz-F8RG6DuHOB1z6Y","Fukumitsuya")
pin("shirakawabt","Shirakawa-go Bus Terminal",36.2619463,136.9068852,"transit","ChIJKx0Jc79x-F8RdUi6Khf_-Is","Shirakawa-go bus")
pin("shiroyama","Shiroyama Viewpoint",36.2630027,136.9085578,"stop","ChIJ4xHe8r9x-F8RybxsbX5Rr-o","Shiroyama view")
pin("wada","Wada House",36.259905,136.907635,"stop","ChIJdRv_s75x-F8R94Uw560g-iM")
pin("higashi","Higashi Chaya District",36.5725825,136.6665601,"stop","ChIJsfC6oXQz-F8RdA1qXiF6jLs","Higashi Chaya")
pin("omicho","Omicho Market",36.5717335,136.6558651,"stop","ChIJ0xPT93Az-F8RpTSlbHwo9L8")
pin("ishiya","Motoyu Ishiya (Fukatani Onsen)",36.6137028,136.7209583,"sleep","ChIJYRXlBUMt-F8RB_F70Zzyx74","Motoyu Ishiya")
# Kyoto
pin("kyotosta","Kyoto Station",34.985849,135.7587667,"transit","ChIJ7wKLka4IAWARCByidG5EGrY","Kyoto Sta")
pin("resol","Hotel Resol Kyoto Kawaramachi Sanjo",35.0079505,135.7692203,"sleep","ChIJq2kbb5MIAWARPjnryqGzDrg","Hotel Resol")
pin("bamboo","Arashiyama Bamboo Grove",35.0168187,135.6713013,"stop","ChIJrYtcv-urAWAR3XzWvXv8n_s","Bamboo Grove")
pin("tenryuji","Tenryu-ji",35.0158379,135.6737654,"stop","ChIJk54PuAGqAWARwEgz_9o-nM0")
pin("okochi","Okochi Sanso Garden",35.0167147,135.6699227,"stop","ChIJGTfQ9gSqAWARvzp3lzOgjk8","Okochi Sanso")
pin("torokko","Sagano Romantic Train (Saga Torokko Sta)",35.018568,135.6807823,"stop","ChIJh2v-m_6pAWAR9TR4D4O6S24","Sagano train")
pin("taiga","Taiga Takahashi (T.T)",35.0019692,135.7743322,"stop","ChIJSVB1LIIJAWARSqg5sapwPYo","Taiga Takahashi")
pin("teramachi","Teramachi + Shinkyogoku arcades",35.0071037,135.7671558,"stop","ChIJ6fUyMZQIAWAR4tOOD7AkWJw","Teramachi")
pin("takashimaya","Takashimaya Kyoto (Shijo)",35.0031004,135.7684962,"stop","ChIJwzqJepUIAWARvlUYqigZpJI","Takashimaya")
pin("kuoe","KUOE Kyoto (build-your-own watch)",35.00851,135.76682,"stop","ChIJBc57aw4JAWARNRkUdgsACvY","KUOE")
pin("hyotei","Hyotei (3-star kaiseki, since 1837)",35.0114133,135.7867623,"stop","ChIJw5-sbOAIAWAR3IVM2hFyg5A","Hyotei")
pin("nishiki","Nishiki Market",35.0050258,135.764723,"stop","ChIJT8uMzZwIAWARnGzsARCjnrY")
pin("kembu","Samurai Kembu Theater",35.0095371,135.7755388,"stop","ChIJXQxzcPgMAWAR2MVdzqV2kkY","Samurai Kembu")
pin("todaiji","Todai-ji (Nara)",34.6889851,135.8398158,"stop","ChIJ3XYIepA5AWARjzzVnT-skPg","Todai-ji")
pin("kasuga","Kasuga Taisha (Nara)",34.6815454,135.8484719,"stop","ChIJ1Wqwa8A5AWARlpXjgoPnl0w","Kasuga Taisha")
pin("fushimisake","Fushimi Sake Village",34.9325,135.7605556,"stop","ChIJRwOaco4PAWARzaIhH6-kLG8","Fushimi sake")
pin("inari","Fushimi Inari Taisha",34.9676945,135.7791876,"stop","ChIJIW0uPRUPAWAR6eI6dRzKGns","Fushimi Inari")
pin("shunkoin","Shunkoin Temple (zazen)",35.0240552,135.7195071,"stop","ChIJq7v2UZsHAWARXkzyx5VseK8","Shunkoin")
pin("ajiro","Ajiro (shojin ryori)",35.0208513,135.7210186,"stop","ChIJc2Ej1JsHAWARDIYCJ-sh5lk","Ajiro")
pin("kurama","Kurama-dera",35.1181404,135.7708892,"stop","ChIJnTF3sxKmAWAROIRwRX49KFA")
pin("kifune","Kifune Shrine",35.1220909,135.7629101,"stop","ChIJCZEK8wimAWARi1RkteQaAh0")
pin("pontocho","Pontocho Alley",35.0039339,135.7710439,"stop","ChIJP2DblBgJAWARAgLlF0vWT6o","Pontocho")
pin("bark6","Bar K6",35.0133198,135.770556,"stop","ChIJ2b4ClM0HAWARHNrgkqv5EDI")
pin("saihoji","Saiho-ji (Moss Temple)",34.9921777,135.6837103,"stop","ChIJM3V7rDEHAWAR1bBbYdXO7K4","Saiho-ji")
pin("kikunoi","Kikunoi Honten",35.0014754,135.7820562,"stop","ChIJVVXF5doIAWARUetIixOU-sw","Kikunoi")
pin("giontea","Gion teahouse (tea ceremony, Hanamikoji)",35.0036,135.7750,"stop",None,"Gion tea ceremony")
pin("ninenzaka","Ninenzaka",34.9983989,135.7808431,"stop","ChIJlwyrGNAIAWARNb5hUHdZruY")
pin("kiyomizu","Kiyomizu-dera",34.9946662,135.784661,"stop","ChIJB_vchdMIAWARujTEUIZlr2I")
pin("hatanaka","Gion Hatanaka (maiko dinner)",35.0023148,135.7789355,"stop","ChIJqWdMmsQIAWAR9LzT5fDOD7c","Gion Hatanaka")
# Kinosaki
pin("kinosakista","Kinosaki Onsen Station",35.6237606,134.8136714,"transit","ChIJ2eGnhDvI_18Rje0B1J-k_Dg","Kinosaki Sta")
pin("nishimuraya","Nishimuraya Hotel Shogetsutei",35.6282431,134.7994994,"sleep","ChIJYSnGGnjJ_18RSVe5KxXSQzA","Shogetsutei")
pin("ichinoyu","Ichino-yu (cave bath)",35.6261765,134.8094851,"stop","ChIJGz-LezDI_18RiRGCeYcJUk4","Ichino-yu")
pin("kinoropeway","Kinosaki Onsen Ropeway",35.6252276,134.8038768,"stop","ChIJeU4pIDfI_18RsS2fCbfb3QA","Ropeway")
# Osaka
pin("shinosaka","Shin-Osaka Station",34.7334658,135.5002547,"transit","ChIJSc4SbDnkAGARz3YQv-DE1zs","Shin-Osaka")
pin("yamazaki","Suntory Yamazaki Distillery",34.8924574,135.6744508,"stop","ChIJ-WxR9WMDAWARHW0W4OC39qE","Yamazaki")
pin("crosshotel","Cross Hotel Osaka",34.6697148,135.5007625,"sleep","ChIJA0zO7hPnAGARHooEfgZ_MsY","Cross Hotel")
pin("dotonbori","Dotonbori",34.6686471,135.5030983,"stop","ChIJg2DcJhXnAGARCbeAHoZrPeQ")
pin("bbgarage","B.B. Garage (vintage watches)",34.6703075,135.4985753,"stop","ChIJ62Sj0EznAGARLILmS20T5LM","B.B. Garage")
pin("kuromon","Kuromon Market",34.6653511,135.5062417,"stop","ChIJXSJB5UHnAGARQcEjvngsHaw","Kuromon")
pin("doguyasuji","Sennichimae Doguyasuji (kitchen street)",34.6640141,135.5035063,"stop","ChIJfQfezmvnAGARy4Sd3VGFy_A","Doguyasuji")
pin("shinsaibashi","Shinsaibashi-suji arcade",34.6725086,135.5013657,"stop","ChIJc7M3_BPnAGARI8OZlTnEXGI","Shinsaibashi")
pin("grandfront","Grand Front Osaka (Umeda)",34.7039162,135.4940095,"stop","ChIJAQAAB4_mAGAR1alcFGtOaAo","Grand Front")
pin("tsutenkaku","Tsutenkaku / Shinsekai",34.6524992,135.5063058,"stop","ChIJ_0Lgd2DnAGARV0X03lbPy-U","Shinsekai")
pin("namba","Namba Station (airport express)",34.6627,135.5021,"transit",None,"Namba Sta")
pin("kix","Kansai International Airport (KIX)",34.4319994,135.2366019,"transit","ChIJ9_rNIxO5AGARiI-QjZ-ncfE","KIX")
# Seoul
pin("icn","Incheon International Airport (ICN)",37.458666,126.4419679,"transit","ChIJWfpeOoOaezUR1L5cy5agS40","ICN")
pin("ninetree","Nine Tree by Parnas Insadong",37.5746394,126.9832068,"sleep","ChIJYRZuA-KjfDUR3EIotimBRBQ","Nine Tree")
pin("gyeongbok","Gyeongbokgung Palace",37.579617,126.977041,"stop","ChIJod7tSseifDUR9hXHLFNGMIs","Gyeongbokgung")
pin("bukchon","Bukchon Hanok Village",37.5814696,126.9849519,"stop","ChIJT8H4r9qifDURmuXJ_6m6vM0","Bukchon")
pin("jogyesa","Jogyesa Temple",37.5738369,126.982202,"stop","ChIJHYhJ5OmifDURMOSQ2D-6lFY","Jogyesa")
pin("gwangjang","Gwangjang Market",37.5700385,126.9996038,"stop","ChIJm3V0fu2ifDURRJ8IMUijVtY","Gwangjang")
pin("myeongdong","Myeongdong Street",37.5637699,126.9844765,"stop","ChIJXz2vx_GifDURImd3aTJZ1VA","Myeongdong")
pin("oliveyoung","Olive Young Myeongdong Town",37.563946,126.9851624,"stop","ChIJ9XDV4O-ifDURKjI94KEc1h4","Olive Young")
pin("gangnam","Gangnam Station (skin clinic area)",37.497952,127.027619,"stop","ChIJKxs2jFmhfDURPP--kvKavw0","Gangnam")
pin("dragonhill","Dragon Hill Spa",37.5281648,126.9643878,"stop","ChIJiVvysQGifDURayzTq-wONHc","Dragon Hill")
pin("seongsu","Seongsu-dong (alt afternoon)",37.5406846,127.0566319,"stop","ChIJgQD8o5OkfDUR6b0_C5FwjNk","Seongsu-dong")
pin("seoulsky","Seoul Sky (Lotte World Tower)",37.5125295,127.102305,"stop","ChIJu7dpc45FezURhLMS5U5eaJk","Seoul Sky")
pin("nseoul","N Seoul Tower",37.5511694,126.9882266,"stop","ChIJqWqOqFeifDURpYJ5LnxX-Fw","N Seoul Tower")
pin("andaz","Andaz Seoul Gangnam",37.5254876,127.0289201,"sleep","ChIJix_5SI6jfDURODDRE4Ama2M","Andaz")
pin("hanaclinic","AGJ Hana Clinic (NAD+ / glutathione IV)",37.5282929,127.037446,"stop","ChIJF-_ROQCjfDUR5Miy1Yc2Uq4","Hana Clinic")
pin("o2on","O2ON (hyperbaric oxygen)",37.5207428,127.0302086,"stop","ChIJu6A69vOjfDURvocQmFQEbFY","O2ON")
pin("garosugil","Garosu-gil",37.5210566,127.0228686,"stop","ChIJI_IUbOujfDUReyU3t6AyGoM","Garosu-gil")
pin("reberry","Reberry Clinic Gangnam (skin)",37.5018395,127.0246454,"stop","ChIJYZZUr5oaO2QRD9IKKBX6Q9U","Reberry")
pin("myshopper","Myshopper (personal color)",37.5231212,127.0323979,"stop","ChIJr9RmQmajfDURfz0pyNU27u4","Myshopper")
pin("parkjun","Park Jun Beauty Lab Cheongdam (scalp spa)",37.5184956,127.0502096,"stop","ChIJsWosT3CkfDURVi3y21bRSUo","Park Jun")
pin("amore","AMORE Seongsu (custom skincare)",37.5444101,127.0591197,"stop","ChIJsy6u20mlfDURQOlVT0xmv6U","Amore Seongsu")
pin("inwangsan","Inwangsan trailhead",37.5812412,126.9545483,"stop","ChIJwVINcm6jfDURGcu6ZKSQZkY","Inwangsan")
pin("tosokchon","Tosokchon Samgyetang",37.5777786,126.9715909,"stop","ChIJb5OOGL6ifDURU29ID3t8aOA","Tosokchon")
# Tokyo 2
pin("metropolitan","Hotel Metropolitan Tokyo Marunouchi",35.6838969,139.7685697,"sleep","ChIJkwDaxf6LGGARl7WXPY_ic9A","Metropolitan")
pin("sushiyuu","Sushi Yuu (Nishiazabu)",35.6618348,139.725206,"stop","ChIJ13sWRHqLGGARX9fpN_Tkxfc","Sushi Yuu")
pin("eastgarden","Imperial Palace East Garden",35.6867824,139.7571445,"stop","ChIJPfFaQhOMGGAR-QPbNQoAG6M","East Garden")

# ---------------- itinerary ----------------
# stop = (pin_id, time, note, hop) ; hop = (minutes, mode) travel FROM the previous stop, or None -> estimate
# mode: walk, train, subway, bus, taxi, flight, ropeway, hike, shuttle
CITIES = [
 dict(id="tokyo", n=1, name="Tokyo", kanji="東京", dates="Nov 28 – Dec 2", nights="4 nights", hotel="gracery",
  hotel_note="Godzilla on the roof. Narita Express stops at Shinjuku. Alt: Shibuya Stream Excel.",
  days=[
   dict(date="Sat Nov 28", title="Land, breathe, ramen, sleep", stops=[
     ("narita","4:30pm","Land. Immigration by 5:30. Buy N'EX tickets at the counter after customs.",None),
     ("gracery","7:15pm","Check in. Hotel by 7:15.",(80,"train")),
     ("shibuya","evening","Stand in the middle of it, then watch from above.",(15,"train")),
     ("gracery","10pm","Ramen on the way. Bed by 10.",(15,"train")),
   ]),
   dict(date="Sun Nov 29", title="Old Tokyo at dawn, the knife street, a chef-led fish market, Ginza, teamLab", stops=[
     ("sensoji","6:30am","Tokyo's oldest temple at dawn, 30 min, then Nakamise street. By 10am it's a mob.",(35,"subway")),
     ("kappabashi","8am","Knives engraved with your name. Buy now, forward home in the suitcase.",(10,"walk")),
     ("tsukiji","10am","Tsukiji food tour with Ali (ex-Milos seafood chef), 10–noon. Meet at the Shinran Shonin statue. Food not included: bring cash. airbnb.com/experiences/6919404",(20,"subway")),
     ("nishikawa","12:30pm","Custom-fit pillow at Nishikawa, Matsuya 7F. Walk-in OK: ~30 min fitting, ~40 min to make, so shop Ginza while it's built.",(15,"walk")),
     ("ginza","1:15pm","12-floor Uniqlo, Itoya, depachika food halls. Pick up the pillows on the way out. Passports out for tax-free.",(5,"walk")),
     ("teamlab","3pm","Timed slot. Barefoot, knee-deep in projected koi. Book 3 weeks out.",(15,"subway")),
     ("zauo","5:45pm","Early dinner: fish your own from the boat, they cook it how you want. Reserve. Done by 7:30.",(40,"subway")),
     ("gracery","7:45pm","Early bed. Nothing past 8pm.",(15,"train")),
   ]),
   dict(date="Mon Nov 30", title="Harajuku to Aoyama on foot, vintage town, yakitori alley, tiny bars", stops=[
     ("solakzade","10:30am","Start in Harajuku back streets (Cat Street). Dad's stop: frames from the 1800s–1980s, fitted like a tailor.",(15,"train")),
     ("mixthinks","11:30am","Vintage designer bags. Ask the condition grade (N/S/A/AB). Passports for tax-free.",(5,"walk")),
     ("momotaro","12:30pm","Japanese selvedge denim. Free hemming while you eat (~1 hr). Omotesando on the way.",(12,"walk")),
     ("zuicho","1:45pm","Katsudon lunch, one dish, 8 seats, short line. Then back to Momotaro for the hemmed jeans.",(20,"subway")),
     ("shimokita","3:30pm","Shimokitazawa: a whole neighborhood of vintage shops, record stores and cafés. Two hours on foot.",(20,"train")),
     ("omoide","7pm","Yakitori under the train tracks.",(20,"train")),
     ("goldengai","8:30pm","Six alleys, 200 six-seat bars. ~¥1,000 cover each.",(8,"walk")),
     ("zoetrope","9pm","Start the whisky here, then hop.",(8,"walk")),
     ("gracery","late","Walk home.",(5,"walk")),
   ]),
   dict(date="Tue Dec 1", title="Mt. Fuji day trip, then the sushi counter", stops=[
     ("shinjuku","7:15am","Fuji Excursion train, 7:30 departure. Right side faces the mountain.",(8,"walk")),
     ("kawaguchiko","9:20am","Arrive lakeside.",(110,"train")),
     ("tenjo","10am","An hour of real climbing to a viewpoint where Fuji fills the horizon. Ropeway down.",(15,"walk")),
     ("hoto","12:30pm","Hoto: fat-noodle miso stew.",(15,"walk")),
     ("oishi","2pm","Lakeshore reflection shot.",(25,"bus")),
     ("kawaguchiko","3:45pm","Train back by 4.",(25,"bus")),
     ("shinjuku","6pm","Shower and change at the hotel.",(110,"train")),
     ("kyubey","7:30pm","Omakase at the classic counter, since 1935. Pack tonight: big bags to the front desk in the morning.",(20,"subway")),
     ("gracery","10pm","",(20,"subway")),
   ]),
  ]),
 dict(id="kanazawa", n=2, name="Kanazawa", kanji="金沢", dates="Dec 2 – 4", nights="2 nights", hotel="intergate",
  hotel_note="Night 1 here: free evening drinks, great breakfast, 15 min from the station. Night 2 at Motoyu Ishiya, a 200-year-old onsen ryokan 25 min out of town (kaiseki dinner + breakfast, iron-red spring water). Big bags forwarded Tokyo → Kyoto.",
  days=[
   dict(date="Wed Dec 2", title="Fish market lunch, geisha lanes, gold leaf, samurai streets, sake", stops=[
     ("tokyosta","7:45am","Hokuriku Shinkansen direct, 8am. Left side for the mountains.",(25,"train")),
     ("kanazawasta","10:30am","In by 10:30.",(150,"train")),
     ("intergate","11am","Drop the overnight bag.",(15,"bus")),
     ("omicho","11:30am","Counter lunch: peak snow crab, uni, sweet shrimp.",(10,"walk")),
     ("higashi","1pm","1820s teahouse district. Gild chopsticks, eat gold-leaf ice cream. Two hours of lanes and shops.",(15,"walk")),
     ("nagamachi","3:30pm","Earthen walls, narrow lanes.",(20,"bus")),
     ("nomura","4pm","Real samurai residence: armor, tea room, tiny garden. 45 min, not a museum day.",(3,"walk")),
     ("fukumitsuya","6pm","Nodoguro dinner nearby, then a sake flight at the 400-year-old brewery.",(15,"walk")),
     ("intergate","9pm","",(20,"bus")),
   ]),
   dict(date="Thu Dec 3", title="The thatched village in the snow, then your own hot spring", stops=[
     ("kanazawasta","7:45am","Check out, bag to the station locker. 8:10 direct bus to Shirakawa-go.",(15,"bus")),
     ("shirakawabt","9:25am","Bus drops you at the village gate. Everything walkable.",(75,"bus")),
     ("shiroyama","10am","The postcard view of 250-year-old gassho farmhouses.",(15,"walk")),
     ("wada","11am","Go inside. Hida beef for lunch nearby, then wander the lanes.",(10,"walk")),
     ("shirakawabt","12:50pm","1pm bus back.",(5,"walk")),
     ("kanazawasta","2:15pm","Grab the bag. Taxi to the ryokan (the inn can also send a shuttle: ask when booking).",(75,"bus")),
     ("ishiya","3pm","Check in. Yukata, the big outdoor bath, then a multi-course crab kaiseki in the room. Early night.",(25,"taxi")),
   ]),
  ]),
 dict(id="kyoto", n=3, name="Kyoto", kanji="京都", dates="Dec 4 – 9", nights="5 nights", hotel="resol",
  hotel_note="Central, public bath, Nishiki Market 2 min, Teramachi arcades 1 min, Pontocho out the back. Gion is a 10-min walk. Bags forwarded from Tokyo are waiting here.",
  days=[
   dict(date="Fri Dec 4", title="Into Kyoto, the market street, a samurai sword lesson", stops=[
     ("kanazawasta","9:45am","Ryokan taxi/shuttle to the station. 10:15 Thunderbird express along Lake Biwa.",(25,"taxi")),
     ("kyotosta","12:30pm","",(135,"train")),
     ("resol","1pm","Bags already here.",(10,"subway")),
     ("nishiki","2pm","Kyoto's kitchen: five blocks of pickles, tofu doughnuts, knives. Graze for lunch.",(5,"walk")),
     ("teramachi","3:30pm","Two covered arcades off the market: vintage, kimono, tea, sneakers. The 2nd-oldest arcade in Japan.",(3,"walk")),
     ("kuoe","4:45pm","Build-your-own watch at the Kyoto flagship (closed Tue). 2 min from the hotel.",(5,"walk")),
     ("resol","5:30pm","Change.",(2,"walk")),
     ("kembu","6:30pm","90 min: hakama on, learn to draw and cut, then the performance.",(10,"walk")),
     ("pontocho","8:30pm","Late dinner in the lantern-lit alley along the river.",(10,"walk")),
     ("resol","10pm","",(5,"walk")),
   ]),
   dict(date="Sat Dec 5", title="The open-air train through the gorge, bamboo, Arashiyama town", stops=[
     ("torokko","12:15pm","Sagano Romantic Train one way through the Hozu gorge in peak fall color. Seats open exactly 1 month out (Nov 5): Car No. 5 (open-air), right side. JR back from Umahori.",(35,"train")),
     ("bamboo","1:45pm","60-ft stalks creaking in the wind. 20 min, then the shop street and the river bridge.",(5,"walk")),
     ("tenryuji","2:15pm","Zen garden, 30 min. Skip the inner buildings.",(5,"walk")),
     ("okochi","3pm","A silent-film star's mountain garden, tea included. 45 min, best view in Arashiyama.",(8,"walk")),
     ("takashimaya","5:30pm","Shijo department-store row: Takashimaya, Daimaru, Fujii Daimaru. Depachika dinner and tax-free on 7F.",(35,"train")),
     ("bark6","8:30pm","Japanese whisky nightcap.",(12,"walk")),
     ("resol","9:30pm","",(10,"walk")),
   ]),
   dict(date="Sun Dec 6", title="Bowing deer, the giant Buddha, sake street, the mountain of gates at dusk", stops=[
     ("todaiji","10am","45 min to Nara + a walk through the deer park. Buy deer crackers.",(60,"train")),
     ("kasuga","noon","Lantern-lined cedar path, 30 min. Lunch on Nara's shopping street (Higashimuki) on the way back.",(15,"walk")),
     ("fushimisake","2:30pm","Willow canal, one counter with 18 breweries.",(45,"train")),
     ("inari","4pm","10,000 gates. Keep going 30 min past where everyone stops. Open all night.",(15,"train")),
     ("resol","7pm","Dinner on Kiyamachi, the bar street behind the hotel.",(25,"train")),
   ]),
   dict(date="Mon Dec 7", title="Gion shopping day, a Kyoto workwear atelier, then the oldest three-star in Japan", stops=[
     ("taiga","11am","Taiga Takahashi: vintage-inspired workwear in a Gion machiya. Then the Hanamikoji / Shijo Gion shops.",(15,"walk")),
     ("giontea","12:30pm","Lunch in Gion, then the Yasaka backstreets: Ishibe-koji, Nene-no-michi.",(8,"walk")),
     ("ninenzaka","2pm","Stone lanes up the hill. Rent kimono for the walk if Mom's in (shops at the bottom of the hill).",(10,"walk")),
     ("kiyomizu","3:30pm","The temple on wooden stilts at golden hour. 45 min, the view is the point.",(10,"walk")),
     ("hyotei","6pm","Hyotei: three stars, 1837, kaiseki in a private garden room. Book through the hotel concierge the day you confirm the trip; it needs a Japanese phone line. Alt: Roan Kikunoi (2*), Gion Nishikawa (2*).",(20,"taxi")),
     ("resol","9pm","",(15,"taxi")),
   ]),
   dict(date="Tue Dec 8 · Mom turns 50", title="Three-star lunch, a private tea ceremony, Pontocho at dusk, a maiko dinner", stops=[
     ("nishiki","10am","Slow morning. Coffee, then a last pass through the market and Teramachi for anything missed.",(5,"walk")),
     ("kikunoi","12:30pm","Three-star lunch kaiseki at half the dinner price. Two Michelin meals in 24 hours: lunch is the lighter one.",(15,"taxi")),
     ("giontea","2:30pm","Private tea ceremony in a Gion teahouse.",(8,"walk")),
     ("pontocho","4:30pm","The lantern alley at blue hour, a glass of something on the river side.",(15,"walk")),
     ("hatanaka","6:30pm","The dinner. Private maiko evening, two hours, cake requested. Fill out Korea's e-Arrival Card tonight.",(15,"walk")),
     ("resol","9pm","",(15,"walk")),
   ]),
  ]),
 dict(id="osaka", n=4, name="Osaka", kanji="大阪", dates="Dec 9 – 11", nights="2 nights", hotel="crosshotel",
  hotel_note="One block from Dotonbori; Amerikamura and Shinsaibashi are a 5-min walk. Alt: Hotel Royal Classic (kabuki-theater building, on Namba Station). Big suitcases forwarded to the Dec 13 Tokyo hotel on the morning of the 11th.",
  days=[
   dict(date="Wed Dec 9", title="Osaka's kitchen, the knife street, Amerikamura, neon", stops=[
     ("kyotosta","9:30am","Shinkansen, 15 min. Bags come with you.",(10,"subway")),
     ("crosshotel","10:30am","Drop bags.",(25,"train")),
     ("kuromon","11am","Kuromon Market: grilled king crab legs, otoro, wagyu skewers, standing up.",(10,"walk")),
     ("doguyasuji","12:30pm","150 m of pro kitchen shops: knives, takoyaki pans, the plastic display food. Closes 6pm.",(5,"walk")),
     ("shinsaibashi","2pm","600 m covered arcade: Uniqlo, drugstores, the giant Don Quijote. Tax-free with passport.",(12,"walk")),
     ("bbgarage","3:30pm","Amerikamura: vintage Americana, and the watch counter at the back. Ask if it's been overhauled and if the dial/hands are original. Open till 8, closed Wed → this is Wednesday: swap to Thursday if they're closed (see Dec 10).",(8,"walk")),
     ("dotonbori","6pm","The canal, the Glico man, kushikatsu and takoyaki standing up.",(10,"walk")),
     ("crosshotel","9pm","",(3,"walk")),
   ]),
   dict(date="Thu Dec 10", title="Whisky at the source, Umeda's mall city, then retro Osaka under the tower", stops=[
     ("yamazaki","10am","Where Japanese whisky was born. Tour is a lottery 2 months out; tasting counter takes a reservation.",(35,"train")),
     ("grandfront","1pm","Umeda: Grand Front, Hankyu, the underground mall maze. Lunch on the top-floor restaurant terrace.",(30,"train")),
     ("bbgarage","4pm","B.B. Garage (open Thu). Vintage watches at the back. Skip if done Wednesday.",(20,"subway")),
     ("tsutenkaku","6pm","Shinsekai: the 1912 tower, kushikatsu counters, Showa-era signs. Go up for the night view. Early night: 7am airport train.",(15,"subway")),
     ("crosshotel","9pm","Repack: Seoul is carry-on only. Big bags to the desk for forwarding.",(15,"subway")),
   ]),
  ]),
 dict(id="seoul", n=5, name="Seoul", kanji="서울", dates="Dec 11 – 13", nights="2 nights", hotel="andaz",
  hotel_note="Gangnam, where every clinic is. Pool, sauna, hot tub on site for contrast bathing. Direct subway access from B2. Alt: Nine Tree Insadong (north side). Use Naver Map or KakaoMap here; Google Maps can't route in Korea.",
  days=[
   dict(date="Fri Dec 11", title="Land, IV drip, oxygen chamber, Garosu-gil, Korean beef", stops=[
     ("namba","6:50am","7am airport express (45 min).",(8,"walk")),
     ("kix","7:45am","Morning flight to Incheon, 2h.",(45,"train")),
     ("icn","11am","Through immigration by noon with the e-Arrival Card. AREX + subway to Gangnam.",(120,"flight")),
     ("andaz","1pm","Drop bags.",(75,"train")),
     ("hanaclinic","2pm","Doctor-led longevity consult + NAD+ or glutathione IV for the jet lag. ~90 min. English, WhatsApp bookings.",(10,"taxi")),
     ("o2on","4pm","60 min of medical-grade hyperbaric oxygen. Cheapest HBOT in Gangnam, no clinic markup.",(10,"taxi")),
     ("garosugil","5:30pm","Tree-lined boutique street, 10 min from the chamber. Olive Young for the K-beauty haul (tax-free with passport).",(10,"walk")),
     ("andaz","8pm","Hanwoo BBQ dinner in Sinsa or Apgujeong (ask the hotel). Then hot tub → cold plunge → sauna before bed.",(15,"taxi")),
   ]),
   dict(date="Sat Dec 12", title="The Gangnam glow: skin, color, scalp, then Seongsu", stops=[
     ("reberry","9:30am","AI skin profiling, then zero-downtime lifting: Thermage FLX / Ultherapy / Potenza, plus an LDM ultrasound for the glass-skin finish. ~3 hrs. Book 2–4 weeks ahead, English staff.",(15,"subway")),
     ("myshopper","1:30pm","16-type personal color analysis, 1 hr. Bring your makeup pouch. You get a palette PDF for the afternoon's shopping.",(15,"taxi")),
     ("parkjun","3pm","15-step scalp spa + neck/back massage in a private room, 90 min. Book ahead; it's an award-winning med-tourism spot.",(10,"taxi")),
     ("amore","5:30pm","Amore Seongsu: AI skin scan and a custom-formulated serum / lipstick. Then Seongsu-dong: warehouses turned cafés, pop-ups, the sneaker shops. Open till 8:30.",(30,"taxi")),
     ("andaz","9pm","Dinner in Seongsu (chimaek or a pocha), noraebang if there's gas left.",(30,"taxi")),
   ]),
   dict(date="Sun Dec 13", title="Sunrise city-wall hike, ginseng chicken, the palace in hanbok, fly to Tokyo", stops=[
     ("inwangsan","7:30am","Inwangsan: 1.5 hrs up the Seoul fortress wall to the summit at sunrise. Granite, stairs, the whole skyline. Trail shoes.",(35,"taxi")),
     ("tosokchon","10am","Tosokchon samgyetang: whole ginseng chicken soup, the recovery meal. Opens 10, be in line at 9:50.",(15,"walk")),
     ("gyeongbok","11am","Rent hanbok by the gate (free palace entry). The photo op of the trip. Non-negotiable. One hour, then out.",(10,"walk")),
     ("icn","12:30pm","Taxi/AREX to Incheon. Early-afternoon flight to Narita (not Haneda).",(70,"train")),
   ]),
  ]),
 dict(id="tokyo2", n=6, name="Tokyo, last night", kanji="東京", dates="Dec 13 – 14", nights="1 night", hotel="metropolitan",
  hotel_note="On top of Tokyo Station, where the Narita Express leaves from. Suitcases forwarded from Osaka are waiting at the desk.",
  days=[
   dict(date="Sun Dec 13", title="Fly back to Tokyo, the last sushi counter", stops=[
     ("narita","4:30pm","Land. Narita Express to Tokyo Station, 1 hour.",(150,"flight")),
     ("metropolitan","6pm","Suitcases waiting. Ginza is 10 min away if you're in by 6.",(65,"train")),
     ("sushiyuu","8pm","The second omakase, a tier up. English-speaking chef. Pack it all tonight.",(25,"subway")),
     ("metropolitan","10:30pm","",(25,"subway")),
   ]),
   dict(date="Mon Dec 14", title="A slow last morning, then home", stops=[
     ("tsukiji","8:30am","One last market breakfast.",(15,"subway")),
     ("eastgarden","10am","Five minutes from the hotel. Check out by noon.",(15,"subway")),
     ("metropolitan","11:45am","Bags at the front desk.",(8,"walk")),
     ("tokyosta","2:30pm","2:45 Narita Express.",(3,"walk")),
     ("narita","3:45pm","AC 6, 6:45pm → Montréal → Miami 11:11pm.",(60,"train")),
   ]),
  ]),
]

# intercity legs for the overview (from the itinerary)
LEGS = [
 ("gracery","intergate","Hokuriku Shinkansen (direct)","2h30","$95 pp"),
 ("intergate","resol","Ryokan taxi 25 min + Thunderbird express","2h45","$50 pp + ~$30 taxi"),
 ("resol","crosshotel","Shinkansen","15 min","$15 pp"),
 ("crosshotel","andaz","Flight KIX → ICN","2h","~$150–250 pp"),
 ("andaz","metropolitan","Flight ICN → NRT","2h30","~$150–250 pp"),
]

# ---------------- helpers ----------------
def hav(a, b):
    R = 6371.0
    la1, lo1, la2, lo2 = map(math.radians, (a["lat"], a["lng"], b["lat"], b["lng"]))
    d = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(d))

def estimate(a, b):
    """Rough door-to-door estimate when the itinerary doesn't state one."""
    d = hav(a, b)
    if d < 1.3:
        return (max(2, round(d*1.35/0.075)), "walk")
    if d < 15:
        return (int(5*round((10 + d*1.4/0.45)/5)), "subway")
    return (int(5*round((15 + d*1.3/0.75)/5)), "train")

MODE_LABEL = dict(walk="walk", train="train", subway="metro", bus="bus", taxi="taxi", flight="flight", ropeway="ropeway", hike="hike", shuttle="shuttle")
GMODE = dict(walk="walking", hike="walking", flight="transit")

def fmt(mins):
    if mins >= 60:
        h, m = divmod(mins, 60)
        return f"{h}h{m:02d}" if m else f"{h}h"
    return f"{mins} min"

def place_url(p):
    q = H.escape(p["name"]).replace(" ", "+")
    u = f"https://www.google.com/maps/search/?api=1&query={q}"
    if p["pid"]:
        u += f"&query_place_id={p['pid']}"
    return u

def dir_url(a, b, mode):
    gm = GMODE.get(mode, "transit")
    return (f"https://www.google.com/maps/dir/?api=1&origin={a['lat']:.6f},{a['lng']:.6f}"
            f"&destination={b['lat']:.6f},{b['lng']:.6f}&travelmode={gm}")

# resolve hops + from-hotel estimates
for c in CITIES:
    hotel = P[c["hotel"]]
    for day in c["days"]:
        first = P[day["stops"][0][0]]
        prev = hotel if (first["id"] != c["hotel"] and hav(hotel, first) < 60) else None
        out = []
        for i, (pid, t, note, hop) in enumerate(day["stops"]):
            p = P[pid]
            if hop is None and prev is not None:
                hop = estimate(prev, p)
            if prev is None:
                hop = None
            fh = None
            if pid != c["hotel"]:
                if prev is not None and prev["id"] == c["hotel"] and hop:
                    fh = hop  # itinerary already states hotel -> here
                else:
                    fh = estimate(hotel, p) if hav(hotel, p) < 60 else None
            out.append(dict(pin=pid, time=t, note=note,
                            hop=None if hop is None else dict(min=hop[0], mode=hop[1], url=dir_url(prev, p, hop[1])),
                            from_hotel=None if fh is None else dict(min=fh[0], mode=fh[1], url=dir_url(hotel, p, fh[1]))))
            prev = p
        day["stops"] = out

USED = {c["hotel"] for c in CITIES} | {s["pin"] for c in CITIES for d in c["days"] for s in d["stops"]} | {x for l in LEGS for x in l[:2]}

# ---------------- KML ----------------
def kml():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<kml xmlns="http://www.opengis.net/kml/2.2"><Document>',
           '<name>Japan for the 50th · Nov 27 – Dec 14, 2026</name>',
           '<description><![CDATA[Red = where you sleep. Blue = stops, numbered in order. Grey = stations and airports. Travel times are estimates from the itinerary (≈); tap the Directions link in any pin for the live time in Google Maps. In Korea use Naver Map or KakaoMap for walking/driving.]]></description>']
    styles = {
      "sleep": ("ff1b36c4", "https://maps.google.com/mapfiles/kml/paddle/red-stars.png"),
      "stop":  ("ffb55824", "https://maps.google.com/mapfiles/kml/paddle/blu-blank.png"),
      "transit": ("ff8a8a8a", "https://maps.google.com/mapfiles/kml/paddle/wht-blank.png"),
    }
    for k, (col, icon) in styles.items():
        out.append(f'<Style id="{k}"><IconStyle><color>{col}</color><scale>1.1</scale><Icon><href>{icon}</href></Icon></IconStyle>'
                   f'<LabelStyle><scale>0.9</scale></LabelStyle></Style>')
    out.append('<Style id="route"><LineStyle><color>b31b36c4</color><width>3</width></LineStyle></Style>')
    for c in CITIES:
        out.append(f'<Folder><name>{c["n"]:02d} {H.escape(c["name"])} · {H.escape(c["dates"])}</name><open>1</open>')
        hotel = P[c["hotel"]]
        desc = f"<b>Sleep · {c['nights']}</b><br/>{H.escape(c['hotel_note'])}<br/><a href='{place_url(hotel)}'>Open in Google Maps</a>"
        out.append(f'<Placemark><name>🏨 {H.escape(hotel["name"])}</name><styleUrl>#sleep</styleUrl>'
                   f'<description><![CDATA[{desc}]]></description>'
                   f'<Point><coordinates>{hotel["lng"]:.6f},{hotel["lat"]:.6f},0</coordinates></Point></Placemark>')
        seen = {c["hotel"]}
        n = 0
        for day in c["days"]:
            for s in day["stops"]:
                if s["pin"] in seen:
                    continue
                seen.add(s["pin"])
                p = P[s["pin"]]
                n += 1
                bits = [f"<b>{H.escape(day['date'])} · {H.escape(s['time'])}</b>"]
                if s["note"]:
                    bits.append(H.escape(s["note"]))
                if s["hop"]:
                    bits.append(f"≈ {fmt(s['hop']['min'])} by {MODE_LABEL[s['hop']['mode']]} from the previous stop · <a href='{s['hop']['url']}'>Directions</a>")
                if s["from_hotel"]:
                    bits.append(f"≈ {fmt(s['from_hotel']['min'])} by {MODE_LABEL[s['from_hotel']['mode']]} from {H.escape(hotel['short'])} · <a href='{s['from_hotel']['url']}'>Directions</a>")
                bits.append(f"<a href='{place_url(p)}'>Open in Google Maps</a>")
                sty = "transit" if p["type"] == "transit" else "stop"
                label = f"{n}. {p['name']}" if sty == "stop" else p["name"]
                out.append(f'<Placemark><name>{H.escape(label)}</name><styleUrl>#{sty}</styleUrl>'
                           f'<description><![CDATA[{"<br/>".join(bits)}]]></description>'
                           f'<Point><coordinates>{p["lng"]:.6f},{p["lat"]:.6f},0</coordinates></Point></Placemark>')
        out.append('</Folder>')
    # route
    coords = " ".join(f"{P[a]['lng']:.5f},{P[a]['lat']:.5f},0" for a, *_ in LEGS) + f" {P['metropolitan']['lng']:.5f},{P['metropolitan']['lat']:.5f},0"
    out.append('<Folder><name>Route between stops</name>')
    out.append(f'<Placemark><name>Tokyo → Kanazawa → Kyoto → Osaka → Seoul → Tokyo</name><styleUrl>#route</styleUrl>'
               f'<LineString><tessellate>1</tessellate><coordinates>{coords}</coordinates></LineString></Placemark>')
    out.append('</Folder></Document></kml>')
    return "\n".join(out)

with open("japan50.kml", "w", encoding="utf-8") as f:
    f.write(kml())

# ---------------- HTML data ----------------
data = dict(
    pins={k: dict(id=v["id"], name=v["name"], short=v["short"], lat=v["lat"], lng=v["lng"], type=v["type"], url=place_url(v)) for k, v in P.items() if k in USED},
    cities=[dict(id=c["id"], n=c["n"], name=c["name"], kanji=c["kanji"], dates=c["dates"], nights=c["nights"],
                 hotel=c["hotel"], hotel_note=c["hotel_note"], days=c["days"]) for c in CITIES],
    legs=[dict(a=a, b=b, how=how, dur=dur, cost=cost) for a, b, how, dur, cost in LEGS],
    modes=MODE_LABEL,
)
tpl = open("map_template.html", encoding="utf-8").read()
html = tpl.replace("/*__DATA__*/", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("pins", len(P), "kml bytes", len(kml()), "html bytes", len(html))
