M$ModelName = "GranadaDictionary";

M$Information =
{ Authors       -> {"John Gargalionis"}
, Version       -> "1.0"
, Date          -> "2022.07.25"
, Institutions  -> {"University of Valencia and IFIC"}
, Emails        -> {"johngargalionis@gmail.com", "johgar@uv.es", "johngarg@ific.uv.es"}
};

DefaultDimensionfulScale = 1000.0
DefaultDimensionlessScale = 1.0

M$InteractionOrderHierarchy =
{ {QCD, 1}
, {QED, 2}
, {NP,1}
};

M$Parameters =
{ kappaS ==
  { ParameterType -> External
  , Value         -> DefaultDimensionfulScale
  , Description   -> "Trilinear \\mathcal{S} \\phi^\\dagger \\phi coupling"
  }

, lambdaS ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Quartic \\mathcal{S} \\mathcal{S} \\phi^\\dagger \\phi coupling"
  }

, kappaS3 ==
  { ParameterType -> External
  , Value         -> DefaultDimensionfulScale
  , Description   -> "Trilinear \\mathcal{S} \\mathcal{S} \\mathcal{S} coupling"
  }

, yS1 ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Yukawa \\mathcal{S}_1^\\dagger \\bar{L} L^c coupling"
  }

, yS2 ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Yukawa \\mathcal{S}_2^\\dagger \\bar{eR} eR^c coupling"
  }

, yvarphie ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Yukawa \\varphi^\\dagger \\bar{eR} L coupling"
  }

, yvarphid ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Yukawa \\varphi^\\dagger \\bar{dR} Q coupling"
  }

, yvarphiu ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Yukawa \\varphi^\\dagger \\bar{Q} uR coupling"
  }

, lambdavarphi ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Quartic \\varphi^\\dagger H H^\\dagger H coupling"
  }

, lambdaXi1 ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Quartic \\Xi_1^\\dagger Xi_1 H^\\dagger H coupling, 1 x 1 contraction"
  }

, lambdaXi1P ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Quartic \\Xi_1^\\dagger Xi_1 H^\\dagger H coupling, 3 x 3 contraction"
  }

, yXi1 ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Yukawa \\Xi_1^\\dagger \\bar{L} L^c coupling"
  }

, kappaXi1 ==
  { ParameterType -> External
  , Value         -> DefaultDimensionfulScale
  , Description   -> "Trilinear \\Xi_1 H^\\dagger H coupling"
  }

(* UP TO HERE *)

, lambdaTheta1 ==
  { ParameterType -> External
  , Value         -> DefaultDimensionlessScale
  , Description   -> "Yukawa \\Xi_1^\\dagger \\bar{L} L^c coupling"
  }



  MR2 ==
  { ParameterType -> External
  , Value         -> 1000.0
  , Description   -> "R2 mass"
  }

, MD2 ==
  { ParameterType -> External
  , Value         -> 2000.0
  , Description   -> "D2 mass"
  }

, Yx ==
  { ParameterType    -> External
  , ComplexParameter -> False
  , Indices          -> {Index[Generation], Index[Generation]}
  , Value            -> { Yx[1,1] -> 0.1, Yx[1,2] -> 0.1, Yx[1,3] -> 0.1
                        , Yx[2,1] -> 0.1, Yx[2,2] -> 0.1, Yx[2,3] -> 0.1
                        , Yx[3,1] -> 0.1, Yx[3,2] -> 0.1, Yx[3,3] -> 0.1
                        }
  , TeX              -> x
  , InteractionOrder -> {NP, 1}
  , Description      -> "Coupling matrix of the R_2 leptoquark to L and u_R"
  }

