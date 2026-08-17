# HKD∞ OBFUSCATE v2 — STATIC PROTECTED MODULE
# CPython 3.9; all protection work occurs at import, never per function call.
import hashlib as _hh
import marshal as _hm
import zlib as _hz

_B=(bytes.fromhex('a7e7871ac6a5d873762af78c67de56a1a525f258cd60e41390e24a26f3dcaadd6710af7c5de07d6c8d624046f7ca52023223a63775d3a7145f84e865c9d9a685d4270e82b63cdddf8549bdf6e1d8f921dd3f85c23120e94971bd1183d812dcbbafc19116aa09e1b821ed7ad226b149d1128ece8c6279a47a06f4b39bdfd125da'),
bytes.fromhex('29e0ae84bee4921823b67c60afd6eb995ce0e7ce1d52c18ea25e3c8b5e413975a64045a568ba7beb92c5c2e62947f751bee0f8bd0d30072fa3cdc17dae607b3b74a79cfc63cee22257783a590ec9f3979c00c5f22f0cc238ddf0732d46956d349dc62e52b549515351818db9c73d11a1ef08ebf1f899977df88b479385001ace'),
bytes.fromhex('6676a59cf88c20b503ad3905aed5a998a6220eeb5efe667329e9cb632322bd8b45f66a29310f7035e4b562b73310521b99359569a93712c67a118ff5c6b0877c07948a7133507adfda1119df508173ebef073f0ed0b4c4d4f4afb1b2a2ef2d121d0262a8509c121364bf629e8a0935898750109d6bdf7ff3da390ba205b65ffd'),
bytes.fromhex('aa72756b726ad7b77bba6c31a0bef0461382747bfee50f9cc73ce9ead7ab9928aa72971b50a28bea5ef11bc2f16aaa61c0ce35f4fb54da21ba954363b97a6754fe9fa2e00b2348c7612cfe05f0a2efeafd180ecf7d780aa7ec8db996549427ad1c2d34aa4e76224b908ee7b96921b05cfb419080ae9480268be6fe75b7e025f5'),
bytes.fromhex('43903386f65dc83a96ba34a7c0fc24d6557a7432603a28f72f378a5e8697c10167da5aa2f21521d53a7aa75f9bcadf624f08c16cce4fb26202533889d1bf8b312b9e88f4af90ddead0055e0e2173124255e971089ec0cabc7ab65844ed99677f0365d671aafb478804c992178478fe6462644a6b371da4ed438f1678fea83d37'),
bytes.fromhex('42dc2da48c2de608c48ee43eff43b2ed942126f18e89b4bc644cca57f356e2f43d418084b1af8b0e775758274bca872f4d3298a91b9415076ea97d4171b303c5d0ab243333b8b9087033b54e0cb2aaf147d54f334c9f1bdece269c83587ed5b63745a98cf664acc65965195629fd404640b92b4e9cc78ef40944cca606737c95'),
bytes.fromhex('83d4484b4110760002539f5d2e7f25b4527020ac447a0b46a9df90724ce350365b565382213970e10b336f9d113c667cab1d1d930c46c96794a3fe2b2ff7627f35c4b9b748ce4c1f1c6d3d82e924fb08c40bf31524ec9c12e5fc40263ff7d9b567423f4be5193adb83a5af3e0c8bfe1fa62030a20284d4c38324dae8c5fe9927'),
bytes.fromhex('722932ce42f525b6126a827f36460b3f21e3b215a299f186c9174cbd87a6905ab4bc7b0fb26d46c73f60346aa7042e24e518af756e03b7109e6440c205f40aeffbd3498530f70a4286b162df44f9dc53657288e6d3032d3bfeb004fc2944750614ca11f6447a45c4b023b2ecf12838eb9a8be69d8a7fb4aa3fec257710371fc8'),
bytes.fromhex('a943ba9d12e4bc3da72e854b983679c26619f4d33ac9670f4c8f438a148b2be09807f684a145ab02f0e7d5c3b87aecf8320f3d475ba9cd6b4872c849660f4f6485bce2e5e550e0e6f261c0cb7547dc76dd2028464aec8efc318b9dd00f9e105272192aa479eb823dcbc7d77e348ef466327be1ed429ee45b2314feab3dac4bd5'),
bytes.fromhex('e9f744c7b98f21cff503d0ef8a360238b9d4c9d5499d9fc7b79fc8ab526e9ec50a5831422eb61febde66f49e27c43159225331c302e70a678c8a17b9b7dec2d9ddebf2cb67cfc2d0b992f79e09b4a479b0e7b527680373b8aa9474398b9572b4965e5f1398fb6ed8362b5b663a747210670aac0f273b51b2c38b22150824fbb8'),
bytes.fromhex('ae670035281c3a14a28dccc6228208b02d39f3965c1a6dd5fe431a89637a5222346078a574e3ffbfa5e9e2fd2d03708c8cbd41aacb862748b44d49296f4c8f69707669ca2aa2d7d14f557a0c835d394ce7f52d2e159769c292a2a06a'),)
_I=(3, 5, 8, 1, 6, 2, 0, 4, 7, 9, 10)
_L=(bytes.fromhex('d44ef5ac0ae24cf793e46417168615487a3485feb799c2fa04e9ac73092a6cfa'),
bytes.fromhex('5f63092dae4b4e15f2eee7d4041f49ed30bf17844f0b4feaf41f95f224e6d4cb'),
bytes.fromhex('c3da1da3cedab2ff998b41f915958a2dd8d3f7a319f89a33c089709f9b5d97ac'),
bytes.fromhex('e1285fb877d27ea15ba879b2dcd439b0abf26ba1ab99955de9888f850229746b'),
bytes.fromhex('e40f9a67cdd285aa1859488af6d6654efc33b0a4c19d34a75447c9b79e9c0a2f'),
bytes.fromhex('7e47445492a7016a0b475510cb8729a5d4963c6c4c9f5a06951e18e2a901e42f'),
bytes.fromhex('23395f53a8e619eed62f335c9a47532bf90cc905d44035987affd7837f98ab69'),
bytes.fromhex('c1bf31d08ad14af6f503f69a477ec15d2e67d99b21f4491e3f1dce66eaaa3d51'),
bytes.fromhex('b3c2c122aa257eb5a53c245601b9bce7de60806db0ae2db89fbf8998514faa92'),
bytes.fromhex('2f2a103918985ecc7ff09609bce1ab42a4de701d853ed602a6b1f9be5c9b3355'),
bytes.fromhex('98dda7983dcb128e23ceb435bd462cd37e4384fd38b143596c7895bfe1199eaf'),)
_R=bytes.fromhex('ffb6200afc375d9ba8cf281fae32b6ccad48a492e9ca7e450bb760e0c376d55e')
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
