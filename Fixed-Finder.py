import sys
import requests
import re
from multiprocessing.dummy import Pool
import logging
from colorama import Fore, init

init(autoreset=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
requests.urllib3.disable_warnings()

def print_banner():
    banner = f"""
{Fore.CYAN}==========================
{Fore.GREEN}  WELCOME TO WEB SHELL FINDER TOOL
{Fore.YELLOW}  Fixed by CyberAlphaWolf /  Xz
{Fore.CYAN}==========================
    """
    print(banner)

def load_targets(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        sys.exit(1)

def normalize_url(url):
    return re.sub(r'^https?://', '', url).split('/')[0]

class WebShellFinder:
    def __init__(self):
        self.user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.paths_to_check = self.get_paths()

    @staticmethod
    def get_paths():
        return [
            '/uploads/',
            '/upload/',
            '/cgi-bin/',
            '/files/',
            '/temp/',
            '/css/',
            '/admin/',
            '/images/',
            '/assets/',
            '/ALFA_DATA/',
            '/.well-known/',
            '/wp-includes/',
            '/wp-content/',
            '/wp-admin/',
            '/sites/default/files/',
            '/media/import/',
            '/site/wp-includes/',
            '/downloader/',
            '/.well-known/pki-validation/',
            '/.well-known/acme-challenge/',
            '/wp-content/uploads/',
            '/wp-content/upload/',
            '/wp-content/plugins/',
            '/wp-content/themes/',
            '/wp-includes/uploads/',
            '/wp-includes/upload/',
            '/wp-admin/js/widgets/',
            '/var/www/uploads/',
            '/admin/uploads/',
            '/upload/image/',
            '/wordpress/wp-includes/',
            '/admin/uploads/images/',
            '/upload_shell.php',
            '/var/www/html/shell.php',
            '/uploads/shell.php',
            '/files/shell.php',
            '/gel4y.php',
            '/simple.php',
            '/about.php',
            '/shell.php',
            '/cmd.php',
            '/test.php',
            '/shell20211028.php', 
            '/images/sfm.php',
            '/images/sendme.php',
            '/wp-admin/maint/about.php',
            '/wp-admin/maint/lol.php',
            '/wp-admin/js/91.php',
            '/wp-includes/24.php',
            '/wp-includes/js/k2ll.php',
            '/wp-admin/js/mintjs.php',
            '/wp-includes/js/b374k.php',
            '/wp-admin/js/pagin.php',
            '/wp-admin/js/widgets/about.php7',
            '/wp-admin/js/widgets/file.php',
            '/wp-includes/js/upload.php',
            '/wp-admin/js/maila.php',
            '/wp-admin/js/mailar.php',
            '/wp-includes/js/500.php',
            '/wp-admin/js/wp-czfnv.php',
            '/wp-admin/js/widgets/browser.php',
            '/wp-admin/js/widgets/uqgipxck.php',
            '/wp-includes/js/plupload/user_error.php',
            '/wp-admin/css/colors/coffee/about.php',
            '/wp-content/plugins/wp-file-upload/upload.php',
            '/wp-content/plugins/download-manager/file-upload.php',
            '/wp-admin/admin-ajax.php',
            '/components/com_joomdle/assets/upload.php',
            '/wp-content/uploads/google-in.php',
            '/wp-content/plugins/WordPressCore/include.php',
            '/wp-content/plugins/wp-help/admin/wp-fclass.php',
            '/wp-includes/css/dist/niil.php',
            '/wp-admin/css/colors/blue/colors.php',
            '/wp-admin/includes/alfa-rex.php',
            '/wp-admin/includes/senbox.php',
            '/wp-admin/images/rk2.php',
            '/wp-admin/includes/admin-ajax.php',
            '/wp-includes/css/alfa-rex.php',
            '/wp-includes/Text/Diff/Engine.php',
            '/images/pushy.php',
            '/uploads/upload_example.php',
            '/wp-admin/includes/send.php',
            '/wp-includes/js/tinymce/plugins/compat3x/css/index.php',
         
        ]

    def scan_site(self, site):
        domain = f"http://{normalize_url(site)}"
        for path in self.paths_to_check:
            self.check_path(domain, path)

    def check_path(self, domain, path):
        full_url = domain + path
        try:
            response = requests.get(full_url, headers=self.user_agent, timeout=10)
            if self.contains_webshell(response.content.decode()):
                logger.info(f'Success: Found webshell potential at {full_url}')
                with open('WebShells.txt', 'a') as f:
                    f.write(f"{full_url}\n")
            else:
                logger.warning(f'No webshell found at {full_url}')
        except requests.RequestException as e:
            logger.error(f'Error accessing {full_url}: {e}')

    @staticmethod
    def contains_webshell(content):
        indicators = [
            'Upload File: <input type="file" name="file"',
            '403Webshell',
            'MSQ_403',
            '#p@@#',
            'Jijle3',
            'drwxr-xr-x',
            'WSO 2.5',
            'WSO 2.6',
            'WSOX ENC',
            'WSO 5.1.4',
            'WSO 4.2.5',
            'WSO 4.2.6',
            'b374k',
            'Gecko',
            'MARIJuANA',
            'CHips L Pro sangad',
            'FoxWSO v1.2',
            'p0wny@shell:~#',
            'Mister Spy',
            'Yanz Webshell!',
            'B Ge Team File Manager',
            'Bypass Sh3ll',
            'xichang1',
            'Graybyt3 Was Here',
            'ineSec Team Shell',
            'C0d3d By Dr.D3m0',
            'WSO YANZ ENC BYPASS',
            'Gel4y Mini Shell',
            'X-Sec Shell V.3',
            '#No_Identity',
            'IndoXploit',
            'indoxploit',
            'Mini Shell',
            '[ Mini Shell ]',
            '[ HOME SHELL ]',
            '[+] MINI SH3LL BYPASS [+]',
            'ALFA TEaM Shell - v4.1-Tesla',
            'Doc Root:',
            'FilesMan',
            'Current dir:',
            'WebShellOrb 2.6',
            'Log In | ECWS',
            'AnonymousFox',
            'anonymousfox',
            'Mr.Combet WebShell',
            '#wp_config_error#',
            'WHY MINI SHELL',
            'PHU Mini Shell',
            'TheAlmightyZeus',
            'Tryag File Manager',
            'aDriv4-Priv8 TOOL',
            'Tiny File Manager 2.4.3',
            'One Hat Cyber Team',
            'Simple File Manage Design by index.php',
            'Bypass 403 Forbidden / 406 Not Acceptable / Imunify360 / Mini Shell',
            'Mini Shell By Black_Shadow',
            'Powered By Indonesian Darknet',
            'TEAM-0ROOT',
            'type="button">Upload File<',
            'shell_exec',
            'eval($_POST[\'cmd\'])',
        ]
        return any(indicator in content for indicator in indicators)

def run_scanner(target):
    scanner = WebShellFinder()
    scanner.scan_site(target)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error('Usage: python script.py <sites.txt>')
        sys.exit(1)

if __name__ == "__main__":
    print_banner()  # Display the banner at the start
    if len(sys.argv) != 2:
        logger.error('Usage: python Fixed-Finder.py <sites.txt>')
        sys.exit(1)

    targets = load_targets(sys.argv[1])
    with Pool(100) as pool:
        pool.map(run_scanner, targets)
