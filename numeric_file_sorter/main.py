import os
import sys
import re
import path


data = os.listdir()

data[0]
# take director 
# take number 
# put number in the front
# numbers = [ os.rename(d, d+ str(re.search("[0-9]\W[0-9]",d))) for d in data if re.search("[0-9]\W[0-9]",d)  ]

for d in data:
    if x := re.search("[0-9]\W[0-9] [a-zA-Z]",d):
        # os.rename(d, x[0] + ' ' + d)
        print(x)
        print(d[:3])
        print(d[4:])
        os.rename(d, f'{d[:3]} P{d[4:]}')

def sort_playlist(playlist_path:str, re_pattern: str) -> None:
    for video in playlist_path:
        if pattern := re.findall(re_pattern, video):
            os.rename(video, f'{pattern[0]}_{video}' )
            
