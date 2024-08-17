import network

def do_connect(networkName, networkPassword):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(networkName, networkPassword)
        while not wlan.isconnected():
            pass
    print('connected!')

if not param == '':
    networkName, networkPassword = param, param2
    do_connect(networkName, networkPassword)