import json
import random
import time
from typing import Dict, Optional, List

import aiohttp

headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 '
                  'Safari/605.1.15',
    'Connection': 'keep-alive',
}


class _TooManyRequestsError(Exception):
    pass


def _create_timestamp(i_size: int) -> int:
    ts = int(time.time() * 1000)

    if i_size == 0:
        return ts

    i_size += 1
    return ts - ts % i_size + i_size


async def _translate(text: str,
                     src: str = 'en',
                     dst: str = 'de',
                     num_alternatives: int = 3,
                     glossaries: Optional[Dict[str, str]] = None,
                     no_translates: List[str] = None,
                     proxy: str = None):
    i_size = text.count('i')
    random.seed(time.time())
    num = random.randint(8300000, 8399998) * 1000

    num_alternatives = max(0, min(3, num_alternatives))

    dicts = []
    if glossaries is not None:
        for key, value in glossaries.items():
            dicts.append('{}\t{}'.format(key, value))
    if no_translates is not None:
        for word in no_translates:
            dicts.append('{}\t{}'.format(word, word))

    data = {
        'jsonrpc': '2.0',
        'method': 'LMT_handle_jobs',
        'params': {
            'jobs': [{
                'kind': 'default',
                'sentences': [{
                    'text': text,
                    'id': 1,
                    'prefix': '',
                }],
                'raw_en_context_before': [],
                'raw_en_context_after': [],
                'preferred_num_beams': num_alternatives + 1,
            }],
            'lang': {
                'target_lang': dst.upper(),
                'preference': {
                    'weight': {},
                    'default': 'default',
                },
                'source_lang_computed': src.upper(),
            },
            'priority': 1,
            'commonJobParams': {
                'mode': 'translate',
                'textType': 'plaintext',
                'browserType': 1,
                'termbase': {
                    'dictionary': '\n'.join(dicts)
                }
            },
            'timestamp': _create_timestamp(i_size),
        },
        'id': num,
    }
    data = json.dumps(data, ensure_ascii=False)

    if (num + 5) % 29 == 0 or (num + 3) % 13 == 0:
        data = data.replace('"method":"', '"method" : "', -1)
    else:
        data = data.replace('"method":"', '"method": "', -1)

    async with aiohttp.ClientSession() as session:
        async with session.post('https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs',
                                data=data,
                                headers=headers,
                                proxy=proxy) as res:
            if res.status == 429:
                raise _TooManyRequestsError()

            body = await res.json()

    texts = []
    for translation in body['result']['translations']:
        for beam in translation['beams']:
            for sentence in beam['sentences']:
                texts.append(sentence['text'])
    return texts
