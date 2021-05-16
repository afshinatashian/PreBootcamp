import random
import json
from web3 import Web3
# import json

MAIN_URL = "https://mainnet.infura.io/v3/bb055071bba745488eda95512a6d0035"
URL = 'https://8cf41633363c49a584fbfb0b556a5927.ropsten.rpc.rivet.cloud/'
URL = 'wss://ropsten.infura.io/ws/v3/bb055071bba745488eda95512a6d0035'

w3 = Web3(Web3.WebsocketProvider(URL))
# w3 = Web3(Web3.HTTPProvider(URL))


def _checking(_addr):
    '''
    ورودی تابع ک استرینگ است که چک میشمود ایا ادرس معبتری هست یا خیر
    false یا addrress درنهایت
    خارح میشود
    '''
    if not isinstance(_addr, str):
        print("ادرس بد وارد کردی باید یک استرینگ باشه")
        return False
    try:
        if not w3.isConnected():
            print("نت مشکل داره ")
            return False
        addr_ = Web3.toChecksumAddress(_addr)
        if not _addr:
            print("ادرس بدی وارد کردی شرمنده تم")
            return False
        return addr_
    except Exception as e:
        print(e)
        print("یه مشکلی وجود داره ×ـ× مثلا نتت ضعیفه")
        return False


def balance(_addr: str) -> float:
    """
    اینجا ادرس خواسته رو به تابع بدید
    توی خروجی یه عدد میده که همون باقیمانده ی حسابش هستش :)
    """
    addr_ = _checking(_addr)
    return float(w3.eth.get_balance(addr_) / 10**18)



def transfer(_to_addr: str, _value: float, private_key: str, public_key: str ,_nounce:int ):
    to_addr_ = _checking(_to_addr)
    public_key = _checking(public_key)
    
    if to_addr_ and public_key:
        try:
            if balance(public_key) < _value:
                print("پول ت کمه ، نمیتونی کمک کنی ")
                return False
            p = w3.eth.gas_price
            
            trancation = {
                'from': public_key,
                'to': to_addr_,
                "gas": "0x200000",
                "gasPrice": p,
                "nonce": _nounce,
                "value": int(_value * 10**18),
            }
            raw_trx = w3.eth.account.privateKeyToAccount(
                private_key).sign_transaction(trancation)
            res = w3.eth.send_raw_transaction(raw_trx.rawTransaction).hex()
            return res
        except Exception as e:
            print(e)
            print("یک اتفاقی افتاده که من نمیدونم ....")
            return 0

            
def get_key(val):
    for key, value in balance_dict.items():
         if val == value:
             return key

balance_dict={}
# account_list=["0xAf77fB90baCE88edad8be674232C4a072BdC29A3" , "0x196eaeBfCF7beaFe7C5C52d3412BB677827924e9" , "0x4dA5d4E0b0AfE7663fdcAB76c2C1e91e416A80bc"]
# account_list=input()
with open("wallets.json", 'r') as f1:
    account_list = (json.loads(f1.read()))
for i in account_list:
    balance_dict[i] = balance(i)
    # balance_list.append(balance(i))

average_balance=sum(balance_dict.values())/len(balance_dict)


low_balance={}
for k,v in balance_dict.items():
    for b in balance_dict.values():
        if b < average_balance/10:
            key_b=get_key(b)
            low_balance[key_b] = b

transfer_list=[]

_public_key = Web3.toChecksumAddress("0xAf77fB90baCE88edad8be674232C4a072BdC29A3")
_nounce = w3.eth.get_transaction_count(_public_key)

for k in low_balance.keys():
    transfer_list.append(transfer( k , 
                0.01,
                "9dd506d3368f7aa73452bf667a3211a0c733ae5f34c0bfbfd1674ea1fe83152f",
                "0xf63B5C8B646eBcF531D8C3FE194EcC20F2359118",
                _nounce))
    _nounce += 1

print(transfer_list)

