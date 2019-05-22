from google_speech import Speech
import os
def notice(text, lang='vi'):
    try:
        speech = Speech(text, lang)
        speech.play()
    except Exception:
        print('No network connect! So i can not speak for you!')

# use file D.txt as input to speech
def notice(path='data', filename='D.txt', lang='vi'):
    if filename in os.listdir(path):
        abs_path = os.path.join(path, filename)
        content = open(abs_path, 'r').read()
        os.remove(abs_path)
        print(content)
        try:
            speech = Speech(content, lang)
            speech.play()
        except Exception:
            print('No network connect! So i can not speak for you!')

# read_txt()