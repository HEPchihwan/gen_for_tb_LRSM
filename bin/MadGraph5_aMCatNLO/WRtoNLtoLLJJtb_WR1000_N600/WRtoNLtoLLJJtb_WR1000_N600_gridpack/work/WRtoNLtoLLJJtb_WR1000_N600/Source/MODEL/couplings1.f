ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_32 = (MDL_EE*MDL_COMPLEXI*MDL_KRL)/(MDL_SW*MDL_SQRT__2)
      GC_33 = (MDL_EE*MDL_COMPLEXI*MDL_KRQ)/(MDL_SW*MDL_SQRT__2)
      END
