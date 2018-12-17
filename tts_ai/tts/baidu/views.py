from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from baidu.wordToVoice import *
import mimetypes
from wsgiref.util import FileWrapper
import re
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

def play_bak(request):
    # f = wave.open(r'F:\python学习\Python-\tts_ai\tts\baidu\wavs\result.wav', 'rb')
    # params = f.getparams()
    # nframes = params[4]
    # str_data = f.readframes(nframes)
    # f.close()
    # fname =file_iterator(r"F:\python学习\Python-\tts_ai\tts\baidu\wavs\result.wav")
    # f = open(fname, 'rb')
    # return StreamingHttpResponse(fname)123
    fname = r"F:\python学习\Python-\tts_ai\tts\baidu\wavs\result.wav"
    size = os.path.getsize(fname)
    content_type = 'application/octet-stream'
    resp = StreamingHttpResponse(FileWrapper(open(fname, 'rb')), content_type=content_type)
    resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp



def play(request):
    path = r"F:\python学习\Python-\tts_ai\tts\baidu\wavs\result.wav"
    """将视频文件以流媒体的方式响应"""
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)
    range_match = range_re.match(range_header)
    size = os.path.getsize(path)
    content_type, encoding = mimetypes.guess_type(path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = first_byte + 1024 * 1024 * 8  # 8M 每片,响应体最大体积
        if last_byte >= size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(file_iterator(path, offset=first_byte, length=length), status=206,
                                     content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        # 不是以视频流方式的获取时，以生成器方式返回整个文件，节省内存
        resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp


def tts_action(request):
    words = request.POST.get('words', '默认')
    action_tts(words)
    print(os.getcwd())
    lujin = os.path.join(os.getcwd(), 'baidu', 'wavs', 'result.wav')
    return render(request, 'play.html',{'lujin':lujin})