config.load_autoconfig(False)

c.qt.args = [
    'disable-gpu-compositing',
    'disable-software-rasterizer',
    'disable-features=CalculateNativeWinOcclusion'
]

c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
c.content.javascript.enabled = True

# File selection
c.fileselect.handler = 'external'
c.fileselect.single_file.command = ['zenity', '--file-selection', '--title=Select File']
c.fileselect.multiple_files.command = ['zenity', '--file-selection', '--multiple', '--title=Select Files']
c.fileselect.folder.command = ['zenity', '--file-selection', '--directory', '--title=Select Folder']

c.tabs.position = "left"
c.tabs.show = 'switching'


