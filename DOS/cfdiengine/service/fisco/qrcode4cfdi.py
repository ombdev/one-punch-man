import tempfile
import qrcode
import random
import string
import base64
from distutils.spawn import find_executable


def cert_base64_cfdi(cert_file):
    """turns cert file into base 64"""
    certb64 = None
    with open(cert_file, 'rb') as f:
        content = f.read()
        certb64 = base64.b64encode(content).decode('ascii')

    return certb64

def _random_str(size=8):
    """generates random string as per size"""
    return ''.join(
        random.SystemRandom().choice(
            string.ascii_uppercase + string.digits
        ) for _ in range(size)
    )

def qrcode_cfdi(as_usr, uuid, erfc, rrfc, total, chunk):
    """
    creates qrcode as per cfdi v33 constrains
    """


    def incept_file(i):
        fname = '{}/{}.jpg'.format(
            tempfile.gettempdir(),
            _random_str()
        )
        with open(fname, 'wb') as q:
            i.save(q, 'JPEG')
        return fname

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(
        '{}?&id={}&re={}&rr={}&tt={}&fe={}'.format(
            as_usr, uuid, erfc, rrfc, total, chunk
        )
    )
    qr.make(fit=True)
    return incept_file(qr.make_image())


def sign_cfdi(pem_pubkey, pem_privkey, str2sign):
    """signs an string and returns base64 string"""

    def erase_bom(path):
        import codecs

        BUFSIZE = 4096
        chunk = None

        def takeout(l, f, c):
            i = 0
            c = c[l:]
            while c:
                f.seek(i)
                f.write(c)
                i += len(c)
                f.seek(l, os.SEEK_CUR)
                c = f.read(BUFSIZE)
            f.seek(-l, os.SEEK_CUR)
            f.truncate()

        with open(path, "r+b") as p:
            chunk = p.read(BUFSIZE)
            if chunk.startswith(codecs.BOM_UTF8):
                takeout(len(codecs.BOM_UTF8), p, chunk)
            if chunk.startswith(codecs.BOM_UTF32_BE):
                takeout(len(codecs.BOM_UTF32_BE), p, chunk)
            if chunk.startswith(codecs.BOM_UTF32_LE):
                takeout(len(codecs.BOM_UTF32_LE), p, chunk)
            if chunk.startswith(codecs.BOM_UTF16_BE):
                takeout(len(codecs.BOM_UTF16_BE), p, chunk)
            if chunk.startswith(codecs.BOM_UTF16_LE):
                takeout(len(codecs.BOM_UTF16_LE), p, chunk)

    def seekout_openssl():
        SSL_BIN = "openssl"
        executable = find_executable(SSL_BIN)
        if executable:
            return os.path.abspath(executable)
        raise SignerError("it has not found {} binary".format(SSL_BIN))

    def touch(self, path):
        with open(path, 'a'):
            os.utime(path, None)

    cipher = 'sha256'
    ssl_bin = seekout_openssl()

    tmp_dir = tempfile.gettempdir()
    sealbin_f = '{}/{}'.format(tmp_dir, _random_str())
    input_f = '{}/{}'.format(tmp_dir, _random_str())
    result_f = '{}/{}'.format(tmp_dir, _random_str())

    touch(input_f)

    with open(input_f, 'r+b') as cf:
        cf.write(str2sign.encode("utf-8-sig"))

    dgst_args = [
         'dgst',
         '-{}'.format(self.cipher),
         '-sign',
         self.pem_privkey,
         '-out',
         sealbin_f,
         input_f
    ]

    base64_args = [
        'base64',
        '-in',
        sealbin_f,
        '-A',
        '-out',
        result_f
    ]
