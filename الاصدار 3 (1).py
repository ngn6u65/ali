
import threading
import os
import random
import uuid
import requests
from user_agent import generate_user_agent as nn

class UsernameGenerator:
    def __init__(self):
        self.num = 0
        os.system('clear')
        print("""
✦ 𝗕𝘆 ➤ https://t.me/nnoomm4
━━━━━━━━━━━━━━━━━━━━
Starting Username List Generator
━━━━━━━━━━━━━━━━━━━━""")

        for _ in range(100):
            threading.Thread(target=self.get_usernames).start()

    def get_usernames(self):
        while True:
            k = random.choice([
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ'
            ])

            try:
                regions = ["AE", "IQ", "US", "FR", "DE"]
                languages = ["ar", "en", "fr", "de"]

                j = ''.join(random.choice(k) for i in range(random.randrange(4, 9)))
                i = "".join(random.choice('1234567890') for i in range(19))
                headers = {"User-Agent": f"com.zhiliaoapp.musically/{j} (Linux; U; Android {random.randrange(7,13)}; ar; RMX3269; Build/{j}; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)"}

                t = requests.get('https://www.tiktok.com/', headers=headers).cookies.get_dict()
                tt = t["ttwid"]

                response = requests.get(
                    'https://www.tiktok.com/api/search/user/full/?WebIdLastTime=1736179856&aid=1988&app_language=ar&app_name=tiktok_web&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv81&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=10&data_collection_enabled=false&device_id=7456835659580671494&device_platform=web_pc&focus_state=true&from_page=search&history_len=13&is_fullscreen=false&is_page_visible=true&keyword=ammar&odinId=7456835545702286341&os=linux&priority_region=&referer=https%3A%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%2540see.yyy4&region=IQ&root_referer=https%3A%2F%2Fwww.tiktok.com%2F%40see.yyy4&screen_height=800&screen_width=360&search_id=2025021309521452926674120EB71230EC&tz_name=Asia%2FBaghdad&user_is_login=false&verifyFp=verify_m735rlkh_KH1xH0SV_JlNX_4rMV_Bhmm_TeXFdT6MAMCT&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=ar&msToken=8qdfDG5yegNQlDbsQQxSjDdv-Lo5OlalRUCxcdjtI9Rrd1DIQLRXTCRinjpPh7bUktfOW4ybWuTL7oYLjZIxWyZ3SLRno2d7UWNxyDJADaH1PC_JQpGxwbNTus0UNKrRZ_T16U4rmKGd-xvSzOZIziTcTg==&X-Bogus=DFSzswVLWuXANjbttkLgYBYRRl7n&_signature=_02B4Z6wo00001QY4DCQAAIDAmCopNUhlpMUGOAiAACYm27'
                )
                g = response.cookies.get_dict().get('msToken')

                se = str(uuid.uuid4()).replace('-', '')
                cookies = {
                    'msToken': str(g),
                    'uid_tt': str(se[:16]),
                    'uid_tt_ss': str(se[:16]),
                    'sid_tt': str(se),
                    'sessionid': str(se),
                    'sessionid_ss': str(se),
                    'ttwid': tt,
                    'msToken': str(g)
                }

                headers = {
                    'authority': 'www.tiktok.com',
                    'accept': '*/*',
                    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'referer': 'https://www.tiktok.com/search/user?q=ahmed_faroojsq50&t=1736099390234',
                    'user-agent': str(nn()),
                }

                params = {
                    'WebIdLastTime': '1731681607',
                    'aid': '1988',
                    'app_language': random.choice(languages),
                    'app_name': 'tiktok_web',
                    'browser_language': 'ar-IQ',
                    'browser_name': 'Mozilla',
                    'browser_online': 'true',
                    'browser_platform': 'Linux armv81',
                    'browser_version': str(nn()),
                    'channel': 'tiktok_web',
                    'cookie_enabled': 'true',
                    'cursor': '70',
                    'data_collection_enabled': 'true',
                    'device_id': str(i),
                    'device_platform': 'web_pc',
                    'focus_state': 'true',
                    'from_page': 'search',
                    'history_len': '6',
                    'is_fullscreen': 'false',
                    'is_page_visible': 'true',
                    'keyword': str(j),
                    'odinId': '7339266198948037633',
                    'os': 'linux',
                    'priority_region': random.choice(regions),
                    'referer': '',
                    'region': random.choice(regions),
                    'screen_height': '800',
                    'screen_width': '360',
                    'search_id': '202501051749510BD3571B3B38F78E0D00',
                    'tz_name': 'Asia/Baghdad',
                    'user_is_login': 'true',
                    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                    'webcast_language': 'ar',
                    'msToken': str(g),
                    'X-Bogus': 'DFSzswVL4xhANn49t8VdsFcyeGaP',
                    '_signature': '_02B4Z6wo00001HnwuZwAAIDA9VDlFgbGYTh58L0AAHkO5e',
                }

                try:
                    r = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, cookies=cookies, headers=headers).json()
                except:
                    continue

                for q in r['user_list']:
                    fo = (q['user_info']['follower_count'])
                    self.num += 1
                    u = (q['user_info']['unique_id'])
                    print(f'{self.num} - User: {u} - Followers: {fo}')

                    if '..' in u or '_' in u:
                        continue
                    elif len(u) < 5 or len(u) > 30:
                        continue
                    else:
                        with open('S1.txt', 'a') as iu:
                            iu.write(u + '\n')

            except Exception as w:
                pass

# تشغيل السكربت
UsernameGenerator()