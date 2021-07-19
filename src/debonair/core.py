import os
import quo
import subprocess
import urllib.request
from quo import command, app, echo, prompt
from subprocess import check_output as inputstream

current_dir = os.getcwd()
_banner = """

╭━━━┳━━━┳━━╮╭━━━┳━╮╱╭┳━━━┳━━┳━━━┳━━━╮
╰╮╭╮┃╭━━┫╭╮┃┃╭━╮┃┃╰╮┃┃╭━╮┣┫┣┫╭━╮┃╭━━╯
╱┃┃┃┃╰━━┫╰╯╰┫┃╱┃┃╭╮╰╯┃┃╱┃┃┃┃┃╰━╯┃╰━━╮
╱┃┃┃┃╭━━┫╭━╮┃┃╱┃┃┃╰╮┃┃╰━╯┃┃┃┃╭╮╭┫╭━━╯
╭╯╰╯┃╰━━┫╰━╯┃╰━╯┃┃╱┃┃┃╭━╮┣┫┣┫┃┃╰┫╰━━╮
╰━━━┻━━━┻━━━┻━━━┻╯╱╰━┻╯╱╰┻━━┻╯╰━┻━━━╯

"""

import sys
import time
_banner2 = """

#####################################
# [99] < Back (Main menu)           #
# [00] Exit Debonair                #
#####################################
"""
os.system("cd /etc/ && touch debonair.conf")
os.system("cd /etc/ && touch debonair_1")
prefix = os.getenv("PREFIX")
configBase = "[HOME] = ~"
configFile = "/etc/debonair.conf"
cache_1 = "/etc/debonair_1"

@command()
@app("--sources_list")
def repo_check(sources_list):
	if os.path.isfile(os.getenv("PREFIX")+"/etc/apt/sources.list.d/"+sources_list):
		return True
	return False

@command()
@app("--statusId")
def writeStatus(statusId):
	open(cache_1,"w").write(str(statusId))

def readStatus():
	try:
		statusId = open(cache_1,"r").read()
		if statusId == "1":
			return True
		return False
	except IOError:
		return False

def checkConfigFile():
	if os.path.exists(configFile):
		if os.path.isdir(configFile):
			os.system(f"rm -rf {configFile}")
			open(configFile,"w").write(configBase)
	else:
		open(configFile,"w").write(configBase)

def loadConfigFile():
	checkConfigFile()
	lfile = ""
	try:
		lfile = [x.split("=")[-1].strip() for x in open(configFile,"r").splitlines() if x.split("=")[0].strip() == "[HOME]"][0]
	except Exception as e:
		lfile = "~"
	return lfile

homeDir = loadConfigFile()

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	if not readStatus():
		echo(f'{_banner2}', foreground="red", bold=True, italic=True) 
		backtomenu = prompt("@dbnr >>> ")
		
		if backtomenu == "99":
			restart_program()
		elif backtomenu == "00":
			sys.exit()
		else:
			echo(f"ERROR: Wrong Input", foreground="red")
			time.sleep(2)
			restart_program()

def banner():
	echo(f'{_banner}', foreground="yellow", bold=True) 

### Repo Installer
def pointless_repo():
	urllib.request.urlretrieve('https://github.com/secretum-inc/debonair/src/debonair/kickstart','kickstart')
	os.system('kickstart')
	os.remove('kickstart')
	os.system('apt update -y')
###

def nmap():
	echo(f"%%%%%%% Installing... Nmap", foreground="vcyan") 
	# secretum inc
	os.system('apt install nmap')
	echo('###### Done')
	echo(f"###### Type 'nmap' to start.", foreground="red")
	backtomenu_option()

