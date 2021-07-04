#!/bin/sh

if [ -d /data/data/com.termux/files/usr/etc ]; then
  conf_dir="/data/data/com.termux/files/usr/etc"
elif [ -d /usr/etc ]; then
  conf_dir="/usr/etc"
elif [ -d /etc ]; then
  conf_dir="/etc"
fi

if [ -e /usr/lib/sudo ]; then
	sudo python3 $conf_dir/debonair_/debonair/start.py
else
	python3 import quo
import os
import sys
import time

@quo.command()
@quo.app("--terms")
def install(terms):
    quo.flair(f"THE SOFTWARE IS PROVIDED `AS IS`, WITHOUT WARRANTY OF ANY KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERRCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL I BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE", foreground="vblack", background="vwhite", bold=True)
    time.sleep(3)
    quo.flair(f"Technically, Moses was the first person with a tablet downloading data from the cloud...", foreground="red", dim=True, bold=True)
    os.system("cd /etc/ && mkdir debonair_ && cd /etc/debonair_/ && git clone --quiet https://github.com/secretum-inc/debonair.git && cd /etc/debonair_/debonair/ && chmod +x debonair && chmod +x dbnr && mv -f  debonair /usr/bin/ && mv -f dbnr /usr/bin/ && dbnr")
           # os.system("cd")
            #os.system("cd /etc/debonair_/debonair && chmod +x debonair")
            #os.system("cd")
           # os.system("cd /etc/debonair_/debonair && chmod +x dbnr")
           # os.system("cd")
           # os.system("cd /etc/debonair_/debonair && mv -f -r dbnr /usr/bin")
           # os.system("cd")
           # os.system("cd /etc/debonair_/debonair  && mv -f -r debonair /usr/bin")
           # os.system("clear")
           # os.system("cd")
           # os.system("rm -rf debonair")
           # os.system("dbnr")
       # else:
           # if inp == "n" or inp== "no" or inp== "N" or inp == "NO":
                #quo.flair(f"Quiting!!", foreground="black", background="vred")
                #time.sleep(1)
               # os.system("clear")
               # os.system("exit")

if __name__ == "__main__":
    install()

fi
exit
