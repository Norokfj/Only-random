# Compiled By Mr Norok | Norok vau
# Github :  https://github.com/Norokfj

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
