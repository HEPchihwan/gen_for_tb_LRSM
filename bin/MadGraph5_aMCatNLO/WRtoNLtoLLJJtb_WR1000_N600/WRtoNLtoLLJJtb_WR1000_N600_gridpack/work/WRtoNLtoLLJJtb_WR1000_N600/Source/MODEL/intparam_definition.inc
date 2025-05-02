ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

C     Parameters that should not be recomputed event by event.
C     
      IF(READLHA) THEN

        G = 2 * DSQRT(AS*PI)  ! for the first init

        MDL_GZRNL = 0.000000D+00

        MDL_GZRNR = 5.000000D-01

        MDL_GZRVR = 0.000000D+00

        MDL_KRL__EXP__2 = MDL_KRL**2

        MDL_KRL2 = MDL_KRL__EXP__2

        MDL_KRQ__EXP__2 = MDL_KRQ**2

        MDL_KRQ2 = MDL_KRQ__EXP__2

        MDL_MZ__EXP__2 = MDL_MZ**2

        MDL_MZ__EXP__4 = MDL_MZ**4

        MDL_SQRT__2 = SQRT(DCMPLX(2.000000D+00))

        MDL_MH__EXP__2 = MDL_MH**2

        MDL_COMPLEXI = DCMPLX(0.000000D+00,1.000000D+00)

        MDL_SQRT__KRL2 = SQRT(DCMPLX(MDL_KRL2))

        MDL_SQRT__KRQ2 = SQRT(DCMPLX(MDL_KRQ2))

        MDL_KRQ2__EXP__2 = MDL_KRQ2**2

        MDL_LOG__KRQ2 = LOG(MDL_KRQ2)

        MDL_MT__EXP__2 = MDL_MT**2

        MDL_AEW = 1.000000D+00/AEWM1

        MDL_MW = SQRT(DCMPLX(MDL_MZ__EXP__2/2.000000D+00
     $   +SQRT(DCMPLX(MDL_MZ__EXP__4/4.000000D+00-(MDL_AEW*PI
     $   *MDL_MZ__EXP__2)/(MDL_GF*MDL_SQRT__2)))))

        MDL_SQRT__AEW = SQRT(DCMPLX(MDL_AEW))

        MDL_EE = 2.000000D+00*MDL_SQRT__AEW*SQRT(DCMPLX(PI))

        MDL_MW__EXP__2 = MDL_MW**2

        MDL_SW2 = 1.000000D+00-MDL_MW__EXP__2/MDL_MZ__EXP__2

        MDL_CW = SQRT(DCMPLX(1.000000D+00-MDL_SW2))

        MDL_SQRT__SW2 = SQRT(DCMPLX(MDL_SW2))

        MDL_SW = MDL_SQRT__SW2

        MDL_TW2 = MDL_SW2/(1.000000D+00-MDL_SW2)

        MDL_GZRDL = -MDL_TW2/(6.000000D+00*MDL_KRQ2)

        MDL_GZRDR = -5.000000D-01+MDL_TW2/(3.000000D+00*MDL_KRQ2)

        MDL_GZREL = MDL_TW2/(2.000000D+00*MDL_KRL2)

        MDL_GZRER = -5.000000D-01+MDL_TW2/MDL_KRL2

        MDL_GZRUL = -MDL_TW2/(6.000000D+00*MDL_KRQ2)

        MDL_GZRUR = 5.000000D-01-(2.000000D+00*MDL_TW2)/(3.000000D+00
     $   *MDL_KRQ2)

        MDL_GZRVL = MDL_TW2/(2.000000D+00*MDL_KRL2)

        MDL_G1 = MDL_EE/MDL_CW

        MDL_GW = MDL_EE/MDL_SW

        MDL_VEV = (2.000000D+00*MDL_MW*MDL_SW)/MDL_EE

        MDL_VEV__EXP__2 = MDL_VEV**2

        MDL_LAM = MDL_MH__EXP__2/(2.000000D+00*MDL_VEV__EXP__2)

        MDL_YT = (MDL_YMT*MDL_SQRT__2)/MDL_VEV

        MDL_MUH = SQRT(DCMPLX(MDL_LAM*MDL_VEV__EXP__2))

        MDL_I2A33 = MDL_YT

        MDL_I3A33 = MDL_YT

        MDL_EE__EXP__2 = MDL_EE**2

        MDL_SW__EXP__2 = MDL_SW**2

        MDL_CW__EXP__2 = MDL_CW**2

        MDL_GZRDL__EXP__2 = MDL_GZRDL**2

        MDL_GZRDR__EXP__2 = MDL_GZRDR**2

        MDL_GZRUL__EXP__2 = MDL_GZRUL**2

        MDL_GZRUR__EXP__2 = MDL_GZRUR**2

        MDL_YT__EXP__2 = MDL_YT**2

      ENDIF
C     
C     Parameters that should be recomputed at an event by even basis.
C     
      AS = G**2/4/PI

      MDL_SQRT__AS = SQRT(DCMPLX(AS))

      MDL_G__EXP__2 = G**2

      MDL_G__EXP__4 = G**4

      MDL_G__EXP__3 = G**3

C     
C     Definition of the EW coupling used in the write out of aqed
C     
      GAL(1) = 3.5449077018110318D0 / DSQRT(AEWM1)
      GAL(2) = 1D0

