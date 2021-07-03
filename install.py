import quo
import os
import sys
import time

@quo.command()
@quo.app("--terms")
def install(terms):
    while True:
        os.system("clear")
        quo.flair(f"THE SOFTWARE IS PROVIDED `AS IS`, WITHOUT WARRANTY OF ANY KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERRCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL I BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE", foreground="vblack", background="vwhite", bold=True)
        inp = quo.prompt("Do you want to install Debonair? [y/n]")
        if inp=="y" or inp=="Y" or inp=="Yes" or inp=="yes":
            os.system("clear")
            quo.flair(f"Technically, Moses was the first person with a tablet downloading data from the cloud...", foreground="red", dim=True, bold=True)
            os.system("cd /etc/ && mkdir debonair_")
            os.system("git clone --quiet https://github.com/secretum-inc/debonair.git /etc/debonair_")
            os.system("cd")
            os.system("cd /etc/debonair_/debonair && chmod +x debonair")
            os.system("cd")
            os.system("cd /etc/debonair_/debonair && chmod +x dbnr")
            os.system("cd")
            os.system("cd /etc/debonair_/debonair && mv -f -r dbnr /usr/bin")
            os.system("cd")
            os.system("cd /etc/debonair_/debonair  && mv -f -r debonair /usr/bin")
            os.system("clear")
            os.system("cd")
            os.system("rm -rf debonair")
            os.system("dbnr")
        else:
            if inp == "n" or inp== "no" or inp== "N" or inp == "NO":
                quo.flair(f"Quiting!!", foreground="black", background="vred")
                time.sleep(1)
                os.system("clear")
                os.system("exit")

if __name__ == "__main__":
    install()
