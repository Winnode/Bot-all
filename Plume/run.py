import zlib, base64
exec(zlib.decompress(base64.b64decode(b'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')))