## Bash Scripts

### ping-sweep.sh

Example: `./ping-sweep.sh 192.168.2` (Only need the first 3 octects of the target IP)

This will ping the IP range from 1 - 254 to see which hosts are up.

***

### recon.sh

Example: `./recon.sh 192.168.2.1`

This runs nmap, gobuster, and whatweb on a host and saves results into results file.