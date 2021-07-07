@echo off
SETLOCAL
set basefilename=blower_pwm
echo avr-gcc -Wall -Os -mmcu=atmega8 -o %basefilename%.o %basefilename%.c > avrc.bat
echo avr-objcopy -j .text -j .data -O ihex %basefilename%.o %basefilename%.hex > avrh.bat
echo avrdude -p ATmega8 -c arduino -P COM3 -b 19200 -U flash:w:%basefilename%.hex:i > avru.bat
ENDLOCAL
