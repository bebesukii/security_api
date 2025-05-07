import pytest
from core.infrastructure.scanners.dns_scan import DNSResolver

def test_dns_resolver():
    resolver = DNSResolver("example.com")
    report = resolver.run()
    assert "example.com" in report["domain"]
