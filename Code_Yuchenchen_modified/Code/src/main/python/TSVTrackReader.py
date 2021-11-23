#!/usr/bin/env python3

# author = "Francois Major"
# version = "1.0"
# date = "4 septembre 2021"
#
# Programme Python pour IFT2015/Mise a niveau
#

# TSVTrackReader reads a TSV file of Tracks
# returns a list that contains the Tracks

import csv
from Track import Track

class TSVTrackReader:

    def __init__( self, file_name ):
        # reading the TSV track file and adding the tracks to a list
        # assume run from IFT2015/Code
        track_file = open( file_name, 'r' )
        # assume TSV file has a header, so remove it
        self._track_reader = list( csv.reader( track_file, delimiter = '\t') )[1:]

    def __len__( self ) : return len( self._track_reader )
    def get_tracks( self ): return self._track_reader
