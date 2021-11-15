#
#   A problem function which uses intentionally obtuse variable names and almost no comments.
#   The goal is for students to find the maximum of the function using gradient ascent,
#   axially-aligned grid search, full grid search, or some combination of these techniques.
#   CSCI-420 students who wish to try using Genetic Algorithms can try that too.
#
#   Dr. Thomas B. Kinsman
#
import math
import numpy as np

def urxyz( exes_parameter, why, zircon, rta, rtb, rtc ) :
    bogart  = np.array( [ exes_parameter, why, zircon ] )
    nu      = rta * (np.pi/180)
    delta   = np.array( [ [1, 0, 0], [0, np.cos(nu), -np.sin(nu)], [0, np.sin(nu), np.cos(nu)] ] )
    mu      = rtb * (np.pi/180);
    unicorn = np.array( [ [np.cos(mu), 0, np.sin(mu)], [0, 1, 0], [-np.sin(mu), 0, np.cos(mu)] ] )
    tu      = rtc * (np.pi/180);
    iocane  = np.array( [[np.cos(tu), -np.sin(tu), 0], [np.sin(tu), np.cos(tu), 0], [0, 0, 1]] )
    rq      = np.matmul( delta, np.matmul( unicorn, iocane ))
    Pegasus = np.matmul( rq, bogart )
    return Pegasus


def BirdBathFunc_CM_cls420( Harry, Dumbledore, Sirius ) :
    Snuffleupagus   = np.array( [ -204e-9, 20e-9, 427.854e-6, 999.87597e-3, 995.41971e-2  ] )
    Susan           = np.array( [  0.98393, -0.54854, -0.91385 ] )
    Ernie           = np.array( Harry )
    Bob             = np.array( [ -0.01503,  0.81146, -0.38980 ] )
    Troll           = np.polyval( Snuffleupagus, Ernie )
    Hooper          = np.array( [  0.17794, -0.20161, -0.11378 ] )
    rot_tri         = urxyz( Susan, Bob, Hooper, Troll, Dumbledore, Sirius )
    if ( rot_tri[2][0] < rot_tri[2][1] ) :
         if ( rot_tri[2][0] < rot_tri[2][2] ) :
             min_idx = 0
         else :
             min_idx = 2
    else :
         if ( rot_tri[2][1] < rot_tri[2][2] ) :
             min_idx = 1
         else :
             min_idx = 2
    minic                   = rot_tri[2][min_idx]
    pradius                 = math.sqrt( 1 - (minic*minic) )
    Hagrid                  = 1 - abs(rot_tri[2][min_idx]) 
    Hedgewig                = ( math.pi * (Hagrid*Hagrid) / 3 ) * ( 3*1 - Hagrid )
    Hermoine                = 4/3 * math.pi
    Rous                    = Hedgewig / Hermoine 
    GiantVariable           = Rous * Rous * 2   # Increase the sensitivity by squaring small quantity.
    return GiantVariable


if __name__ == '__main__' :
    # Emit the answer, with sensitivity analysis:
    ans = [  -2.959,  10.250,   0.875 ]
    nn  = BirdBathFunc_CM_cls420(  -2.959,  10.250,    0.875 )
    print('Fraction of Water = ', nn, '<-- THE BEST ANSWER\n' )


    print('Sensitivity analysis for =/- 0.5 degrees:')
    delta_deg = 1.0
    nn  = BirdBathFunc_CM_cls420(   -2.959+delta_deg,  10.250,    0.875 )
    print('Fraction of Water with roll + delta_deg   = ', nn )
    nn  = BirdBathFunc_CM_cls420(   -2.959-delta_deg,  10.250,    0.875 )
    print('Fraction of Water with roll - delta_deg   = ', nn )
    nn  = BirdBathFunc_CM_cls420(   -2.959,  10.250+delta_deg,    0.875 )
    print('Fraction of Water with tilt + delta_deg   = ', nn )
    nn  = BirdBathFunc_CM_cls420(   -2.959,  10.250-delta_deg,    0.875 )
    print('Fraction of Water with tilt - delta_deg   = ', nn )
    nn  = BirdBathFunc_CM_cls420(   -2.959,  10.250,    0.875+delta_deg )
    print('Fraction of Water with twist+ delta_deg   = ', nn )
    nn  = BirdBathFunc_CM_cls420(   -2.959,  10.250,    0.875-delta_deg )
    print('Fraction of Water with twist- delta_deg   = ', nn )

    #  THIS IS AN EXAMPLE OF GRID SEARCH:
    best_fract  = -100
    min__parms  = [ -30.0, -30.0, -20.0 ]
    max__parms  = [ +30.0, +30.0, +20.0 ]
    best_parms  = [ -0.125, 0.125, 0.125 ]    # Small values near (0,0,0)
    deg_inc     = 12 
    while deg_inc > 0.00125 :

        # Set the search ranges:
        roll_min   = best_parms[0]-deg_inc*5
        roll_max   = best_parms[0]+deg_inc*5
        tilt_min   = best_parms[1]-deg_inc*5
        tilt_max   = best_parms[1]+deg_inc*5
        twst_min   = best_parms[2]-deg_inc*5
        twst_max   = best_parms[2]+deg_inc*5

        if ( roll_min <= min__parms[0] ) :
            roll_min = min__parms[0]
        if ( tilt_min <= min__parms[1] ) :
            tilt_min = min__parms[1]
        if ( twst_min <= min__parms[2] ) :
            twst_min = min__parms[2]

        if ( roll_max > max__parms[0] ) :
            roll_max = max__parms[0]
        if ( tilt_max > max__parms[1] ) :
            tilt_max = max__parms[1]
        if ( twst_max > max__parms[2] ) :
            twst_max = max__parms[2]

        # Initialize the search range:

        #
        # Run the actual grid search, with user feedback every <so many> iterations:
        #
        case_count = 1
        for twst in np.arange( twst_min, twst_max+deg_inc, deg_inc ) :
            case_count = case_count+1
            if ( case_count == 10 ) :
                case_count = 0
                print( '...Testing with twist = ', twst );
            for tilt in np.arange( tilt_min, tilt_max+deg_inc, deg_inc ) :
                for roll in np.arange( roll_min, roll_max+deg_inc, deg_inc ) :
                    fract = BirdBathFunc_CM_cls420(  roll, tilt, twst )
                    if ( fract >= best_fract ) :
                        best_fract = fract
                        best_parms = [ roll, tilt, twst ]

        # Shrink the size of the grid slowly:
        deg_inc = (deg_inc * 15)/16;
        
    print('\nBest Value Found:' );
    print('    Roll= ', best_parms[0], ' Tilt = ', best_parms[1], ' Twist = ', best_parms[2] )
    print('    Fraction = ', best_fract  )

    nn  = BirdBathFunc_CM_cls420(  -2.959,  10.250,    0.875 )

    print('NOMINAL ANSWER WAS:\n    Roll= ', ans[0], ' Tilt= ', ans[1], ' Twist = ', ans[2] );
    print('    Fraction of Water =  ', nn, '  <-- NOMINAL expected best.\n' )




    #  Emit a trial test case here, etc...:
    print('\n\n\n')
    nn  = BirdBathFunc_CM_cls420( -10.2500, -0.8750, 2.9590 )
    print('Fraction of Water = ', nn, '<-- Example test case results\n' )



    print('###########################################################################################')

