import io

import qrcode
from flask import Blueprint, send_file
from app.src.local_ip import get_local_ip

qr_bp = Blueprint('qr', __name__)

@qr_bp.route('/qr.png')
def qr_code():
    ip_address = get_local_ip()
    port = 5000
    ref = "clients"
    url = f"http://{ip_address}:{port}/{ref}"

    qr_img = qrcode.make(url)
    img_io = io.BytesIO()
    qr_img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')