def red_hawk():
	echo(f"%%%%%%% Installing... RED HAWK", foreground="vcyan") 
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def dtect():
	echo(f"%%%%%%% Installing... D-TECT", foreground="vcyan") 
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	os.system('mv D-Tech {}/D-TECT'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sqlmap():
	echo(f"%%%%%%% Installing... sqlmap", foreground="vcyan") 
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def infoga():
	echo(f"%%%%%%% Installing... Infoga", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def reconDog():
	echo(f"%%%%%%% Installing... ReconDog", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/ReconDog')
	os.system('mv ReconDog {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def androZenmap():
	echo(f"%%%%%%% Installing... AndroZenmap", foreground="vcyan")
	# secretum inc
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir {}/AndroZenmap'.format(homeDir))
	os.system('mv androzenmap.sh {}/AndroZenmap'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sqlmate():
	echo(f"%%%%%%% Installing... sqlmate", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/s0md3v/sqlmate')
	os.system('mv sqlmate {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def astraNmap():
	echo(f"%%%%%%% Installing... AstraNmap", foreground="vcyan")
	# secretum inc
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def weeman():
	echo(f"%%%%%%% Installing... weeman", foreground="vcyan")
	# secretum inc
	os.system('apt install clang git python2')
	os.system('python2 -m pip bs4 html5lib lxml')
	os.system('git clone https://github.com/evait-security/weeman')
	os.system('mv weeman {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def easyMap():
	echo(f"%%%%%%% Installing... Easymap", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap {}'.format(homeDir))
	os.system('cd {}/Easymap && sh install.sh'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xd3v():
	echo(f"%%%%%%% Installing... XD3v", foreground="vcyan")
	# secretum inc
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh {0}/../usr/bin/xd3v && chmod +x {0}/../usr/bin/xd3v'.format(homeDir))
	echo('###### Done')
	echo(f"###### Type 'xd3v' to start.")
	backtomenu_option()

def crips():
	echo(f"%%%%%%% Installing... Crips", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sir():
	echo(f"%%%%%%% Installing... SIR", foreground="vcyan")
	# secretum inxlc
	os.system("apt install python2 git")
	os.system("python2 -m pip install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xshell():
	echo(f"%%%%%%% Installing... Xshell", foreground="vcyan")
	# secretum inxlc
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def evilURL():
	echo(f"%%%%%%% Installing... EvilURL", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def striker():
	echo(f"%%%%%%% Installing... Striker", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/s0md3v/Striker')
	os.system('mv Striker {}'.format(homeDir))
	os.system('cd {}/Striker && python2 -m pip install -r requirements.txt'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def dsss():
	echo(f"%%%%%%% Installing... DSSS", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sqliv():
	echo(f"%%%%%%% Installing... SQLiv", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/the-robot/sqliv')
	os.system('mv sqliv {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sqlscan():
	echo(f"%%%%%%% Installing... sqlscan", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def wordpreSScan():
	echo(f"%%%%%%% Installing... Wordpresscan", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan {}'.format(homeDir))
	os.system('cd {}/Wordpresscan && python2 -m pip install -r requirements.txt'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def wpscan():
	echo(f"%%%%%%% Installing... WPScan", foreground="vcyan")
	# secretum inc
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan {0} && cd {0}/wpscan'.format(homeDir))
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	echo('###### Done')
	backtomenu_option()

def wordpresscan():
	echo(f"%%%%%%% Installing... wordpresscan(2)", foreground="vcyan")
	# secretum inc
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan {}'.format(homeDir))
	echo('###### Done')
	echo(f"###### Type 'wordpresscan' to start.")
	backtomenu_option()

def routersploit():
	echo(f"%%%%%%% Installing... Routersploit", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/threat9/routersploit')
	os.system('mv routersploit {0};cd {0}/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def torshammer():
	echo(f"%%%%%%% Installing... Torshammer", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def slowloris():
	echo(f"%%%%%%% Installing... Slowloris", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def fl00d12():
	echo(f"%%%%%%% Installing... Fl00d & Fl00d2", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 curl')
	os.system('mkdir {}/fl00d'.format(homeDir))
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	os.system('mv fl00d.py {0}/fl00d && mv fl00d2.py {0}/fl00d'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def goldeneye():
	echo(f"%%%%%%% Installing... GoldenEye", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xerxes():
	echo(f"%%%%%%% Installing... Xerxes", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/baraalmasri/xerxes')
	os.system('mv xerxes {}'.format(homeDir))
	os.system('cd {}/xerxes && clang xerxes.c -o xerxes'.format(homeDir))
	os.system('chmod 755 {0}/xerxes/xerxes && cp {0}/xerxes/xerxes $PREFIX/bin'.format(homeDir))
	echo('###### Done')
	echo('###### Usage: xerxes ​www.fakesite.com​ 80')
	backtomenu_option()

def planetwork_ddos():
	echo(f"%%%%%%% Installing... Planetwork-DDOS", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hydra():
	echo(f"%%%%%%% Installing... Hydra", foreground="vcyan")
	# secretum inc
	os.system('apt install hydra')
	echo('###### Done')
	backtomenu_option()

def black_hydra():
	echo(f"%%%%%%% Installing... Black Hydra", foreground="vcyan")
	# secretum inc
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def cupp():
	echo(f"%%%%%%% Installing... Cupp", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def asu():
	echo(f"%%%%%%% Installing... ASU", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hash_buster():
	echo(f"%%%%%%% Installing... Hash-Buster", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/Hash-Buster')
	os.system('mv Hash-Buster {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def instaHack():
	echo(f"%%%%%%% Installing... InstaHack", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Slayeri4/instahack')
	os.system('mv instahack {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def indonesian_wordlist():
	echo(f"%%%%%%% Installing... indonesian-wordlist", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	os.system('mv indonesian-wordlist {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def fbBrute():
	echo(f"%%%%%%% Installing... Facebook Brute Force 3", foreground="vcyan")
	# secretum inc
	os.system('apt install curl python2')
	os.system('python2 -m pip install mechanize')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt')
	os.system('mkdir {}/facebook-brute-3'.format(homeDir))
	os.system('mv facebook3.py {0}/facebook-brute-3 && mv password.txt {0}/facebook-brute-3'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def webdav():
	echo(f"%%%%%%% Installing... WebDAV", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 openssl curl libcurl')
	os.system('python2 -m pip install urllib3 chardet certifi idna requests')
	os.system('mkdir {}/webdav'.format(homeDir))
	os.system('curl -k -O https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR {}/webdav/webdav.py'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def webmassploit():
	echo(f"%%%%%%% Installing... Webdav Mass Exploiter", foreground="vcyan")
	# secretum inxlc
	os.system("apt install python2 openssl curl libcurl")
	os.system("python2 -m pip install requests")
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir {0}/webdav-mass-exploit && mv webdav.py {0}/webdav-mass-exploit".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sqldump():
	echo(f"%%%%%%% Installing... sqldump", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 curl')
	os.system('python2 -m pip install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir {0}/sqldump && chmod +x sqldump.py && mv sqldump.py {0}/sqldump'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def websploit():
	echo(f"%%%%%%% Installing... Websploit", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def metasploit():
	echo(f"%%%%%%% Installing... Metasploit", foreground="vcyan")
	# secretum inxlc
	os.system("apt install unstable-repo")
	os.system("cd {} && apt install metasploit".format(homeDir))
	echo('###### Done')
	echo(f"###### Type 'msfconsole' to start.")
	backtomenu_option()

def commix():
	echo(f"%%%%%%% Installing... Commix", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def brutal():
	echo(f"%%%%%%% Installing... Brutal", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def knockmail():
	echo(f"%%%%%%% Installing... KnockMail", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hac():
	echo(f"%%%%%%% Installing... Hac", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def rang3r():
	echo(f"%%%%%%% Installing... Rang3r", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sh33ll():
	echo(f"%%%%%%% Installing... SH33LL", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def social():
	echo(f"%%%%%%% Installing... Social-Engineering", foreground="vcyan")
	# secretum inxlc
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def spiderbot():
	echo(f"%%%%%%% Installing... SpiderBot", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot {}".format(homeDir))
	echo('###### Done')
	backtomenu_option()

def ngrok():
	echo(f"%%%%%%% Installing... Ngrok", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sudo():
	echo(f"%%%%%%% Installing... sudo", foreground="vcyan")
	# secretum inc
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo {0} && cd {0}/termux-sudo && chmod 777 *'.format(homeDir))
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	echo('###### Done')
	backtomenu_option()

def ubuntu():
	echo(f"%%%%%%% Installing... Ubuntu", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu {0} && cd {0}/termux-ubuntu && bash ubuntu.sh'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def fedora():
	echo(f"%%%%%%% Installing... Fedora", foreground="vcyan")
	# secretum inc
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def nethunter():
	echo(f"%%%%%%% Installing... Kali NetHunter", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def blackbox():
	echo(f"%%%%%%% Installing... BlackBox", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xattacker():
	echo(f"%%%%%%% Installing... XAttacker", foreground="vcyan")
	# secretum inc
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def vcrt():
	echo(f"%%%%%%% Installing... VCRT", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def socfish():
	echo(f"%%%%%%% Installing... SocialFish", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def ecode():
	echo(f"%%%%%%% Installing... ECode", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xsstrike():
	echo(f"%%%%%%% Installing... XSStrike", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/s0md3v/XSStrike')
	os.system('mv XSStrike {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def breacher():
	echo(f"%%%%%%% Installing... Breacher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests argparse')
	os.system('git clone https://github.com/s0md3v/Breacher')
	os.system('mv Breacher {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def stylemux():
	echo(f"%%%%%%% Installing... Termux-Styling", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def txtool():
	echo(f"%%%%%%% Installing... TXTool", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def passgencvar():
	echo(f"%%%%%%% Installing... PassGen", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def owscan():
	echo(f"%%%%%%% Installing... OWScan", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sanlen():
	echo(f"%%%%%%% Installing... santet-online", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def spazsms():
	echo(f"%%%%%%% Installing... SpazSMS", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hasher():
	echo(f"%%%%%%% Installing... Hasher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install passlib binascii progressbar')
	os.system('git clone https://github.com/CiKu370/hasher')
	os.system('mv hasher {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hashgenerator():
	echo(f"%%%%%%% Installing... Hash-Generator", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/CiKu370/hash-generator')
	os.system('mv hash-generator {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def kodork():
	echo(f"%%%%%%% Installing... ko-dork", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/CiKu370/ko-dork')
	os.system('mv ko-dork {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def snitch():
	echo(f"%%%%%%% Installing... snitch", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def osif():
	echo(f"%%%%%%% Installing... OSIF", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/CiKu370/OSIF')
	os.system('mv OSIF {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def nk26():
	echo(f"%%%%%%% Installing... nk26", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/milio48/nk26')
	os.system('mv nk26 {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def devploit():
	echo(f"%%%%%%% Installing... Devploit", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hasherdotid():
	echo(f"%%%%%%% Installing... Hasherdotid", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	os.system('mv hasherdotid {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def namechk():
	echo(f"%%%%%%% Installing... Namechk", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xlPy():
	echo(f"%%%%%%% Installing... xl-py", foreground="vcyan")
	# secretum inc
	os.system('apt install python git')
	os.system('git clone https://github.com/albertoanggi/xl-py')
	os.system('mv xl-py {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def beanshell():
	echo(f"%%%%%%% Installing... Beanshell", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	echo('###### Done')
	echo(f"###### Type 'bsh' to start.")
	backtomenu_option()

def crunch():
	echo(f"%%%%%%% Installing... Crunch", foreground="vcyan")
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	echo(f"###### Done")
	echo(f"###### Type 'crunch' to start.")
	backtomenu_option()

def binploit():
	echo(f"%%%%%%% Installing... Binary Exploitation", foreground="vcyan")
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	echo(f"###### Done")
	echo(f"###### Tutorial: https://youtu.be/3NTXFUxcKPc")
	backtomenu_option()

def textr():
	echo(f"%%%%%%% Installing... Textr", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	echo('###### Done')
	echo(f"###### Type 'textr' to start.")
	backtomenu_option()

def apsca():
	echo(f"%%%%%%% Installing... ApSca", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	echo('###### Done')
	echo(f"###### Type 'apsca' to start.")
	backtomenu_option()

def amox():
	echo(f"%%%%%%% Installing... amox", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	echo('###### Done')
	echo(f"###### Type 'amox' to start.")
	backtomenu_option()

def fade():
	echo(f"%%%%%%% Installing... FaDe", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FaDe')
	os.system('mv FaDe {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def ginf():
	echo(f"%%%%%%% Installing... GINF", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def auxile():
	echo(f"%%%%%%% Installing... AUXILE", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def inther():
	echo(f"%%%%%%% Installing... inther", foreground="vcyan")
	# secretum inc
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hpb():
	echo(f"%%%%%%% Installing... HPB", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	echo('###### Done')
	echo(f"###### Type 'hpb' to start.")
	backtomenu_option()

def fmbrute():
	echo(f"%%%%%%% Installing... FMBrute", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FMBrute')
	os.system('mv FMBrute {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def hashid():
	echo(f"%%%%%%% Installing... HashID", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 && python2 -m pip install hashid')
	echo(f"###### Done")
	echo(f"###### Type 'hashid -h' to show usage of hashid")
	backtomenu_option()

def gpstr():
	echo(f"%%%%%%% Installing... GPS Tracking", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	os.system('mv gps_tracking {}'.format(homeDir))
	echo(f"###### Done")
	backtomenu_option()

def pret():
	echo(f"%%%%%%% Installing... PRET", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 imagemagick git')
	os.system('python2 -m pip install colorama pysnmp')
	os.system('git clone https://github.com/RUB-NDS/PRET')
	os.system('mv PRET {}'.format(homeDir))
	echo(f"###### Done")
	backtomenu_option()

def atlas():
	echo(f"%%%%%%% Installing... Atlas", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/m4ll0k/Atlas')
	os.system('mv Atlas {}'.format(homeDir))
	echo(f"###### Done")
	backtomenu_option()

def hashcat():
	echo(f"%%%%%%% Installing... Hashcat", foreground="vcyan")
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	echo(f"###### Done")
	echo(f"###### Type 'hashcat' to start.")
	backtomenu_option()

def liteotp():
	echo(f"%%%%%%% Installing... LiteOTP", foreground="vcyan")
	# secretum inc
	os.system('apt install php wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite')
	echo(f"###### Done")
	echo(f"###### Type 'lite' to start.")
	backtomenu_option()

def fbbrutex():
	echo(f"%%%%%%% Installing... FBBrute", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FBBrute')
	os.system('mv FBBrute {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def fim():
	echo(f"%%%%%%% Installing... fim", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	os.system('mv fim {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def rshell():
	echo(f"%%%%%%% Installing... RShell", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install colorama')
	os.system('git clone https://github.com/Jishu-Epic/RShell')
	os.system('mv RShell {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def termpyter():
	echo(f"%%%%%%% Installing... TermPyter", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Jishu-Epic/TermPyter')
	os.system('mv TermPyter {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def maxsubdofinder():
	echo(f"%%%%%%% Installing... MaxSubdoFinder", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	os.system('mv MaxSubdoFinder {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def jadx():
	echo(f"%%%%%%% Installing... jadx", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
	os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
	os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	echo('###### Done')
	echo(f"###### Type 'jadx' to start.")
	backtomenu_option()

def pwnedornot():
	echo(f"%%%%%%% Installing... pwnedOrNot", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	os.system('mv pwnedOrNot {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def maclook():
	echo(f"%%%%%%% Installing... Mac-Lookup", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	os.system('mv Mac-Lookup {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def f4k3():
	echo(f"%%%%%%% Installing... F4K3", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Gameye98/Gameye98.github.io/blob/master/package/f4k3_1.0_all.deb')
	os.system('dpkg -i f4k3_1.0_all.deb')
	os.system('rm -rf f4k3_1.0_all.deb')
	echo('###### Done')
	echo(f"###### Type 'f4k3' to start.")
	backtomenu_option()

def katak():
	echo(f"%%%%%%% Installing... Katak", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests progressbar')
	os.system('git clone https://github.com/Gameye98/Katak')
	os.system('mv Katak {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def heroku():
	echo(f"%%%%%%% Installing... heroku", foreground="vcyan")
	# secretum inc
	os.system('apt install nodejs')
	os.system('npm install heroku -g')
	echo('###### Done')
	echo(f"###### Type 'heroku' to start.")
	backtomenu_option()

def google():
	echo(f"%%%%%%% Installing... google", foreground="vcyan")
	# secretum inc
	os.system('apt install python')
	os.system('python -m pip install google')
	echo('###### Done')
	echo(f"###### Type 'google' to start.")
	backtomenu_option()

def billcypher():
	echo(f"%%%%%%% Installing... BillCypher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install argparse dnspython requests urllib3 colorama')
	os.system('git clone https://github.com/GitHackTools/BillCipher')
	os.system('mv BillCypher {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def vbug():
	echo(f"%%%%%%% Installing... vbug", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Gameye98/vbug')
	os.system('mv vbug {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def kojawafft():
	echo(f"%%%%%%% Installing... kojawafft", foreground="vcyan")
	# secretum inc
	os.system('apt install git nodejs')
	os.system('git clone https://github.com/sandalpenyok/kojawafft')
	os.system('mv kojawafft {}'.format(homeDir))
	os.system('cd $HOME/kojawafft && unzip node_modules.zip && cd -')
	echo('###### Done')
	backtomenu_option()

def aircrackng():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: echo(f"ERROR: Make sure you're device has been rooted");
	else:
		echo(f"%%%%%%% Installing... aircrack-ng", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo aircrack-ng')
		echo('###### Done')
		echo(f"###### Type 'aircrack-ng' to start.")
	backtomenu_option()

def ettercap():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: echo(f"ERROR: Make sure you're device has been rooted");
	else:
		echo(f"%%%%%%% Installing... ettercap", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo ettercap')
		echo('###### Done')
		echo(f"###### Type 'ettercap' to start.")
	backtomenu_option()

def ccgen():
	echo(f"%%%%%%% Installing... ccgen", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ccgen')
	os.system('mv ccgen {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def ddcrypt():
	echo(f"%%%%%%% Installing... ddcrypt", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ddcrypt')
	os.system('mv ddcrypt {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def dnsrecon():
	echo(f"%%%%%%% Installing... dnsrecon", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/darkoperator/dnsrecon')
	os.system('python -m pip install -r dnsrecon/requirements.txt')
	os.system('mv dnsrecon {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def zphisher():
	echo(f"%%%%%%% Installing... zphisher", foreground="vcyan")
	# secretum inc
	os.system('apt install git php openssh curl')
	os.system('git clone https://github.com/htr-tech/zphisher')
	os.system('mv zphisher {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def apktool():
	echo(f"%%%%%%% Installing... apktool", foreground="vcyan")
	# secretum inc
	os.system('apt install git dpkg')
	os.system('git clone https://github.com/Lexiie/Termux-Apktool')
	os.system('mv Termux-Apktool {}'.format(homeDir))
	os.system('cd {}/Termux-Apktool && dpkg -i *.deb'.format(homeDir))
	echo('###### Done')
	echo(f"###### Type 'apktool' to start.")
	backtomenu_option()

def uncompyle():
	echo(f"%%%%%%% Installing... uncompyle6", foreground="vcyan")
	# secretum inc
	os.system('apt install python python2')
	os.system('python2 -m pip install uncompyle6')
	os.system('mv $PREFIX/bin/uncompyle6 $PREFIX/bin/uncompyle')
	os.system('python -m pip install uncompyle6')
	echo('###### Done')
	echo('###### (py2) Usage: uncompyle')
	echo('###### (py3) Usage: uncompyle6')
	backtomenu_option()

def wifite():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: echo(f"ERROR: Make sure you're device has been rooted");
	else:
		echo(f"%%%%%%% Installing... Wifite", foreground="vcyan")
		# secretum inc
		os.system('apt install git python2')
		os.system('git clone https://github.com/derv82/wifite')
		os.system('mv wifite {}'.format(homeDir))
		echo('###### Done')
	backtomenu_option()

def parrot():
	echo(f"%%%%%%% Installing... Parrot", foreground="vcyan")
	# secretum inc
	os.system('apt install wget openssl-tool proot -y && hash -r && cd {} && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Parrot/parrot.sh && bash parrot.sh'.format(homeDir))
	os.system('cd {} && bash start-parrot.sh'.format(homeDir))
	echo('###### Done')
	echo('###### Make sure visit: https://techriz.com/how-to-install-parrot-linux-on-android-without-root/')
	os.system('am start -a android.intent.action.VIEW -d "https://techriz.com/how-to-install-parrot-linux-on-android-without-root/"')
	backtomenu_option()

def archlinux():
	echo(f"%%%%%%% Installing... Arch Linux", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('cd $HOME && git clone https://github.com/sdrausty/TermuxArch')
	os.system('cd $HOME && bash TermuxArch/setupTermuxArch.sh')
	echo('###### Done')
	backtomenu_option()

def tshark():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: echo(f"ERROR: Make sure you're device has been rooted");
	else:
		echo(f"%%%%%%% Installing... tshark", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo tshark')
		echo('###### Done')
		echo(f"###### Type 'tshark' to start.")
	backtomenu_option()

def dos2unix():
	echo(f"%%%%%%% Installing... dos2unix", foreground="vcyan")
	# secretum inc
	os.system('apt install dos2unix')
	echo('###### Done')
	echo(f"###### Type 'dos2unix' to start.")
	backtomenu_option()

def exiftool():
	echo(f"%%%%%%% Installing... exiftool", foreground="vcyan")
	# secretum inc
	os.system('apt install exiftool')
	echo('###### Done')
	echo(f"###### Type 'exiftool' to start.")
	backtomenu_option()

def iconv():
	echo(f"%%%%%%% Installing... iconv", foreground="vcyan")
	# secretum inc
	os.system('apt install iconv')
	echo('###### Done')
	echo(f"###### Type 'iconv' to start.")
	backtomenu_option()

def mediainfo():
	echo(f"%%%%%%% Installing... mediainfo", foreground="vcyan")
	# secretum inc
	os.system('apt install mediainfo')
	echo('###### Done')
	echo('###### Usage: mediainfo filename.pdf')
	backtomenu_option()

def pdfinfo():
	echo(f"%%%%%%% Installing... pdfinfo", foreground="vcyan")
	# secretum inc
	os.system('apt install poppler')
	echo('###### Done')
	echo('###### Usage: pdfinfo filename.pdf')
	backtomenu_option()

def tcpdump():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: echo(f"ERROR: Make sure you're device has been rooted");
	else:
		echo(f"%%%%%%% Installing... tcpdump", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo tcpdump')
		echo('###### Done')
		echo(f"###### Type 'tcpdump' to start.")
	backtomenu_option()

def hping3():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: echo(f"ERROR: Make sure you're device has been rooted");
	else:
		echo(f"%%%%%%% Installing... hping3", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo hping3')
		echo('###### Done')
		echo(f"###### Type 'hping3' to start.")
	backtomenu_option()

def dbdat():
	echo(f"%%%%%%% Installing... DbDat", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install MySQL-python psycopg2 cx_Oracle pymssql ibm_db pymongo pyyaml couchdb')
	os.system('git clone https://github.com/foospidy/DbDat')
	os.system('mv DbDat {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def nosqlmap():
	echo(f"%%%%%%% Installing... NoSQLMap", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 unstable-repo metasploit')
	os.system('python2 -m pip install pymongo httplib2')
	os.system('git clone https://github.com/codingo/NoSQLMap')
	os.system('mv NoSQLMap {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def audit_couchdb():
	echo(f"%%%%%%% Installing... audit_couchdb", foreground="vcyan")
	# secretum inc
	os.system('apt install git nodejs')
	os.system('npm install -g npm@next audit_couchdb')
	os.system('git clone https://github.com/iriscouch/audit_couchdb')
	os.system('mv audit_couchdb {}'.format(homeDir))
	echo('###### Done')
	echo('###### Usage: audit_couchdb https://admin:secret@localhost:5984')
	backtomenu_option()

def mongoaudit():
	echo(f"%%%%%%% Installing... mongoaudit", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install pymongo mongoaudit')
	echo('###### Done')
	echo(f"###### Type 'mongoaudit' to start.")
	backtomenu_option()

def wifiphisher():
	echo(f"%%%%%%% Installing... Wifiphisher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install setuptools scapy')
	os.system('git clone https://github.com/wifiphisher/wifiphisher')
	os.system('mv wifiphisher {0} && cd {0}/wifiphisher && python setup.py install'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sherlock():
	echo(f"%%%%%%% Installing... sherlock", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('git clone https://github.com/sherlock-project/sherlock')
	os.system('mv sherlock {0} && cd {0}/sherlock && python -m pip install -r requirements.txt'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def shc():
	echo(f"%%%%%%% Installing... shc", foreground="vcyan")
	# secretum inc
	os.system('apt install shc -y')
	echo('###### Done')
	echo(f"###### Type 'shc' to start.")
	backtomenu_option()

def steghide():
	echo(f"%%%%%%% Installing... steghide", foreground="vcyan")
	# secretum inc
	os.system('apt install steghide -y')
	echo('###### Done')
	echo(f"###### Type 'steghide' to start.")
	backtomenu_option()

def tesseract():
	echo(f"%%%%%%% Installing... tesseract", foreground="vcyan")
	# secretum inc
	os.system('apt install tesseract -y')
	echo('###### Done')
	echo(f"###### Type 'tesseract' to start.")
	backtomenu_option()

def sleuthkit():
	echo(f"%%%%%%% Installing... sleuthkit", foreground="vcyan")
	# secretum inc
	os.system('apt install sleuthkit -y')
	echo('###### Done')
	echo(f"###### Type 'pkg files sleuthkit | grep usr/bin' to check executable file related to sleuthkit package.")
	backtomenu_option()

def octave():
	echo(f"%%%%%%% Installing... Octave", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install octave -y')
	echo('###### Done')
	echo(f"###### Type 'octave' to start.")
	backtomenu_option()

def fpcompiler():
	echo(f"%%%%%%% Installing... fp-compiler", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install fp-compiler -y')
	echo('###### Done')
	echo(f"###### Type 'fpc' to start.")
	backtomenu_option()

def numpy():
	echo(f"%%%%%%% Installing... numpy", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install numpy -y')
	echo('###### Done')
	echo(f"###### Type 'pkg files numpy | grep usr/bin' to check executable file related to numpy package.")
	backtomenu_option()

def userrecon():
	echo(f"%%%%%%% Installing... userrecon", foreground="vcyan")
	# secretum inc
	os.system('apt install wget dpkg curl -y')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	os.system('dpkg -i userrecon_1.0_all.deb')
	os.system('rm userrecon_1.0_all.deb')
	echo('###### Done')
	echo(f"###### Type 'userrecon' to start.")
	backtomenu_option()

def mrsip():
	echo(f"%%%%%%% Installing... Mr.SIP", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	os.system('git clone https://github.com/meliht/Mr.SIP')
	os.system('mv Mr.SIP {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def tmscanner():
	echo(f"%%%%%%% Installing... TM-scanner", foreground="vcyan")
	# secretum inc
	os.system('apt install python python2 nmap git -y')
	os.system('python -m pip install colorama requests')
	os.system('python2 -m pip install colorama requests')
	os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
	os.system('mv TM-scanner {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xss_payload_list():
	echo(f"%%%%%%% Installing... xss-payload-list", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/payloadbox/xss-payload-list')
	os.system('mv xss-payload-list {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def clickbot():
	echo(f"%%%%%%% Installing... ClickBot", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ziziwho/clickbot')
	os.system("python -m pip install asyncio colorama telethon rsa pyaes asyncio async_generator colorama bs4 requests")
	os.system('mv clickbot {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def phoneinfoga():
	echo(f"%%%%%%% Installing... PhoneInfoga", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
	os.chdir("PhoneInfoga")
	os.system("python -m pip install -r requirements.txt")
	os.chdir("..")
	os.system('mv PhoneInfoga {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def btc2idr():
	echo(f"%%%%%%% Installing... BTC-to-IDR-checker", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/guruku/BTC-to-IDR-checker')
	os.system('mv BTC-to-IDR-checker {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def sitebroker():
	echo(f"%%%%%%% Installing... SiteBroker", foreground="vcyan")
	# secretum inc
	os.system('apt install python php git -y')
	os.system('git clone https://github.com/Anon-Exploiter/SiteBroker')
	os.chdir("SiteBroker")
	os.system('python -m pip install -r requirements.txt')
	os.system('python -m pip install html5lib')
	os.chdir("..")
	os.system('mv SiteBroker {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def dostattack():
	echo(f"%%%%%%% Installing... dost-attack", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/verluchie/dost-attack')
	os.system('mv dost-attack {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def cfr():
	echo(f"%%%%%%% Installing... CFR", foreground="vcyan")
	# secretum inc
	os.system('apt install dx wget -y')
	os.system('mkdir $PREFIX/bin/lib')
	os.system('wget https://www.benf.org/other/cfr/cfr-0.151.jar -O $PREFIX/bin/lib/cfr-0.151.jar')
	os.chdir(prefix+"/bin/lib")
	os.system('dx --dex --output=cfr-0.151.dex cfr-0.151.jar')
	with open(prefix+"/bin/cfr","w") as f:
		f.write("#!/usr/bin/bash\n")
		f.write("dalvikvm -cp $PREFIX/bin/lib/cfr-0.151.dex org/benf/cfr/reader/Main \"$@\"")
	os.system('chmod 755 $PREFIX/bin/cfr')
	os.system('chmod 755 $PREFIX/bin/lib/cfr-0.151.dex')
	os.chdir(current_dir)
	echo('###### Done')
	echo(f"###### Type 'cfr' to start.")
	backtomenu_option()

def upx():
	echo(f"%%%%%%% Installing... UPX", foreground="vcyan")
	# secretum inc
	os.system('apt install wget tar -y')
	os.system('wget https://github.com/upx/upx/releases/download/v3.96/upx-3.96-arm64_linux.tar.xz')
	os.system('tar xf upx-3.96-arm64_linux.tar.xz')
	os.system('mv upx-3.96-arm64_linux/upx $PREFIX/bin/upx')
	os.system('rm -rf upx-3.96-arm64_linux upx-3.96-arm64_linux.tar.xz')
	os.system('chmod 755 $PREFIX/bin/upx')
	echo('###### Done')
	echo(f"###### Type 'upx' to start.")
	backtomenu_option()

def pyinstxtractor():
	echo(f"%%%%%%% Installing... pyinstxtractor", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('git clone https://github.com/extremecoders-re/pyinstxtractor')
	os.system('mv pyinstxtractor {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def innoextract():
	echo(f"%%%%%%% Installing... innoextract", foreground="vcyan")
	# secretum inc
	os.system('apt install git clang -y')
	os.system('git clone https://github.com/dscharrer/innoextract')
	os.chdir("innoextract")
	os.system('mkdir -p build')
	os.chdir("build")
	os.system('cmake .. && make')
	os.system('mv innoextract $PREFIX/bin && chmod 755 $PREFIX/bin/innoextract')
	os.chdir(current_dir)
	os.system('rm -rf innoextract')
	echo('###### Done')
	echo(f"###### Type 'innoextract' to start.")
	backtomenu_option()

def lynis():
	echo(f"%%%%%%% Installing... Lynis", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/CISOfy/lynis')
	os.system('mv lynis {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def chkrootkit():
	echo(f"%%%%%%% Installing... Chkrootkit", foreground="vcyan")
	# secretum inc
	os.system('apt install clang git -y')
	os.system('git clone https://github.com/Magentron/chkrootkit')
	os.system('mv chkrootkit {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def clamav():
	echo(f"%%%%%%% Installing... ClamAV", foreground="vcyan")
	# secretum inc
	os.system('apt install clamav -y')
	os.system('freshclam')
	echo('###### Done')
	echo(f"###### Type 'clamscan' to start.")
	backtomenu_option()

def yara():
	echo(f"%%%%%%% Installing... Yara", foreground="vcyan")
	# secretum inc
	os.system('apt install yara -y')
	echo('###### Done')
	echo(f"###### Type 'yara' to start.")
	backtomenu_option()

def virustotal():
	echo(f"%%%%%%% Installing... VirusTotal-CLI", foreground="vcyan")
	# secretum inc
	os.system('apt install virustotal-cli -y')
	echo('###### Done')
	echo(f"###### Type 'vt' to start.")
	backtomenu_option()

def maigret():
	echo(f"%%%%%%% Installing... maigret", foreground="vcyan")
	# secretum inc
	os.system('apt install python -y')
	os.system('python -m pip install maigret')
	echo('###### Done')
	echo(f"###### Usage: maigret <username>")
	echo(f"###### Usage: maigret -h")
	backtomenu_option()

def xplsearch():
	echo(f"%%%%%%% Installing... XPL-SEARCH", foreground="vcyan")
	# secretum inc
	os.system('apt install git php -y')
	os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
	os.system('mv XPL-SEARCH {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def xadmin():
	echo(f"%%%%%%% Installing... Xadmin", foreground="vcyan")
	# secretum inc
	os.system('apt install git perl -y')
	os.system('git clone https://github.com/Manisso/Xadmin')
	os.system('mv Xadmin {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def credmap():
	echo(f"%%%%%%% Installing... Credmap", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/lightos/credmap')
	os.system('mv credmap {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def mapeye():
	echo(f"%%%%%%% Installing... MapEye", foreground="vcyan")
	# secretum inc
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	os.system('mv MapEye {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def gathetool():
	echo(f"%%%%%%% Installing... GatheTOOL", foreground="vcyan")
	# secretum inc
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	os.system('mv GatheTOOL {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def avpass():
	echo(f"%%%%%%% Installing... avpass", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 python -y')
	os.system('git clone https://github.com/sslab-gatech/avpass')
	os.system('mv avpass {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def binwalk():
	echo(f"%%%%%%% Installing... binwalk", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install gzip bzip2 tar arj lhasa p7zip cabextract sleuthkit lzop mtd-utils cmake build-essential make numpy scipy python git -y')
	os.system('git clone https://github.com/ReFirmLabs/binwalk')
	os.chdir("binwalk")
	os.system('python setup.py install')
	os.chdir("..")
	os.system('mv binwalk {}'.format(homeDir))
	echo('###### Done')
	echo(f"###### Type 'binwalk' to start.")
	backtomenu_option()

def arat():
	echo(f"%%%%%%% Installing... A-Rat", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/RexTheGod/A-Rat')
	os.system('mv A-Rat {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def adbtk():
	echo(f"%%%%%%% Installing... ADB-Toolkit", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	os.system('mv ADB-Toolkit {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def androbugs():
	echo(f"%%%%%%% Installing... AndroBugs_Framework", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install pymongo')
	os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
	os.system('mv AndroBugs_Framework {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def tekdefense():
	echo(f"%%%%%%% Installing... TekDefense-Automater", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	os.system('mv TekDefense-Automater {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def baf():
	echo(f"%%%%%%% Installing... BAF", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests bs4 selenium colored termcolor')
	os.system('git clone https://github.com/engMaher/BAF')
	os.system('mv BAF {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def brutex():
	echo(f"%%%%%%% Installing... BruteX", foreground="vcyan")
	# secretum inc
	os.system('apt install git hydra -y')
	os.system('git clone https://github.com/1N3/BruteX')
	os.system('mv BruteX {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def cmseek():
	echo(f"%%%%%%% Installing... CMSeeK", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/Tuhinshubhra/CMSeeK')
	os.system('mv CMSeeK {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

### Compiler/Interpreter
def python2():
	echo(f"%%%%%%% Installing... Python2", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 -y')
	echo('###### Done')
	echo(f"###### Type 'python2' to start.")
	backtomenu_option()

def ecj():
	echo(f"%%%%%%% Installing... ecj", foreground="vcyan")
	# secretum inc
	os.system('apt install ecj -y')
	echo('###### Done')
	echo(f"###### Type 'ecj' to start.")
	backtomenu_option()

def golang():
	echo(f"%%%%%%% Installing... Golang", foreground="vcyan")
	# secretum inc
	os.system('apt install golang -y')
	echo('###### Done')
	echo(f"###### Type 'go' to start.")
	backtomenu_option()

def ldc():
	echo(f"%%%%%%% Installing... ldc", foreground="vcyan")
	# secretum inc
	os.system('apt install ldc -y')
	echo('###### Done')
	echo(f"###### Type 'ldc2' to start.")
	backtomenu_option()

def nim():
	echo(f"%%%%%%% Installing... Nim", foreground="vcyan")
	# secretum inc
	os.system('apt install nim -y')
	echo('###### Done')
	echo(f"###### Type 'nim' to start.")
	backtomenu_option()

def shc():
	echo(f"%%%%%%% Installing... shc", foreground="vcyan")
	# secretum inc
	os.system('apt install shc -y')
	echo('###### Done')
	echo(f"###### Type 'shc' to start.")
	backtomenu_option()

def tcc():
	echo(f"%%%%%%% Installing... TCC", foreground="vcyan")
	# secretum inc
	os.system('apt install tcc -y')
	echo('###### Done')
	echo(f"###### Type 'tcc' to start.")
	backtomenu_option()

def php():
	echo(f"%%%%%%% Installing... PHP", foreground="vcyan")
	# secretum inc
	os.system('apt install php -y')
	echo('###### Done')
	echo(f"###### Type 'php' to start.")
	backtomenu_option()

def ruby():
	echo(f"%%%%%%% Installing... Ruby", foreground="vcyan")
	# secretum inc
	os.system('apt install ruby -y')
	echo('###### Done')
	echo(f"###### Type 'ruby' to start.")
	backtomenu_option()

def perl():
	echo(f"%%%%%%% Installing... Perl", foreground="vcyan")
	# secretum inc
	os.system('apt install perl -y')
	echo('###### Done')
	echo(f"###### Type 'perl' to start.")
	backtomenu_option()

def vlang():
	echo(f"%%%%%%% Installing... Vlang", foreground="vcyan")
	# secretum inc
	os.system('apt install vlang -y')
	echo('###### Done')
	echo(f"###### Type 'vlang' to start.")
	backtomenu_option()

def blogc():
	echo(f"%%%%%%% Installing... BlogC", foreground="vcyan")
	# secretum inc
	os.system('apt install blogc -y')
	echo('###### Done')
	echo(f"###### Type 'blogc' to start.")
	backtomenu_option()

### termux games
def street_car():
	echo(f"%%%%%%% Installing... street-car", foreground="vcyan")
	# secretum inc
	os.system('apt install git python python2 -y')
	os.system('git clone https://github.com/JustaHackers/street_car')
	os.system('mv street_car {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def flappy_bird():
	echo(f"%%%%%%% Installing... flappy-bird", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/flappy_bird')
	os.system('mv flappy_bird {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def speed_typing():
	echo(f"%%%%%%% Installing... Speed Typing", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/typing-speed-test')
	os.system('mv typing-speed-test {}'.format(homeDir))
	echo('###### Done')
	backtomenu_option()

def nsnake():
	echo(f"%%%%%%% Installing... nsnake", foreground="vcyan")
	# secretum inc
	os.system('apt install nsnake -y')
	echo('###### Done')
	echo(f"###### Type 'nsnake' to start.")
	backtomenu_option()

def nudoku():
	echo(f"%%%%%%% Installing... Sudoku", foreground="vcyan")
	# secretum inc
	os.system('apt install nudoku -y')
	echo('###### Done')
	echo(f"###### Type 'nudoku' to start.")
	backtomenu_option()

def moon_buggy():
	echo(f"%%%%%%% Installing... Moon-Buggy", foreground="vcyan")
	# secretum inc
	os.system('apt install moon-buggy -y')
	echo('###### Done')
	echo(f"###### Type 'moon-buggy' to start.")
	backtomenu_option()

def ttysolitaire():
	echo(f"%%%%%%% Installing... tty-solitaire", foreground="vcyan")
	# secretum inc
	os.system('apt install tty-solitaire -y')
	echo('###### Done')
	echo(f"###### Type 'ttysolitaire' to start.")
	backtomenu_option()

def pacman4console():
	echo(f"%%%%%%% Installing... Pacman4Console", foreground="vcyan")
	# secretum inc
	os.system('apt install pacman4console -y')
	echo('###### Done')
	echo(f"###### Type 'pacman' to start.")
	backtomenu_option()

### bash function ---
def fbvid():
	echo(f"%%%%%%% Installing... fbvid", foreground="vcyan")
	# secretum inc
	os.system('apt install python ffmpeg -y')
	os.system('python -m pip install youtube-dl')
	fbvid_code = open(".myshfunc/fbvid.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(fbvid_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	echo('###### Done')
	echo('###### Usage: fbvid "POST_URL"')
	backtomenu_option()

def cast2video():
	echo(f"%%%%%%% Installing... cast2video", foreground="vcyan")
	# secretum inc
	os.system('apt install clang python ffmpeg -y')
	os.system('python -m pip install CPython ttygif')
	cast2video_code = open(".myshfunc/cast2video.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(cast2video_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	echo('###### Done')
	echo('###### Usage: cast2video file.cast')
	backtomenu_option()

def iconset():
	echo(f"%%%%%%% Installing... iconset", foreground="vcyan")
	iconset_code = open(".myshfunc/iconset.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(iconset_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	echo('###### Done')
	echo('###### Usage: iconset project_name icon.png')
	backtomenu_option()

def readme():
	echo(f"%%%%%%% Installing... readme", foreground="vcyan")
	# secretum inc
	os.system('apt install curl -y')
	readme_code = open(".myshfunc/readme.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(readme_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	echo('###### Done')
	echo('###### Usage: readme User/Repo')
	backtomenu_option()

def makedeb():
	echo(f"%%%%%%% Installing... makedeb", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg neovim -y')
	makedeb_code = open(".myshfunc/makedeb.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(makedeb_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	echo('###### Done')
	echo('###### Usage: makedeb')
	backtomenu_option()

def quikfind():
	echo(f"%%%%%%% Installing... quikfind", foreground="vcyan")
	quikfind_code = open(".myshfunc/quikfind.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(quikfind_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	echo('###### Done')
	echo('###### Usage: quikfind')
	backtomenu_option()

def pranayama():
	echo(f"%%%%%%% Installing... pranayama", foreground="vcyan")
	# secretum inc
	os.system('apt install termux-api -y')
	pranayama_code = open(".myshfunc/pranayama.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(pranayama_code)
	os.system('source '+os.getenv("HOME")+"./bashrc")
	echo('###### Done')
	echo('###### Usage: pranayama')
	echo('######            or')
	echo('######        pranayama [n]')
	backtomenu_option()

def sqlc():
	echo(f"%%%%%%% Installing... sqlc", foreground="vcyan")
	# secretum inc
	os.system('apt install python sqlite3 -y')
	sqlc_code = open(".myshfunc/sqlc.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(sqlc_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	echo('###### Done')
	echo('###### Usage: sqlc db_file sql_script')
	backtomenu_option()
