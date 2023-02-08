from flask import Flask, Response, request
import qrcode
import io

app = Flask(__name__)

@app.route("/qr/", methods=["GET"])
def generate_qr():
    url = request.args.get("url")
    if not url:
        return "No URL provided", 400

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)

    return Response(
        buf.read(),
        content_type="image/png",
        headers={"Content-Disposition": "attachment;filename=qr-code.png"}
    )

if __name__ == "__main__":
    app.run(debug=True)
