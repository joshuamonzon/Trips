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

# ---- Oct 12 additions ----
# Tokyo
pin("shibuyasky","Shibuya Sky",35.6586719,139.7019848,"stop","ChIJ4Rr2JWiLGGARcyRSHuZ-9G8")
pin("hatoya","Hatoya Asakusa (matcha)",35.7145375,139.8014641,"stop","ChIJnXCWIE2NGGARgRGu9pKd8qM","Hatoya")
pin("micasadeco","Micasadeco & Cafe (pancakes)",35.6665545,139.7054272,"stop","ChIJDf7Vf6aMGGARzNimzxLN2ds","Micasadeco")
pin("watchnian","Watchnian Shibuya (pre-owned Rolex etc.)",35.659994,139.69884,"stop","ChIJSwFANKiMGGARf4vhiae-dkk","Watchnian")
pin("onodera","Kaiten Sushi Ginza Onodera Honten (Omotesando)",35.665805,139.7100254,"stop","ChIJyZOxItGNGGARWwp9_I4dZDA","Onodera kaiten")
pin("tnaka","T Nakameguro (Omi-beef T-bone)",35.6411925,139.6961587,"stop","ChIJv6eIxzeLGGAR3wUJpK4BB6w","T Nakameguro")
pin("azabudai","Azabudai Hills",35.6615447,139.7408302,"stop","ChIJJSI0QC6LGGARwWmKE3MWmj8")
pin("frontroom","The Front Room (Marunouchi Bldg)",35.6812689,139.7638917,"stop","ChIJRc0u95GLGGARCt-gXrexQ9Q","Front Room")
# Tokyo picks / bench
pin("imopippi","Imo Pippi (sweet-potato dessert)",35.7140814,139.7944112,"stop","ChIJ24IzFrqPGGAR3ptfNiVp9xo","Imo Pippi")
pin("iyoshi","Iyoshi Cola Asakusa Rokku",35.7124974,139.7925828,"stop","ChIJCdYEmyOPGGARIBZriyhh-Bo","Iyoshi Cola")
pin("andra","American Diner Andra (Ueno)",35.7136331,139.7813983,"stop","ChIJG4Z_vJmOGGARjUQ6EKP7nu0","Andra")
pin("mameya","Koffee Mameya",35.668368,139.710888,"stop","ChIJB1oleKOMGGAR_10GNeoySkY","Koffee Mameya")
pin("matchatokyo","The Matcha Tokyo Omotesando",35.666928,139.7063615,"stop","ChIJ17f1w_qNGGARfQzEoh19PyE","Matcha Tokyo")
pin("nozy","The Roastery by Nozy Coffee (Cat St)",35.6655724,139.7047658,"stop","ChIJCS0wmqaMGGAR2h4xKb_ah8c","Nozy Roastery")
pin("sedai","Sedai Coffee & Roasters",35.6642972,139.7030516,"stop","ChIJ1aRTMACNGGAR8W16w3Uzd00","Sedai")
pin("menchirashi","Menchirashi (carbonara udon)",35.6664994,139.7050912,"stop","ChIJ651p-W-NGGARi41d0DEi2l8","Menchirashi")
pin("harry","Harry Harajuku Terrace (otter cafe)",35.6691908,139.7080074,"stop","ChIJA0y7o6OMGGAROgRqIXDRAss","Otter cafe")
pin("megadonki","Mega Don Quijote Shibuya",35.6603873,139.6978172,"stop","ChIJr4J6pKmMGGARdQLOgrzToH4","Mega Donki")
pin("jbs","JB's Tokyo (burgers, Yoyogi)",35.6827992,139.7021823,"stop","ChIJI42jra-NGGARz8-Vdy1WPx4","JB's")
pin("littlenap","Little Nap Coffee Stand (Yoyogi Park)",35.6720937,139.6905932,"stop","ChIJUyaS0ErzGGAR6_mFuqndQ9o","Little Nap")
pin("mitaba","Ramen Mitaba (Kabukicho, till 5:45am)",35.694468,139.7039137,"stop","ChIJ466CzkaNGGARpwPGpF4dx9w","Mitaba")
pin("bongen","Bongen Coffee Ginza",35.6710713,139.7708038,"stop","ChIJP2BtW-CLGGAR_-5-Dk9pFoE","Bongen")
pin("glitch","Glitch Coffee Ginza",35.6689171,139.7686324,"stop","ChIJE0xjRfqLGGARkLg8IUjcu2o","Glitch")
pin("hachigou","Ginza Hachigou (6-seat ramen, Bib Gourmand)",35.6705477,139.77015,"stop","ChIJX05jZOaLGGAR2rUy9EXaYLk","Hachigou")
pin("iroriya","Iroriya Higashiginza (irori izakaya)",35.6705,139.768348,"stop","ChIJSeu70OCLGGARoLGr-u6oV_k","Iroriya")
pin("butter","BUTTER Biei pancakes (Marunouchi Bldg B1)",35.6807194,139.7636391,"stop","ChIJ0TUQMf-LGGARGckAvNCVZZ8","BUTTER")
pin("shima","Shima (Nihonbashi steak)",35.6790472,139.7728957,"stop","ChIJNb3eqeKLGGARYo0br3E36Q4","Shima")
pin("mimasu","Mimasu (1910 family sushi, Yotsuya)",35.6878112,139.7149935,"stop","ChIJ9YBS2-uMGGARht93gmUhZxY","Mimasu")
pin("wagyumafia","Wagyumafia The Cutlet Sandwich (Nakameguro)",35.6440853,139.7004345,"stop","ChIJefdmkkiLGGAR0RhNwDVxI5g","Wagyumafia")
pin("iiii","II II II Coffee (Akasaka, weekdays)",35.6677939,139.7393941,"stop","ChIJVbJCxmeLGGARVoHoBbTmUDQ","II II II")
pin("common","Common (Roppongi cafe)",35.6641123,139.7333372,"stop","ChIJ1drE4CyLGGAR9-g-0v5WNCI","Common")
pin("tokyotower","Tokyo Tower",35.6585805,139.7454329,"stop","ChIJCewJkL2LGGAR3Qmk0vCTGkg")
pin("yaguchi","Yaguchi Book Store (Jimbocho)",35.6957527,139.7570227,"stop","ChIJ1T0T-hOMGGAROQIyW12-Mgs","Yaguchi Books")
pin("onibus","Onibus Coffee Yakumo",35.625949,139.6710691,"stop","ChIJCaW9Ty31GGARd3cEq5taDM0","Onibus")
pin("coconemaru","Yakiniku Coco Nemaru Ginza",35.6717064,139.7612311,"stop",None,"Coco Nemaru")
pin("sgclub","The SG Club (Shibuya)",35.6642434,139.6992314,"stop",None,"SG Club")
pin("sushipunch","Sushi Punch (Azabujuban)",35.6536546,139.7357535,"stop",None,"Sushi Punch")
pin("yoroniku","Yoroniku Ebisu",35.6463571,139.7118057,"stop",None,"Yoroniku")
pin("goodwood","Good Wood Terrace (jerk chicken)",35.6578,139.6935,"stop",None,"Good Wood")
# Kanazawa
pin("ikiiki","Iki-iki Tei (Omicho kaisendon counter)",36.5718691,136.6563848,"stop","ChIJh9CWN3Az-F8RNVCyCT8xvxA","Iki-iki Tei")
pin("turban","Turban Curry (Kanazawa curry)",36.5618895,136.6551811,"stop","ChIJw2HKQYAz-F8RxAPmgKWGxxI","Turban Curry")
pin("amano","Amano Tea Shop (Higashi Chaya)",36.573196,136.665815,"stop","ChIJD_dkRHMz-F8RNv6ifBwLKEY","Amano tea")
pin("hakuichi","Hakuichi (gold-leaf ice cream)",36.5723142,136.6664755,"stop","ChIJ12QUl3Qz-F8Rf8aIc9cRDwc","Hakuichi")
pin("gyohan","Gyohan (jibu-ni duck stew, Korinbo)",36.5640981,136.652682,"stop","ChIJe96vq38z-F8RebGpcmVcbYQ","Gyohan")
pin("kanacastle","Kanazawa Castle Park",36.5659458,136.6588451,"stop","ChIJlUfxPYIz-F8RSh7ml54YJ6g","Castle Park")
# Kyoto
pin("marufukuro","Marufukuro (Tadao Ando, ex-Nintendo HQ)",34.991777,135.7662705,"sleep","ChIJaaNt6YIJAWARL2yVsTV42nw","Marufukuro")
pin("arabica","% Arabica Arashiyama",35.0135422,135.6764367,"stop","ChIJCWDv__-pAWARwLeeqs_cVew","% Arabica")
pin("ebisuya","Ebisuya rickshaw (Arashiyama)",35.013606,135.6773004,"stop","ChIJuRmAHACqAWAR9uSfNe-g90s","Rickshaw")
pin("otsuka","Steak Otsuka (Arashiyama)",35.020412,135.6804664,"stop","ChIJeVvryfipAWARmfvGZx3CApw","Steak Otsuka")
pin("wakakusa","Mt. Wakakusa (Nara)",34.6911496,135.8544345,"stop","ChIJLwbhyrs5AWARXrfL75d3_j8","Wakakusa")
pin("taisushi","Tai Sushi (Kyoto)",35.0042636,135.7698039,"stop","ChIJyxIaFZUIAWARMBcBFbbFKCg","Tai Sushi")
pin("hikiniku","Hikiniku to Come (Gion)",35.0050975,135.7745747,"stop","ChIJY28nVm4JAWARwfSwGp7gxk0","Hikiniku to Come")
pin("katsugyu","Gyukatsu Katsugyu Sanjo-Kawaramachi",35.0086539,135.7686303,"stop","ChIJU5Oa7OMJAWARwF_Lbib3xrs","Katsugyu")
pin("komori","Gion Komori (warabi mochi)",35.0058422,135.7746072,"stop","ChIJDSr9RuoIAWARsw05VvoRb5w","Gion Komori")
pin("yasakapagoda","Yasaka Pagoda (Hokan-ji)",34.9985591,135.7791783,"stop","ChIJIcT4YMUIAWARSTUi4EEky7E","Yasaka Pagoda")
pin("mouriya","Mouriya Gion (Kobe beef)",35.0033503,135.7727499,"stop","ChIJ1U7cN8AIAWARhsp2Q0XDoFk","Mouriya")
pin("itoh","Itoh Dining by Nobu (Gion)",35.0051389,135.77416,"stop","ChIJxbCtcOoIAWARfuiDAOw-zJk","Itoh Dining")
pin("enraku","Yasaka-dori Enraku (private ozashiki, dropped: no geisha)",34.9989147,135.7756299,"stop","ChIJgfk1fsYIAWAR9JXG1Z1X6uA","Enraku")
# Osaka
pin("kokuryu","Kokuryu Osaka (Kobe-beef kaiseki, Namba 7F)",34.6673743,135.5014321,"stop","ChIJjc46RgDnAGARBnJalgG25Hk","Kokuryu")
pin("wanaka","Takoyaki Wanaka Dotonbori",34.6687742,135.5027298,"stop","ChIJza-i6hHnAGAR07AQeEhDkh0","Wanaka")
pin("chibo","Chibo Dotonbori (okonomiyaki)",34.6688552,135.5038377,"stop","ChIJk9v34BTnAGAR8SL3pWF-3Js","Chibo")
pin("nambayasaka","Namba Yasaka Shrine (lion head)",34.6615592,135.4967039,"stop","ChIJQVW9eXLnAGARn-pUdRl0w4A","Namba Yasaka")
pin("rikuro","Rikuro's Namba (jiggly cheesecake)",34.666127,135.501566,"stop","ChIJK2A0qGznAGARxPHcddHFYYA","Rikuro's")
pin("hozenji","Hozenji Yokocho",34.6681187,135.5026104,"stop","ChIJY4ZQxRTnAGAR0mjfWQwO7ho","Hozenji")
pin("bearpaw","Bear Paw Cafe (Uehonmachi)",34.6665779,135.5186423,"stop","ChIJiWw4hHvnAGARtMh6YnrFVOQ","Bear Paw")
pin("fsspa","The Spa at Four Seasons Osaka",34.696121,135.4935933,"stop","ChIJVQHAl5vnAGAR0P0kuLzg1Mo","Four Seasons spa")
pin("usj","Universal Studios Japan",34.6656768,135.4323185,"stop","ChIJXeLVg9DgAGARqlIyMCX-BTY","USJ")
pin("katsuoji","Katsuo-ji (daruma temple, Minoh)",34.8657752,135.491087,"stop","ChIJtX8053n5AGARND16wXHGXg0","Katsuo-ji")
pin("minoh","Minoh Falls",34.8538281,135.4719911,"stop","ChIJE8YKbYz5AGARoCiDnK6410w","Minoh Falls")
pin("mrhiro","Mr. Hiro Car Studio (JDM garage + cafe)",34.6566761,135.4718702,"stop","ChIJI5z19PTnAGARqCxr7S7_H0g","Mr. Hiro")
# Seoul
pin("lucid","Lucid Dental Clinic (Gangnam)",37.507916,127.0340879,"stop","ChIJv_yR47WjfDURuElu__ohgTM","Lucid Dental")
pin("snuh","SNUH Healthcare System Gangnam Center (38–40F)",37.5000225,127.0364688,"stop","ChIJu9HgOf6jfDUR0J5KS_pgG_E","SNUH Gangnam")