, Yy ==
  { ParameterType    -> External
  , ComplexParameter -> False
  , Indices          -> {Index[Generation], Index[Generation]}
  ,  Value           -> { Yy[1,1] -> 0.1, Yy[1,2] -> 0.1, Yy[1,3] -> 0.1
                        , Yy[2,1] -> 0.1, Yy[2,2] -> 0.1, Yy[2,3] -> 0.1
                        , Yy[3,1] -> 0.1, Yy[3,2] -> 0.1, Yy[3,3] -> 0.1
                        }
  , TeX              -> y
  , InteractionOrder -> {NP, 1}
  , Description      -> "Coupling matrix of the R_2 leptoquark to e_R and d_L"
  }

, Yz ==
  { ParameterType    -> External
  , ComplexParameter -> False
  , Indices          -> {Index[Generation]}
  , Value            -> {Yz[1] -> 0.1, Yz[2] -> 0.1, Yz[3] -> 0.1}
  , TeX              -> z
  , InteractionOrder -> {NP, 1}
  , Description      -> "R2 leptoquark couplings to D2 and L"
  }

, Yw ==
  { ParameterType    -> External
  , ComplexParameter -> False
  , Indices          -> {Index[Generation]}
  , Value            -> {Yw[1] -> 0.1, Yw[2] -> 0.1, Yw[3] -> 0.1}
  , TeX              -> w
  , InteractionOrder -> {NP, 1}
  , Description      -> "R2 leptoquark couplings to D2 and Q"
  }

};

M$ClassesDescription =
{ S[200] ==
  { ClassName        -> R2p53
  , Mass             -> {MR2, Internal}
  , Width            -> {WR253, 5.0}
  , SelfConjugate    -> False
  , PropagatorLabel  -> "R253"
  , PropagatorType   -> D
  , PropagatorArrow  -> None
  , QuantumNumbers   -> {Q -> 5/3, LeptonNumber -> -1}
  , Indices          -> {Index[Colour]}
  , ParticleName     -> "R2p53"
  , AntiParticleName -> "R2p53*"
  , FullName         -> "R53"
  }

, S[201] ==
  { ClassName        -> R2p23
  , Mass             -> {MR2, Internal}
  , Width            -> {WR223, 5.0}
  , SelfConjugate    -> False
  , PropagatorLabel  -> "R2p23"
  , PropagatorType   -> D
  , PropagatorArrow  -> None
  , QuantumNumbers   -> {Q -> 2/3, LeptonNumber -> -1}
  , Indices          -> {Index[Colour]}
  , ParticleName     -> "R2p23"
  , AntiParticleName -> "R2p23*"
  , FullName         -> "R23"
  }

  (* VLQ Quarks X, Q=5/3*)
, F[200] ==
  { ClassName       -> X
  , SelfConjugate   -> False
  , Indices         -> {Index[Colour]}
  , Mass            -> {MX, 600}
  , Width           -> {WX, 5.0}
  , QuantumNumbers  -> {Q -> 5/3}
  , PropagatorLabel -> "X"
  , PropagatorType  -> Straight
  , PropagatorArrow -> Forward
  , PDG             -> 6000005
  , FullName        -> "X-quark"
  }

  (* VLQ Quarks T, Q=2/3 *)
, F[201] ==
  { ClassName       -> tp
  , SelfConjugate   -> False
  , Indices         -> {Index[Colour]}
  , Mass            -> {MTP, 600}
  , Width           -> {WTP, 5.0}
  , QuantumNumbers  -> {Q -> 2/3}
  , PropagatorLabel -> "tp"
  , PropagatorType  -> Straight
  , PropagatorArrow -> Forward
  , PDG             -> 6000006
  , FullName        -> "T-quark"
  }

  (* VLQ Quarks B, Q=-1/3 *)
, F[202] ==
  { ClassName       -> bp
  , SelfConjugate   -> False
  , Indices         -> {Index[Colour]}
  , Mass            -> {MBP, 600}
  , Width           -> {WBP, 5.0}
  , QuantumNumbers  -> {Q -> -1/3}
  , PropagatorLabel -> "bp"
  , PropagatorType  -> Straight
  , PropagatorArrow -> Forward
  , PDG             -> 6000007
  , FullName        -> "B-quark"
  }

  (* unphysical fields *)
, S[203] ==
  { ClassName      -> R2
  , Unphysical     -> True
  , Indices        -> {Index[SU2D], Index[Colour]}
  , FlavorIndex    -> SU2D
  , SelfConjugate  -> False
  , QuantumNumbers -> {Y -> 7/6}
  , Definitions    -> {R2[1,cc_] :> R2p53[cc], R2[2,cc_] :> R2p23[cc]}
  }

, F[103] ==
  { ClassName      -> D2
  , Unphysical     -> True
  , Indices        -> {Index[SU2W], Index[Colour]}
  , FlavorIndex    -> SU2W
  , SelfConjugate  -> False
  , QuantumNumbers -> {Y -> 2/3}
  , Definitions    -> { D2[sp_,1,cc_] :> (bp[sp,cc] + X[sp,cc])/Sqrt[2]
                      , D2[sp_,2,cc_] :> (bp[sp,cc] - X[sp,cc])/(I*Sqrt[2])
                      , D2[sp_,3,cc_] :> tp[sp,cc]
                      }
  }

};


