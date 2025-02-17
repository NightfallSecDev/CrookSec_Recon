
# CrookSec Recon Tool

The **CrookSec Recon Tool** is a Python-based tool designed for website reconnaissance. It automates the process of subdomain discovery, checking live subdomains, discovering URLs, and identifying potential vulnerabilities using various GF patterns. This tool is intended to assist cybersecurity professionals and researchers in gathering information and analyzing websites for security testing.

## Features

- Subdomain discovery with **Subfinder**.
- Check live subdomains using **httpx**.
- Discover URLs using **Katana** and **Waybackurls**.
- Filter URLs for potential vulnerabilities using various GF patterns such as:
  - `debug_logic`
  - `idor`
  - `img-traversal`
  - `interestingEXT`
  - `interestingparams`
  - `interestingsubs`
  - `jsvar`
  - `lfi`
  - `rce`
  - `redirect`
  - `sqli`
  - `ssrf`
  - `ssti`
  - `xss`
- Store results in an organized directory structure for easy access.

## Requirements

To run this tool, you'll need Python 3.x and the following Python libraries:

- `colorama` for colored terminal output.

You can install the dependencies using:

```bash
pip install -r requirements.txt
```

The tool also uses the following external tools that must be installed on your system:

- **Subfinder**: For subdomain discovery.
- **httpx**: To check live subdomains.
- **Katana**: For URL discovery.
- **Waybackurls**: For fetching archived URLs.
- **GF**: For vulnerability pattern matching.

## Installation

1. Clone this repository to your local machine:

```bash
https://github.com/NightfallSecDev/CrookSec_Recon.git
cd CrookSec_Recon
```

2. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install the external tools required for the script:

- **Subfinder**: [Installation Guide](https://github.com/projectdiscovery/subfinder)
- **httpx**: [Installation Guide](https://github.com/projectdiscovery/httpx)
- **Katana**: [Installation Guide](https://github.com/projectdiscovery/katana)
- **Waybackurls**: [Installation Guide](https://github.com/tomnomnom/waybackurls)
- **GF**: [Installation Guide](https://github.com/1ndianl33t/Gf-Patterns)

## Usage

1. Run the script:

```bash
python main.py
```

2. When prompted, enter the target domain for reconnaissance (e.g., `example.com`).

3. The tool will create a directory with the domain name and save all findings, including:
   - Subdomains
   - Live subdomains
   - Discovered URLs
   - Results from GF pattern matching

## Output

The output will be saved in a directory named after the target domain (e.g., `example.com/`). Inside the folder, you'll find the following files:

- `subdomain.txt`: List of discovered subdomains.
- `live_subdomain.txt`: List of live subdomains.
- `katana_output.txt`: Discovered URLs using Katana.
- `waybackurls_url.txt`: Archived URLs using Waybackurls.
- `urls.txt`: Combined list of URLs from Katana and Waybackurls.
- Vulnerability pattern files (e.g., `sqli.txt`, `xss.txt`, etc.) containing potential security vulnerabilities detected using GF patterns.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational and ethical use only. Do not use this tool against websites or domains without proper authorization. Always have written consent before performing any security testing.

