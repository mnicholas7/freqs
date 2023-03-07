#!/usr/bin/python3

# SOLFEGGIOS + Schumann ( 7.83 )
#SOLF = [ 174 , 285 , 396 , 417 , 528 , 639 , 741 , 852 , 963 , 7 , 8]
SOLF = [ 174 , 285 , 396 , 417 , 528 , 639 , 741 , 852 , 963 ]

# Carlos Harmonic Twelve Tone
R2 = [ "1/1" , "17/16"   , "9/8"  , "19/16" , "5/4"   , "21/16" , "11/8"    , "3/2" , "13/8"    , "27/16" , "7/4"  , "15/8"    ]

# Pythagorean C
R7 = [ "1/1" , "256/243" , "9/8"  , "32/27" , "81/64" , "4/3"   , "729/512" , "3/2" , "128/81"  , "27/16" , "16/9" , "243/128" ]

# JI in A w/ 7-Limit Tritone at D#
R8 = [ "1/1" , "16/15"   , "9/8"  , "6/5"   , "5/4"   , "7/5"   , "3/2"     , "8/5" , "5/3"     , "9/5"   , "15/8"             ]

# 3-5 Lattice in A
R9 = [ "1/1" , "16/15"   , "10/9" , "6/5"   , "5/4"   , "4/3"   , "64/45"   , "3/2" , "8/5"     , "5/3"   , "16/9" , "15/8"    ]

# 3-7 Lattice in A
R10 = [ "1/1" , "9/8"    , "8/7"  , "7/6"   , "9/7"   , "21/16" , "4/3"     , "3/2" , "32/21"   , "12/7"  , "7/4"  , "63/32"   ]

# Other Music 7-Limit Black Keys in C
R11 = [ "1/1" , "15/14"  , "9/8"  , "7/6"   , "5/4"   , "4/3"   , "7/5"     , "3/2" , "14/9"    , "5/3"   , "7/4"  , "15/8"    ]

# Dan Schmidt Pelog/Slendro
R12 = [ "1/1" , "1/1"    , "9/8"  , "7/6"   , "5/4"   , "4/3"   , "11/8"    , "3/2" , "3/2"     , "7/4"   , "7/4"  , "15/8"    ]

# Yamaha Just Major C
R13 = [ "1/1" , "16/15"  , "9/8"  , "6/5"   , "5/4"   , "4/3"   , "45/32"   , "3/2" , "8/5"     , "5/3"   , "16/9" , "15/8"    ]

# Yamaha Just Minor C
R14 = [ "1/1" , "25/24"  , "10/9" , "6/5"   , "5/4"   , "4/3"   , "45/32"   , "3/2" , "8/5"     , "5/3"   , "16/9" , "15/8"    ]

def FCALC ( START , RATIOS ):

    BELOW      = START     / 2
    BBELOW     = BELOW     / 2
    BBBELOW    = BBELOW    / 2
    BBBBELOW   = BBBELOW   / 2
    BBBBBELOW  = BBBBELOW  / 2
    #BBBBBBELOW = BBBBBELOW / 2

    MIDDLE  = START
    ABOVE   = START * 2

    SOFTOT = 0

    LINES = []

    for h,i in enumerate(RATIOS):
        h += 1
        #breakpoint()
        x,y = i.split("/")
        x = int(x)
        y = int(y)
        #BBBBBB =  ( BBBBBBELOW * x ) / y
        BBBBB  =  ( BBBBBELOW  * x ) / y
        BBBB   =  ( BBBBELOW   * x ) / y
        BBB    =  ( BBBELOW    * x ) / y
        BB     =  ( BBELOW     * x ) / y
        B      =  ( BELOW      * x ) / y
        M      =  ( MIDDLE     * x ) / y
        A      =  ( ABOVE      * x ) / y

        #COMB = [ BBBBBB , BBBBB , BBBB , BBB , BB , B , M , A ]
        COMB = [  BBBBB , BBBB , BBB , BB , B , M , A ]


        for y,z in enumerate(COMB):
            if int(z) in SOLF:
                COMB[y] = f"√ {z:>5}"
                SOFTOT += 1
                #print(z)

        #print( f"{h:4} => {x:3} / {y:3} = {BBBBBB:10} {BBBBB:10} {BBBB:8} {BBB:8} {BB:8} {B:8} {M:8} {A:8}")
        #print( f"{h:4} => {x:3} / {y:1} = {COMB[0]:>15} {COMB[1]:>15} {COMB[2]:>15} {COMB[3]:>15} {COMB[4]:>15} {COMB[5]:>15} {COMB[6]:>15} {COMB[7]:>15}")
        # LINE = f"{h:4} => {x:3} / {y:1} = {COMB[0]:>15} {COMB[1]:>15} {COMB[2]:>15} {COMB[3]:>15} {COMB[4]:>15} {COMB[5]:>15} {COMB[6]:>15} {COMB[7]:>15}"
        LINE = f"{h:4} => {x:3} / {y:1} = {COMB[0]:>25} {COMB[1]:>25} {COMB[2]:>25} {COMB[3]:>25} {COMB[4]:>25} {COMB[5]:>25} {COMB[6]:>25}"

        LINES.append(LINE)


    if (SOFTOT >= 3):
        print("")
        print(f"SOLFGEGGIOs = {SOFTOT}")
        print("\n".join(LINES))


def SCAN(RANGE, RATIOS):
    for x in RANGE:
        FCALC( x , RATIOS )


Z = range(174,528)

# check out the 297 one!
SCAN(Z, R14)

# check out the 297 one!
SCAN(Z, R13)

# lot of doubling of the same freq in this one, might be handy for chord shapes
SCAN(Z, R12)

# check out the 487 one!
SCAN(Z, R10)

# got a 238 and 476
SCAN(Z, R9)

# got a 317
SCAN(Z, R9)

# got two with x4 ! 313 and 352,, 352 has a perfect 528.0
SCAN(Z, R7)





