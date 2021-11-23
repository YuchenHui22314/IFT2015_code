#!/usr/local/bin/python3

# author = "Francois Major"
# version = "1.0"
# date = "4 septembre 2021"
#
# Programme Python pour IFT2015/Mise a niveau
#

# Track (base class for Muzik Tracks)
class Track:

    # default constructor
    def __init__( self, track = None ):
        if track is not None :
            self._album = track[0]
            self._artist = track[1]
            self._tempo = int( track[2] )
            self._comment = track[3]
            self._composer = track[4]
            self._energy = int( track[5] )
            self._genre = track[6]
            self._key = track[7]
            self._number = int( track[8] )
            self._time = track[9]
            self._title = track[10]
            self._year = int( track[11] )
        else:
            # attributes and default values
            self._album = ""
            self._artist = ""
            self._tempo = 0
            self._comment = ""
            self._composer = ""
            self._energy = 0
            self._genre = ""
            self._key = ""
            self._number = 0
            self._time = ""
            self._title = ""
            self._year = 0

    # setters (all with String arguments)
    def set_album( self, s ): self._album = s
    def set_artist( self, s ): self._artist = s
    def set_tempo( self, s ): self._tempo = int( s )
    def set_comment( self, s ): self._comment = s
    def set_composer( self, s ): self._composer = s
    def set_energy( self, s ): self._energy = int( s )
    def set_genre( self, s ): self._genre = s
    def set_key( self, s ): self._key = s
    def set_number( self, s ): self._number = int( s )
    def set_time( self, s ): self._time = s
    def set_title( self, s ): self._title = s
    def set_year( self, s ): self._year = int( s )

    def __gt__( self, t ): return self._title > t._title

    def __str__( self ):
        return '' + self._album + '\t' + self._artist + '\t' + str( self._tempo ) + '\t' + self._comment + '\t' + self._composer + '\t' +  str( self._energy ) + '\t' + self._genre + '\t' + self._key + '\t' + str( self._number ) + '\t' + self._duration + '\t' + self._time + '\t' + self._title + '\t' + str( self._year ) + '\t'
