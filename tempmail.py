import logging as _A, requests as _B
from telegram import Update as _C
import base64 as _b64
from telegram.ext import Updater as _D, CommandHandler as _E, CallbackContext as _F

_G = '6127129179:AAGxr-0cr0CO7JK9B298WkL1AFoKcLbDsrU'
_A.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=_A.INFO)
_H = _A.getLogger(__name__)
_I = "https://www.1secmail.com/api/v1/"

def _J(_K=1):
    _L = {"action": "genRandomMailbox", "count": _K}
    _M = _B.get(_I, params=_L)
    return _M.json() if _M.status_code == 200 else None

def _N(_O):
    _P, _Q = _O.split("@")
    _R = {"action": "getMessages", "login": _P, "domain": _Q}
    _S = _B.get(_I, params=_R)
    return _S.json() if _S.status_code == 200 else None

def _T(_U, _V): _U.message.reply_text('Welcome to TempMailBot! By Forever Knights Made by @WASCIV Use /getmail to get a temporary email address.')

def _W(_X, _Y):
    _Z = _J()
    if _Z:
        _0 = _Z[0]
        _Y.user_data['temp_email'] = _0
        _X.message.reply_text(f'Your temporary email address is: {_0}')
    else: _X.message.reply_text('Sorry, something went wrong. Please try again later. If problem persists DM @WASCIV ')

def _1(_2, _3):
    _4 = _3.user_data.get('temp_email')
    if _4:
        _5 = _N(_4)
        if _5 is not None:
            if _5:
                _2.message.reply_text('Here are your recent emails:')
                for _6 in _5:
                    _7 = _8(_4, _6['id'])
                    if _7:
                        _2.message.reply_text(f"From: {_7['from']}\nSubject: {_7['subject']}\nDate: {_7['date']}\n\nBody: {_7['body']}")
                    else: _2.message.reply_text('Failed to fetch email content. Please try again later.')
            else: _2.message.reply_text('No emails found. Please wait for a while and try again.')
        else: _2.message.reply_text('Something went wrong. Please try again later.')
    else: _2.message.reply_text('No temporary email found. Please use /getmail to get a new temporary email.')

def _8(_9, _a):
    _b = _9.split("@")
    _c = _B.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={_b[0]}&domain={_b[1]}&id={_a}')
    return _c.json() if _c.status_code == 200 else None

_obf_message = b'U29tZVJhbmRvbVN0cmluZ0Zvck9iZnVzY2F0aW9uQDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MCAmJiYgSm9pbiBUZWxlZ3JhbSBDaGFubmVsIEBmb3JldmVyX2tuaWdodHNzICYmJg=='
decoded_bytes = _b64.b64decode(_obf_message)
decoded_str = decoded_bytes.decode('utf-8')
start_index = decoded_str.find('&&&') + 3
end_index = decoded_str.rfind('&&&')
message = decoded_str[start_index:end_index]
print(message)    

def _d():
    _e = _D(_G, use_context=True)
    _f = _e.dispatcher
    _f.add_handler(_E('start', _T))
    _f.add_handler(_E('getmail', _W))
    _f.add_handler(_E('fetchmail', _1))
    _e.start_polling()
    _e.idle()

if __name__ == '__main__':
    _d()
