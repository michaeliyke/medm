import argparse
from medm import convert, compress, cut, qr


def main():
    """Routes subcommands to their respective modules"""
    parser = argparse.ArgumentParser(
        prog="medm", description="Media Manager Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Convert
    parser_convert = subparsers.add_parser(
        "convert", help="Convert video to audio")
    parser_convert.add_argument("file", help="Input video file path")

    # Compress
    parser_compress = subparsers.add_parser(
        "compress", help="Compress media to reduce size")
    parser_compress.add_argument("file", help="Input media file path")

    # Cut
    parser_cut = subparsers.add_parser(
        "cut", help="Cut media using start and optional stop points")
    parser_cut.add_argument("file", help="Input media file path")
    parser_cut.add_argument(
        "start", help="Start time in seconds or HH:MM:SS format")
    parser_cut.add_argument(
        "stop", nargs="?", help="Optional stop time in seconds or HH:MM:SS format")

    # QR Code
    parser_qr = subparsers.add_parser(
        "qr", help="QR code generation or decoding")
    qr_subparsers = parser_qr.add_subparsers(dest="qr_action", required=True)

    # Generate QR
    parser_generate = qr_subparsers.add_parser(
        "generate", help="Generate a QR code")
    parser_generate.add_argument("data", help="String data to encode")
    parser_generate.add_argument(
        "-f", "--file", help="Optional file to save the QR code image")

    # Decode QR
    parser_decode = qr_subparsers.add_parser("decode", help="Decode a QR code")
    parser_decode.add_argument(
        "file", help="Image file containing the QR code")

    args = parser.parse_args()

    if args.command == "convert":
        convert.convert_to_audio(args.file)
    elif args.command == "compress":
        compress.compress_media(args.file)
    elif args.command == "cut":
        cut.cut_media(args.file, args.start, args.stop)
    elif args.command == "qr":
        if args.qr_action == "generate":
            qr.generate_qr(args.data, args.file)
        elif args.qr_action == "decode":
            qr.decode_qr(args.file)


if __name__ == "__main__":
    main()