# ---------------- itinerary ----------------
# stop = (pin_id, time, note, hop) ; hop = (minutes, mode) travel FROM the previous stop, or None -> estimate
# mode: walk, train, subway, bus, taxi, flight, ropeway, hike, shuttle
# picks = (pin_id, blurb): "while you're here" options, no schedule
CITIES = [
 dict(id="tokyo", n=1, name="Tokyo", kanji="東京", dates="Nov 28 – Dec 2", nights="4 nights", hotel="gracery",
  hotel_note="Godzilla on the roof. Narita Express stops at Shinjuku. Alt: Shibuya Stream Excel.",
  days=[
   dict(date="Sat Nov 28", title="Land, breathe, ramen, sleep", stops=[
     ("narita","4:30pm","Land. Immigration by 5:30. Buy N'EX tickets at the counter after customs.",None),
     ("gracery","7:15pm","Check in. Hotel by 7:15.",(80,"train")),
     ("shibuya","evening","Stand in the middle of it. (You go above it tomorrow at sunset.)",(15,"train")),
     ("gracery","10pm","Ramen on the way. Bed by 10.",(15,"train")),
   ], picks=[
     ("omoide","Yakitori under the train tracks, 5 min from the hotel. If you want more than ramen."),
     ("mitaba","Ramen 5 min from the hotel, open till 5:45am. The jet-lag bowl."),
   ]),
   dict(date="Sun Nov 29", title="Old Tokyo at dawn, matcha, pancakes, Dad's watch, Mom's frames (order today), denim, the city from the roof at sunset", stops=[
     ("sensoji","6:30am","Tokyo's oldest temple at dawn, 30 min, then Nakamise street. By 10am it's a mob.",(35,"subway")),
     ("hatoya","9am","Matcha whisked in front of you. Opens 9; be there at 8:50 or the line is 30 min.",(8,"walk")),
     ("micasadeco","9:45am","Ricotta pancakes. Opens 10 on Sunday; the line forms 30 min early. Harajuku.",(40,"subway")),
     ("watchnian","11:30am","Pre-owned Rolex / Omega / Cartier with service records, tax-free, English staff. Dad's browse. 5.0 across 1,600 reviews.",(15,"walk")),
     ("onodera","12:30pm","Lunch: the high-end conveyor-belt sushi. Chutoro and uni. No reservations; 20–40 min line.",(15,"walk")),
     ("solakzade","2pm","Opens at 2. Mom's frames: vintage stock from the 1800s–1980s, bespoke if she wants, fitted like a tailor. ORDER TODAY: lenses/custom work take about a week. Ship to the Dec 13 hotel (Metropolitan Marunouchi) if not ready. Closed Wed.",(10,"walk")),
     ("momotaro","3pm","Selvedge denim. Free hemming, ~1 hr. Pick up after Shibuya Sky (open till 8) or have them send to the hotel.",(12,"walk")),
     ("mixthinks","3:30pm","Vintage designer bags. Ask the condition grade (N/S/A/AB). Passports for tax-free.",(10,"walk")),
     ("shibuyasky","4pm","The open-air roof over the crossing. Sunset is 4:28; book the 4pm slot the day tickets open (sunset sells out first). Fuji on a clear day.",(12,"walk")),
     ("zauo","6:15pm","Fish your own dinner from the boat; they cook it how you want. Reserve. Done by 8.",(8,"walk")),
     ("gracery","8:30pm","Day two of jet lag is the hard one. Bed.",(15,"train")),
   ], picks=[
     ("imopippi","Asakusa: crème-brûlée sweet potato, cash only, 11am open (so only if you're still in Asakusa)."),
     ("iyoshi","Asakusa: craft cola made in front of you. Opens 12:30, so a Nov 30 Kappabashi add-on instead."),
     ("mameya","Omotesando: the best coffee shop in Tokyo, no sign, beans from 20 roasters. 10–6."),
     ("nozy","Cat Street: roastery + espresso martinis. On the walk between Micasadeco and Watchnian."),
     ("sedai","Harajuku: tiny roaster, 4.8, cheap. Two min from Micasadeco."),
     ("matchatokyo","Omotesando: matcha latte with a window over the street. 11–6:50."),
     ("menchirashi","Harajuku: the carbonara udon. 30-min line, next door to Micasadeco. Only if you skip Onodera."),
     ("harry","Harajuku: the otter café. Reserve. Novelty, skip unless Mom wants the otters."),
     ("megadonki","Shibuya: 7 floors of Don Quijote, 24 hrs, tax-free on 7F. Souvenir run any night."),
     ("sgclub","Shibuya: one of the world's top-50 cocktail bars, opens 6. Not on a jet-lag night."),
   ]),
   dict(date="Mon Nov 30", title="A chef walks you through the fish market, the knife street, pillows made to your neck, teamLab, vintage town, then the T-bone", stops=[
     ("tsukiji","10am","Tsukiji food tour with Ali (ex-Milos seafood chef), 10–noon. Meet at the Shinran Shonin statue. Food not included: bring cash. airbnb.com/experiences/6919404. Not booked yet: book it.",(25,"subway")),
     ("kappabashi","12:30pm","Knives engraved with your name. Buy now, forward home in the suitcase.",(20,"subway")),
     ("nishikawa","1:30pm","Custom-fit pillow at Nishikawa, Matsuya 7F. Walk-in OK: ~30 min fitting, ~40 min to make, so shop Ginza while it's built.",(25,"subway")),
     ("ginza","2:15pm","12-floor Uniqlo, Itoya, depachika food halls. Pick up the pillows on the way out. Passports out for tax-free.",(5,"walk")),
     ("teamlab","3:30pm","Timed slot. Barefoot, knee-deep in projected koi. Book 3 weeks out.",(15,"subway")),
     ("shimokita","5:30pm","Shimokitazawa: a whole neighborhood of vintage shops, record stores and cafés. Two hours on foot, no plan.",(50,"train")),
     ("tnaka","8pm","The Tokyo steak: Omi-beef T-bone grilled over an open flame, 4.8 across 500 reviews, one of the top steak rooms in the world. ¥20–30k pp, reservation only (phone 2–5pm JST, or through the hotel). 15 min from Shimokita.",(15,"train")),
     ("goldengai","10:45pm","Six alleys, 200 six-seat bars, 10 min from the hotel. Start the whisky at Bar Zoetrope. Only if there's gas left.",(25,"train")),
     ("gracery","late","Walk home.",(8,"walk")),
   ], picks=[
     ("iyoshi","Asakusa: craft cola, 12:30–6:30, a 5-min detour from Kappabashi."),
     ("andra","Ueno: the viral cheeseburger dunked in a skillet of cheese. 11:30–2 lunch, 10 min from Kappabashi. Only if you skipped the market snacks."),
     ("bongen","Ginza: Japanese-style espresso bar, 30-min line, 10–5."),
     ("glitch","Ginza: single-origin, 9–6. Coffee nerds' pick; Bongen for the vibe."),
     ("hachigou","Ginza: 6-seat Bib Gourmand ramen with truffle ravioli, reservation only, closed Mon (so not today)."),
     ("iroriya","Higashi-Ginza: basement irori izakaya, ikura bowl, drums when the caviar comes. Dinner alt if T doesn't come through."),
     ("zuicho","Shibuya: katsudon, 8 seats, one dish. Closed Sun; a lunch alt any other day."),
     ("shima","Nihonbashi: the other legendary steak (Kobe sirloin, the ¥9,600 takeaway sando). Closed Sun, ~¥30k pp. Backup for T; book via byFood."),
     ("wagyumafia","Nakameguro: the wagyu katsu sando. Same street as T; lunch, not dinner."),
     ("zoetrope","Shinjuku: 300 Japanese whiskies, 5 min from the hotel."),
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
   ], picks=[
     ("jbs","Yoyogi: the best cheap cheeseburger in Tokyo, 11 seats, 5 min from Shinjuku Station. If you get back early and hungry."),
     ("littlenap","Yoyogi Park: cortado by the train tracks. Morning-of coffee if you're up early."),
   ]),
  ]),
 dict(id="kanazawa", n=2, name="Kanazawa", kanji="金沢", dates="Dec 2 – 4", nights="2 nights", hotel="ishiya",
  hotel_note="Both nights at Motoyu Ishiya, a 200-year-old onsen ryokan in Fukatani, 25 min by taxi from the station (the inn also runs a shuttle: ask). Night 1 with the crab kaiseki in the room; night 2 room + breakfast only, dinner in town. Big bags forwarded Tokyo → Kyoto.",
  days=[
   dict(date="Wed Dec 2", title="Fish-market lunch, the garden, geisha lanes, gold leaf, samurai streets, out to the hot spring", stops=[
     ("tokyosta","7:45am","Hokuriku Shinkansen direct, 8am. Left side for the mountains.",(25,"train")),
     ("kanazawasta","10:30am","In by 10:30. Overnight bag into a station locker.",(150,"train")),
     ("ikiiki","11am","Omicho Market: the kaisendon counter (write your name on the sheet at the door). Peak snow crab, nodoguro, uni, sweet shrimp. Cash. Closes 1:30.",(15,"bus")),
     ("kenrokuen","12:30pm","Kenroku-en, one of Japan's three great gardens. Back in (your new notes call it a must). One hour: the winter yukitsuri rope cones are up on the pines, the pond, the oldest fountain in Japan. Then out.",(15,"walk")),
     ("higashi","2:15pm","1820s teahouse district. Gold-leaf ice cream at Hakuichi, matcha at Amano's back room, gild a pair of chopsticks. Two hours of lanes and shops.",(20,"bus")),
     ("nagamachi","4:15pm","Earthen walls, narrow lanes.",(20,"bus")),
     ("nomura","4:30pm","Real samurai residence: armor, tea room, tiny garden. 45 min, last entry 5.",(3,"walk")),
     ("kanazawasta","5:30pm","Grab the bag. Taxi out to the ryokan (or the inn's shuttle).",(20,"bus")),
     ("ishiya","6pm","Check in. Yukata, the big outdoor bath, then the crab kaiseki in the room.",(25,"taxi")),
   ], picks=[
     ("hakuichi","Higashi Chaya: the gold-leaf soft serve, ¥900. Do it once."),
     ("amano","Higashi Chaya: tea shop with a tatami room in back; matcha set with a sweet, ~¥1,300."),
     ("kanacastle","Next to Kenroku-en: the rebuilt white castle, free grounds, 20 min if you want it. (teamLab's castle show was a 2023 one-off; nothing scheduled for Dec 2026.)"),
     ("turban","Hirosaka: Kanazawa's thick black curry with a katsu, ¥1,200, 5 min from Kenroku-en. Lunch alt if the market line is long."),
   ]),
   dict(date="Thu Dec 3", title="The thatched village in the snow, sake, duck stew and the buttery fish, back to the bath", stops=[
     ("kanazawasta","7:45am","7:15 taxi from the inn. 8:10 direct bus to Shirakawa-go.",(25,"taxi")),
     ("shirakawabt","9:25am","Bus drops you at the village gate. Everything walkable.",(75,"bus")),
     ("shiroyama","10am","The postcard view of 250-year-old gassho farmhouses.",(15,"walk")),
     ("wada","11am","Go inside. Hida beef for lunch nearby, then wander the lanes.",(10,"walk")),
     ("shirakawabt","12:50pm","1pm bus back.",(5,"walk")),
     ("kanazawasta","2:15pm","",(75,"bus")),
     ("fukumitsuya","3pm","Sake flight at the 400-year-old brewery.",(15,"bus")),
     ("gyohan","5:30pm","Gyohan, hidden up an alley in Korinbo: jibu-ni (Kanazawa's duck stew, Edo-era recipe) and nodoguro grilled with salt; the ¥5,000 local kaiseki set does both. Walk in at 5. Closed Wed; today's Thursday.",(15,"bus")),
     ("ishiya","8pm","Taxi back. One more soak, early night.",(30,"taxi")),
   ]),
  ]),
 dict(id="kyoto", n=3, name="Kyoto", kanji="京都", dates="Dec 4 – 9", nights="5 nights", hotel="resol",
  hotel_note="Central, public bath, Nishiki Market 2 min, Teramachi arcades 1 min, Pontocho out the back. Gion is a 10-min walk. Bags forwarded from Tokyo are waiting here. OPTION for the birthday: move Dec 7–9 to Marufukuro, Tadao Ando's hotel inside Nintendo's original 1889 headquarters (7 min from Kyoto Station, 20 min from Gion; all-day lounge snacks and drinks, tempura counter; ~$500–700/night).",
  days=[
   dict(date="Fri Dec 4", title="Into Kyoto, the market street, the arcades, build a watch, a samurai sword lesson, sushi on the floor", stops=[
     ("kanazawasta","9:45am","Ryokan taxi/shuttle to the station. 10:15 Thunderbird express along Lake Biwa.",(25,"taxi")),
     ("kyotosta","12:30pm","",(135,"train")),
     ("resol","1pm","Bags already here.",(10,"subway")),
     ("nishiki","2pm","Kyoto's kitchen: five blocks of pickles, tofu doughnuts, knives. Graze for lunch.",(5,"walk")),
     ("teramachi","3:30pm","Two covered arcades off the market: vintage, kimono, tea, sneakers. The 2nd-oldest arcade in Japan.",(3,"walk")),
     ("kuoe","4:45pm","Build-your-own watch at the Kyoto flagship (closed Tue). 2 min from the hotel.",(5,"walk")),
     ("resol","5:30pm","Change.",(2,"walk")),
     ("kembu","6:30pm","90 min: hakama on, learn to draw and cut, then the performance.",(10,"walk")),
     ("taisushi","8:30pm","Tai Sushi: shoes off, a family counter, otoro and uni that locals send you to. 5 min from the hotel, 5–10pm, closed Thu/Sun. Reserve or walk in by 8.",(10,"walk")),
     ("resol","10pm","",(5,"walk")),
   ], picks=[
     ("katsugyu","Across the street from the hotel, B1: gyukatsu (rare beef cutlet you finish on a stone), 4.9 across 4,300 reviews, 10:30am–10:30pm. The any-day lunch."),
     ("hikiniku","Gion: hamburg steak course grilled over charcoal in front of you, refillable rice. Reserve; closed Wed. Lunch or dinner alt any day but Dec 9."),
     ("pontocho","Out the back door: the lantern lane along the river. Walk it tonight on the way home."),
   ]),
   dict(date="Sat Dec 5", title="Arashiyama early: the Kyoto latte, a rickshaw through the bamboo, the villa garden, Kyoto beef, then the open-air train through the gorge", stops=[
     ("arabica","9am","% Arabica on the river: the Kyoto latte, opens 9. Be in line at 8:45; by 10:30 it's 50 min. Drink it on the riverbank by the bridge.",(35,"train")),
     ("ebisuya","9:30am","Ebisuya rickshaw, 30 min for two (~¥10,000): they run a rickshaw-only path through the bamboo, no crowds in the photo, and the puller shoots your pictures. 4.9 across 1,700 reviews.",(2,"walk")),
     ("okochi","10:15am","A silent-film star's mountain garden, tea included. 45 min, best view in Arashiyama. Then the bamboo on foot if the rickshaw didn't cover it.",(8,"walk")),
     ("otsuka","11:30am","Steak Otsuka: the Murasawa sirloin ('phantom beef', 80 head a year) on a hot iron plate, with rice and ponzu. The best wagyu in Kyoto for the money. Opens 11, closed Sun; reserve on TableCheck or be in line at 10:45.",(12,"walk")),
     ("torokko","1pm","Sagano Romantic Train one way through the Hozu gorge. Seats open exactly 1 month out (Nov 5): Car No. 5 (open-air), right side. JR back from Umahori.",(10,"walk")),
     ("takashimaya","4pm","Shijo department-store row: Takashimaya, Daimaru, Fujii Daimaru. Depachika dinner and tax-free on 7F.",(40,"train")),
     ("bark6","8:30pm","Japanese whisky nightcap.",(12,"walk")),
     ("resol","9:30pm","",(10,"walk")),
   ], picks=[
     ("tenryuji","Arashiyama: the Zen garden, 30 min, if the rickshaw leaves you time before lunch."),
     ("bamboo","Arashiyama: the grove on foot, 20 min, if you want it without the rickshaw."),
   ]),
   dict(date="Sun Dec 6", title="Nara the right way round: lanterns first, up the grass mountain, down through the deer to the giant Buddha; sake street; the mountain of gates at dusk", stops=[
     ("kasuga","10:15am","45 min to Kintetsu Nara, then the bus up. Start at the top: the lantern-lined cedar path and the vermilion shrine, 30 min. Friendlier deer, no crowds yet.",(60,"train")),
     ("wakakusa","11:15am","Mt. Wakakusa: 25 min up a grass hill (¥150) to the view over all of Nara, deer on the slope. Your notes were right: walk DOWN through the park, not up.",(12,"walk")),
     ("todaiji","12:30pm","Down through the deer park to Todai-ji, the largest wooden building on earth, 50-ft bronze Buddha from 752. Buy the crackers here, where the deer are hungriest. Lunch on Higashimuki shopping street on the way to the train.",(20,"walk")),
     ("fushimisake","3pm","Willow canal, one counter with 18 breweries.",(45,"train")),
     ("inari","4:30pm","10,000 gates. Keep going 30 min past where everyone stops. Open all night.",(15,"train")),
     ("resol","7:30pm","Dinner on Kiyamachi, the bar street behind the hotel.",(25,"train")),
   ]),
   dict(date="Mon Dec 7", title="Gion shopping day, a Kyoto workwear atelier, a three-star lunch, the pagoda lane, the temple on stilts at golden hour, Kobe beef", stops=[
     ("taiga","11am","Taiga Takahashi: vintage-inspired workwear in a Gion machiya. Then the Hanamikoji / Shijo Gion shops.",(15,"walk")),
     ("kikunoi","12:30pm","Kikunoi Honten: three Michelin stars, 100-year-old family, the lunch kaiseki at half the dinner price, the room on a garden in red maple. 10 min from Taiga.",(10,"walk")),
     ("yasakapagoda","2:30pm","The postcard: the five-story pagoda rising over the stone lane. 10 min, the photo.",(8,"walk")),
     ("ninenzaka","2:45pm","Stone lanes up the hill. Rent kimono for the walk if Mom wants a practice run before tomorrow's shoot.",(3,"walk")),
     ("kiyomizu","3:45pm","The temple on wooden stilts at golden hour. 45 min, the view is the point.",(10,"walk")),
     ("mouriya","6:30pm","Mouriya Gion, a private room on the 2nd floor: certified Kobe beef (sirloin and fillet) cooked on the teppan in front of you, foie gras course. 4.8 across 1,700 reviews. ~$400 for two. Reserve the private room by name.",(20,"walk")),
     ("resol","9pm","",(12,"walk")),
   ], picks=[
     ("komori","Gion: warabi mochi on tatami, 11–6:30, cash. Closed Tue, so today, not tomorrow."),
     ("itoh","Gion: Nobu's Kyoto room, wagyu + black cod miso. Dinner backup if Mouriya's room is gone."),
   ]),
   dict(date="Tue Dec 8 · Mom turns 50", title="The birthday: kimono and a photographer in the empty lanes, a private tea ceremony, Pontocho at blue hour, then the oldest three-star in Japan", stops=[
     ("yasakapagoda","8:30am","Kimono dressed at 7:45 (book a shop that opens early for shoots), then a private photographer for 90 min: the pagoda lane, Ninenzaka, Gion, before anyone's there. ~$350. Both of you in kimono; Dad gets a haori.",(15,"taxi")),
     ("nishiki","12pm","Slow lunch: the market and Teramachi, or Katsugyu across from the hotel. Keep it light; tonight is the meal.",(15,"taxi")),
     ("giontea","2:30pm","Private tea ceremony in a Gion teahouse.",(12,"walk")),
     ("pontocho","4:30pm","The lantern alley at blue hour, a glass of something on the river side.",(15,"walk")),
     ("hyotei","6pm","THE DINNER. Hyotei: three Michelin stars, the same family since 1837, kaiseki served course by course in a private tatami room off a lantern-lit garden beside Nanzen-ji. The oldest three-star in Japan. Cake arranged. ~$800 for two. Book through the hotel concierge the day the hotel is confirmed (Japanese phone line); open daily. Backups: Roan Kikunoi (2*), Gion Nishikawa (2*), Sushi Matsumoto (Michelin omakase counter, ~$200–300 pp).",(15,"taxi")),
     ("resol","9:30pm","Or one more whisky at Bar K6. Fill out Korea's e-Arrival Card tonight.",(15,"taxi")),
   ]),
  ]),
 dict(id="osaka", n=4, name="Osaka", kanji="大阪", dates="Dec 9 – 11", nights="2 nights", hotel="crosshotel",
  hotel_note="One block from Dotonbori; Amerikamura and Shinsaibashi are a 5-min walk. Alt: Hotel Royal Classic (kabuki-theater building, on Namba Station). Big suitcases forwarded to the Dec 13 Tokyo hotel on the morning of the 11th.",
  days=[
   dict(date="Wed Dec 9", title="Osaka's kitchen, the knife street, Amerikamura, neon, Kobe beef, the lantern alley", stops=[
     ("kyotosta","9:30am","Shinkansen, 15 min. Bags come with you.",(10,"subway")),
     ("crosshotel","10:30am","Drop bags.",(25,"train")),
     ("kuromon","11am","Kuromon Market: grilled king crab legs, otoro, wagyu skewers, standing up.",(10,"walk")),
     ("doguyasuji","12:30pm","150 m of pro kitchen shops: knives, takoyaki pans, the plastic display food. Closes 6pm.",(5,"walk")),
     ("shinsaibashi","2pm","600 m covered arcade: Uniqlo, drugstores, the giant Don Quijote. Tax-free with passport.",(12,"walk")),
     ("bbgarage","3:30pm","Amerikamura: vintage Americana, and the watch counter at the back. Ask if it's been overhauled and if the dial/hands are original. Open till 8, closed Wed → this is Wednesday: swap to Thursday if they're closed (see Dec 10).",(8,"walk")),
     ("dotonbori","5:15pm","The canal and the Glico man at dusk. Wanaka takoyaki standing up (one tray, you're eating at 7).",(10,"walk")),
     ("kokuryu","7pm","Kokuryu, 7F above Namba: Kobe-beef kaiseki, or the 20-course omakase (bluefin, wagyu, tempura). 4.9 across 1,700 reviews. Reserve.",(8,"walk")),
     ("hozenji","9:30pm","Hozenji Yokocho: the 1-block stone alley behind Dotonbori, lanterns, the moss-covered Buddha you splash with water. 2 min from dinner.",(3,"walk")),
     ("crosshotel","10pm","",(3,"walk")),
   ], picks=[
     ("wanaka","Dotonbori: the takoyaki line locals stand in. Let them cool 5 min."),
     ("chibo","Dotonbori: the okonomiyaki institution, griddled at your counter. If you'd rather sit than stand before Kokuryu, skip the tray."),
     ("rikuro","Namba: the jiggly cheesecake, baked in front of you, ¥1,000. Grab one on the walk home; breakfast tomorrow."),
   ]),
   dict(date="Thu Dec 10", title="The lion-head shrine, whisky at the source, Umeda's mall city, then retro Osaka under the tower (and the slide)", stops=[
     ("nambayasaka","8:45am","Namba Yasaka: the shrine with a 40-ft lion head for a stage. 20 min, 10 from the hotel, empty this early.",(10,"walk")),
     ("yamazaki","10:30am","Where Japanese whisky was born. Tour is a lottery 2 months out; tasting counter takes a reservation.",(40,"train")),
     ("grandfront","1:30pm","Umeda: Grand Front, Hankyu, the underground mall maze. Lunch on the top-floor restaurant terrace.",(30,"train")),
     ("bbgarage","4pm","B.B. Garage (open Thu). Vintage watches at the back. Skip if done Wednesday.",(20,"subway")),
     ("tsutenkaku","6pm","Shinsekai: the 1912 tower, kushikatsu counters, Showa-era signs. Go up for the night view, then take the 60-m spiral slide down (¥1,000). Early night: 7am airport train.",(15,"subway")),
     ("crosshotel","9pm","Repack: Seoul is carry-on only. Big bags to the desk for forwarding.",(15,"subway")),
   ], picks=[
     ("bearpaw","Uehonmachi: a bear's paw hands you your parfait through a hole in the wall. Cute, slow, 15 min from the hotel."),
     ("fsspa","Dojima: the Four Seasons spa, 10 min from Umeda. A massage + ofuro soak instead of the second mall hour, if Mom wants it. Book ahead."),
     ("mrhiro","Taisho: a JDM dream garage with a café and simulators, 5.0 across 3,700 reviews. Dad's, if he's a car guy; 25 min from Namba."),
     ("usj","If you'd trade the whole Umeda/Yamazaki day: Super Nintendo World + Harry Potter. It's a full day and a 10,000-step crowd. Not worth it for two 50-year-olds who don't game; left here so you can overrule."),
     ("katsuoji","Minoh: the temple of 10,000 red daruma dolls, 1 hr out by train + bus; pair with Minoh Falls (40-min walk down). The better trade for the Umeda afternoon if you want nature over malls."),
   ]),
  ]),
 dict(id="seoul", n=5, name="Seoul", kanji="서울", dates="Dec 11 – 13", nights="2 nights", hotel="andaz",
  hotel_note="Gangnam, where every clinic is. Pool, sauna, hot tub on site for contrast bathing. Direct subway access from B2. Use Naver Map or KakaoMap here; Google Maps can't route in Korea.",
  days=[
   dict(date="Fri Dec 11", title="Land, Dad's veneers start, Mom's IV, the oxygen chamber, Garosu-gil, Korean beef", stops=[
     ("namba","6:50am","7am airport express (45 min).",(8,"walk")),
     ("kix","7:45am","Morning flight to Incheon, 2h.",(45,"train")),
     ("icn","11am","Through immigration by noon with the e-Arrival Card. AREX + subway to Gangnam.",(120,"flight")),
     ("andaz","1pm","Drop bags.",(75,"train")),
     ("lucid","2pm","DAD: Lucid Dental, 3–4F, 606 Nonhyeon-ro, 10 min from the hotel. Veneers ('Lucinate' laminates): consult, scan, prep and temporaries today (Fri till 6), final seat tomorrow. Send photos on WhatsApp now and confirm two visits is enough. Quoted ₩9.8M (~$7,000) for a full set; not in the budget.",(10,"taxi")),
     ("hanaclinic","2pm","MOM: Hana Clinic, Apgujeong: longevity consult + NAD+ or glutathione IV, 90 min. English, WhatsApp bookings.",(10,"taxi")),
     ("o2on","4pm","Hyperbaric oxygen, 60 min. Mom first; Dad joins if the dentist lets him out.",(10,"taxi")),
     ("garosugil","5:30pm","Tree-lined boutique street, 10 min from the chamber. Olive Young for the K-beauty haul (tax-free with passport).",(10,"walk")),
     ("andaz","8pm","Hanwoo BBQ dinner in Sinsa or Apgujeong (ask the hotel). Then hot tub → cold plunge → sauna before bed. Nothing to eat or drink after midnight: tomorrow starts fasting.",(15,"taxi")),
   ]),
   dict(date="Sat Dec 12", title="The full-body scan, then skin, veneers, scalp, custom skincare, Seongsu", stops=[
     ("snuh","7:30am","Both: Seoul National University Hospital's Gangnam Center, 38–40F of the Finance Center. The comprehensive checkup: bloods, cardiac CT, abdominal ultrasound, DEXA, sedated endoscopy, plus the brain MRI/MRA add-on. 3–4 hours, English results in a week. Saturday runs till noon. Book NOW (4–6 weeks lead). ~$900–1,500 pp. This is the 'high-tech stuff they've never seen'.",(10,"taxi")),
     ("reberry","1:30pm","MOM: Reberry: AI skin profiling, then botox (forehead/eyes, 20 min) and the LDM glow, or Thermage if she wants the lift. ~2 hrs. Book 2–4 weeks ahead.",(10,"taxi")),
     ("lucid","1:30pm","DAD: final fitting and bonding of the veneers (Sat till 4).",(5,"taxi")),
     ("parkjun","4:15pm","Both: 15-step scalp spa + neck/back massage in a private room, 90 min. The massage of the trip.",(15,"taxi")),
     ("amore","6:30pm","Amore Seongsu: AI skin scan and a custom-formulated serum / lipstick. Then Seongsu-dong: warehouses turned cafés, the sneaker shops. Open till 8:30.",(30,"taxi")),
     ("andaz","9:30pm","Dinner in Seongsu (chimaek or a pocha), noraebang if there's gas left.",(30,"taxi")),
   ], picks=[
     ("myshopper","Sinsa: the 16-type personal color analysis, 1 hr, ~$100. Squeeze in before Park Jun if Reberry runs short."),
     ("seongsu","Seongsu-dong: the Brooklyn of Seoul. Already on tonight's route."),
   ]),
   dict(date="Sun Dec 13", title="Sunrise city-wall hike, ginseng chicken, the palace in hanbok, fly to Tokyo", stops=[
     ("inwangsan","7:30am","Inwangsan: 1.5 hrs up the Seoul fortress wall to the summit at sunrise. Granite, stairs, the whole skyline. Trail shoes.",(35,"taxi")),
     ("tosokchon","10am","Tosokchon samgyetang: whole ginseng chicken soup, the recovery meal. Opens 10, be in line at 9:50.",(15,"walk")),
     ("gyeongbok","11am","Rent hanbok by the gate (free palace entry). The photo op of the trip. Non-negotiable. One hour, then out.",(10,"walk")),
     ("icn","12:30pm","Taxi/AREX to Incheon. Early-afternoon flight to Narita (not Haneda).",(70,"train")),
   ]),
  ]),
 dict(id="tokyo2", n=6, name="Tokyo, last night", kanji="東京", dates="Dec 13 – 14", nights="1 night", hotel="metropolitan",
  hotel_note="On top of Tokyo Station, where the Narita Express leaves from. Suitcases forwarded from Osaka are waiting at the desk; so are Mom's frames from Solakzade.",
  days=[
   dict(date="Sun Dec 13", title="Fly back to Tokyo, Tokyo Tower from the garden, the last sushi counter", stops=[
     ("narita","4:30pm","Land. Narita Express to Tokyo Station, 1 hour.",(150,"flight")),
     ("metropolitan","6pm","Suitcases waiting. Change, 20 min.",(65,"train")),
     ("azabudai","7pm","Azabudai Hills: the rooftop garden / 33F lounge with Tokyo Tower lit up right in front of you (one drink buys the seat). The last photo. 10 min to dinner.",(20,"taxi")),
     ("sushiyuu","8pm","The second omakase, a tier up. English-speaking chef. Pack it all tonight.",(10,"taxi")),
     ("metropolitan","10:30pm","",(25,"subway")),
   ], picks=[
     ("tokyotower","Shibakoen: walk under it after dinner, lit till 11. You don't need to go up."),
     ("coconemaru","Ginza: wagyu yakiniku in private rooms, 1 min from Ginza Stn. The swap if two sushi counters is one too many."),
     ("yoroniku","Ebisu: the wagyu yakiniku omakase. Book a month out. Other swap."),
     ("shima","Nihonbashi: closed Sundays, so not tonight."),
     ("mimasu","Yotsuya: 1910 family sushi, ¥4,500 omakase. Closed Sundays; a cheap lunch any other day."),
     ("sushipunch","Azabujuban: omakase 7F, closed Sun. Backup for Sushi Yuu on a different night."),
   ]),
   dict(date="Mon Dec 14", title="French toast, the palace garden, then home", stops=[
     ("frontroom","8:30am","The Front Room, Marunouchi Building 1F, 3 min from the hotel: the 'drinkable' French toast on a hot skillet. Opens 8.",(3,"walk")),
     ("eastgarden","9:45am","Five minutes from the hotel. Check out by noon.",(10,"walk")),
     ("metropolitan","11:45am","Bags at the front desk.",(10,"walk")),
     ("tokyosta","2:30pm","2:45 Narita Express.",(3,"walk")),
     ("narita","3:45pm","AC 6, 6:45pm → Montréal → Miami 11:11pm.",(60,"train")),
   ], picks=[
     ("butter","Same building, B1: the Biei butter pancakes with a 100 g block of butter churned in the window. The other breakfast."),
     ("tsukiji","One last market breakfast instead, 15 min away, if you'd rather eat standing up."),
     ("yaguchi","Jimbocho: the 3-generation film-and-art bookstore, 10:30 open, 10 min from the hotel. If there's an hour."),
   ]),
  ]),
]

