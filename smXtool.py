#!/usr/bin/env python3

import sys
import binascii

try:
    from gmssl import (
        sm2,
        sm3,
        sm4,
        func,
    )
except ImportError:
    print('Please install package "gmssl" first. Execute "pip3 install gmssl" and rerun this program.')
    sys.exit(-1)


def help_info_and_exit(extcode):
    print("""
smXtool --type=[sm2 | sm3 | sm4] 
        --pri_key=[16进制格式的密(私)钥]
        --pub_key=[16进制格式的公钥，如果是对称加密则此参数无效]
        --action=[encrypt | decrypt, 加密或者解密]
        --enc_data=[密文，16进制，如果是加密则不需要此参数]
        --dec_data=[明文或消息，16进制，如果是解密则不需要此参数]
        --random=[随机字符串，16进制，用于sm2的数字签名]
        --sign=[签名，用于sm2的签名验证]
        --iv=[sm4加密时使用的填充数据，16进制，sm4_type为cbc时本参数必须]
        --sm4_type=[加密算法类型，只能是ecb或cbc，type为sm4时此参数必须]
        
        返回格式是16进制
        
        hanfei@g-cloud.com.cn
        v1.0   2020.11.13
    """)

    sys.exit(extcode)


def output_hex(byte_str):
    output = []
    for byte in byte_str:
        # in case of 0xY
        hex_str = hex(byte).replace("0x", "")
        if len(hex_str) == 1:
            hex_str = '0' + hex_str
        output.append(hex_str)
    print(''.join(output))


def SM2():
    pri_key = params.get('pri_key')
    pub_key = params.get('pub_key')
    action = params.get('action')

    if not pri_key or not pub_key:
        help_info_and_exit(-1)
    sm2_crypt = sm2.CryptSM2(public_key=params.get('pub_key'), private_key=params.get('pri_key'))

    if action == 'encrypt':
        origbytes = binascii.unhexlify(params.get('dec_data'))
        enc_data = sm2_crypt.encrypt(origbytes)
        output_hex(enc_data)

    elif action == 'decrypt':
        encrypt_data = binascii.unhexlify(params.get('enc_data'))

        dec = sm2_crypt.decrypt(encrypt_data)
        output_hex(dec)

    elif action == 'sign':
        if not params.get('random'):
            help_info_and_exit(-1)
        decrypt_data = binascii.unhexlify(params.get('dec_data'))
        sign = sm2_crypt.sign_with_sm3(decrypt_data, params.get('random'))
        print(sign)

    elif action == 'verify':
        if not params.get('sign'):
            help_info_and_exit(-1)
        decrypt_data = binascii.unhexlify(params.get('dec_data'))
        sign = binascii.unhexlify(params.get('sign'))
        verify = sm2_crypt.verify_with_sm3(sign, decrypt_data)
        print(verify)


def SM3():
    data = binascii.unhexlify(params.get('dec_data'))
    digest = sm3.sm3_hash(func.bytes_to_list(data))
    print(digest)


def SM4():
    from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
    pri_key = binascii.unhexlify(params.get('pri_key'))
    dec_data = binascii.unhexlify(params.get('dec_data'))
    enc_data = binascii.unhexlify(params.get('enc_data'))
    iv = binascii.unhexlify(params.get('iv'))
    action = params.get('action')
    sm4_t = params.get('sm4_type')
    if sm4_t not in sm4_type:
        help_info_and_exit(-1)

    crypt_sm4 = CryptSM4()
    if sm4_t == "ecb":
        if action == 'encrypt':
            crypt_sm4.set_key(pri_key, SM4_ENCRYPT)
            encrypt_value = crypt_sm4.crypt_ecb(dec_data)
            output_hex(encrypt_value)
        elif action == 'decrypt':
            crypt_sm4.set_key(pri_key, SM4_DECRYPT)
            decrypt_value = crypt_sm4.crypt_ecb(enc_data)
            output_hex(decrypt_value)

    elif sm4_t == 'cbc':
        if action == 'encrypt':
            crypt_sm4.set_key(pri_key, SM4_ENCRYPT)
            encrypt_value = crypt_sm4.crypt_cbc(iv, dec_data)
            output_hex(encrypt_value)
        elif action == 'decrypt':
            crypt_sm4.set_key(pri_key, SM4_DECRYPT)
            dec_value = crypt_sm4.crypt_cbc(iv, enc_data)
            output_hex(dec_value)


types = {'sm2': SM2, 'sm3': SM3, 'sm4': SM4}
actions = ('encrypt', 'decrypt', 'sign', 'verify', 'digest')
sm4_type = ('ecb', 'cbc')
params = {
    "type": "",
    "pri_key": "",
    "pub_key": "",
    "action": "digest",
    "enc_data": "",
    "dec_data": "",
    "random": "",
    "sign": "",
    "sm4_type": "",
    "iv": "",
}


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        try:
            key, val = arg.replace('--', '').split('=')
            if key not in params:
                help_info_and_exit(-1)
            params[key] = val

        except Exception as e:
            print(str(e))
            help_info_and_exit(-1)

    if params.get('type') not in types or params.get('action') not in actions:
        help_info_and_exit(-1)

    types.get(params.get('type'))()
    sys.exit(0)

