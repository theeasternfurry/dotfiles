config.load_autoconfig(False)


c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
c.content.javascript.enabled = True

c.tabs.position = "left"
c.tabs.show = 'switching'

c.qt.args = [
    'disable-gpu-compositing',
    'disable-software-rasterizer',
    'disable-features=CalculateNativeWinOcclusion'
]