# bench: saved, not slotted, not tied to a day
BENCH = [
 ("Tokyo", [
  ("goodwood","Caribbean jerk chicken in Shibuya (viral after Kanye). Novelty pick."),
  ("iiii","Akasaka: 1-person espresso stand, weekdays 7:30–3:30. Coffee pilgrimage only."),
  ("common","Roppongi: big bright all-day café, matcha latte, breakfast plates."),
  ("onibus","Yakumo: the roaster's flagship, banana bread with espresso butter. Out of the way."),
 ]),
 ("Kyoto", [
  ("marufukuro","Birthday-nights hotel option, Dec 7–9. Tadao Ando inside Nintendo's 1889 HQ. ~$500–700/night."),
 ]),
]
BENCH = [(c,[x for x in items if len(x)==2 and x[0] in P]) for c,items in BENCH]

# intercity legs for the overview (from the itinerary)
LEGS = [
 ("gracery","ishiya","Hokuriku Shinkansen (direct) + taxi","3h","$95 pp + ~$30 taxi"),
 ("ishiya","resol","Ryokan taxi 25 min + Thunderbird express","2h45","$50 pp + ~$30 taxi"),
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

USED = {c["hotel"] for c in CITIES} | {s["pin"] for c in CITIES for d in c["days"] for s in d["stops"]} | {x for l in LEGS for x in l[:2]} | {p for c in CITIES for d in c["days"] for p,_ in d.get("picks",[])} | {p for _,items in BENCH for p,_ in items}

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

# ---------------- "While you're here" + bench layer ----------------
def ideas_kml():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<kml xmlns="http://www.opengis.net/kml/2.2"><Document>',
           '<name>Japan 50 · While you\'re here (picks by day) + bench</name>',
           '<description><![CDATA[Yellow stars: nothing scheduled, just the good options near where you already are that day. Import as a second layer on the same My Map and turn it on when you have a gap.]]></description>',
           '<Style id="pick"><IconStyle><color>ff00d7ff</color><scale>1.0</scale><Icon><href>https://maps.google.com/mapfiles/kml/paddle/ylw-stars.png</href></Icon></IconStyle><LabelStyle><scale>0.8</scale></LabelStyle></Style>',
           '<Style id="bench"><IconStyle><color>ff8ab7ff</color><scale>0.9</scale><Icon><href>https://maps.google.com/mapfiles/kml/paddle/orange-stars.png</href></Icon></IconStyle><LabelStyle><scale>0.8</scale></LabelStyle></Style>']
    rows = ["folder,day,name,lat,lng,notes"]
    for c in CITIES:
        pk = [(d, p, b) for d in c["days"] for p, b in d.get("picks", [])]
        if not pk: continue
        out.append(f'<Folder><name>{c["n"]:02d} {H.escape(c["name"])} · while you\'re here</name>')
        for d, pid, blurb in pk:
            p = P[pid]
            desc = f"<b>{H.escape(d['date'])}</b><br/>{H.escape(blurb)}<br/><a href='{place_url(p)}'>Open in Google Maps</a>"
            out.append(f'<Placemark><name>☆ {H.escape(p["name"])}</name><styleUrl>#pick</styleUrl><description><![CDATA[{desc}]]></description>'
                       f'<Point><coordinates>{p["lng"]:.6f},{p["lat"]:.6f},0</coordinates></Point></Placemark>')
            rows.append(",".join('"' + str(x).replace('"', '""') + '"' for x in (c["name"], d["date"], p["name"], p["lat"], p["lng"], blurb)))
        out.append('</Folder>')
    for city, items in BENCH:
        if not items: continue
        out.append(f'<Folder><name>Bench · {H.escape(city)}</name>')
        for pid, blurb in items:
            p = P[pid]
            desc = f"{H.escape(blurb)}<br/><a href='{place_url(p)}'>Open in Google Maps</a>"
            out.append(f'<Placemark><name>{H.escape(p["name"])}</name><styleUrl>#bench</styleUrl><description><![CDATA[{desc}]]></description>'
                       f'<Point><coordinates>{p["lng"]:.6f},{p["lat"]:.6f},0</coordinates></Point></Placemark>')
            rows.append(",".join('"' + str(x).replace('"', '""') + '"' for x in (city + " (bench)", "", p["name"], p["lat"], p["lng"], blurb)))
        out.append('</Folder>')
    out.append('</Document></kml>')
    return "\n".join(out), "\n".join(rows) + "\n"

ik, ic = ideas_kml()
open("ideas.kml", "w", encoding="utf-8").write(ik)
open("ideas.csv", "w", encoding="utf-8").write(ic)

# ---------------- HTML data ----------------
data = dict(
    pins={k: dict(id=v["id"], name=v["name"], short=v["short"], lat=v["lat"], lng=v["lng"], type=v["type"], url=place_url(v)) for k, v in P.items() if k in USED},
    cities=[dict(id=c["id"], n=c["n"], name=c["name"], kanji=c["kanji"], dates=c["dates"], nights=c["nights"],
                 hotel=c["hotel"], hotel_note=c["hotel_note"], days=[dict(d, picks=[dict(pin=p, blurb=b) for p,b in d.get("picks",[])]) for d in c["days"]]) for c in CITIES],
    legs=[dict(a=a, b=b, how=how, dur=dur, cost=cost) for a, b, how, dur, cost in LEGS],
    modes=MODE_LABEL,
)
tpl = open("map_template.html", encoding="utf-8").read()
html = tpl.replace("/*__DATA__*/", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("pins", len(P), "used", len(USED), "kml bytes", len(kml()), "ideas bytes", len(ik), "html bytes", len(html))
