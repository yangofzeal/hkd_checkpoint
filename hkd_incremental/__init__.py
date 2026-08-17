# HKD∞ OBFUSCATE v2 — STATIC PROTECTED MODULE
# CPython 3.9; all protection work occurs at import, never per function call.
import hashlib as _hh
import marshal as _hm
import zlib as _hz

_B=(bytes.fromhex('0d292c5e19409f6aafe3ffcd0dd67bcfbd9b6e0c4ab70d47967189f869bac373de4516b08e5ab452193cddb4b692e6565be98776b5b1ef5a38364dc7febae3df69db8e69559f0179e360f9a4114c8929340f0a1ba87f7fdc42713e81874a2792b4e6830948a2c45c79e8603ff0b9e06feafb1b1ac892a1c252ab580baaf9c1ce'),
bytes.fromhex('aa726d68f48bdfb77fd023c241a50b14a49d474f4ade5e01889a773506259ff032fd792d83f7264cc15f965e8e06d4c33a185d393d8437e5e9f3a38f4dd0d26eee1a5df801e8b9dd115494d197e6c21428e5299d4315ff1e7d2ae542e1efc53afc16b9e41f2c934f9a66a3efc13de1caeb411872a6427e9da71ed4f0ad7109c3'),
bytes.fromhex('7f2902022183c55a3754c9e13562f6a986ecc1232366527ca8e62e03cb9ef924eb5158dfc9f2b6d838058acc94ae7527f8c756b0f8840a47658c92c8e050cad90d4df2e970b6cb68fb8069aea173f56069b47787d988f5b286943ac757958b944813598466990d5c92b6ce0160efea62b548bdd3df5776174242061f03d75f5b'),
bytes.fromhex('be4fba845dea8badb15d7110c21607633d96eeab746635712c666b07929210146312f4468002a6a53417255244afad1d32ae6cd2e83a52c7b8811e5461dcb042b54dbf7b70174e232779284efb1a8390e575f8'),
bytes.fromhex('1b91dcb6c7a14efa7495d38ac9e264f5124d65d0985a73ce203e6fc91a05af203b12d17a370f0f7cf98f683df32177cdb0f1715cdccfefe2db97b3a381105154f3411f25f88383d07a8932c6eb78e5a3976d982fa352d5638a31889e0e3e9f68b7f2698b14cdf0775e9a9bddd11534f8e52cb2aa60e3e25e26a80f9c83c88d67'),
bytes.fromhex('6a639d75c0eccfd425bdad2d9e3951886c6204fc208323a8dd6ff7a9d28515a836e405190e74dc4009d6d63c8fe38cb8cf8997bc812a4f9bb937f9ee7d3bba12c918ec7a6022456c4b9440c71360ef7f2f632ce82ba0ee7364c97c6dfc52cfd5fffd91e86eebc087981b08123e121e9798f732ec9e5cb42a732fcf7e8ad050b3'),
bytes.fromhex('15f16ced00f83fd323519e3ebace0d5b4d81394d1f4b0a036daa27e8c3bcbe633eb2626a20198ea495bb592e08965812f9b3c97a3cfb36687eb2c18192df9638d8e00efb6881c8ed425461a1692361a43fc38fed99edbb745266bd992d5abc920b2236dcfa49584397463e6bff38d46bc5e4bdeb80996d3368f2daf1c31f0899'),
bytes.fromhex('7a65cc1156078353de23ea86015d4723a997d2b7e87cfec64452a89b21704a5571213ca4bfe58ba3867f3a9cc801ef6ea4c8b51e012d460a8b3f5facf1bbed8de60f7f75b2fb6ae166890fc1cab0564895a6f461ec4a5d81d5f217bbe190e89fd390b686d3ca6ef95c064db80fcebdd817a83b229f963e91c1ab48c5b3df4366'),)
_I=(1, 6, 7, 0, 4, 2, 5, 3)
_L=(bytes.fromhex('309668013e363aa2f5da1a8efc3fff76d2ccfc2f3650af1423e6f3d4385ce75b'),
bytes.fromhex('0b900b473b57da2c1b9ebc30d34391f162644b3f06db87ed4634e351e5cdc2b3'),
bytes.fromhex('b9dd7fd26cb4c1fe9a017b9f2e7ccec5c98553de96eb5b7824564a57e6474bbb'),
bytes.fromhex('6cf964aec1458159b8ac9044a91892793e9dfda5cbe40de59dd1ade6c299267c'),
bytes.fromhex('dacdb2260067ece2a1733fc48c3da7f625d9f7234da01fae9e5d5e11577b039c'),
bytes.fromhex('23fba328b71359a70992b190d1f46324775867ac1c0b652d23ec3989735c6615'),
bytes.fromhex('b9f5b94df0b9d80f51957ef1f67f95ccd4e294bf621bbca6db406864df481a4d'),
bytes.fromhex('2a855267d873b1d1d3c15d206ae32f32df3eb5b3aa8b2f7470b448231b74b822'),)
_R=bytes.fromhex('e1c9915b3d737c94c589743baaaea484b2afd11fa3f7d24a19c6bfa22b32870f')
_S1=bytes.fromhex('b4c44a1d49f84630e6a3d8f9e940b5fe9bac91bad310595a9d955dd8b13e68ff')
_S2=bytes.fromhex('7e50262985a1f8adbb970e2cb7aaab9a1c50293fd48e23303c28fc9662bd3098')

def _x(a,b):
    return bytes(i^j for i,j in zip(a,b))

def _ks(k,idx,n):
    o=bytearray(); c=0; s=k+idx.to_bytes(4,'big')
    while len(o)<n:
        o.extend(_hh.sha256(s+c.to_bytes(4,'big')).digest()); c+=1
    return bytes(o[:n])

def _mr(v):
    if not v:
        return _hh.sha256(b'').digest()
    v=list(v)
    while len(v)>1:
        if len(v)&1: v.append(v[-1])
        v=[_hh.sha256(v[i]+v[i+1]).digest() for i in range(0,len(v),2)]
    return v[0]

_K=_x(_S1,_S2)
_P=[]
_V=[]
for _i in range(len(_I)):
    _m=_B[_I[_i]]
    _r=_x(_m,_ks(_K,_i,len(_m)))
    _P.append(_r)
    _V.append(_hh.sha256(_i.to_bytes(4,'big')+_r).digest())
if tuple(_V)!=_L or _mr(_V)!=_R:
    raise ImportError('HKD∞ SHA-256 integrity verification failed')

_C=_hm.loads(_hz.decompress(b''.join(_P)))

# Execute protected code in a fresh module-shaped namespace. This is critical
# for hot paths: loader temporaries never contaminate the function globals
# dictionary with deleted slots/tombstones.
_G=globals()
_N={
    '__name__':_G.get('__name__'),
    '__doc__':_G.get('__doc__'),
    '__package__':_G.get('__package__'),
    '__loader__':_G.get('__loader__'),
    '__spec__':_G.get('__spec__'),
    '__file__':_G.get('__file__'),
    '__cached__':_G.get('__cached__'),
    '__builtins__':_G.get('__builtins__'),
}
exec(_C,_N,_N)

# Publish source-defined names to the actual module object. Functions keep _N
# as __globals__, matching a clean normal module execution environment.
for _q,_v in _N.items():
    if _q != '__builtins__':
        _G[_q]=_v

del _B,_I,_L,_R,_S1,_S2,_K,_P,_V,_C,_i,_m,_r,_x,_ks,_mr,_q,_v,_N,_G,_hh,_hm,_hz
