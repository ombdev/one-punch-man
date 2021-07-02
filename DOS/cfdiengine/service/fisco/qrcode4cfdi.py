import tempfile
import qrcode
import random
import string

def qrcode_cfdi(as_usr, uuid, erfc, rrfc, total, chunk):
    """
    creates qrcode as per cfdi v33 constrains
    """

    def random_str(size=8):
        """generates random string as per size"""
        return ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(size)
        )

    def incept_file(i):
        SIZE_RANDOM_STR = 8
        fname = '{}/{}.jpg'.format(
            tempfile.gettempdir(),
            random_str(SIZE_RANDOM_STR)
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