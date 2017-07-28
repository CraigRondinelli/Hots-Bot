import discord
from discord.ext.commands import Bot
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup

Client = discord.Client()
bot_prefix="?"
client = commands.Bot(command_prefix = bot_prefix)

@client.event
async def on_ready():
	print ("Bot Online!")
	print ("Name: {}".format(client.user.name))
	print ("ID: {}".format(client.user.id))
	await client.change_presence(game=discord.Game(name='Heroes of the Storm'))

@client.event	
async def on_message(hero):
	
	async def herodata(url):
		page = urlopen(url)
		
		soup = BeautifulSoup(page,'lxml')
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')
	
		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	
	
		for txt in tags:
			await client.send_message(hero.channel, txt)

	if hero in ['butcher', 'the butcher']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The%20Butcher'
		
	elif hero =='abathur':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Abathur'
		
	elif hero =='alarak':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Alarak'
		
	elif hero in ['anubarak', 'anub arak', 'anub\'arak']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Anub\'arak'
		
	elif hero =='artanis':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Artanis'
		
	elif hero =='arthas':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Arthas'
		
	elif hero =='auriel':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Auriel'
		
	elif hero =='azmodan':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Azmodan'
		
	elif hero =='brightwing':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Brightwing'
		
	elif hero =='cassia':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cassia'
		
	elif hero =='chen':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chen'
		
	elif hero =='cho':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cho'
		
	elif hero =='chromie':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chromie'
		
	elif hero in ['dva', 'd.va', 'diva']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=D.Va'
		
	elif hero =='dehaka':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Dehaka'
		
	elif hero =='diablo':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Diablo'
		
	elif hero in ['etc', 'e.t.c.']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=E.T.C.'
		
	elif hero =='falstad':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Falstad'
		
	elif hero in ['gazlowe', 'gallywix']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gazlowe'
		
	elif hero =='genji':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Genji'
		
	elif hero in ['greymane' , 'graymane']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Greymane'
		
	elif hero in ['guldan', 'gul\'dan']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gul\'dan'
		
	elif hero =='illidan':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Illidan'
		
	elif hero =='jaina':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Jaina'
		
	elif hero =='johanna':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Johanna'
		
	elif hero in ['kaelthas', 'kael\'thas', 'kt']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kael\'thas'
		
	elif hero =='kerrigan':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kerrigan'
		
	elif hero in ['kharazim' , 'khara', 'monk']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kharazim'
		
	elif hero =='leoric':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Leoric'
		
	elif hero =='lili':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li Li'
		
	elif hero in ['liming', 'li-ming', 'ping']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li-Ming'
		
	elif hero in ['lt. morales', 'morales', 'medic']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lt. Morales'
		
	elif hero =='lunara':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lunara'
		
	elif hero =='lucio':
		#Link shortened due to encoding issues.
		url = 'https://goo.gl/4spScG'
		
	elif hero in ['malfurion' , 'malf']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malfurion'
		
	elif hero in ['malthael', 'malth']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malthael'
		
	elif hero =='medivh':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Medivh'
		
	elif hero =='muradin':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Muradin'
		
	elif hero =='murky':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Murky'
		
	elif hero =='nazeebo':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nazeebo'
		
	elif hero =='nova':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nova'
		
	elif hero in ['probius', 'probe']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Probius'
		
	elif hero in ['ragnaros', 'rag']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Ragnaros'
		
	elif hero =='raynor':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Raynor'
		
	elif hero =='rehgar':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rehgar'
		
	elif hero =='rexxar':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rexxar'
		
	elif hero =='samuro':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Samuro'
		
	elif hero in ['sgt. hammer', 'hammer']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sgt. Hammer'
		
	elif hero =='sonya':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sonya'
		
	elif hero =='stitches':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stitches'
		
	elif hero =='stukov':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stukov'
		
	elif hero in ['sylvanas', 'sylv']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sylvanas'
		
	elif hero in ['tassadar', 'tass']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tassadar'
		
	elif hero =='diablo':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Diablo'
		
	elif hero in ['the lost vikings', 'lost vikings', 'vikings' , 'tlv']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The Lost Vikings'
		
	elif hero =='thrall':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Thrall'
		
	elif hero =='tracer':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tracer'
		
	elif hero =='tychus':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tychus'
		
	elif hero =='tyrael':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrael'
		
	elif hero =='tyrande':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrande'
		
	elif hero =='uther':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Uther'
		
	elif hero =='valeera':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valeera'
		
	elif hero =='valla':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valla'
		
	elif hero =='varian':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Varian'
		
	elif hero =='xul':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Xul'
		
	elif hero =='zagara':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zagara'
		
	elif hero =='zarya':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zayra'
		
	elif hero =='zeratul':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zeratul'
		
	elif hero in ['zul\'jin', 'zuljin']:
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zul\'jin'
		
	elif hero == 'stukov':
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stukov'
	
	else:
		url = 'empty'
		
	if 'empty' == url:
		txt = 'Do you even know what you are looking for?'
		await client.send_message(hero.channel, txt)
	
	else:
		#todo finish error handling
		try:
			herodata(url)
		except: #catch *all* exceptions
			txt = 'What did you break?'
			await client.send_message(hero.channel, txt)

client.run("MzM5MjE1MjM5NTY2NTg5OTUz.DFqjRg.auY7zoNcL2YQHjmNqwv2h-o39X4")
