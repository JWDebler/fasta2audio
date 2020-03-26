import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio

PyAudio = pyaudio.PyAudio     #initialize pyaudio
WAVE_OUTPUT_FILENAME = "test.wav"

sequence = 'AGCT'
LENGTH = 0.5
BITRATE = 44000
NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = (NUMBEROFFRAMES % BITRATE) % 2
WAVEDATA=""

for base in sequence:
    if base == 'A':
        FREQUENCY = 300
        for x in range(NUMBEROFFRAMES):
            WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
        for x in range(RESTFRAMES): 
            WAVEDATA = WAVEDATA+chr(128)
        
    elif base == 'G':
        FREQUENCY = 600
        for x in range(NUMBEROFFRAMES):
            WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
        for x in range(RESTFRAMES): 
            WAVEDATA = WAVEDATA+chr(128)        
    elif base == 'C':
        FREQUENCY = 900
        for x in range(NUMBEROFFRAMES):
            WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
        for x in range(RESTFRAMES): 
            WAVEDATA = WAVEDATA+chr(128)       
    elif base == 'T':
        FREQUENCY = 1200
        for x in range(NUMBEROFFRAMES):
            WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
        for x in range(RESTFRAMES): 
            WAVEDATA = WAVEDATA+chr(128)        



p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 2, 
                rate = BITRATE, 
                output = True)



stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()


