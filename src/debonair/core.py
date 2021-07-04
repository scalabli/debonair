import os
import quo
import subprocess
import urllib.request
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

@quo.command()
@quo.app("--sources_list")
def repo_check(sources_list):
	if os.path.isfile(os.getenv("PREFIX")+"/etc/apt/sources.list.d/"+sources_list):
		return True
	return False

@quo.command()
@quo.app("--statusId")
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
		quo.flair(f'{_banner2}', foreground="red", bold=True) 
		backtomenu = quo.prompt("lzmx > ")
		
		if backtomenu == "99":
			restart_program()
		elif backtomenu == "00":
			sys.exit()
		else:
			quo.flair(f"ERROR: Wrong Input", foreground="red")
			time.sleep(2)
			restart_program()

def banner():
	quo.flair(f'{_banner}', foreground="yellow", bold=True) 

### Repo Installer
def pointless_repo():
	urllib.request.urlretrieve('https://github.com/secretum-inc/debonair/src/debonair/kickstart','kickstart')
	os.system('kickstart')
	os.remove('kickstart')
	os.system('apt update -y')
###

def nmap():
	quo.flair(f"%%%%%%% Installing... Nmap", foreground="vcyan") 
	# secretum inc
	os.system('apt install nmap')
	print('###### Done')
	quo.flair(f"###### Type 'nmap' to start.", foreground="red")
	backtomenu_option()

