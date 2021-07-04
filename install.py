import quo
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

if __name__ == "__main__":
    install()
