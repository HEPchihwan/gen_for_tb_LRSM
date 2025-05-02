# This file was automatically created by FeynRules 2.3.10
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Sun 30 Oct 2016 21:38:37


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_N1 = Decay(name = 'Decay_N1',
                 particle = P.N1,
                 partial_widths = {(P.WR__plus__,P.e__minus__):'((mN1**2 - MWR**2)*((ee**2*kRl**2*mN1**2)/(2.*sw**2) + (ee**2*kRl**2*mN1**4)/(2.*MWR**2*sw**2) - (ee**2*kRl**2*MWR**2)/sw**2))/(32.*cmath.pi*abs(mN1)**3)',
                                   (P.WR__minus__,P.e__plus__):'((mN1**2 - MWR**2)*((ee**2*kRl**2*mN1**2)/(2.*sw**2) + (ee**2*kRl**2*mN1**4)/(2.*MWR**2*sw**2) - (ee**2*kRl**2*MWR**2)/sw**2))/(32.*cmath.pi*abs(mN1)**3)'})

Decay_N2 = Decay(name = 'Decay_N2',
                 particle = P.N2,
                 partial_widths = {(P.WR__plus__,P.mu__minus__):'((mN2**2 - MWR**2)*((ee**2*kRl**2*mN2**2)/(2.*sw**2) + (ee**2*kRl**2*mN2**4)/(2.*MWR**2*sw**2) - (ee**2*kRl**2*MWR**2)/sw**2))/(32.*cmath.pi*abs(mN2)**3)',
                                   (P.WR__minus__,P.mu__plus__):'((mN2**2 - MWR**2)*((ee**2*kRl**2*mN2**2)/(2.*sw**2) + (ee**2*kRl**2*mN2**4)/(2.*MWR**2*sw**2) - (ee**2*kRl**2*MWR**2)/sw**2))/(32.*cmath.pi*abs(mN2)**3)'})

