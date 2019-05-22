from google_speech import Speech
import os
import time


def notice(text, lang='vi'):
    try:
        speech = Speech(text, lang)
        speech.play()
    except Exception:
        print('No network connect! So i can not speak for you!')

# use file D.txt as input to speech
def notice_by_speech(path='data', filename='D.txt', lang='vi'):
    if filename in os.listdir(path):

        # reach content file
        abs_path = os.path.join(path, filename)
        content = open(abs_path, 'r').read()

        if content is None or content=="":
            return
        # empty file
        with open(abs_path, 'w') as f:
            f.write("")
        # print(content)
        notice(content)

while True:
    notice_by_speech()
    time.sleep(0.5)