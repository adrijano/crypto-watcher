# Crypto-watcher
# Coded by Adrijan Petek

import PySimpleGUI as sg
import requests
import json
import datetime
from json import (load as jsonload, dump as jsondump)
from os import path
import webbrowser

def tim():
    tim = datetime.datetime.now()
    return (tim.strftime("%H:%M:%S %d-%m-%Y"))

def euus():
    url = 'https://www.bitstamp.net/api/v2/ticker/eurusd/'
    try:
        r = requests.get(url)
        eu = float(json.loads(r.text)['last'])
        return eu
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")



def btcus():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        btc = float(json.loads(r.text)['last'])
        return btc
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def btceu():
    url = 'https://www.bitstamp.net/api/v2/ticker/btceur/'
    try:
        r = requests.get(url)
        bteth = float(json.loads(r.text)['last'])
        return bteth
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def btcgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/btcgbp/'
    try:
        r = requests.get(url)
        bteth = float(json.loads(r.text)['last'])
        return bteth
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def ethus():
    url = 'https://www.bitstamp.net/api/v2/ticker/ethusd/'
    try:
        r = requests.get(url)
        eth = float(json.loads(r.text)['last'])
        return eth
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")




def etheu():
    url = 'https://www.bitstamp.net/api/v2/ticker/etheur/'
    try:
        r = requests.get(url)
        eth = float(json.loads(r.text)['last'])
        return eth
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def ethgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/ethgbp/'
    try:
        r = requests.get(url)
        gbp = float(json.loads(r.text)['last'])
        return gbp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")



def xrpus():
    url = 'https://www.bitstamp.net/api/v2/ticker/xrpusd/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def xrpeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/xrpeur/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def xrpgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/xrpgbp/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")




def ltcus():
    url = 'https://www.bitstamp.net/api/v2/ticker/ltcusd/'
    try:
        r = requests.get(url)
        ltc = float(json.loads(r.text)['last'])
        return ltc
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def ltceu():
    url = 'https://www.bitstamp.net/api/v2/ticker/ltceur/'
    try:
        r = requests.get(url)
        ltc = float(json.loads(r.text)['last'])
        return ltc
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def ltcgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/ltcgbp/'
    try:
        r = requests.get(url)
        ltc = float(json.loads(r.text)['last'])
        return ltc
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def bchus():
    url = 'https://www.bitstamp.net/api/v2/ticker/bchusd/'
    try:
        r = requests.get(url)
        bch = float(json.loads(r.text)['last'])
        return bch
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def bcheu():
    url = 'https://www.bitstamp.net/api/v2/ticker/bcheur/'
    try:
        r = requests.get(url)
        bch = float(json.loads(r.text)['last'])
        return bch
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def bchgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/bchgbp/'
    try:
        r = requests.get(url)
        bch = float(json.loads(r.text)['last'])
        return bch
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def paxus():
    url = 'https://www.bitstamp.net/api/v2/ticker/paxusd/'
    try:
        r = requests.get(url)
        pax = float(json.loads(r.text)['last'])
        return pax
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def paxeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/paxeur/'
    try:
        r = requests.get(url)
        pax = float(json.loads(r.text)['last'])
        return pax
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def paxgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/paxgbp/'
    try:
        r = requests.get(url)
        pax = float(json.loads(r.text)['last'])
        return pax
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def xlmus():
    url = 'https://www.bitstamp.net/api/v2/ticker/xlmusd/'
    try:
        r = requests.get(url)
        xlm = float(json.loads(r.text)['last'])
        return xlm
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def xlmeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/xlmeur/'
    try:
        r = requests.get(url)
        xlm = float(json.loads(r.text)['last'])
        return xlm
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def xlmgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/xlmgbp/'
    try:
        r = requests.get(url)
        xlm = float(json.loads(r.text)['last'])
        return xlm
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def linkus():
    url = 'https://www.bitstamp.net/api/v2/ticker/linkusd/'
    try:
        r = requests.get(url)
        link = float(json.loads(r.text)['last'])
        return link
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def linkeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/linkeur/'
    try:
        r = requests.get(url)
        link = float(json.loads(r.text)['last'])
        return link
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def linkgb():
    url = 'https://www.bitstamp.net/api/v2/ticker/linkgbp/'
    try:
        r = requests.get(url)
        link = float(json.loads(r.text)['last'])
        return link
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def omgus():
    url = 'https://www.bitstamp.net/api/v2/ticker/omgusd/'
    try:
        r = requests.get(url)
        omg = float(json.loads(r.text)['last'])
        return omg
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def omgeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/omgeur/'
    try:
        r = requests.get(url)
        omg = float(json.loads(r.text)['last'])
        return omg
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def omggb():
    url = 'https://www.bitstamp.net/api/v2/ticker/omggbp/'
    try:
        r = requests.get(url)
        omg = float(json.loads(r.text)['last'])
        return omg
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def knceu():
    url = 'https://www.bitstamp.net/api/v2/ticker/knceur/'
    try:
        r = requests.get(url)
        knc = float(json.loads(r.text)['last'])
        return knc
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def kncus():
    url = 'https://www.bitstamp.net/api/v2/ticker/kncusd/'
    try:
        r = requests.get(url)
        knc = float(json.loads(r.text)['last'])
        return knc
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def mkrus():
    url = 'https://www.bitstamp.net/api/v2/ticker/mkrusd/'
    try:
        r = requests.get(url)
        mkr = float(json.loads(r.text)['last'])
        return mkr
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def mkreu():
    url = 'https://www.bitstamp.net/api/v2/ticker/mkreur/'
    try:
        r = requests.get(url)
        mkr = float(json.loads(r.text)['last'])
        return mkr
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")    

