"""
QR Code Generator
-----------------
Generate a QR code from any text or URL.

Requirements:
    pip install Pillow
    pip install qrcode


Usage:
    Run the script and enter any text or URL when prompted.
"""

import qrcode


def generate_qr_code(data: str) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    try:
        from PIL import Image
        img = qr.make_image(fill_color="black", back_color="white")
        filename = "qrcode_output.png"
        img.save(filename)
        print(f"QR code saved as '{filename}'")
    except ImportError:
        print("Pillow not installed. Showing QR code in terminal instead.")
        print("Install Pillow to save as image: pip install Pillow\n")
        qr.print_ascii(invert=True)


def main():
    print("=== QR Code Generator ===")
    data = input("Enter text or URL: ").strip()

    if not data:
        print("No input provided.")
        return

    generate_qr_code(data)


if __name__ == "__main__":
    main()
