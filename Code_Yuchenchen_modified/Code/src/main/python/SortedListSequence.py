#!/usr/bin/env python3

# author = "Francois Major"
# version = "1.0"
# date = "4 septembre 2021"
#
# Programme Python pour IFT2015/Mise a niveau
#
from Sequence import Sequence

# SortedListSequence implements Sequence
class SortedListSequence( Sequence ):

    def __init__( self ): self._sequence = []
    def __len__( self ): return len( self._sequence )
    def delete( self, element ): self._sequence.remove( element )
    def get( self, i ): return self._sequence[i]
    def index( self, element ): return self._sequence.index( element )

    # add an element
    def add( self, element ):
        insertion_index = -1
        for i in range( len( self._sequence ) ):
            if self._sequence[i] > element:
                insertion_index = i
                break
        if insertion_index == -1: self._sequence.append( element )
        else: self._sequence.insert( insertion_index, element )

