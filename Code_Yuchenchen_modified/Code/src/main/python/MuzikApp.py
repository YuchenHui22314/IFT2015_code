#!/usr/bin/env python3

# author = "Francois Major"
# version = "1.0"
# date = "4 septembre 2021"
#
# Programme Python pour IFT2015/Mise a niveau
#
# Test the TSVTrackReader and Sequence data structures
#   using list (ListSequence) only, convincing enough!

import time
import random
from Track import Track
from TSVTrackReader import TSVTrackReader
from ListSequence import ListSequence
from SortedListSequence import SortedListSequence

# assume run from IFT2015/Code
start_time = time.time()
track_reader = TSVTrackReader( 'data/tracks.tsv' )
print( "finished reading", len( track_reader ), "tracks in", ( time.time() - start_time ) * 1000, "milliseconds" )

# adding to a ListSequence
track_list = track_reader.get_tracks()
tracks = ListSequence()
start_time = time.time()
for track in track_list:
    t = Track( track )
    tracks.add( t )
print( "finished adding", len( tracks ), "tracks to list in", ( time.time() - start_time ) * 1000, "milliseconds" )
for i in range( 10 ):
    print( tracks.get( i )._title )

start_time = time.time()
initial_size = len( tracks )
for i in range( initial_size ):
    delete_index = random.randint( 0, len( tracks ) - 1 )
    tracks.delete( tracks.get( delete_index ) )
print( "finished deleting", initial_size, "tracks from list in", ( time.time() - start_time ) * 1000, "milliseconds" )

# adding to a sorted ListSequence
track_list = track_reader.get_tracks()
tracks = SortedListSequence()
start_time = time.time()
for track in track_list:
    t = Track( track )
    tracks.add( t )
print( "finished adding", len( tracks ), "tracks to sorted list in", ( time.time() - start_time ) * 1000, "milliseconds" )
for i in range( 10 ):
    print( tracks.get( i )._title )

start_time = time.time()
initial_size = len( tracks )
for i in range( initial_size ):
    delete_index = random.randint( 0, len( tracks ) - 1 )
    tracks.delete( tracks.get( delete_index ) )
print( "finished deleting", initial_size, "tracks from list in", ( time.time() - start_time ) * 1000, "milliseconds" )