Decay_N3 = Decay(name = 'Decay_N3',
                 particle = P.N3,
                 partial_widths = {(P.WR__plus__,P.ta__minus__):'((mN3**2 - MWR**2)*((ee**2*kRl**2*mN3**2)/(2.*sw**2) + (ee**2*kRl**2*mN3**4)/(2.*MWR**2*sw**2) - (ee**2*kRl**2*MWR**2)/sw**2))/(32.*cmath.pi*abs(mN3)**3)',
                                   (P.WR__minus__,P.ta__plus__):'((mN3**2 - MWR**2)*((ee**2*kRl**2*mN3**2)/(2.*sw**2) + (ee**2*kRl**2*mN3**4)/(2.*MWR**2*sw**2) - (ee**2*kRl**2*MWR**2)/sw**2))/(32.*cmath.pi*abs(mN3)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.WR__plus__,P.b):'((MT**2 - MWR**2)*((3*ee**2*kRq**2*MT**2)/(2.*sw**2) + (3*ee**2*kRq**2*MT**4)/(2.*MWR**2*sw**2) - (3*ee**2*kRq**2*MWR**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)'})

Decay_WR__plus__ = Decay(name = 'Decay_WR__plus__',
                         particle = P.WR__plus__,
                         partial_widths = {(P.c,P.s__tilde__):'(ee**2*kRq**2*MWR**4)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.N1,P.e__plus__):'((-mN1**2 + MWR**2)*(-(ee**2*kRl**2*mN1**2)/(2.*sw**2) - (ee**2*kRl**2*mN1**4)/(2.*MWR**2*sw**2) + (ee**2*kRl**2*MWR**2)/sw**2))/(48.*cmath.pi*abs(MWR)**3)',
                                           (P.N2,P.mu__plus__):'((-mN2**2 + MWR**2)*(-(ee**2*kRl**2*mN2**2)/(2.*sw**2) - (ee**2*kRl**2*mN2**4)/(2.*MWR**2*sw**2) + (ee**2*kRl**2*MWR**2)/sw**2))/(48.*cmath.pi*abs(MWR)**3)',
                                           (P.N3,P.ta__plus__):'((-mN3**2 + MWR**2)*(-(ee**2*kRl**2*mN3**2)/(2.*sw**2) - (ee**2*kRl**2*mN3**4)/(2.*MWR**2*sw**2) + (ee**2*kRl**2*MWR**2)/sw**2))/(48.*cmath.pi*abs(MWR)**3)',
                                           (P.t,P.b__tilde__):'((-MT**2 + MWR**2)*((-3*ee**2*kRq**2*MT**2)/(2.*sw**2) - (3*ee**2*kRq**2*MT**4)/(2.*MWR**2*sw**2) + (3*ee**2*kRq**2*MWR**2)/sw**2))/(48.*cmath.pi*abs(MWR)**3)',
                                           (P.u,P.d__tilde__):'(ee**2*kRq**2*MWR**4)/(16.*cmath.pi*sw**2*abs(MWR)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_ZR = Decay(name = 'Decay_ZR',
                 particle = P.ZR,
                 partial_widths = {(P.b,P.b__tilde__):'(MZR**2*((6*ee**2*gZRdL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRdR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.c,P.c__tilde__):'(MZR**2*((6*ee**2*gZRuL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRuR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.d,P.d__tilde__):'(MZR**2*((6*ee**2*gZRdL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRdR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.e__minus__,P.e__plus__):'(MZR**2*((2*ee**2*gZReL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZReR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.mu__minus__,P.mu__plus__):'(MZR**2*((2*ee**2*gZReL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZReR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.N1,P.N1):'(((-16*ee**2*gZRNL**2*kRl**2*kRl2*mN1**2)/(sw**2*(kRl2 - tw2)) + (32*ee**2*gZRNL*gZRNR*kRl**2*kRl2*mN1**2)/(sw**2*(kRl2 - tw2)) - (16*ee**2*gZRNR**2*kRl**2*kRl2*mN1**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) - (8*ee**2*gZRNL*gZRNR*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)))*cmath.sqrt(-4*mN1**2*MZR**2 + MZR**4))/(96.*cmath.pi*abs(MZR)**3)',
                                   (P.N2,P.N2):'(((-16*ee**2*gZRNL**2*kRl**2*kRl2*mN2**2)/(sw**2*(kRl2 - tw2)) + (32*ee**2*gZRNL*gZRNR*kRl**2*kRl2*mN2**2)/(sw**2*(kRl2 - tw2)) - (16*ee**2*gZRNR**2*kRl**2*kRl2*mN2**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) - (8*ee**2*gZRNL*gZRNR*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)))*cmath.sqrt(-4*mN2**2*MZR**2 + MZR**4))/(96.*cmath.pi*abs(MZR)**3)',
                                   (P.N3,P.N3):'(((-16*ee**2*gZRNL**2*kRl**2*kRl2*mN3**2)/(sw**2*(kRl2 - tw2)) + (32*ee**2*gZRNL*gZRNR*kRl**2*kRl2*mN3**2)/(sw**2*(kRl2 - tw2)) - (16*ee**2*gZRNR**2*kRl**2*kRl2*mN3**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) - (8*ee**2*gZRNL*gZRNR*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)))*cmath.sqrt(-4*mN3**2*MZR**2 + MZR**4))/(96.*cmath.pi*abs(MZR)**3)',
                                   (P.s,P.s__tilde__):'(MZR**2*((6*ee**2*gZRdL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRdR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.t,P.t__tilde__):'(((-6*ee**2*gZRuL**2*kRq**2*kRq2*MT**2)/(sw**2*(kRq2 - tw2)) + (36*ee**2*gZRuL*gZRuR*kRq**2*kRq2*MT**2)/(sw**2*(kRq2 - tw2)) - (6*ee**2*gZRuR**2*kRq**2*kRq2*MT**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRuL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRuR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)))*cmath.sqrt(-4*MT**2*MZR**2 + MZR**4))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.ta__minus__,P.ta__plus__):'(MZR**2*((2*ee**2*gZReL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZReR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.u,P.u__tilde__):'(MZR**2*((6*ee**2*gZRuL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRuR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.ve,P.ve__tilde__):'(MZR**2*((2*ee**2*gZRvL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZRvR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.vm,P.vm__tilde__):'(MZR**2*((2*ee**2*gZRvL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZRvR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.vt,P.vt__tilde__):'(MZR**2*((2*ee**2*gZRvL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZRvR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)'})

