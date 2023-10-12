import time
import datetime
import requests
import json
from playsound import playsound


def bbs(s):
    if not is_alarm_on:
        print('[{}] {}'.format(datetime.datetime.now().strftime('%H:%M:%S'), s))


print('Fuck Apple')
sound_alarm = './alarm.mp3'
for i in range(2):
    playsound(sound_alarm)




list_iphone=['MU783ZD/A','MU773ZD/A','MU7A3ZD/A','MU793ZD/A']

# Corrige Code post
provinceCityDistrict='75016'

# Loop for checking iPhone status
count = 0
is_alarm_on = False
while True:
    for code_iphone in list_iphone:
        headers = {}
        if code_iphone == 'MU793ZD/A':
            print('Titan')
        elif code_iphone == 'MU783ZD/A':
            print('Blanc')
        elif code_iphone == 'MU773ZD/A':
            print('Noir')
        elif code_iphone == 'MU7A3ZD/A':
            print('Bleu')
              
        else:
            print('code_iphone')
        try:
            url = "https://www.apple.com/fr/shop/fulfillment-messages?pl=true&parts.0={}&location={}".format(code_iphone, provinceCityDistrict)
            response = requests.request("GET", url, headers=headers, data={})
            res_text = response.text
            res_json = json.loads(res_text)
            
            stores = res_json['body']['content']['pickupMessage']['stores']
            is_available = False
            lst_available = []
            print('--------------------------------')
            for item in stores:
                storeName = item['storeName']
                # For paris
                if storeName not in ['Champs-Élysées','Les Quatre Temps','Marché Saint-Germain','Opéra']:
                    continue
                # For paris
                pickupSearchQuote = item['partsAvailability'][code_iphone]['pickupSearchQuote']
                bbs('{} - {}'.format(storeName, pickupSearchQuote))
                storeSelectionEnabled = item['partsAvailability'][code_iphone]['messageTypes']['regular']['storeSelectionEnabled']
                if storeSelectionEnabled:
                    is_available = True
                    lst_available.append(storeName)
                    if code_iphone == 'MU793ZD/A':
                        print('Titan en stock')
                    elif code_iphone == 'MU783ZD/A':
                        print('Blanc en stock')
                    elif code_iphone == 'MU773ZD/A':
                        print('Noir en stock')
                    elif code_iphone == 'MU7A3ZD/A':
                        print('Bleu en stock')
     

            if len(lst_available) > 0:
                if not is_alarm_on:
                    is_alarm_on = True
                    # Display while iPhone is available
                    print('Apple Store suicent: \n{}'.format(','.join(lst_available)))
                for i in range(1000):
                    playsound(sound_alarm)



            if not is_available:
                is_alarm_on = False

        except Exception as err:
            bbs(err)
    count += 1
    if not is_alarm_on:
        print('--------------------------------')
        bbs('Nouveau test {} fois...'.format(count))
        time.sleep(60)
    else:
        time.sleep(60)
