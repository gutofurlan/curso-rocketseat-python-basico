import uuid
import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        # mock de dados pois n tem integracao com instituicao financeira
        bank_payment_id = str(uuid.uuid4())

        # qr code
        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make(hash_payment)
        #salva img como png
        img.save(f"{base_dir}static/img/{hash_payment}.png")

        return {
            "bank_payment_id" :bank_payment_id,
            "qr_code_path" : f"{hash_payment}"
        }