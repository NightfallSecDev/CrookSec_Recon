import os
import subprocess
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Function to print the colorful banner
def print_banner():
    print(Fore.GREEN + Style.BRIGHT + """
    ██████╗ ██████╗ ██████╗  ██████╗ ███████╗██╗███████╗███████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██╔════╝██╔════╝
    ██████╔╝██████╔╝██║  ██║██║  ██║█████╗  ██║███████╗███████╗
    ██╔══██╗██╔══██╗██║  ██║██║  ██║██╔══╝  ██║╚════██║╚════██║
    ██████╔╝██║  ██║██████╔╝██████╔╝███████╗██║███████║███████║
    ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚══════╝
    """)
    print(Fore.YELLOW + Style.BRIGHT + "CrookSec Recon Tool - Website Reconnaissance")
    print(Fore.CYAN + "-----------------------------------------------------------")

# Print the banner
print_banner()

# Prompt the user for the target domain
target_domain = input(Fore.MAGENTA + "Enter your target domain: ")

# Create a folder with the target domain name
target_folder = os.path.join(os.getcwd(), target_domain)
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(Fore.GREEN + f"Folder '{target_folder}' created successfully.")
else:
    print(Fore.RED + f"Folder '{target_folder}' already exists.")

# File paths for subdomain discovery and results
subdomain_file = os.path.join(target_folder, "subdomain.txt")
live_subdomain_file = os.path.join(target_folder, "live_subdomain.txt")
katana_output_file = os.path.join(target_folder, "katana_output.txt")
waybackurls_file = os.path.join(target_folder, "waybackurls_url.txt")
urls_file = os.path.join(target_folder, "urls.txt")

# Define the output files for each gf pattern inside the target folder
gf_patterns = [
    "debug_logic", "idor", "img-traversal", "interestingEXT", "interestingparams",
    "interestingsubs", "jsvar", "lfi", "rce", "redirect", "sqli", "ssrf", "ssti", "xss"
]

# Create the output file paths for each pattern dynamically inside the target folder
gf_output_files = {pattern: os.path.join(target_folder, f"{pattern}.txt") for pattern in gf_patterns}

# Run subfinder and save the output
print(Fore.CYAN + "[+] Running subfinder...")
subfinder_cmd = f"subfinder -d {target_domain} -o {subdomain_file}"
subprocess.run(subfinder_cmd, shell=True)
print(Fore.GREEN + f"[+] Subdomains saved in '{subdomain_file}'")

# Use httpx to check for live subdomains
print(Fore.CYAN + "[+] Checking for live subdomains using httpx...")
httpx_cmd = f"cat {subdomain_file} | httpx --silent -o {live_subdomain_file}"
subprocess.run(httpx_cmd, shell=True)
print(Fore.GREEN + f"[+] Live subdomains saved in '{live_subdomain_file}'")

# Use katana to perform URL discovery
print(Fore.CYAN + "[+] Running katana on all subdomains...")
katana_cmd = f"cat {subdomain_file} | katana -o {katana_output_file}"
subprocess.run(katana_cmd, shell=True)
print(Fore.GREEN + f"[+] Katana output saved in '{katana_output_file}'")

# Use waybackurls to fetch archived URLs
print(Fore.CYAN + "[+] Fetching archived URLs using waybackurls...")
waybackurls_cmd = f"cat {subdomain_file} | waybackurls > {waybackurls_file}"
subprocess.run(waybackurls_cmd, shell=True)
print(Fore.GREEN + f"[+] Archived URLs saved in '{waybackurls_file}'")

# Combine and sort the outputs, removing duplicates
print(Fore.CYAN + "[+] Combining and sorting URLs...")
sort_cmd = f"sort -u {katana_output_file} {waybackurls_file} > {urls_file}"
subprocess.run(sort_cmd, shell=True)
print(Fore.GREEN + f"[+] Combined and sorted URLs saved in '{urls_file}'")

# Run gf with all patterns and save the results in respective files
for pattern, output_file in gf_output_files.items():
    print(Fore.CYAN + f"[+] Filtering URLs with gf {pattern} pattern...")
    gf_cmd = f"cat {urls_file} | gf {pattern} > {output_file}"
    subprocess.run(gf_cmd, shell=True)
    print(Fore.GREEN + f"[+] {pattern} results saved in '{output_file}'")
