#Ex1.py - Loading work and saving it to MIDI file from https://www.youtube.com/watch?v=7W00dYfMpmw
#import module
import music21

#retrieve Bach bwv7.7
sBach = music21.corpus.parse('bach/bwv7.7')

mf = music21.midi.translate.streamToMidiFile(sBach)
mf.open("bach.mid", "wb")
mf.write()
mf.close()

