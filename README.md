# DeepL Ex: Unlimited Free DeepL Translation

> :warning: This project is currently under the development.

This project is inspired by [Vincent Young](https://github.com/missuo)'s [DeepLX](https://github.com/OwO-Network/DeepLX).

But the project does not support Glossaries, thus I made this with DeepL's new internal APIs.

## Prerequisites
```
pip install aiohttp brotli
```

## Usage

```python
import asyncio
import deeplex


async def main():
    texts = await deeplex.translate(
        'Hello World, John!', 'EN', 'DE',
        glossaries={'John': 'Python'},
    )

    # ['Hallo Welt, Python!', 'Hallo Python, Welt!', 'Hallo, Python!', 'Hallo Python!']
    print(texts)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.close()
```

# License

Licensed under the [MIT license](https://github.com/OrigamiDream/deeplex/blob/main/LICENSE).