def zrxus():
    url = 'https://www.bitstamp.net/api/v2/ticker/zrxusd/'
    try:
        r = requests.get(url)
        zrx = float(json.loads(r.text)['last'])
        return zrx
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def zrxeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/zrxeur/'
    try:
        r = requests.get(url)
        zrx = float(json.loads(r.text)['last'])
        return zrx
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")    


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}

def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window



def create_main_window(settings):
    sg.theme(settings['theme'])

    menu_def = [['&Menu',['Settings', 'E&xit']],
                ['&Help','&About...']]

    right_click_menu = ['Unused', ['Settings', 'E&xit']]
    
    layout =   [[sg.Menu(menu_def)],
                [sg.Text('', size=(28,1), font=('Helvetica', 11), key='_DATE_'),
                 sg.Text('1 EUR  =', font=('Helvetica', 11)), sg.Text('', size=(6,1), font=('Helvetica', 11), key='eurusd'),
                 sg.Button('', key='paypal', size=(12,1), font=('Helvetica', 9), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                           image_filename='png/paypal.png', image_size=(80, 50), image_subsample=2, border_width=0),
                 sg.Button('', key='bitcoin', size=(12,1), font=('Helvetica', 9), button_color=(sg.theme_background_color(), sg.theme_background_color()),
                           image_filename='png/bitcoin.png', image_size=(80, 60), image_subsample=2, border_width=0)],
                
                [sg.Text('')],
                [sg.Text('#', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Text('Name', font=('Helvetica', 11, 'bold'), size=(24,1)),
                 sg.Text(' Price USD', size=(10,1), font=('Helvetica', 11, 'bold')), sg.Text(' Price EUR', size=(10,1), font=('Helvetica', 11, 'bold')),
                 sg.Text(' Price GBP', size=(10,1), font=('Helvetica', 11, 'bold'))],
                
                [sg.Text('1', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/bit.png', size=(30, 30)),
                 sg.Text('Bitcoin (BTC)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='btcu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='btce'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='btcgb')],
                
                [sg.Text('2', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/eth.png', size=(30, 30)),
                 sg.Text('Ethereum (ETH)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='ethu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='ethe'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='ethgb')],
                
                [sg.Text('3', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/xrp.png', size=(30, 30)),
                 sg.Text('Ripple (XRP)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='xrpu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='xrpe'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='xrpgb')],
                
                [sg.Text('4', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/lite.png', size=(30, 30)),
                 sg.Text('Litecoin (LTC)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='ltcu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='ltce'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='ltcgb')],
                
                [sg.Text('5', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/bch.png', size=(30, 30)),
                 sg.Text('Bitcoin Cash (BCH)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='bchu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='bche'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='bchgb')],
                
                [sg.Text('6', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/pax.png', size=(30, 30)),
                 sg.Text('Paxos Standard (PAX)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='paxu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='paxe'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='paxgb')],
                
                [sg.Text('7', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/stellar.png', size=(30, 30)),
                 sg.Text('Stellar (XLM)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='xlmu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='xlme'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='xlmgbp')],

                [sg.Text('8', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/link.png', size=(30, 30)),
                 sg.Text('Chainlink (LINK)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='linku'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='linke'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='linkgb')],

                [sg.Text('9', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/omg.png', size=(30, 30)),
                 sg.Text('OMG Network(OMG)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='omgu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='omge'), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='omggb')],

                [sg.Text('10', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/knc.png', size=(30, 30)),
                 sg.Text('Kyber Network(KNC)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='kncu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='knce'), sg.Text('coming soon', size=(10,1), font=('Helvetica', 11),  key='kncgb')],

                [sg.Text('11', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/mkr.png', size=(30, 30)),
                 sg.Text('Maker(MKR)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='mkru'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='mkre'), sg.Text('coming soon', size=(10,1), font=('Helvetica', 11),  key='mkrgb')],

                [sg.Text('12', font=('Helvetica', 11, 'bold'), size=(2,1)), sg.Image('png/zrx.png', size=(30, 30)),
                 sg.Text('0x (ZRX)', font=('Helvetica', 11), size=(20,1)), sg.Text('', size=(10,1), font=('Helvetica', 11),  key='zrxu'),
                 sg.Text('', size=(10,1), font=('Helvetica', 11),  key='zrxe'), sg.Text('coming soon', size=(10,1), font=('Helvetica', 11),  key='zrxgb')]]

    return sg.Window('Crypto Watcher', layout=layout,
                     right_click_menu=right_click_menu)

def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    while True:
        if window is None:
            window = create_main_window(settings)
        time = tim()
        eurusd = euus()
        btcusd = btcus()
        btceur = btceu()
        btcgbp = btcgb()
        ethusd = ethus()
        etheur = etheu()
        ethgbp = ethgb()
        xrpusd = xrpus()
        xrpeur = xrpeu()
        xrpgbp = xrpgb()
        ltcusd = ltcus()
        ltceur = ltceu()
        ltcgbp = ltcgb()
        bchusd = bchus()
        bcheur = bcheu()
        bchgbp = bchgb()
        paxusd = paxus()
        paxeur = paxeu()
        paxgbp = paxgb()
        xlmeur = xlmeu()
        xlmusd = xlmus()
        xlmgbp = xlmgb()
        linkusd = linkus()
        linkeur = linkeu()
        linkgbp = linkgb()
        omgusd = omgus()
        omgeur = omgeu()
        omggbp = omggb()
        knceur = knceu()
        kncusd = kncus()
        mkrusd = mkrus()
        mkreur = mkreu()
        zrxusd = zrxus()
        zrxeur = zrxeu()
        
        event, values = window.Read(timeout=0)
        window.Element('_DATE_').Update(str(time))
        window.Element('eurusd').Update('$ '+str(eurusd))
        window.Element('btcu').Update('$ '+str(btcusd))
        window.Element('btce').Update('€ '+str(btceur))
        window.Element('btcgb').Update('$ '+str(btcgbp))
        window.Element('ethu').Update('$ '+str(ethusd))
        window.Element('ethe').Update('€ '+str(etheur))
        window.Element('ethgb').Update('$ '+str(ethgbp))
        window.Element('xrpu').Update('$ '+str(xrpusd))
        window.Element('xrpe').Update('€ '+str(xrpeur))
        window.Element('xrpgb').Update('$ '+str(xrpgbp))
        window.Element('ltcu').Update('$ '+str(ltcusd))
        window.Element('ltce').Update('€ '+str(ltceur))
        window.Element('ltcgb').Update('$ '+str(ltcgbp))
        window.Element('bchu').Update('$ '+str(bchusd))
        window.Element('bche').Update('€ '+str(bcheur))
        window.Element('bchgb').Update('$ '+str(bchgbp))
        window.Element('paxu').Update('$ '+str(paxusd))
        window.Element('paxe').Update('€ '+str(paxeur))
        window.Element('paxgb').Update('$ '+str(paxgbp))
        window.Element('xlme').Update('€ '+str(xlmeur))
        window.Element('xlmu').Update('$ '+str(xlmusd))
        window.Element('xlmgbp').Update('$ '+str(xlmgbp))
        window.Element('linku').Update('$ '+str(linkusd))
        window.Element('linke').Update('$ '+str(linkeur))
        window.Element('linkgb').Update('$ '+str(linkgbp))
        window.Element('omgu').Update('$ '+str(omgusd))
        window.Element('omge').Update('$ '+str(omgeur))
        window.Element('omggb').Update('$ '+str(omggbp))
        window.Element('kncu').Update('$ '+str(kncusd))
        window.Element('knce').Update('$ '+str(knceur))
        window.Element('mkru').Update('$ '+str(mkrusd))
        window.Element('mkre').Update('$ '+str(mkreur))
        window.Element('zrxu').Update('$ '+str(zrxusd))
        window.Element('zrxe').Update('$ '+str(zrxeur))

        if event in (None, 'Exit'):
            break
        elif event == 'About...':
            window.disappear()
            sg.popup('Created by Adrijan P.', 'Crypto Watcher', 'Version 2.0')
            window.reappear()

        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)

        elif event == 'paypal':
            webbrowser.open_new_tab("https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=PFB6A6HLAQHC2&source=url")
        
        elif event == 'bitcoin':
            webbrowser.open_new_tab("https://commerce.coinbase.com/checkout/149a6235-ec7e-4d3b-a1ae-b08c4f08b4f6")

        
    window.Close()   

main()
