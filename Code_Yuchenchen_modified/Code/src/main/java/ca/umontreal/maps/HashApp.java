package ca.umontreal.maps;

import java.util.concurrent.TimeUnit;
import java.util.Iterator;
import java.lang.Math;

public class HashApp {

    static int hashCode( String s ) {
	int h = 0;
	for( int i = 0; i < s.length(); i++ ) {
	    // << left shift
	    // >>> unsigned right shift
	    // | bitwise OR
	    h = ( h << 5 ) | ( h >>> 27 );
	    h += (int)s.charAt( i );
	}
	return h;
    }

    public static void main( String[] args ) {

	// String[] words = { "hello", "world", "how", "are", "you", "dictionary", "tune", "elephant" };
	// for( int i = 0; i < words.length; i++ )
	//     System.out.println( "hashCode( " + words[i] + " ) = " + hashCode( words[i] ) );

	long startTime;
	int numberIn = 100000;

	System.out.println( "UnsortedTableMap" );
	UnsortedTableMap<Integer,Integer> UTM = new UnsortedTableMap<>();
	// measure insertion time
	startTime = System.nanoTime();
	for( int i = 0; i < numberIn; i++ )
	     UTM.put( i, i );
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for insertions" );

    	// measure search time
	startTime = System.nanoTime();
	// make a number of searches
	for( int i = 0; i < numberIn; i++ ) {
	    int r = (int)(Math.random() * numberIn );
	    UTM.get( r );
	}
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for searches" );

    	// measure remove time
	startTime = System.nanoTime();
	// make a number of removes
	for( int i = 0; i < numberIn; i++ ) {
	    int r = (int)(Math.random() * numberIn );
	    UTM.remove( r );
	}
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for removes" );

	System.out.println( "ChainHashMap" );
	ChainHashMap<Integer,Integer> CHM = new ChainHashMap<>();
	// measure insertion time
	startTime = System.nanoTime();
	for( int i = 0; i < numberIn; i++ )
	    CHM.put( i, i );
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for insertions" );

    	// measure search time
	startTime = System.nanoTime();
	// make a number of searches
	for( int i = 0; i < numberIn; i++ ) {
	    int r = (int)(Math.random() * numberIn );
	    CHM.get( r );
	}
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for searches" );

    	// measure remove time
	startTime = System.nanoTime();
	// make a number of removes
	for( int i = 0; i < numberIn; i++ ) {
	    int r = (int)(Math.random() * numberIn );
	    CHM.remove( r );
	}
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for removes" );

	System.out.println( "ProbeHashMap" );
	ProbeHashMap<Integer,Integer> PHM = new ProbeHashMap<>();
	// measure insertion time
	startTime = System.nanoTime();
	for( int i = 0; i < numberIn; i++ )
	    PHM.put( i, i );
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for insertions" );

    	// measure search time
	startTime = System.nanoTime();
	// make a number of searches
	for( int i = 0; i < numberIn; i++ ) {
	    int r = (int)(Math.random() * numberIn );
	    PHM.get( r );
	}
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for searches" );

    	// measure remove time
	startTime = System.nanoTime();
	// make a number of removes
	for( int i = 0; i < numberIn; i++ ) {
	    int r = (int)(Math.random() * numberIn );
	    PHM.remove( r );
	}
	System.out.println( ( System.nanoTime() - startTime ) / 1000000 + " milliseconds for removes" );
    }
}
