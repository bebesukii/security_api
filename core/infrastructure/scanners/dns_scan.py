import dns.resolver 
import whois 
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict

class DNSResolver:
    def __init__(self, domain: str, record_types: List[str] = None):
        self.domain = domain
        self.record_types = record_types or ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
        self.resolver = dns.resolver.Resolver()
        self.report = {
            "domain": domain,
            "resolved_at": datetime.utcnow().isoformat(),
            "records": {},
            "whois": {},
            "nmap": []
        }

    def resolve_all(self):
        for record_type in self.record_types:
            try:
                answers = self.resolver.resolve(self.domain, record_type)
                self.report["records"][record_type] = [str(data) for data in answers]
            except Exception:
                self.report["records"][record_type] = []

    def get_whois(self):
        try:
            w = whois.whois(self.domain)
            self.report["whois"] = {k: str(v) for k, v in w.items() if v}
        except Exception:
            self.report["whois"] = {}

    def run_nmap(self):
        try:
            result = subprocess.run(
                ["nmap", "-T4", "-F", self.domain, "-oX", "-"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            root = ET.fromstring(result.stdout)
            for host in root.findall("host"):
                ip = host.find("address").attrib.get("addr")
                ports = [
                    {
                        "port": port.attrib["portid"],
                        "state": port.find("state").attrib["state"],
                        "service": port.find("service").attrib.get("name", "")
                    }
                    for port in host.findall(".//port")
                ]
                self.report["nmap"].append({"ip": ip, "ports": ports})
        except Exception:
            self.report["nmap"] = []

    def run(self) -> Dict:
        self.resolve_all()
        self.get_whois()
        self.run_nmap()
        return self.report
