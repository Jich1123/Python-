from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from baidu.wordToVoice import *
from wsgiref.util import FileWrapper
import os
import wave
# Create your views here.
def index(request):
    return render(request, 'index.html')

def file_iterator(file_name, chunk_size=8192, offset=0, length=None):
    with open(file_name, "rb") as f:
        f.seek(offset, os.SEEK_SET)
        remaining = length
        while True:
            bytes_length = chunk_size if remaining is None else min(remaining, chunk_size)
            data = f.read(bytes_length)
            if not data:
                break
            if remaining:
                remaining -= len(data)
            yield data

def play(request):
    # f = wave.open(r'F:\python学习\Python-\tts_ai\tts\baidu\wavs\result.wav', 'rb')
    # params = f.getparams()
    # nframes = params[4]
    # str_data = f.readframes(nframes)
    # f.close()
    # fname =file_iterator(r"F:\python学习\Python-\tts_ai\tts\baidu\wavs\result.wav")
    # f = open(fname, 'rb')
    # return StreamingHttpResponse(fname)
    fname = r"F:\python学习\Python-\tts_ai\tts\baidu\wavs\result.wav"
    size = os.path.getsize(fname)
    content_type = 'application/octet-stream'
    resp = StreamingHttpResponse(FileWrapper(open(fname, 'rb')), content_type=content_type)
    resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp


def tts_action(request):
    words = request.POST.get('words', '默认')
    action_tts(words)
    print(os.getcwd())
    lujin = os.path.join(os.getcwd(), 'baidu', 'wavs', 'result.wav')
    return render(request, 'play.html',{'lujin':lujin})