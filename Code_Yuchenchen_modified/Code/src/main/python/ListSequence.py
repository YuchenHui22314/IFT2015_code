#!/usr/bin/env python3

# author = "Francois Major"
# version = "1.0"
# date = "4 septembre 2021"
#
# Programme Python pour IFT2015/Mise a niveau
#
from Sequence import Sequence

# ListSequence implements Sequence
class ListSequence( Sequence ):

    def __init__( self ): self._sequence = [] # initializator
    def __len__( self ): return len( self._sequence )
    def add( self, element ): self._sequence.append( element )
    def delete( self, element ): self._sequence.remove( element )
    def get( self, i ): return self._sequence[i]
    def index( self, element ): return self._sequence.index( element )

