import os
import json
import sys
from docmaker.builder import builder
from misc.tricks import dump_exception
from engine.error import ErrorCode


def _empty_tmp_file():
   
    def _random_str(size=8):
        """generates random string as per size"""

        import random
        import string

        return ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(size)
        )

    tmp_dir = tempfile.gettempdir()
    return  os.path.join(tmp_dir, _random_str())


class PipeLiner(object):

    @classmethod
    def facturar(cls, pt, req):

        resdir = os.path.abspath(os.path.join(os.path.dirname(pt["source"]), os.pardir))
        tmp_file = _empty_tmp_file()

        rc = builder(
                resdir,
                pt["res"]["dirs"], 'facxml', tmp_file, **kwargs)

        filename = req['content']['filename']
        if rc == ErrorCode.SUCCESS:
            out_dir = os.path.join(rdirs['cfdi_output'], inceptor_data['rfc'])
            rc, outfile = cls._pac_sign(tmp_file, filename, out_dir, pt["tparty"]["pac"])
            
        if os.path.isfile(tmp_file):
            os.remove(tmp_file)

        return rc.value

    @staticmethod
    def pago(pt, req):
        pass

    @staticmethod
    def nota_cred(pt, req):
        pass

    @staticmethod
    def _pac_sign(f_xmlin, xid, out_dir, pac_conf):
        """Signs xml with pac connector mechanism"""
        pass

    @classmethod
    def maneuver_req(cls, pt, req, adapter=None):
        """"""
        def apply_adapter():
            if adapter is not None:
                return adapter()
            # So we assumed request are bytes of a json string
            json_lines = req.decode(encoding='UTF-8')
            return json.loads(json_lines)

        d = apply_adapter()
        try:
            motive = d['req']['motive']
            content = d['req']['content']

            if not hasattr(cls, motive):
                msg = "The {0} has no motive {1}".format(cls.__name__, motive)
                raise RuntimeError(msg)

            return getattr(cls, motive)(pt, content)
        except (RuntimeError) as e:
            _logger.fatal("support module failure {}".format(e))
            return ErrorCode.MOTIVE_NOT_MANEUVERED.value
        except:
            _logger.error(dump_exception())
            return ErrorCode.MOTIVE_UNEXPECTED_FAIL.value
