
class banner(object):
    def __init__(self, version):
        self.version = version

    def banner(self):
        banner = """
          ____
        ,'  , `.                   .--.--.
     ,-+-,.' _ |                  /  /    '.
  ,-+-. ;   , ||  ,---.    ,---. |  :  /`. /                           ,---,
 ,--.'|'   |  ;| '   ,'\  '   ,'\;  |  |--`                        ,-+-. /  |
|   |  ,', |  ':/   /   |/   /   |  :  ;_      ,---.    ,--.--.   ,--.'|'   |
|   | /  | |  |.   ; ,. .   ; ,. :\  \    `.  /     \  /       \ |   |  ,"' |
'   | :  | :  |'   | |: '   | |: : `----.   \/    / ' .--.  .-. ||   | /  | |
;   . |  ; |--''   | .; '   | .; : __ \  \  .    ' /   \__\/: . .|   | |  | |
|   : |  | ,   |   :    |   :    |/  /`--'  '   ; :__  ," .--.; ||   | |  |/
|   : '  |/     \   \  / \   \  /'--'.     /'   | '.'|/  /  ,.  ||   | |--'
;   | |`-'       `----'   `----'   `--'---' |   :    ;  :   .'   |   |/
|   ;/                                       \   \  /|  ,     .-.'---'
'---'                                         `----'  `--`---'
"""

        text = """MooScan - by @vortexau
Please do not use this tool against environments you do not have explicit
permission to scan.
The author will not be held responsible for any unauthorised usage of this
software.
"""
        return banner + text
