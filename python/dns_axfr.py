#!/usr/bin/env python3

import dns.query
import dns.zone
import dns.resolver

# replace the example ip address and domain name with an actual ip and domain #

z = dns.zone.from_xfr(dns.query.xfr('123.456.789.10', 'example.com'))
names = z.nodes.keys()
names.sort()
for n in names:
    print(z[n].to_text(n))
