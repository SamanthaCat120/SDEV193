#Ex1.py - Loading work and saving it to MIDI file
import music21
sBach = music21.corpus.parse('bach/bwv7.7')
mf = music21.midi.translate.streamToMidiFile(sBach)
mf.open("bach.mid", "wb")
mf.write()
mf.open()
