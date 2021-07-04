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
	print('\n###### Installing Nmap')
	# secretum inc
	os.system('apt install nmap')
	print('###### Done')
	quo.flair(f"###### Type 'nmap' to start.", foreground="red")
	backtomenu_option()

def red_hawk():
	print('\n###### Installing RED HAWK')
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dtect():
	print('\n###### Installing D-TECT')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	os.system('mv D-Tech {}/D-TECT'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmap():
	print('\n###### Installing sqlmap')
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def infoga():
	print('\n###### Installing Infoga')
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def reconDog():
	print('\n###### Installing ReconDog')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/ReconDog')
	os.system('mv ReconDog {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androZenmap():
	print('\n###### Installing AndroZenmap')
	# secretum inc
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir {}/AndroZenmap'.format(homeDir))
	os.system('mv androzenmap.sh {}/AndroZenmap'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlmate():
	print('\n###### Installing sqlmate')
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/s0md3v/sqlmate')
	os.system('mv sqlmate {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def astraNmap():
	print('\n###### Installing AstraNmap')
	# secretum inc
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def weeman():
	print('\n###### Installing weeman')
	# secretum inc
	os.system('apt install clang git python2')
	os.system('python2 -m pip bs4 html5lib lxml')
	os.system('git clone https://github.com/evait-security/weeman')
	os.system('mv weeman {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def easyMap():
	print('\n###### Installing Easymap')
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap {}'.format(homeDir))
	os.system('cd {}/Easymap && sh install.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xd3v():
	print('\n###### Installing XD3v')
	# secretum inc
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh {0}/../usr/bin/xd3v && chmod +x {0}/../usr/bin/xd3v'.format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'xd3v' to start.")
	backtomenu_option()

def crips():
	print('\n###### Installing Crips')
	# secretum inxlc
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sir():
	print('\n###### Installing SIR')
	# secretum inxlc
	os.system("apt install python2 git")
	os.system("python2 -m pip install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def xshell():
	print('\n###### Installing Xshell')
	# secretum inxlc
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def evilURL():
	print('\n###### Installing EvilURL')
	# secretum inxlc
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def striker():
	print('\n###### Installing Striker')
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/s0md3v/Striker')
	os.system('mv Striker {}'.format(homeDir))
	os.system('cd {}/Striker && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dsss():
	print('\n###### Installing DSSS')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqliv():
	print('\n###### Installing SQLiv')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/the-robot/sqliv')
	os.system('mv sqliv {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqlscan():
	print('\n###### Installing sqlscan')
	# secretum inc
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wordpreSScan():
	print('\n###### Installing Wordpresscan')
	# secretum inc
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan {}'.format(homeDir))
	os.system('cd {}/Wordpresscan && python2 -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def wpscan():
	print('\n###### Installing WPScan')
	# secretum inc
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan {0} && cd {0}/wpscan'.format(homeDir))
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print('###### Done')
	backtomenu_option()

def wordpresscan():
	print('\n###### Installing wordpresscan(2)')
	# secretum inc
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan {}'.format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'wordpresscan' to start.")
	backtomenu_option()

def routersploit():
	print('\n###### Installing Routersploit')
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/threat9/routersploit')
	os.system('mv routersploit {0};cd {0}/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def torshammer():
	print('\n###### Installing Torshammer')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def slowloris():
	print('\n###### Installing Slowloris')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fl00d12():
	print('\n###### Installing Fl00d & Fl00d2')
	# secretum inc
	os.system('apt install python2 curl')
	os.system('mkdir {}/fl00d'.format(homeDir))
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	os.system('mv fl00d.py {0}/fl00d && mv fl00d2.py {0}/fl00d'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def goldeneye():
	print('\n###### Installing GoldenEye')
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xerxes():
	print('\n###### Installing Xerxes')
	# secretum inc
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/baraalmasri/xerxes')
	os.system('mv xerxes {}'.format(homeDir))
	os.system('cd {}/xerxes && clang xerxes.c -o xerxes'.format(homeDir))
	os.system('chmod 755 {0}/xerxes/xerxes && cp {0}/xerxes/xerxes $PREFIX/bin'.format(homeDir))
	print('###### Done')
	print('###### Usage: xerxes ​www.fakesite.com​ 80')
	backtomenu_option()

def planetwork_ddos():
	print('\n###### Installing Planetwork-DDOS')
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hydra():
	print('\n###### Installing Hydra')
	# secretum inc
	os.system('apt install hydra')
	print('###### Done')
	backtomenu_option()

def black_hydra():
	print('\n###### Installing Black Hydra')
	# secretum inc
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cupp():
	print('\n###### Installing Cupp')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def asu():
	print('\n###### Installing ASU')
	# secretum inc
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hash_buster():
	print('\n###### Installing Hash-Buster')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/s0md3v/Hash-Buster')
	os.system('mv Hash-Buster {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def instaHack():
	print('\n###### Installing InstaHack')
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Slayeri4/instahack')
	os.system('mv instahack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def indonesian_wordlist():
	print('\n###### Installing indonesian-wordlist')
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	os.system('mv indonesian-wordlist {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fbBrute():
	print('\n###### Installing Facebook Brute Force 3')
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
	print('\n###### Installing WebDAV')
	# secretum inc
	os.system('apt install python2 openssl curl libcurl')
	os.system('python2 -m pip install urllib3 chardet certifi idna requests')
	os.system('mkdir {}/webdav'.format(homeDir))
	os.system('curl -k -O https://pastebin.com/raw/HnVyQPtR;mv HnVyQPtR {}/webdav/webdav.py'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def webmassploit():
	print('\n###### Installing Webdav Mass Exploiter')
	# secretum inxlc
	os.system("apt install python2 openssl curl libcurl")
	os.system("python2 -m pip install requests")
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir {0}/webdav-mass-exploit && mv webdav.py {0}/webdav-mass-exploit".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sqldump():
	print('\n###### Installing sqldump')
	# secretum inc
	os.system('apt install python2 curl')
	os.system('python2 -m pip install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir {0}/sqldump && chmod +x sqldump.py && mv sqldump.py {0}/sqldump'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def websploit():
	print('\n###### Installing Websploit')
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def metasploit():
	print('\n###### Installing Metasploit')
	# secretum inxlc
	os.system("apt install unstable-repo")
	os.system("cd {} && apt install metasploit".format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'msfconsole' to start.")
	backtomenu_option()

def commix():
	print('\n###### Installing Commix')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutal():
	print('\n###### Installing Brutal')
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def knockmail():
	print('\n###### Installing KnockMail')
	# secretum inc
	os.system('apt install python2 git')
	os.system('python2 -m pip install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hac():
	print('\n###### Installing Hac')
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rang3r():
	print('\n###### Installing Rang3r')
	# secretum inxlc
	os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def sh33ll():
	print('\n###### Installing SH33LL')
	# secretum inxlc
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def social():
	print('\n###### Installing Social-Engineering')
	# secretum inxlc
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def spiderbot():
	print('\n###### Installing SpiderBot')
	# secretum inxlc
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot {}".format(homeDir))
	print('###### Done')
	backtomenu_option()

def ngrok():
	print('\n###### Installing Ngrok')
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sudo():
	print('\n###### Installing sudo')
	# secretum inc
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo {0} && cd {0}/termux-sudo && chmod 777 *'.format(homeDir))
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print('###### Done')
	backtomenu_option()

def ubuntu():
	print('\n###### Installing Ubuntu')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu {0} && cd {0}/termux-ubuntu && bash ubuntu.sh'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fedora():
	print('\n###### Installing Fedora')
	# secretum inc
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nethunter():
	print('\n###### Installing Kali NetHunter')
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def blackbox():
	print('\n###### Installing BlackBox')
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xattacker():
	print('\n###### Installing XAttacker')
	# secretum inc
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vcrt():
	print('\n###### Installing VCRT')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def socfish():
	print('\n###### Installing SocialFish')
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ecode():
	print('\n###### Installing ECode')
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xsstrike():
	print('\n###### Installing XSStrike')
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/s0md3v/XSStrike')
	os.system('mv XSStrike {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def breacher():
	print('\n###### Installing Breacher')
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests argparse')
	os.system('git clone https://github.com/s0md3v/Breacher')
	os.system('mv Breacher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def stylemux():
	print('\n###### Installing Termux-Styling')
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def txtool():
	print('\n###### Installing TXTool')
	# secretum inc
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def passgencvar():
	print('\n###### Installing PassGen')
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def owscan():
	print('\n###### Installing OWScan')
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sanlen():
	print('\n###### Installing santet-online')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def spazsms():
	print('\n###### Installing SpazSMS')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasher():
	print('\n###### Installing Hasher')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install passlib binascii progressbar')
	os.system('git clone https://github.com/CiKu370/hasher')
	os.system('mv hasher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashgenerator():
	print('\n###### Installing Hash-Generator')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/CiKu370/hash-generator')
	os.system('mv hash-generator {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kodork():
	print('\n###### Installing ko-dork')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/CiKu370/ko-dork')
	os.system('mv ko-dork {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def snitch():
	print('\n###### Installing snitch')
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def osif():
	print('\n###### Installing OSIF')
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/CiKu370/OSIF')
	os.system('mv OSIF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nk26():
	print('\n###### Installing nk26')
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/milio48/nk26')
	os.system('mv nk26 {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def devploit():
	print('\n###### Installing Devploit')
	# secretum inc
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hasherdotid():
	print('\n###### Installing Hasherdotid')
	# secretum inc
	os.system('apt install python2 git')
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	os.system('mv hasherdotid {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def namechk():
	print('\n###### Installing Namechk')
	# secretum inc
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xlPy():
	print('\n###### Installing xl-py')
	# secretum inc
	os.system('apt install python git')
	os.system('git clone https://github.com/albertoanggi/xl-py')
	os.system('mv xl-py {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def beanshell():
	print('\n###### Installing Beanshell')
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'bsh' to start.")
	backtomenu_option()

def crunch():
	print('\n###### Installing Crunch')
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'crunch' to start.")
	backtomenu_option()

def binploit():
	print('\n###### Installing Binary Exploitation')
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	quo.flair(f"###### Done")
	quo.flair(f"###### Tutorial: https://youtu.be/3NTXFUxcKPc")
	backtomenu_option()

def textr():
	print('\n###### Installing Textr')
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'textr' to start.")
	backtomenu_option()

def apsca():
	print('\n###### Installing ApSca')
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'apsca' to start.")
	backtomenu_option()

def amox():
	print('\n###### Installing amox')
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'amox' to start.")
	backtomenu_option()

def fade():
	print('\n###### Installing FaDe')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FaDe')
	os.system('mv FaDe {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ginf():
	print('\n###### Installing GINF')
	# secretum inc
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def auxile():
	print('\n###### Installing AUXILE')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def inther():
	print('\n###### Installing inther')
	# secretum inc
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hpb():
	print('\n###### Installing HPB')
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'hpb' to start.")
	backtomenu_option()

def fmbrute():
	print('\n###### Installing FMBrute')
	# secretum inc
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FMBrute')
	os.system('mv FMBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def hashid():
	print('\n###### Installing HashID')
	# secretum inc
	os.system('apt install python2 && python2 -m pip install hashid')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'hashid -h' to show usage of hashid")
	backtomenu_option()

def gpstr():
	print('\n###### Installing GPS Tracking')
	# secretum inc
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	os.system('mv gps_tracking {}'.format(homeDir))
	quo.flair(f"###### Done")
	backtomenu_option()

def pret():
	print('\n###### Installing PRET')
	# secretum inc
	os.system('apt install python2 imagemagick git')
	os.system('python2 -m pip install colorama pysnmp')
	os.system('git clone https://github.com/RUB-NDS/PRET')
	os.system('mv PRET {}'.format(homeDir))
	quo.flair(f"###### Done")
	backtomenu_option()

def atlas():
	print('\n###### Installing Atlas')
	# secretum inc
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/m4ll0k/Atlas')
	os.system('mv Atlas {}'.format(homeDir))
	quo.flair(f"###### Done")
	backtomenu_option()

def hashcat():
	print('\n###### Installing Hashcat')
	# secretum inc
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'hashcat' to start.")
	backtomenu_option()

def liteotp():
	print('\n###### Installing LiteOTP')
	# secretum inc
	os.system('apt install php wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite')
	quo.flair(f"###### Done")
	quo.flair(f"###### Type 'lite' to start.")
	backtomenu_option()

def fbbrutex():
	print('\n###### Installing FBBrute')
	# secretum inc
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FBBrute')
	os.system('mv FBBrute {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def fim():
	print('\n###### Installing fim')
	# secretum inc
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	os.system('mv fim {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def rshell():
	print('\n###### Installing RShell')
	# secretum inc
	os.system('apt install git python && python -m pip install colorama')
	os.system('git clone https://github.com/Jishu-Epic/RShell')
	os.system('mv RShell {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def termpyter():
	print('\n###### Installing TermPyter')
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Jishu-Epic/TermPyter')
	os.system('mv TermPyter {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maxsubdofinder():
	print('\n###### Installing MaxSubdoFinder')
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	os.system('mv MaxSubdoFinder {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def jadx():
	print('\n###### Installing jadx')
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
	os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
	os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	print('###### Done')
	quo.flair(f"###### Type 'jadx' to start.")
	backtomenu_option()

def pwnedornot():
	print('\n###### Installing pwnedOrNot')
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/thewhiteh4t/pwnedOrNot')
	os.system('mv pwnedOrNot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def maclook():
	print('\n###### Installing Mac-Lookup')
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/T4P4N/Mac-Lookup')
	os.system('mv Mac-Lookup {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def f4k3():
	print('\n###### Installing F4K3')
	# secretum inc
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Gameye98/Gameye98.github.io/blob/master/package/f4k3_1.0_all.deb')
	os.system('dpkg -i f4k3_1.0_all.deb')
	os.system('rm -rf f4k3_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'f4k3' to start.")
	backtomenu_option()

def katak():
	print('\n###### Installing Katak')
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install requests progressbar')
	os.system('git clone https://github.com/Gameye98/Katak')
	os.system('mv Katak {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def heroku():
	print('\n###### Installing heroku')
	# secretum inc
	os.system('apt install nodejs')
	os.system('npm install heroku -g')
	print('###### Done')
	quo.flair(f"###### Type 'heroku' to start.")
	backtomenu_option()

def google():
	print('\n###### Installing google')
	# secretum inc
	os.system('apt install python')
	os.system('python -m pip install google')
	print('###### Done')
	quo.flair(f"###### Type 'google' to start.")
	backtomenu_option()

def billcypher():
	print('\n###### Installing BillCypher')
	# secretum inc
	os.system('apt install git python')
	os.system('python -m pip install argparse dnspython requests urllib3 colorama')
	os.system('git clone https://github.com/GitHackTools/BillCipher')
	os.system('mv BillCypher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def vbug():
	print('\n###### Installing vbug')
	# secretum inc
	os.system('apt install git python2')
	os.system('git clone https://github.com/Gameye98/vbug')
	os.system('mv vbug {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def kojawafft():
	print('\n###### Installing kojawafft')
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
		print('\n###### Installing aircrack-ng')
		# secretum inc
		os.system('apt install root-repo aircrack-ng')
		print('###### Done')
		quo.flair(f"###### Type 'aircrack-ng' to start.")
	backtomenu_option()

def ettercap():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing ettercap')
		# secretum inc
		os.system('apt install root-repo ettercap')
		print('###### Done')
		quo.flair(f"###### Type 'ettercap' to start.")
	backtomenu_option()

def ccgen():
	print('\n###### Installing ccgen')
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ccgen')
	os.system('mv ccgen {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def ddcrypt():
	print('\n###### Installing ddcrypt')
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/Gameye98/ddcrypt')
	os.system('mv ddcrypt {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def dnsrecon():
	print('\n###### Installing dnsrecon')
	# secretum inc
	os.system('apt install git python')
	os.system('git clone https://github.com/darkoperator/dnsrecon')
	os.system('python -m pip install -r dnsrecon/requirements.txt')
	os.system('mv dnsrecon {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def zphisher():
	print('\n###### Installing zphisher')
	# secretum inc
	os.system('apt install git php openssh curl')
	os.system('git clone https://github.com/htr-tech/zphisher')
	os.system('mv zphisher {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def apktool():
	print('\n###### Installing apktool')
	# secretum inc
	os.system('apt install git dpkg')
	os.system('git clone https://github.com/Lexiie/Termux-Apktool')
	os.system('mv Termux-Apktool {}'.format(homeDir))
	os.system('cd {}/Termux-Apktool && dpkg -i *.deb'.format(homeDir))
	print('###### Done')
	quo.flair(f"###### Type 'apktool' to start.")
	backtomenu_option()

def uncompyle():
	print('\n###### Installing uncompyle6')
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
		print('\n###### Installing Wifite')
		# secretum inc
		os.system('apt install git python2')
		os.system('git clone https://github.com/derv82/wifite')
		os.system('mv wifite {}'.format(homeDir))
		print('###### Done')
	backtomenu_option()

def parrot():
	print('\n###### Installing Parrot')
	# secretum inc
	os.system('apt install wget openssl-tool proot -y && hash -r && cd {} && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Parrot/parrot.sh && bash parrot.sh'.format(homeDir))
	os.system('cd {} && bash start-parrot.sh'.format(homeDir))
	print('###### Done')
	print('###### Make sure visit: https://techriz.com/how-to-install-parrot-linux-on-android-without-root/')
	os.system('am start -a android.intent.action.VIEW -d "https://techriz.com/how-to-install-parrot-linux-on-android-without-root/"')
	backtomenu_option()

def archlinux():
	print('\n###### Installing Arch Linux')
	# secretum inc
	os.system('apt install git')
	os.system('cd $HOME && git clone https://github.com/sdrausty/TermuxArch')
	os.system('cd $HOME && bash TermuxArch/setupTermuxArch.sh')
	print('###### Done')
	backtomenu_option()

def tshark():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing tshark')
		# secretum inc
		os.system('apt install root-repo tshark')
		print('###### Done')
		quo.flair(f"###### Type 'tshark' to start.")
	backtomenu_option()

def dos2unix():
	print('\n###### Installing dos2unix')
	# secretum inc
	os.system('apt install dos2unix')
	print('###### Done')
	quo.flair(f"###### Type 'dos2unix' to start.")
	backtomenu_option()

def exiftool():
	print('\n###### Installing exiftool')
	# secretum inc
	os.system('apt install exiftool')
	print('###### Done')
	quo.flair(f"###### Type 'exiftool' to start.")
	backtomenu_option()

def iconv():
	print('\n###### Installing iconv')
	# secretum inc
	os.system('apt install iconv')
	print('###### Done')
	quo.flair(f"###### Type 'iconv' to start.")
	backtomenu_option()

def mediainfo():
	print('\n###### Installing mediainfo')
	# secretum inc
	os.system('apt install mediainfo')
	print('###### Done')
	print('###### Usage: mediainfo filename.pdf')
	backtomenu_option()

def pdfinfo():
	print('\n###### Installing pdfinfo')
	# secretum inc
	os.system('apt install poppler')
	print('###### Done')
	print('###### Usage: pdfinfo filename.pdf')
	backtomenu_option()

def tcpdump():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing tcpdump')
		# secretum inc
		os.system('apt install root-repo tcpdump')
		print('###### Done')
		quo.flair(f"###### Type 'tcpdump' to start.")
	backtomenu_option()

def hping3():
	if int(inputstream("id -u".split()).decode("utf8")) != 0: quo.flair(f"ERROR: Make sure you're device has been rooted");
	else:
		print('\n###### Installing hping3')
		# secretum inc
		os.system('apt install root-repo hping3')
		print('###### Done')
		quo.flair(f"###### Type 'hping3' to start.")
	backtomenu_option()

def dbdat():
	print('\n###### Installing DbDat')
	# secretum inc
	os.system('apt install git python2')
	os.system('python2 -m pip install MySQL-python psycopg2 cx_Oracle pymssql ibm_db pymongo pyyaml couchdb')
	os.system('git clone https://github.com/foospidy/DbDat')
	os.system('mv DbDat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nosqlmap():
	print('\n###### Installing NoSQLMap')
	# secretum inc
	os.system('apt install git python2 unstable-repo metasploit')
	os.system('python2 -m pip install pymongo httplib2')
	os.system('git clone https://github.com/codingo/NoSQLMap')
	os.system('mv NoSQLMap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def audit_couchdb():
	print('\n###### Installing audit_couchdb')
	# secretum inc
	os.system('apt install git nodejs')
	os.system('npm install -g npm@next audit_couchdb')
	os.system('git clone https://github.com/iriscouch/audit_couchdb')
	os.system('mv audit_couchdb {}'.format(homeDir))
	print('###### Done')
	print('###### Usage: audit_couchdb https://admin:secret@localhost:5984')
	backtomenu_option()

def mongoaudit():
	print('\n###### Installing mongoaudit')
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install pymongo mongoaudit')
	print('###### Done')
	quo.flair(f"###### Type 'mongoaudit' to start.")
	backtomenu_option()

def wifiphisher():
	print('\n###### Installing Wifiphisher')
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install setuptools scapy')
	os.system('git clone https://github.com/wifiphisher/wifiphisher')
	os.system('mv wifiphisher {0} && cd {0}/wifiphisher && python setup.py install'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sherlock():
	print('\n###### Installing sherlock')
	# secretum inc
	os.system('apt install git python -y')
	os.system('git clone https://github.com/sherlock-project/sherlock')
	os.system('mv sherlock {0} && cd {0}/sherlock && python -m pip install -r requirements.txt'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def shc():
	print('\n###### Installing shc')
	# secretum inc
	os.system('apt install shc -y')
	print('###### Done')
	quo.flair(f"###### Type 'shc' to start.")
	backtomenu_option()

def steghide():
	print('\n###### Installing steghide')
	# secretum inc
	os.system('apt install steghide -y')
	print('###### Done')
	quo.flair(f"###### Type 'steghide' to start.")
	backtomenu_option()

def tesseract():
	print('\n###### Installing tesseract')
	# secretum inc
	os.system('apt install tesseract -y')
	print('###### Done')
	quo.flair(f"###### Type 'tesseract' to start.")
	backtomenu_option()

def sleuthkit():
	print('\n###### Installing sleuthkit')
	# secretum inc
	os.system('apt install sleuthkit -y')
	print('###### Done')
	quo.flair(f"###### Type 'pkg files sleuthkit | grep usr/bin' to check executable file related to sleuthkit package.")
	backtomenu_option()

def octave():
	print('\n###### Installing Octave')
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install octave -y')
	print('###### Done')
	quo.flair(f"###### Type 'octave' to start.")
	backtomenu_option()

def fpcompiler():
	print('\n###### Installing fp-compiler')
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install fp-compiler -y')
	print('###### Done')
	quo.flair(f"###### Type 'fpc' to start.")
	backtomenu_option()

def numpy():
	print('\n###### Installing numpy')
	# secretum inc
	if not repo_check("pointless.list"):
		pointless_repo()
	os.system('apt install numpy -y')
	print('###### Done')
	quo.flair(f"###### Type 'pkg files numpy | grep usr/bin' to check executable file related to numpy package.")
	backtomenu_option()

def userrecon():
	print('\n###### Installing userrecon')
	# secretum inc
	os.system('apt install wget dpkg curl -y')
	os.system('wget https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/package/userrecon_1.0_all.deb')
	os.system('dpkg -i userrecon_1.0_all.deb')
	os.system('rm userrecon_1.0_all.deb')
	print('###### Done')
	quo.flair(f"###### Type 'userrecon' to start.")
	backtomenu_option()

def mrsip():
	print('\n###### Installing Mr.SIP')
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install netifaces ipaddress scapy pyfiglet')
	os.system('git clone https://github.com/meliht/Mr.SIP')
	os.system('mv Mr.SIP {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tmscanner():
	print('\n###### Installing TM-scanner')
	# secretum inc
	os.system('apt install python python2 nmap git -y')
	os.system('python -m pip install colorama requests')
	os.system('python2 -m pip install colorama requests')
	os.system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
	os.system('mv TM-scanner {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xss_payload_list():
	print('\n###### Installing xss-payload-list')
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/payloadbox/xss-payload-list')
	os.system('mv xss-payload-list {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clickbot():
	print('\n###### Installing ClickBot')
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/ziziwho/clickbot')
	os.system("python -m pip install asyncio colorama telethon rsa pyaes asyncio async_generator colorama bs4 requests")
	os.system('mv clickbot {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def phoneinfoga():
	print('\n###### Installing PhoneInfoga')
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
	print('\n###### Installing BTC-to-IDR-checker')
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/guruku/BTC-to-IDR-checker')
	os.system('mv BTC-to-IDR-checker {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def sitebroker():
	print('\n###### Installing SiteBroker')
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
	print('\n###### Installing dost-attack')
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/verluchie/dost-attack')
	os.system('mv dost-attack {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cfr():
	print('\n###### Installing CFR')
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
	print('\n###### Installing UPX')
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
	print('\n###### Installing pyinstxtractor')
	# secretum inc
	os.system('apt install git python -y')
	os.system('git clone https://github.com/extremecoders-re/pyinstxtractor')
	os.system('mv pyinstxtractor {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def innoextract():
	print('\n###### Installing innoextract')
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
	print('\n###### Installing Lynis')
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/CISOfy/lynis')
	os.system('mv lynis {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def chkrootkit():
	print('\n###### Installing Chkrootkit')
	# secretum inc
	os.system('apt install clang git -y')
	os.system('git clone https://github.com/Magentron/chkrootkit')
	os.system('mv chkrootkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def clamav():
	print('\n###### Installing ClamAV')
	# secretum inc
	os.system('apt install clamav -y')
	os.system('freshclam')
	print('###### Done')
	quo.flair(f"###### Type 'clamscan' to start.")
	backtomenu_option()

def yara():
	print('\n###### Installing Yara')
	# secretum inc
	os.system('apt install yara -y')
	print('###### Done')
	quo.flair(f"###### Type 'yara' to start.")
	backtomenu_option()

def virustotal():
	print('\n###### Installing VirusTotal-CLI')
	# secretum inc
	os.system('apt install virustotal-cli -y')
	print('###### Done')
	quo.flair(f"###### Type 'vt' to start.")
	backtomenu_option()

def maigret():
	print('\n###### Installing maigret')
	# secretum inc
	os.system('apt install python -y')
	os.system('python -m pip install maigret')
	print('###### Done')
	quo.flair(f"###### Usage: maigret <username>")
	quo.flair(f"###### Usage: maigret -h")
	backtomenu_option()

def xplsearch():
	print('\n###### Installing XPL-SEARCH')
	# secretum inc
	os.system('apt install git php -y')
	os.system('git clone https://github.com/r00tmars/XPL-SEARCH')
	os.system('mv XPL-SEARCH {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def xadmin():
	print('\n###### Installing Xadmin')
	# secretum inc
	os.system('apt install git perl -y')
	os.system('git clone https://github.com/Manisso/Xadmin')
	os.system('mv Xadmin {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def credmap():
	print('\n###### Installing Credmap')
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/lightos/credmap')
	os.system('mv credmap {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def mapeye():
	print('\n###### Installing MapEye')
	# secretum inc
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/bhikandeshmukh/MapEye')
	os.system('mv MapEye {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def gathetool():
	print('\n###### Installing GatheTOOL')
	# secretum inc
	os.system('apt install git php python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/AngelSecurityTeam/GatheTOOL')
	os.system('mv GatheTOOL {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def avpass():
	print('\n###### Installing avpass')
	# secretum inc
	os.system('apt install git python2 python -y')
	os.system('git clone https://github.com/sslab-gatech/avpass')
	os.system('mv avpass {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def binwalk():
	print('\n###### Installing binwalk')
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
	print('\n###### Installing A-Rat')
	# secretum inc
	os.system('apt install python git -y')
	os.system('git clone https://github.com/RexTheGod/A-Rat')
	os.system('mv A-Rat {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def adbtk():
	print('\n###### Installing ADB-Toolkit')
	# secretum inc
	os.system('apt install git -y')
	os.system('git clone https://github.com/ASHWIN990/ADB-Toolkit')
	os.system('mv ADB-Toolkit {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def androbugs():
	print('\n###### Installing AndroBugs_Framework')
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install pymongo')
	os.system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
	os.system('mv AndroBugs_Framework {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def tekdefense():
	print('\n###### Installing TekDefense-Automater')
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/1aN0rmus/TekDefense-Automater')
	os.system('mv TekDefense-Automater {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def baf():
	print('\n###### Installing BAF')
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('python2 -m pip install requests bs4 selenium colored termcolor')
	os.system('git clone https://github.com/engMaher/BAF')
	os.system('mv BAF {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def brutex():
	print('\n###### Installing BruteX')
	# secretum inc
	os.system('apt install git hydra -y')
	os.system('git clone https://github.com/1N3/BruteX')
	os.system('mv BruteX {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def cmseek():
	print('\n###### Installing CMSeeK')
	# secretum inc
	os.system('apt install git python -y')
	os.system('python -m pip install requests')
	os.system('git clone https://github.com/Tuhinshubhra/CMSeeK')
	os.system('mv CMSeeK {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

### Compiler/Interpreter
def python2():
	print('\n###### Installing Python2')
	# secretum inc
	os.system('apt install python2 -y')
	print('###### Done')
	quo.flair(f"###### Type 'python2' to start.")
	backtomenu_option()

def ecj():
	print('\n###### Installing ecj')
	# secretum inc
	os.system('apt install ecj -y')
	print('###### Done')
	quo.flair(f"###### Type 'ecj' to start.")
	backtomenu_option()

def golang():
	print('\n###### Installing Golang')
	# secretum inc
	os.system('apt install golang -y')
	print('###### Done')
	quo.flair(f"###### Type 'go' to start.")
	backtomenu_option()

def ldc():
	print('\n###### Installing ldc')
	# secretum inc
	os.system('apt install ldc -y')
	print('###### Done')
	quo.flair(f"###### Type 'ldc2' to start.")
	backtomenu_option()

def nim():
	print('\n###### Installing Nim')
	# secretum inc
	os.system('apt install nim -y')
	print('###### Done')
	quo.flair(f"###### Type 'nim' to start.")
	backtomenu_option()

def shc():
	print('\n###### Installing shc')
	# secretum inc
	os.system('apt install shc -y')
	print('###### Done')
	quo.flair(f"###### Type 'shc' to start.")
	backtomenu_option()

def tcc():
	print('\n###### Installing TCC')
	# secretum inc
	os.system('apt install tcc -y')
	print('###### Done')
	quo.flair(f"###### Type 'tcc' to start.")
	backtomenu_option()

def php():
	print('\n###### Installing PHP')
	# secretum inc
	os.system('apt install php -y')
	print('###### Done')
	quo.flair(f"###### Type 'php' to start.")
	backtomenu_option()

def ruby():
	print('\n###### Installing Ruby')
	# secretum inc
	os.system('apt install ruby -y')
	print('###### Done')
	quo.flair(f"###### Type 'ruby' to start.")
	backtomenu_option()

def perl():
	print('\n###### Installing Perl')
	# secretum inc
	os.system('apt install perl -y')
	print('###### Done')
	quo.flair(f"###### Type 'perl' to start.")
	backtomenu_option()

def vlang():
	print('\n###### Installing Vlang')
	# secretum inc
	os.system('apt install vlang -y')
	print('###### Done')
	quo.flair(f"###### Type 'vlang' to start.")
	backtomenu_option()

def blogc():
	print('\n###### Installing BlogC')
	# secretum inc
	os.system('apt install blogc -y')
	print('###### Done')
	quo.flair(f"###### Type 'blogc' to start.")
	backtomenu_option()

### termux games
def street_car():
	print('\n###### Installing street-car')
	# secretum inc
	os.system('apt install git python python2 -y')
	os.system('git clone https://github.com/JustaHackers/street_car')
	os.system('mv street_car {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def flappy_bird():
	print('\n###### Installing flappy-bird')
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/flappy_bird')
	os.system('mv flappy_bird {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def speed_typing():
	print('\n###### Installing Speed Typing')
	# secretum inc
	os.system('apt install git python2 -y')
	os.system('git clone https://github.com/JustAHackers/typing-speed-test')
	os.system('mv typing-speed-test {}'.format(homeDir))
	print('###### Done')
	backtomenu_option()

def nsnake():
	print('\n###### Installing nsnake')
	# secretum inc
	os.system('apt install nsnake -y')
	print('###### Done')
	quo.flair(f"###### Type 'nsnake' to start.")
	backtomenu_option()

def nudoku():
	print('\n###### Installing Sudoku')
	# secretum inc
	os.system('apt install nudoku -y')
	print('###### Done')
	quo.flair(f"###### Type 'nudoku' to start.")
	backtomenu_option()

def moon_buggy():
	print('\n###### Installing Moon-Buggy')
	# secretum inc
	os.system('apt install moon-buggy -y')
	print('###### Done')
	quo.flair(f"###### Type 'moon-buggy' to start.")
	backtomenu_option()

def ttysolitaire():
	print('\n###### Installing tty-solitaire')
	# secretum inc
	os.system('apt install tty-solitaire -y')
	print('###### Done')
	quo.flair(f"###### Type 'ttysolitaire' to start.")
	backtomenu_option()

def pacman4console():
	print('\n###### Installing Pacman4Console')
	# secretum inc
	os.system('apt install pacman4console -y')
	print('###### Done')
	quo.flair(f"###### Type 'pacman' to start.")
	backtomenu_option()

### bash function ---
def fbvid():
	print('\n###### Installing fbvid')
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
	print('\n###### Installing cast2video')
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
	print('\n###### Installing iconset')
	iconset_code = open(".myshfunc/iconset.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(iconset_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: iconset project_name icon.png')
	backtomenu_option()

def readme():
	print('\n###### Installing readme')
	# secretum inc
	os.system('apt install curl -y')
	readme_code = open(".myshfunc/readme.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(readme_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: readme User/Repo')
	backtomenu_option()

def makedeb():
	print('\n###### Installing makedeb')
	# secretum inc
	os.system('apt install dpkg neovim -y')
	makedeb_code = open(".myshfunc/makedeb.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(makedeb_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: makedeb')
	backtomenu_option()

def quikfind():
	print('\n###### Installing quikfind')
	quikfind_code = open(".myshfunc/quikfind.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(quikfind_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: quikfind')
	backtomenu_option()

def pranayama():
	print('\n###### Installing pranayama')
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
	print('\n###### Installing sqlc')
	# secretum inc
	os.system('apt install python sqlite3 -y')
	sqlc_code = open(".myshfunc/sqlc.sh","r").read()
	open(os.getenv("HOME")+"/.bashrc","a").write(sqlc_code)
	os.system('source '+os.getenv("HOME")+"/.bashrc")
	print('###### Done')
	print('###### Usage: sqlc db_file sql_script')
	backtomenu_option()
