import requests, json

# define program-wide variables

BIGIP_USER = 'admin'
BIGIP_PASS = 'M'

def show_VIP(BIGIP_URL_BASE, bigip, kind, VS_ADDRESS):
    if kind == 'VIP':
        kind2 = 'cs-server-addr'
    elif kind == 'pool member':
        kind2 = 'ss-server-addr'

    return bigip.get('%s/sys/connection?options=%s+%s' % (BIGIP_URL_BASE, kind2, VS_ADDRESS))

def main(datacenter, kind, IP):
    """ datacenter = which datacenter the load balancer is in
        kind = VIP('cs-server-addr') or pool member('ss-server-addr')
        IP = ip of either VIP or pool member
    """

    if datacenter.strip().upper() == "IAD":
        BIGIP_ADDRESS = '6.5.4.3'
    elif datacenter.strip().upper() == "LAS":
        BIGIP_ADDRESS = '1.2.3.4'
    else:
        return "THATS NOT A DATACENTER!!"
        sys.exit()

    # REST resource for BIG-IP that all other requests will use
    bigip = requests.session()
    bigip.auth = (BIGIP_USER, BIGIP_PASS)
    bigip.verify = False
    bigip.headers.update({'Content-Type' : 'application/json'})

    # Requests requires a full URL to be sent as arg for every request, define base URL globally here
    BIGIP_URL_BASE = 'https://%s/mgmt/tm' % BIGIP_ADDRESS

    r = show_VIP(BIGIP_URL_BASE, bigip, kind, IP)
    response = json.loads(r.text)

    return response['apiRawValues']['apiAnonymous']

if __name__ == "__main__":
    main()
