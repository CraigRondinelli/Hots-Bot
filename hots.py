#terrible work in progress
#soon to be discord bot to pull heroes of the storm talent builds from hotslogs.

import urllib2

hero = raw_input('What hero?').lower()

if hero in ['butcher', 'the butcher']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The%20Butcher'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='abathur':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Abathur'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])


	print soup.title.string
	print tags

elif hero =='alarak':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Alarak'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['anubarak', 'anub arak', 'anub\'arak']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Anub\'arak'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='artanis':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Artanis'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='arthas':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Arthas'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='auriel':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Auriel'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='azmodan':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Azmodan'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='brightwing':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Brightwing'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='cassia':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cassia'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='chen':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chen'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='cho':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cho'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='chromie':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chromie'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['dva', 'd.va', 'diva']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=D.Va'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='dehaka':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Dehaka'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='diablo':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Diablo'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['etc', 'e.t.c.']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=E.T.C.'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='falstad':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Falstad'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['gazlowe', 'gallywix']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gazlowe'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='genji':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Genji'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['greymane' , 'graymane']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Greymane'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['guldan', 'gul\'dan']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gul\'dan'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='illidan':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Illidan'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='jaina':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Jaina'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print 

elif hero =='johanna':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Johanna'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['kaelthas', 'kael\'thas', 'kt']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kael\'thas'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='kerrigan':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kerrigan'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['kharazim' , 'khara', 'monk']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kharazim'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='leoric':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Leoric'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='lili':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li Li'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['liming', 'li-ming', 'ping']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li-Ming'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['lt. morales', 'morales', 'medic']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lt. Morales'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='lunara':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lunara'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	popularBuild = popularBuild.findAll('img')
	for img in popularBuild:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='lucio':
	#Link shortened due to encoding issues.
	url = 'https://goo.gl/4spScG'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['malfurion' , 'malf']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malfurion'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['malthael', 'malth']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malthael'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='medivh':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Medivh'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='muradin':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Muradin'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='murky':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Murky'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='nazeebo':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nazeebo'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='nova':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nova'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['probius', 'probe']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Probius'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['ragnaros', 'rag']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Ragnaros'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='raynor':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Raynor'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='rehgar':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rehgar'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='rexxar':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rexxar'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='samuro':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Samuro'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['sgt. hammer', 'hammer']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sgt. Hammer'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='sonya':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sonya'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='stitches':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stitches'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='stukov':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stukov'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['sylvanas', 'sylv']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sylvanas'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['tassadar', 'tass']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tassadar'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='diablo':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Diablo'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['the lost vikings', 'lost vikings', 'vikings' , 'tlv']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The Lost Vikings'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='thrall':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Thrall'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='tracer':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tracer'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='tychus':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tychus'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='tyrael':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrael'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='tyrande':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrande'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='uther':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Uther'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='valeera':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valeera'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='valla':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valla'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='varian':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Varian'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='xul':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Xul'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='zagara':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zagara'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='zarya':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zayra'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero =='zeratul':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zeratul'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero in ['zul\'jin', 'zuljin']:
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zul\'jin'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags

elif hero == 'stukov':
	url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stukov'
	page = urllib2.urlopen(url)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(page,'lxml')
	soup.title.string
	popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

	tags = []
	talents = popularBuild.findAll('img')
	for img in talents:
		if 'alt' in img.attrs:
			tags.append(img.attrs['alt'])	

	print soup.title.string
	print tags