#terrible work in progress
#soon to be discord bot to pull heroes of the storm talent builds from hotslogs.

import urllib2
from bs4 import BeautifulSoup

def herodata(url):
	page = urllib2.urlopen(url)
	
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	for txt in tags:
		#todo print pretty
		print txt

hero = raw_input('What hero?').lower()

if hero in ['butcher', 'the butcher']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The%20Butcher'
	herodata(url)

elif hero =='abathur':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Abathur'
	herodata(url)

elif hero =='alarak':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Alarak'
	herodata(url)

elif hero in ['anubarak', 'anub arak', 'anub\'arak']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Anub\'arak'
	herodata(url)

elif hero =='artanis':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Artanis'
	herodata(url)

elif hero =='arthas':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Arthas'
	herodata(url)

elif hero =='auriel':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Auriel'
	herodata(url)

elif hero =='azmodan':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Azmodan'
	herodata(url)

elif hero =='brightwing':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Brightwing'
	herodata(url)

elif hero =='cassia':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cassia'
	herodata(url)

elif hero =='chen':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chen'
	herodata(url)

elif hero =='cho':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cho'
	herodata(url)

elif hero =='chromie':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chromie'
	herodata(url)

elif hero in ['dva', 'd.va', 'diva']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=D.Va'
	herodata(url)

elif hero =='dehaka':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Dehaka'
	herodata(url)

elif hero =='diablo':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Diablo'
	herodata(url)

elif hero in ['etc', 'e.t.c.']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=E.T.C.'
	herodata(url)

elif hero =='falstad':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Falstad'
	herodata(url)

elif hero in ['gazlowe', 'gallywix']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gazlowe'
	herodata(url)

elif hero =='genji':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Genji'
	herodata(url)

elif hero in ['greymane' , 'graymane']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Greymane'
	herodata(url)

elif hero in ['guldan', 'gul\'dan']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gul\'dan'
	herodata(url)

elif hero =='illidan':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Illidan'
	herodata(url)

elif hero =='jaina':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Jaina'
	herodata(url)

elif hero =='johanna':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Johanna'
	herodata(url)

elif hero in ['kaelthas', 'kael\'thas', 'kt']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kael\'thas'
	herodata(url)

elif hero =='kerrigan':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kerrigan'
	herodata(url)

elif hero in ['kharazim' , 'khara', 'monk']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kharazim'
	herodata(url)

elif hero =='leoric':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Leoric'
	herodata(url)

elif hero =='lili':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li Li'
	herodata(url)

elif hero in ['liming', 'li-ming', 'ping']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li-Ming'
	herodata(url)

elif hero in ['lt. morales', 'morales', 'medic']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lt. Morales'
	herodata(url)

elif hero =='lunara':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lunara'
	herodata(url)

elif hero =='lucio':
	#Link shortened due to encoding issues.
	url = 'https://goo.gl/4spScG'
	herodata(url)

elif hero in ['malfurion' , 'malf']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malfurion'
	herodata(url)

elif hero in ['malthael', 'malth']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malthael'
	herodata(url)

elif hero =='medivh':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Medivh'
	herodata(url)

elif hero =='muradin':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Muradin'
	herodata(url)

elif hero =='murky':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Murky'
	herodata(url)

elif hero =='nazeebo':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nazeebo'
	herodata(url)

elif hero =='nova':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nova'
	herodata(url)

elif hero in ['probius', 'probe']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Probius'
	herodata(url)

elif hero in ['ragnaros', 'rag']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Ragnaros'
	herodata(url)

elif hero =='raynor':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Raynor'
	herodata(url)

elif hero =='rehgar':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rehgar'
	herodata(url)

elif hero =='rexxar':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rexxar'
	herodata(url)

elif hero =='samuro':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Samuro'
	herodata(url)

elif hero in ['sgt. hammer', 'hammer']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sgt. Hammer'
	herodata(url)

elif hero =='sonya':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sonya'
	herodata(url)

elif hero =='stitches':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stitches'
	herodata(url)

elif hero =='stukov':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stukov'
	herodata(url)

elif hero in ['sylvanas', 'sylv']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sylvanas'
	herodata(url)

elif hero in ['tassadar', 'tass']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tassadar'
	herodata(url)

elif hero =='diablo':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Diablo'
	herodata(url)

elif hero in ['the lost vikings', 'lost vikings', 'vikings' , 'tlv']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The Lost Vikings'
	herodata(url)

elif hero =='thrall':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Thrall'
	herodata(url)

elif hero =='tracer':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tracer'
	herodata(url)

elif hero =='tychus':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tychus'
	herodata(url)

elif hero =='tyrael':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrael'
	herodata(url)

elif hero =='tyrande':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrande'
	herodata(url)

elif hero =='uther':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Uther'
	herodata(url)

elif hero =='valeera':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valeera'
	herodata(url)

elif hero =='valla':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valla'
	herodata(url)

elif hero =='varian':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Varian'
	herodata(url)

elif hero =='xul':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Xul'
	herodata(url)

elif hero =='zagara':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zagara'
	herodata(url)

elif hero =='zarya':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zayra'
	herodata(url)

elif hero =='zeratul':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zeratul'
	herodata(url)

elif hero in ['zul\'jin', 'zuljin']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zul\'jin'
	herodata(url)

elif hero == 'stukov':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stukov'
	herodata(url)

else:
	print("Do you even know what you are looking for?")