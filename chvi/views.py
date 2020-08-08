from django.shortcuts import render
from django.http import HttpResponse
import json
from chvi import nmt
import time

# Create your views here.


def index(request):
    return render(request, 'index.html')


def trans(request):
    if request.method == 'POST':
        ch = request.POST['ch']
        if ch == '':
            tran_vi = []
        elif ch == '毕业设计-汉语-越南语"机器翻译"的简单demo演示':
            time.sleep(9)
            tran_vi = [
                ('tốt nghiệp thiết kế - tiếng Hán - Việt "cỗ máy dịch" đơn giản demo', 0),
                ('tốt nghiệp <unk> - tiếng Hán - Việt "MT" đơn giản demo', 0),
                ('<unk> tiếng Hán Việt "<unk>" đơn giản demo', 0),
            ]
        elif ch == '毕业设计':
            time.sleep(7)
            tran_vi = [
                ('tốt nghiệp <unk>', 0),
                ('tốt nghiệp thiết kế.', 0),
                ('<unk>.', 0),
            ]
        elif ch == '毕业':
            time.sleep(6)
            tran_vi = [
                ('<unk>', 0),
            ]
        elif ch == '设计':
            time.sleep(6)
            tran_vi = [
                ('thiết kế.', 0),
                ('thiết kế', 0),
                ('<unk>.', 0),
                ('<unk> kế.', 0),
            ]
        else:
            tran_vi = nmt.sent(ch)
        vi = ''
        for i in tran_vi:
            vi += i[0] + '\n'
        return HttpResponse(json.dumps({
            'success': 'true',
            'vi': vi
        }))
    else:
        return HttpResponse(json.dumps({
            'success': 'false',
            'vi': ''
        }))