def red_hawk():
	quo.flair(f"%%%%%%% Installing... RED HAWK", foreground="vcyan") 
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dtect():
	quo.flair(f"%%%%%%% Installing... D-TECT", foreground="vcyan") 
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	os.system('mv D-Tech {}/D-TECT'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmap():
	quo.flair(f"%%%%%%% Installing... sqlmap", foreground="vcyan") 
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def infoga():
	quo.flair(f"%%%%%%% Installing... Infoga", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def reconDog():
	quo.flair(f"%%%%%%% Installing... ReconDog", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/ReconDog')
	os.system('mv ReconDog {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androZenmap():
	quo.flair(f"%%%%%%% Installing... AndroZenmap", foreground="vcyan")
	# secretum inc
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir {}/AndroZenmap'.format(homeDir))
	os.system('mv androzenmap.sh {}/AndroZenmap'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmate():
	quo.flair(f"%%%%%%% Installing... sqlmate", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/s0md3v/sqlmate')
	os.system('mv sqlmate {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def astraNmap():
	quo.flair(f"%%%%%%% Installing... AstraNmap", foreground="vcyan")
	# secretum inc
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def weeman():
	quo.flair(f"%%%%%%% Installing... weeman", foreground="vcyan")
	# secretum inc
	os.system('apt install clang git python2')
	os.system('python2 -m pip bs4 html5lib lxml')
	os.system('git clone https://github.com/evait-security/weeman')
	os.system('mv weeman {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def easyMap():
	quo.flair(f"%%%%%%% Installing... Easymap", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap {}'.format(homeDir))
	os.system('cd {}/Easymap && sh install.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xd3v():
	quo.flair(f"%%%%%%% Installing... XD3v", foreground="vcyan")
	# secretum inc
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh {0}/../usr/bin/xd3v && chmod +x {0}/../usr/bin/xd3v'.format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'xd3v' to start.")
	backtomenu_option()

def crips():
	quo.flair(f"%%%%%%% Installing... Crips", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sir():
	quo.flair(f"%%%%%%% Installing... SIR", foreground="vcyan")
	# secretum inxlc
	os.system("apt install python2 git")
	os.system("python2 -m pip install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def xshell():
	quo.flair(f"%%%%%%% Installing... Xshell", foreground="vcyan")
	# secretum inxlc
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def evilURL():
	quo.flair(f"%%%%%%% Installing... EvilURL", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def striker():
	quo.flair(f"%%%%%%% Installing... Striker", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/s0md3v/Striker')
	os.system('mv Striker {}'.format(homeDir))
	os.system('cd {}/Striker && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dsss():
	quo.flair(f"%%%%%%% Installing... DSSS", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqliv():
	quo.flair(f"%%%%%%% Installing... SQLiv", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/the-robot/sqliv')
	os.system('mv sqliv {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlscan():
	quo.flair(f"%%%%%%% Installing... sqlscan", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wordpreSScan():
	quo.flair(f"%%%%%%% Installing... Wordpresscan", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan {}'.format(homeDir))
	os.system('cd {}/Wordpresscan && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wpscan():
	quo.flair(f"%%%%%%% Installing... WPScan", foreground="vcyan")
	# secretum inc
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan {0} && cd {0}/wpscan'.format(homeDir))
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print('###### Done')
	backtomenu_option()

def wordpresscan():
	quo.flair(f"%%%%%%% Installing... wordpresscan(2)", foreground="vcyan")
	# secretum inc
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan {}'.format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'wordpresscan' to start.")
	backtomenu_option()

def routersploit():
	quo.flair(f"%%%%%%% Installing... Routersploit", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/threat9/routersploit')
	os.system('mv routersploit {0};cd {0}/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def torshammer():
	quo.flair(f"%%%%%%% Installing... Torshammer", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def slowloris():
	quo.flair(f"%%%%%%% Installing... Slowloris", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fl00d12():
	quo.flair(f"%%%%%%% Installing... Fl00d & Fl00d2", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 curl')
	os.system('mkdir {}/fl00d'.format(homeDir))
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	os.system('mv fl00d.py {0}/fl00d && mv fl00d2.py {0}/fl00d'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def goldeneye():
	quo.flair(f"%%%%%%% Installing... GoldenEye", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xerxes():
	quo.flair(f"%%%%%%% Installing... Xerxes", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/baraalmasri/xerxes')
	os.system('mv xerxes {}'.format(homeDir))
	os.system('cd {}/xerxes && clang xerxes.c -o xerxes'.format(homeDir))
	os.system('chmod 755 {0}/xerxes/xerxes && cp {0}/xerxes/xerxes $PREFIX/bin'.format(homeDir))
	print('###### Done')
	print('###### Usage: xerxes ​www.fakesite.com​ 80')
	backtomenu_option()

def planetwork_ddos():
	quo.flair(f"%%%%%%% Installing... Planetwork-DDOS", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hydra():
	quo.flair(f"%%%%%%% Installing... Hydra", foreground="vcyan")
	# secretum inc
	os.system('apt install hydra')
	print('###### Done')
	backtomenu_option()

def black_hydra():
	quo.flair(f"%%%%%%% Installing... Black Hydra", foreground="vcyan")
	# secretum inc
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cupp():
	quo.flair(f"%%%%%%% Installing... Cupp", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def asu():
	quo.flair(f"%%%%%%% Installing... ASU", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hash_buster():
	quo.flair(f"%%%%%%% Installing... Hash-Buster", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/Hash-Buster')
	os.system('mv Hash-Buster {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def instaHack():
	quo.flair(f"%%%%%%% Installing... InstaHack", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Slayeri4/instahack')
	os.system('mv instahack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def indonesian_wordlist():
	quo.flair(f"%%%%%%% Installing... indonesian-wordlist", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	os.system('mv indonesian-wordlist {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fbBrute():
	quo.flair(f"%%%%%%% Installing... Facebook Brute Force 3", foreground="vcyan")
	# secretum inc
	os.system('apt install curl python2')
	os.system('python2 -m pip install mechanize')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt')
	os.system('mkdir {}/facebook-brute-3'.format(homeDir))
	os.system('mv facebook3.py {0}/facebook-brute-3 && mv password.txt {0}/facebook-brute-3'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def webdav():
	quo.flair(f"%%%%%%% Installing... WebDAV", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 openssl curl libcurl')
	os.system('python2 -m pip install urllib3 chardet certifi idna requests')
	os.system('mkdir {}/webdav'.format(homeDir))
	os.system('curl -k -O https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR {}/webdav/webdav.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def webmassploit():
	quo.flair(f"%%%%%%% Installing... Webdav Mass Exploiter", foreground="vcyan")
	# secretum inxlc
	os.system("apt install python2 openssl curl libcurl")
	os.system("python2 -m pip install requests")
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir {0}/webdav-mass-exploit && mv webdav.py {0}/webdav-mass-exploit".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqldump():
	quo.flair(f"%%%%%%% Installing... sqldump", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 curl')
	os.system('python2 -m pip install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir {0}/sqldump && chmod +x sqldump.py && mv sqldump.py {0}/sqldump'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def websploit():
	quo.flair(f"%%%%%%% Installing... Websploit", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def metasploit():
	quo.flair(f"%%%%%%% Installing... Metasploit", foreground="vcyan")
	# secretum inxlc
	os.system("apt install unstable-repo")
	os.system("cd {} && apt install metasploit".format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'msfconsole' to start.")
	backtomenu_option()

def commix():
	quo.flair(f"%%%%%%% Installing... Commix", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutal():
	quo.flair(f"%%%%%%% Installing... Brutal", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def knockmail():
	quo.flair(f"%%%%%%% Installing... KnockMail", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hac():
	quo.flair(f"%%%%%%% Installing... Hac", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rang3r():
	quo.flair(f"%%%%%%% Installing... Rang3r", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sh33ll():
	quo.flair(f"%%%%%%% Installing... SH33LL", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def social():
	quo.flair(f"%%%%%%% Installing... Social-Engineering", foreground="vcyan")
	# secretum inxlc
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def spiderbot():
	quo.flair(f"%%%%%%% Installing... SpiderBot", foreground="vcyan")
	# secretum inxlc
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def ngrok():
	quo.flair(f"%%%%%%% Installing... Ngrok", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sudo():
	quo.flair(f"%%%%%%% Installing... sudo", foreground="vcyan")
	# secretum inc
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo {0} && cd {0}/termux-sudo && chmod 777 *'.format(homeDir))
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print('###### Done')
	backtomenu_option()

def ubuntu():
	quo.flair(f"%%%%%%% Installing... Ubuntu", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu {0} && cd {0}/termux-ubuntu && bash ubuntu.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fedora():
	quo.flair(f"%%%%%%% Installing... Fedora", foreground="vcyan")
	# secretum inc
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nethunter():
	quo.flair(f"%%%%%%% Installing... Kali NetHunter", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def blackbox():
	quo.flair(f"%%%%%%% Installing... BlackBox", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xattacker():
	quo.flair(f"%%%%%%% Installing... XAttacker", foreground="vcyan")
	# secretum inc
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vcrt():
	quo.flair(f"%%%%%%% Installing... VCRT", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def socfish():
	quo.flair(f"%%%%%%% Installing... SocialFish", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ecode():
	quo.flair(f"%%%%%%% Installing... ECode", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xsstrike():
	quo.flair(f"%%%%%%% Installing... XSStrike", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/s0md3v/XSStrike')
	os.system('mv XSStrike {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def breacher():
	quo.flair(f"%%%%%%% Installing... Breacher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests argparse')
	os.system('git clone https://github.com/s0md3v/Breacher')
	os.system('mv Breacher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def stylemux():
	quo.flair(f"%%%%%%% Installing... Termux-Styling", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def txtool():
	quo.flair(f"%%%%%%% Installing... TXTool", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def passgencvar():
	quo.flair(f"%%%%%%% Installing... PassGen", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def owscan():
	quo.flair(f"%%%%%%% Installing... OWScan", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sanlen():
	quo.flair(f"%%%%%%% Installing... santet-online", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def spazsms():
	quo.flair(f"%%%%%%% Installing... SpazSMS", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasher():
	quo.flair(f"%%%%%%% Installing... Hasher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install passlib binascii progressbar')
	os.system('git clone https://github.com/CiKu370/hasher')
	os.system('mv hasher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashgenerator():
	quo.flair(f"%%%%%%% Installing... Hash-Generator", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/CiKu370/hash-generator')
	os.system('mv hash-generator {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kodork():
	quo.flair(f"%%%%%%% Installing... ko-dork", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/CiKu370/ko-dork')
	os.system('mv ko-dork {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def snitch():
	quo.flair(f"%%%%%%% Installing... snitch", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def osif():
	quo.flair(f"%%%%%%% Installing... OSIF", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/CiKu370/OSIF')
	os.system('mv OSIF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nk26():
	quo.flair(f"%%%%%%% Installing... nk26", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/milio48/nk26')
	os.system('mv nk26 {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def devploit():
	quo.flair(f"%%%%%%% Installing... Devploit", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasherdotid():
	quo.flair(f"%%%%%%% Installing... Hasherdotid", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	os.system('mv hasherdotid {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def namechk():
	quo.flair(f"%%%%%%% Installing... Namechk", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xlPy():
	quo.flair(f"%%%%%%% Installing... xl-py", foreground="vcyan")
	# secretum inc
	os.system('apt install python git')
	os.system('git clone https://github.com/albertoanggi/xl-py')
	os.system('mv xl-py {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def beanshell():
	quo.flair(f"%%%%%%% Installing... Beanshell", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'bsh' to start.")
	backtomenu_option()

def crunch():
	quo.flair(f"%%%%%%% Installing... Crunch", foreground="vcyan")
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'crunch' to start.")
	backtomenu_option()

def binploit():
	quo.flair(f"%%%%%%% Installing... Binary Exploitation", foreground="vcyan")
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	quo.flair(f"###### Done")
	quo.flair(f"###### Tutorial: https://youtu.be/3NTXFUxcKPc")
	backtomenu_option()

def textr():
	quo.flair(f"%%%%%%% Installing... Textr", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'textr' to start.")
	backtomenu_option()

def apsca():
	quo.flair(f"%%%%%%% Installing... ApSca", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'apsca' to start.")
	backtomenu_option()

def amox():
	quo.flair(f"%%%%%%% Installing... amox", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'amox' to start.")
	backtomenu_option()

def fade():
	quo.flair(f"%%%%%%% Installing... FaDe", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FaDe')
	os.system('mv FaDe {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ginf():
	quo.flair(f"%%%%%%% Installing... GINF", foreground="vcyan")
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def auxile():
	quo.flair(f"%%%%%%% Installing... AUXILE", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def inther():
	quo.flair(f"%%%%%%% Installing... inther", foreground="vcyan")
	# secretum inc
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hpb():
	quo.flair(f"%%%%%%% Installing... HPB", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'hpb' to start.")
	backtomenu_option()

def fmbrute():
	quo.flair(f"%%%%%%% Installing... FMBrute", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FMBrute')
	os.system('mv FMBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashid():
	quo.flair(f"%%%%%%% Installing... HashID", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 && python2 -m pip install hashid')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'hashid -h' to show usage of hashid")
	backtomenu_option()

def gpstr():
	quo.flair(f"%%%%%%% Installing... GPS Tracking", foreground="vcyan")
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	os.system('mv gps_tracking {}'.format(homeDir))
	quo.flair(f"###### Done")
	backtomenu_option()

def pret():
	quo.flair(f"%%%%%%% Installing... PRET", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 imagemagick git')
	os.system('python2 -m pip install colorama pysnmp')
	os.system('git clone https://github.com/RUB-NDS/PRET')
	os.system('mv PRET {}'.format(homeDir))
	quo.flair(f"###### Done")
	backtomenu_option()

def atlas():
	quo.flair(f"%%%%%%% Installing... Atlas", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/m4ll0k/Atlas')
	os.system('mv Atlas {}'.format(homeDir))
	quo.flair(f"###### Done")
	backtomenu_option()

def hashcat():
	quo.flair(f"%%%%%%% Installing... Hashcat", foreground="vcyan")
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'hashcat' to start.")
	backtomenu_option()

def liteotp():
	quo.flair(f"%%%%%%% Installing... LiteOTP", foreground="vcyan")
	# secretum inc
	os.system('apt install php wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'lite' to start.")
	backtomenu_option()

def fbbrutex():
	quo.flair(f"%%%%%%% Installing... FBBrute", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FBBrute')
	os.system('mv FBBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fim():
	quo.flair(f"%%%%%%% Installing... fim", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	os.system('mv fim {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rshell():
	quo.flair(f"%%%%%%% Installing... RShell", foreground="vcyan")
	# secretum inc
	os.system('apt install git python && python -m pip install colorama')
	os.system('git clone https://github.com/Jishu-Epic/RShell')
	os.system('mv RShell {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def termpyter():
	quo.flair(f"%%%%%%% Installing... TermPyter", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Jishu-Epic/TermPyter')
	os.system('mv TermPyter {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maxsubdofinder():
	quo.flair(f"%%%%%%% Installing... MaxSubdoFinder", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	os.system('mv MaxSubdoFinder {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def jadx():
	quo.flair(f"%%%%%%% Installing... jadx", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
	os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
	os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	print('###### Done')
	quo.flair(f"###### Type 'jadx' to start.")
	backtomenu_option()

def pwnedornot():
	quo.flair(f"%%%%%%% Installing... pwnedOrNot", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	os.system('mv pwnedOrNot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maclook():
	quo.flair(f"%%%%%%% Installing... Mac-Lookup", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	os.system('mv Mac-Lookup {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def f4k3():
	quo.flair(f"%%%%%%% Installing... F4K3", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Gameye98/Gameye98.github.io/blob/master/package/f4k3_1.0_all.deb')
	os.system('dpkg -i f4k3_1.0_all.deb')
	os.system('rm -rf f4k3_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'f4k3' to start.")
	backtomenu_option()

def katak():
	quo.flair(f"%%%%%%% Installing... Katak", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests progressbar')
	os.system('git clone https://github.com/Gameye98/Katak')
	os.system('mv Katak {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def heroku():
	quo.flair(f"%%%%%%% Installing... heroku", foreground="vcyan")
	# secretum inc
	os.system('apt install nodejs')
	os.system('npm install heroku -g')
	print('###### Done')
	quo.flair(f"###### Type 'heroku' to start.")
	backtomenu_option()

def google():
	quo.flair(f"%%%%%%% Installing... google", foreground="vcyan")
	# secretum inc
	os.system('apt install python')
	os.system('python -m pip install google')
	print('###### Done')
	quo.flair(f"###### Type 'google' to start.")
	backtomenu_option()

def billcypher():
	quo.flair(f"%%%%%%% Installing... BillCypher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install argparse dnspython requests urllib3 colorama')
	os.system('git clone https://github.com/GitHackTools/BillCipher')
	os.system('mv BillCypher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vbug():
	quo.flair(f"%%%%%%% Installing... vbug", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Gameye98/vbug')
	os.system('mv vbug {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kojawafft():
	quo.flair(f"%%%%%%% Installing... kojawafft", foreground="vcyan")
	# secretum inc
	os.system('apt install git nodejs')
	os.system('git clone https://github.com/sandalpenyok/kojawafft')
	os.system('mv kojawafft {}'.format(homeDir))
	os.system('cd $HOME/kojawafft && unzip node_modules.zip && cd -')
	print('###### Done')
	backtomenu_option()

def aircrackng():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		quo.flair(f"%%%%%%% Installing... aircrack-ng", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo aircrack-ng')
		print('###### Done')
		quo.flair(f"###### Type 'aircrack-ng' to start.")
	backtomenu_option()

def ettercap():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		quo.flair(f"%%%%%%% Installing... ettercap", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo ettercap')
		print('###### Done')
		quo.flair(f"###### Type 'ettercap' to start.")
	backtomenu_option()

def ccgen():
	quo.flair(f"%%%%%%% Installing... ccgen", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ccgen')
	os.system('mv ccgen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ddcrypt():
	quo.flair(f"%%%%%%% Installing... ddcrypt", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ddcrypt')
	os.system('mv ddcrypt {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dnsrecon():
	quo.flair(f"%%%%%%% Installing... dnsrecon", foreground="vcyan")
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/darkoperator/dnsrecon')
	os.system('python -m pip install -r dnsrecon/requirements.txt')
	os.system('mv dnsrecon {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def zphisher():
	quo.flair(f"%%%%%%% Installing... zphisher", foreground="vcyan")
	# secretum inc
	os.system('apt install git php openssh curl')
	os.system('git clone https://github.com/htr-tech/zphisher')
	os.system('mv zphisher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def apktool():
	quo.flair(f"%%%%%%% Installing... apktool", foreground="vcyan")
	# secretum inc
	os.system('apt install git dpkg')
	os.system('git clone https://github.com/Lexiie/Termux-Apktool')
	os.system('mv Termux-Apktool {}'.format(homeDir))
	os.system('cd {}/Termux-Apktool && dpkg -i *.deb'.format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'apktool' to start.")
	backtomenu_option()

def uncompyle():
	quo.flair(f"%%%%%%% Installing... uncompyle6", foreground="vcyan")
	# secretum inc
	os.system('apt install python python2')
	os.system('python2 -m pip install uncompyle6')
	os.system('mv $PREFIX/bin/uncompyle6 $PREFIX/bin/uncompyle')
	os.system('python -m pip install uncompyle6')
	print('###### Done')
	print('###### (py2) Usage: uncompyle')
	print('###### (py3) Usage: uncompyle6')
	backtomenu_option()

def wifite():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		quo.flair(f"%%%%%%% Installing... Wifite", foreground="vcyan")
		# secretum inc
		os.system('apt install git python2')
		os.system('git clone https://github.com/derv82/wifite')
		os.system('mv wifite {}'.format(homeDir))
		print('###### Done')
	backtomenu_option()

def parrot():
	quo.flair(f"%%%%%%% Installing... Parrot", foreground="vcyan")
	# secretum inc
	os.system('apt install wget openssl-tool proot -y && hash -r && cd {} && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Parrot/parrot.sh && bash parrot.sh'.format(homeDir))
	os.system('cd {} && bash start-parrot.sh'.format(homeDir))
	print('###### Done')
	print('###### Make sure visit: https://techriz.com/how-to-install-parrot-linux-on-android-without-root/')
	os.system('am start -a android.intent.action.VIEW -d "https://techriz.com/how-to-install-parrot-linux-on-android-without-root/"')
	backtomenu_option()

def archlinux():
	quo.flair(f"%%%%%%% Installing... Arch Linux", foreground="vcyan")
	# secretum inc
	os.system('apt install git')
	os.system('cd $HOME && git clone https://github.com/sdrausty/TermuxArch')
	os.system('cd $HOME && bash TermuxArch/setupTermuxArch.sh')
	print('###### Done')
	backtomenu_option()

def tshark():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		quo.flair(f"%%%%%%% Installing... tshark", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo tshark')
		print('###### Done')
		quo.flair(f"###### Type 'tshark' to start.")
	backtomenu_option()

def dos2unix():
	quo.flair(f"%%%%%%% Installing... dos2unix", foreground="vcyan")
	# secretum inc
	os.system('apt install dos2unix')
	print('###### Done')
	quo.flair(f"###### Type 'dos2unix' to start.")
	backtomenu_option()

def exiftool():
	quo.flair(f"%%%%%%% Installing... exiftool", foreground="vcyan")
	# secretum inc
	os.system('apt install exiftool')
	print('###### Done')
	quo.flair(f"###### Type 'exiftool' to start.")
	backtomenu_option()

def iconv():
	quo.flair(f"%%%%%%% Installing... iconv", foreground="vcyan")
	# secretum inc
	os.system('apt install iconv')
	print('###### Done')
	quo.flair(f"###### Type 'iconv' to start.")
	backtomenu_option()

def mediainfo():
	quo.flair(f"%%%%%%% Installing... mediainfo", foreground="vcyan")
	# secretum inc
	os.system('apt install mediainfo')
	print('###### Done')
	print('###### Usage: mediainfo filename.pdf')
	backtomenu_option()

def pdfinfo():
	quo.flair(f"%%%%%%% Installing... pdfinfo", foreground="vcyan")
	# secretum inc
	os.system('apt install poppler')
	print('###### Done')
	print('###### Usage: pdfinfo filename.pdf')
	backtomenu_option()

def tcpdump():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		quo.flair(f"%%%%%%% Installing... tcpdump", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo tcpdump')
		print('###### Done')
		quo.flair(f"###### Type 'tcpdump' to start.")
	backtomenu_option()

def hping3():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		quo.flair(f"%%%%%%% Installing... hping3", foreground="vcyan")
		# secretum inc
		os.system('apt install root-repo hping3')
		print('###### Done')
		quo.flair(f"###### Type 'hping3' to start.")
	backtomenu_option()

def dbdat():
	quo.flair(f"%%%%%%% Installing... DbDat", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install MySQL-python psycopg2 cx_Oracle pymssql ibm_db pymongo pyyaml couchdb')
	os.system('git clone https://github.com/foospidy/DbDat')
	os.system('mv DbDat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nosqlmap():
	quo.flair(f"%%%%%%% Installing... NoSQLMap", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 unstable-repo metasploit')
	os.system('python2 -m pip install pymongo httplib2')
	os.system('git clone https://github.com/codingo/NoSQLMap')
	os.system('mv NoSQLMap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def audit_couchdb():
	quo.flair(f"%%%%%%% Installing... audit_couchdb", foreground="vcyan")
	# secretum inc
	os.system('apt install git nodejs')
	os.system('npm install -g npm@next audit_couchdb')
	os.system('git clone https://github.com/iriscouch/audit_couchdb')
	os.system('mv audit_couchdb {}'.format(homeDir))
	print('###### Done')
	print('###### Usage: audit_couchdb https://admin:secret@localhost:5984')
	backtomenu_option()

def mongoaudit():
	quo.flair(f"%%%%%%% Installing... mongoaudit", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install pymongo mongoaudit')
	print('###### Done')
	quo.flair(f"###### Type 'mongoaudit' to start.")
	backtomenu_option()

def wifiphisher():
	quo.flair(f"%%%%%%% Installing... Wifiphisher", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install setuptools scapy')
	os.system('git clone https://github.com/wifiphisher/wifiphisher')
	os.system('mv wifiphisher {0} && cd {0}/wifiphisher && python setup.py install'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sherlock():
	quo.flair(f"%%%%%%% Installing... sherlock", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('git clone https://github.com/sherlock-project/sherlock')
	os.system('mv sherlock {0} && cd {0}/sherlock && python -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def shc():
	quo.flair(f"%%%%%%% Installing... shc", foreground="vcyan")
	# secretum inc
	os.system('apt install shc -y')
	print('###### Done')
	quo.flair(f"###### Type 'shc' to start.")
	backtomenu_option()

def steghide():
	quo.flair(f"%%%%%%% Installing... steghide", foreground="vcyan")
	# secretum inc
	os.system('apt install steghide -y')
	print('###### Done')
	quo.flair(f"###### Type 'steghide' to start.")
	backtomenu_option()

def tesseract():
	quo.flair(f"%%%%%%% Installing... tesseract", foreground="vcyan")
	# secretum inc
	os.system('apt install tesseract -y')
	print('###### Done')
	quo.flair(f"###### Type 'tesseract' to start.")
	backtomenu_option()

def sleuthkit():
	quo.flair(f"%%%%%%% Installing... sleuthkit", foreground="vcyan")
	# secretum inc
	os.system('apt install sleuthkit -y')
	print('###### Done')
	quo.flair(f"###### Type 'pkg files sleuthkit | grep usr/bin' to check executable file related to sleuthkit package.")
	backtomenu_option()

def octave():
	quo.flair(f"%%%%%%% Installing... Octave", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install octave -y')
	print('###### Done')
	quo.flair(f"###### Type 'octave' to start.")
	backtomenu_option()

def fpcompiler():
	quo.flair(f"%%%%%%% Installing... fp-compiler", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install fp-compiler -y')
	print('###### Done')
	quo.flair(f"###### Type 'fpc' to start.")
	backtomenu_option()

def numpy():
	quo.flair(f"%%%%%%% Installing... numpy", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install numpy -y')
	print('###### Done')
	quo.flair(f"###### Type 'pkg files numpy | grep usr/bin' to check executable file related to numpy package.")
	backtomenu_option()

def userrecon():
	quo.flair(f"%%%%%%% Installing... userrecon", foreground="vcyan")
	# secretum inc
	os.system('apt install wget dpkg curl -y')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	os.system('dpkg -i userrecon_1.0_all.deb')
	os.system('rm userrecon_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'userrecon' to start.")
	backtomenu_option()

def mrsip():
	quo.flair(f"%%%%%%% Installing... Mr.SIP", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	os.system('git clone https://github.com/meliht/Mr.SIP')
	os.system('mv Mr.SIP {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tmscanner():
	quo.flair(f"%%%%%%% Installing... TM-scanner", foreground="vcyan")
	# secretum inc
	os.system('apt install python python2 nmap git -y')
	os.system('python -m pip install colorama requests')
	os.system('python2 -m pip install colorama requests')
	os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
	os.system('mv TM-scanner {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xss_payload_list():
	quo.flair(f"%%%%%%% Installing... xss-payload-list", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/payloadbox/xss-payload-list')
	os.system('mv xss-payload-list {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clickbot():
	quo.flair(f"%%%%%%% Installing... ClickBot", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ziziwho/clickbot')
	os.system("python -m pip install asyncio colorama telethon rsa pyaes asyncio async_generator colorama bs4 requests")
	os.system('mv clickbot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def phoneinfoga():
	quo.flair(f"%%%%%%% Installing... PhoneInfoga", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
	os.chdir("PhoneInfoga")
	os.system("python -m pip install -r requirements.txt")
	os.chdir("..")
	os.system('mv PhoneInfoga {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def btc2idr():
	quo.flair(f"%%%%%%% Installing... BTC-to-IDR-checker", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/guruku/BTC-to-IDR-checker')
	os.system('mv BTC-to-IDR-checker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sitebroker():
	quo.flair(f"%%%%%%% Installing... SiteBroker", foreground="vcyan")
	# secretum inc
	os.system('apt install python php git -y')
	os.system('git clone https://github.com/Anon-Exploiter/SiteBroker')
	os.chdir("SiteBroker")
	os.system('python -m pip install -r requirements.txt')
	os.system('python -m pip install html5lib')
	os.chdir("..")
	os.system('mv SiteBroker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dostattack():
	quo.flair(f"%%%%%%% Installing... dost-attack", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/verluchie/dost-attack')
	os.system('mv dost-attack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cfr():
	quo.flair(f"%%%%%%% Installing... CFR", foreground="vcyan")
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
	print('###### Done')
	quo.flair(f"###### Type 'cfr' to start.")
	backtomenu_option()

def upx():
	quo.flair(f"%%%%%%% Installing... UPX", foreground="vcyan")
	# secretum inc
	os.system('apt install wget tar -y')
	os.system('wget https://github.com/upx/upx/releases/download/v3.96/upx-3.96-arm64_linux.tar.xz')
	os.system('tar xf upx-3.96-arm64_linux.tar.xz')
	os.system('mv upx-3.96-arm64_linux/upx $PREFIX/bin/upx')
	os.system('rm -rf upx-3.96-arm64_linux upx-3.96-arm64_linux.tar.xz')
	os.system('chmod 755 $PREFIX/bin/upx')
	print('###### Done')
	quo.flair(f"###### Type 'upx' to start.")
	backtomenu_option()

def pyinstxtractor():
	quo.flair(f"%%%%%%% Installing... pyinstxtractor", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('git clone https://github.com/extremecoders-re/pyinstxtractor')
	os.system('mv pyinstxtractor {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def innoextract():
	quo.flair(f"%%%%%%% Installing... innoextract", foreground="vcyan")
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
	print('###### Done')
	quo.flair(f"###### Type 'innoextract' to start.")
	backtomenu_option()

def lynis():
	quo.flair(f"%%%%%%% Installing... Lynis", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/CISOfy/lynis')
	os.system('mv lynis {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def chkrootkit():
	quo.flair(f"%%%%%%% Installing... Chkrootkit", foreground="vcyan")
	# secretum inc
	os.system('apt install clang git -y')
	os.system('git clone https://github.com/Magentron/chkrootkit')
	os.system('mv chkrootkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clamav():
	quo.flair(f"%%%%%%% Installing... ClamAV", foreground="vcyan")
	# secretum inc
	os.system('apt install clamav -y')
	os.system('freshclam')
	print('###### Done')
	quo.flair(f"###### Type 'clamscan' to start.")
	backtomenu_option()

def yara():
	quo.flair(f"%%%%%%% Installing... Yara", foreground="vcyan")
	# secretum inc
	os.system('apt install yara -y')
	print('###### Done')
	quo.flair(f"###### Type 'yara' to start.")
	backtomenu_option()

def virustotal():
	quo.flair(f"%%%%%%% Installing... VirusTotal-CLI", foreground="vcyan")
	# secretum inc
	os.system('apt install virustotal-cli -y')
	print('###### Done')
	quo.flair(f"###### Type 'vt' to start.")
	backtomenu_option()

def maigret():
	quo.flair(f"%%%%%%% Installing... maigret", foreground="vcyan")
	# secretum inc
	os.system('apt install python -y')
	os.system('python -m pip install maigret')
	print('###### Done')
	quo.flair(f"###### Usage: maigret <username>")
	quo.flair(f"###### Usage: maigret -h")
	backtomenu_option()

def xplsearch():
	quo.flair(f"%%%%%%% Installing... XPL-SEARCH", foreground="vcyan")
	# secretum inc
	os.system('apt install git php -y')
	os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
	os.system('mv XPL-SEARCH {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xadmin():
	quo.flair(f"%%%%%%% Installing... Xadmin", foreground="vcyan")
	# secretum inc
	os.system('apt install git perl -y')
	os.system('git clone https://github.com/Manisso/Xadmin')
	os.system('mv Xadmin {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def credmap():
	quo.flair(f"%%%%%%% Installing... Credmap", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/lightos/credmap')
	os.system('mv credmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def mapeye():
	quo.flair(f"%%%%%%% Installing... MapEye", foreground="vcyan")
	# secretum inc
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	os.system('mv MapEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gathetool():
	quo.flair(f"%%%%%%% Installing... GatheTOOL", foreground="vcyan")
	# secretum inc
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	os.system('mv GatheTOOL {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def avpass():
	quo.flair(f"%%%%%%% Installing... avpass", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 python -y')
	os.system('git clone https://github.com/sslab-gatech/avpass')
	os.system('mv avpass {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def binwalk():
	quo.flair(f"%%%%%%% Installing... binwalk", foreground="vcyan")
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install gzip bzip2 tar arj lhasa p7zip cabextract sleuthkit lzop mtd-utils cmake build-essential make numpy scipy python git -y')
	os.system('git clone https://github.com/ReFirmLabs/binwalk')
	os.chdir("binwalk")
	os.system('python setup.py install')
	os.chdir("..")
	os.system('mv binwalk {}'.format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'binwalk' to start.")
	backtomenu_option()

def arat():
	quo.flair(f"%%%%%%% Installing... A-Rat", foreground="vcyan")
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/RexTheGod/A-Rat')
	os.system('mv A-Rat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def adbtk():
	quo.flair(f"%%%%%%% Installing... ADB-Toolkit", foreground="vcyan")
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	os.system('mv ADB-Toolkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androbugs():
	quo.flair(f"%%%%%%% Installing... AndroBugs_Framework", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install pymongo')
	os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
	os.system('mv AndroBugs_Framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tekdefense():
	quo.flair(f"%%%%%%% Installing... TekDefense-Automater", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	os.system('mv TekDefense-Automater {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def baf():
	quo.flair(f"%%%%%%% Installing... BAF", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests bs4 selenium colored termcolor')
	os.system('git clone https://github.com/engMaher/BAF')
	os.system('mv BAF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutex():
	quo.flair(f"%%%%%%% Installing... BruteX", foreground="vcyan")
	# secretum inc
	os.system('apt install git hydra -y')
	os.system('git clone https://github.com/1N3/BruteX')
	os.system('mv BruteX {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cmseek():
	quo.flair(f"%%%%%%% Installing... CMSeeK", foreground="vcyan")
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/Tuhinshubhra/CMSeeK')
	os.system('mv CMSeeK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

### Compiler/Interpreter
def python2():
	quo.flair(f"%%%%%%% Installing... Python2", foreground="vcyan")
	# secretum inc
	os.system('apt install python2 -y')
	print('###### Done')
	quo.flair(f"###### Type 'python2' to start.")
	backtomenu_option()

def ecj():
	quo.flair(f"%%%%%%% Installing... ecj", foreground="vcyan")
	# secretum inc
	os.system('apt install ecj -y')
	print('###### Done')
	quo.flair(f"###### Type 'ecj' to start.")
	backtomenu_option()

def golang():
	quo.flair(f"%%%%%%% Installing... Golang", foreground="vcyan")
	# secretum inc
	os.system('apt install golang -y')
	print('###### Done')
	quo.flair(f"###### Type 'go' to start.")
	backtomenu_option()

def ldc():
	quo.flair(f"%%%%%%% Installing... ldc", foreground="vcyan")
	# secretum inc
	os.system('apt install ldc -y')
	print('###### Done')
	quo.flair(f"###### Type 'ldc2' to start.")
	backtomenu_option()

def nim():
	quo.flair(f"%%%%%%% Installing... Nim", foreground="vcyan")
	# secretum inc
	os.system('apt install nim -y')
	print('###### Done')
	quo.flair(f"###### Type 'nim' to start.")
	backtomenu_option()

def shc():
	quo.flair(f"%%%%%%% Installing... shc", foreground="vcyan")
	# secretum inc
	os.system('apt install shc -y')
	print('###### Done')
	quo.flair(f"###### Type 'shc' to start.")
	backtomenu_option()

def tcc():
	quo.flair(f"%%%%%%% Installing... TCC", foreground="vcyan")
	# secretum inc
	os.system('apt install tcc -y')
	print('###### Done')
	quo.flair(f"###### Type 'tcc' to start.")
	backtomenu_option()

def php():
	quo.flair(f"%%%%%%% Installing... PHP", foreground="vcyan")
	# secretum inc
	os.system('apt install php -y')
	print('###### Done')
	quo.flair(f"###### Type 'php' to start.")
	backtomenu_option()

def ruby():
	quo.flair(f"%%%%%%% Installing... Ruby", foreground="vcyan")
	# secretum inc
	os.system('apt install ruby -y')
	print('###### Done')
	quo.flair(f"###### Type 'ruby' to start.")
	backtomenu_option()

def perl():
	quo.flair(f"%%%%%%% Installing... Perl", foreground="vcyan")
	# secretum inc
	os.system('apt install perl -y')
	print('###### Done')
	quo.flair(f"###### Type 'perl' to start.")
	backtomenu_option()

def vlang():
	quo.flair(f"%%%%%%% Installing... Vlang", foreground="vcyan")
	# secretum inc
	os.system('apt install vlang -y')
	print('###### Done')
	quo.flair(f"###### Type 'vlang' to start.")
	backtomenu_option()

def blogc():
	quo.flair(f"%%%%%%% Installing... BlogC", foreground="vcyan")
	# secretum inc
	os.system('apt install blogc -y')
	print('###### Done')
	quo.flair(f"###### Type 'blogc' to start.")
	backtomenu_option()

### termux games
def street_car():
	quo.flair(f"%%%%%%% Installing... street-car", foreground="vcyan")
	# secretum inc
	os.system('apt install git python python2 -y')
	os.system('git clone https://github.com/JustaHackers/street_car')
	os.system('mv street_car {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def flappy_bird():
	quo.flair(f"%%%%%%% Installing... flappy-bird", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/flappy_bird')
	os.system('mv flappy_bird {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def speed_typing():
	quo.flair(f"%%%%%%% Installing... Speed Typing", foreground="vcyan")
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/typing-speed-test')
	os.system('mv typing-speed-test {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nsnake():
	quo.flair(f"%%%%%%% Installing... nsnake", foreground="vcyan")
	# secretum inc
	os.system('apt install nsnake -y')
	print('###### Done')
	quo.flair(f"###### Type 'nsnake' to start.")
	backtomenu_option()

def nudoku():
	quo.flair(f"%%%%%%% Installing... Sudoku", foreground="vcyan")
	# secretum inc
	os.system('apt install nudoku -y')
	print('###### Done')
	quo.flair(f"###### Type 'nudoku' to start.")
	backtomenu_option()

def moon_buggy():
	quo.flair(f"%%%%%%% Installing... Moon-Buggy", foreground="vcyan")
	# secretum inc
	os.system('apt install moon-buggy -y')
	print('###### Done')
	quo.flair(f"###### Type 'moon-buggy' to start.")
	backtomenu_option()

def ttysolitaire():
	quo.flair(f"%%%%%%% Installing... tty-solitaire", foreground="vcyan")
	# secretum inc
	os.system('apt install tty-solitaire -y')
	print('###### Done')
	quo.flair(f"###### Type 'ttysolitaire' to start.")
	backtomenu_option()

def pacman4console():
	quo.flair(f"%%%%%%% Installing... Pacman4Console", foreground="vcyan")
	# secretum inc
	os.system('apt install pacman4console -y')
	print('###### Done')
	quo.flair(f"###### Type 'pacman' to start.")
	backtomenu_option()

### bash function ---
def fbvid():
	quo.flair(f"%%%%%%% Installing... fbvid", foreground="vcyan")
	# secretum inc
	os.system('apt install python ffmpeg -y')
	os.system('python -m pip install youtube-dl')
	fbvid_code = open(".myshfunc/fbvid.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(fbvid_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: fbvid "POST_URL"')
	backtomenu_option()

def cast2video():
	quo.flair(f"%%%%%%% Installing... cast2video", foreground="vcyan")
	# secretum inc
	os.system('apt install clang python ffmpeg -y')
	os.system('python -m pip install CPython ttygif')
	cast2video_code = open(".myshfunc/cast2video.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(cast2video_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: cast2video file.cast')
	backtomenu_option()

def iconset():
	quo.flair(f"%%%%%%% Installing... iconset", foreground="vcyan")
	iconset_code = open(".myshfunc/iconset.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(iconset_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: iconset project_name icon.png')
	backtomenu_option()

def readme():
	quo.flair(f"%%%%%%% Installing... readme", foreground="vcyan")
	# secretum inc
	os.system('apt install curl -y')
	readme_code = open(".myshfunc/readme.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(readme_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: readme User/Repo')
	backtomenu_option()

def makedeb():
	quo.flair(f"%%%%%%% Installing... makedeb", foreground="vcyan")
	# secretum inc
	os.system('apt install dpkg neovim -y')
	makedeb_code = open(".myshfunc/makedeb.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(makedeb_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: makedeb')
	backtomenu_option()

def quikfind():
	quo.flair(f"%%%%%%% Installing... quikfind", foreground="vcyan")
	quikfind_code = open(".myshfunc/quikfind.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(quikfind_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: quikfind')
	backtomenu_option()

def pranayama():
	quo.flair(f"%%%%%%% Installing... pranayama", foreground="vcyan")
	# secretum inc
	os.system('apt install termux-api -y')
	pranayama_code = open(".myshfunc/pranayama.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(pranayama_code)
	os.system('source '+os.getenv("HOME")+"./bashrc")
	print('###### Done')
	print('###### Usage: pranayama')
	print('######            or')
	print('######        pranayama [n]')
	backtomenu_option()

def sqlc():
	quo.flair(f"%%%%%%% Installing... sqlc", foreground="vcyan")
	# secretum inc
	os.system('apt install python sqlite3 -y')
	sqlc_code = open(".myshfunc/sqlc.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(sqlc_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: sqlc db_file sql_script')
	backtomenu_option()
