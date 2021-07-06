import argparse, re
from AVRUtilities import AVRUtilities
from AVRUtilities import MCU

success, cfile = AVRUtilities.GetSingleCFile()

avr_parser = argparse.ArgumentParser(description="AVR commands")

group = avr_parser.add_mutually_exclusive_group()
group.add_argument('-compile', '--compile', action='store_true')
group.add_argument('-hex', '--hex', action='store_true')
group.add_argument('-upload', '--upload', action='store_true')
group.add_argument('-all', '--all', action='store_true', default=True)

avr_parser.add_argument('-port', '--port', action='store', default='COM18')
avr_parser.add_argument('-file', '--file', help='Input file. It needs to be .c for -compile, .o for -hex and .hex for -upload', default=cfile)

args = avr_parser.parse_args()

if args.compile:
	if not re.search("\.c", args.file):
		print("ERROR: Invalid input c file. It does not have .c extension.")
	else:
		ofile = re.sub(".c", ".o", args.file)
		AVRUtilities.Compile(MCU.ATmega8, args.file, ofile)
elif args.hex:
	if not re.search("\.o", args.file):
		print("ERROR: Invalid input obj file. It does not have .o extension.")
	else:
		hexfile = re.sub("\.o", ".hex", args.file)
		AVRUtilities.GenerateHexFile(args.file, hexfile)
elif args.upload:
	if not re.search("\.hex", args.file):
		print("ERROR: Invalid input hex file. It does not have .hex extension.")
	else:
		AVRUtilities.Upload(MCU.ATmega8, args.file, args.port)
elif args.all:
	if not re.search("\.c", args.file):
		print("ERROR: Invalid input c file. It does not have .c extension.")
	else:
		AVRUtilities.PerformAll(MCU.ATmega8, args.file, args.port)
