from bot.config import settings

headers_notcoin = {
    'Accept': 'application/json',
    'Accept-Language': f'{settings.LANGUAGE_CODE},{settings.LANGUAGE_CODE};q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Origin': 'https://webapp.notcoin.tg',
    'Referer': 'https://webapp.notcoin.tg/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-mobile': '?1',
    'Sec-Ch-Ua-platform': '"Android"',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36',
    'X-Auth-Token': 'Bearer null',
}