(********************* The Lagrangian *********************)

(***** Kinetic and mass terms *****)
LR2Kin :=
  Module[
    {mu,a,cc},
    ExpandIndices[
      DC[R2bar[a,cc], mu] DC[R2[a,cc], mu] - MR2^2 R2bar[a,cc] R2[a,cc]
    , FlavorExpand -> {SU2W, SU2D}
    ]
  ];

LD2Kin :=
  Module[
    {mu,a,cc,sp,sp1,sp2},
    ExpandIndices[
      I D2bar[sp1,a,cc].Ga[mu,sp1,sp2].DC[D2[sp2,a,cc], mu] - MD2 D2bar[sp,a,cc] D2[sp,a,cc]
    , FlavorExpand -> {SU2W, SU2D}
    ]
  ];

(***** LQ-quark-lepton interactions *****)

(* This is the conjugate of what you have in the notes. You've made Yx real so
this should be fine for now *)

LR2YukRL :=
  Module[
    {a,b,sp,i,j,cc},
    ExpandIndices[
      - Yx[i,j] uRbar[sp,j,cc].LL[sp,b,i] R2[a,cc] Eps[a,b]
    , FlavorExpand->{SU2D, Generation}
    ]
  ];

LR2YukLR :=
  Module[
    {a,sp,i,j,cc},
    ExpandIndices[
      - Yy[i,j] lRbar[sp,i].QL[sp,a,j,cc] R2bar[a,cc]
    , FlavorExpand->{SU2D, Generation}
    ]
  ];

(***** R2D2 interactions *****)

LD2YukL :=
  Module[
    {a,b,c,sp,i,j,cc,k},
    ExpandIndices[
      - Yz[i] LLbar[sp,a,i].D2[sp,k,cc] R2bar[c,cc] 2*Ta[k,b,c] Eps[a,b]
    , FlavorExpand -> {SU2W, SU2D, Generation}
    ]
  ];

LD2YukQ :=
  Module[
    {a,b,c,sp,i,j,cc,k},
    ExpandIndices[
      - Yw[i] QLbar[sp,a,i,cc].D2[sp,k,cc] Phibar[c] 2*Ta[k,a,b] Eps[b,c]
    , FlavorExpand -> {SU2W, SU2D, Generation}
    ]
  ];

(***** Complete R2 Lagrangian *****)

LR2   := LR2Kin + LR2YukRL + HC[LR2YukRL] + LR2YukLR + HC[LR2YukLR];
LD2   := LD2Kin;
LMix  := LD2YukL + HC[LD2YukL] + LD2YukQ + HC[LD2YukQ];
LFull := LR2 + LD2 + LMix;
