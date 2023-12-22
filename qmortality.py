import math


def qmortality_female(
    age: int,
    alcohol_cat6: int,
    b_AF: int,
    b_CCF: int,
    b_antipsychotic: int,
    b_anycancer: int,
    b_asthmacopd: int,
    b_carehome: int,
    b_corticosteroids: int,
    b_cvd: int,
    b_dementia: int,
    b_epilepsy: int,
    b_learning: int,
    b_legulcer: int,
    b_liverpancreas: int,
    b_parkinsons: int,
    b_poormobility: int,
    b_ra: int,
    b_renal: int,
    b_type1: int,
    b_type2: int,
    b_vte: int,
    bmi: float,
    c_hb: int,
    ethrisk: int,
    hes_admitprior_cat: int,
    high_lft: int,
    high_platlet: int,
    s1_appetiteloss: int,
    s1_dyspnoea: int,
    s1_weightloss: int,
    smoke_cat: int,
    surv: int,
    town: float,
) -> int:
    survivor = [0, 0.984712481498718, 0.971753656864166]

    # Conditional Arrays

    Ialcohol = [
        0,
        -0.1743519944196435800000000,
        -0.2037985915003640000000000,
        -0.1487866194850515400000000,
        0.1934616863915854500000000,
        0.3817719239353779000000000,
    ]

    Iethrisk = [
        0,
        0,
        -0.1184311122140491900000000,
        -0.0079993587678865198000000,
        -0.0819024843978672780000000,
        -0.2031967274638343500000000,
        -0.2878522264880571400000000,
        -0.3863917396822835200000000,
        -0.6352339686269850000000000,
        -0.1431116831880673600000000,
    ]

    Ihesprior = [
        0,
        0.7183345278452039100000000,
        1.0908031544870831000000000,
        1.5451828140923398000000000,
    ]

    Ismoke = [
        0,
        0.1671745442187545500000000,
        0.5814293829425862800000000,
        0.7287899092313985200000000,
        0.8285737297861006700000000,
    ]

    # Applying fractional polynomial transforms

    age = age / 10
    age_2: float = pow(age, -2) * math.log(age)
    age_1: float = pow(age, -2)

    bmi = bmi / 10
    bmi_2 = pow(bmi, -0.5)
    bmi_1 = pow(bmi, -1)

    age_1 = age_1 - 0.017261177301407
    age_2 = age_2 - 0.035034108906984
    bmi_1 = bmi_1 - 0.369150280952454
    bmi_2 = bmi_2 - 0.607577383518219
    town = town - -0.626556754112244

    # Start of sum
    a = 0.0

    # == Sum from conditional values ==
    a += Ialcohol[alcohol_cat6]
    a += Iethrisk[ethrisk]
    a += Ihesprior[hes_admitprior_cat]
    a += Ismoke[smoke_cat]

    # == Sum from continuous values ==
    a += age_1 * 1508.5794831250275000000000000
    a += age_2 * -1177.0684822755481000000000000
    a += bmi_1 * 21.1133405539211200000000000
    a += bmi_2 * -24.5730725246275060000000000
    a += town * 0.0240907697129667110000000

    # == Sum from boolean values ==

    a += b_AF * 0.3325235176067262700000000
    a += b_CCF * 0.5064168315327032300000000
    a += b_antipsychotic * 0.4762650644070562900000000
    a += b_anycancer * 0.6472008940542218800000000
    a += b_asthmacopd * 0.1779972151465200300000000
    a += b_carehome * 0.5873959878506748200000000
    a += b_corticosteroids * 0.3633787252029762600000000
    a += b_cvd * 0.2710536519380971600000000
    a += b_dementia * 0.9597731758531232700000000
    a += b_epilepsy * 0.2011576211215723400000000
    a += b_learning * 0.1383932819999377200000000
    a += b_legulcer * 0.4761272769263114000000000
    a += b_liverpancreas * 0.4740335757824246100000000
    a += b_parkinsons * 0.5909056393737474000000000
    a += b_poormobility * 0.4900408466685850000000000
    a += b_ra * 0.2567732758493634400000000
    a += b_renal * 0.6771627443705151600000000
    a += b_type1 * 0.3127839118187618600000000
    a += b_type2 * 0.2973793306107276900000000
    a += b_vte * 0.1780046583740140200000000
    a += c_hb * 0.6586424893734315100000000
    a += high_lft * 0.4761223716365546900000000
    a += high_platlet * 0.3075672826462378400000000
    a += s1_appetiteloss * 0.2603422570683565600000000
    a += s1_dyspnoea * 0.2827368282380097200000000
    a += s1_weightloss * 0.2241662410988176600000000

    # == Sum from interaction terms

    a += age_1 * (hes_admitprior_cat == 1) * 0.0351583942110549120000000
    a += age_1 * (hes_admitprior_cat == 2) * -109.5168823277328200000000000
    a += age_1 * (hes_admitprior_cat == 3) * -351.3546190484985900000000000
    a += age_1 * b_CCF * -19.1721614342637530000000000
    a += age_1 * b_antipsychotic * -133.2331971051913500000000000
    a += age_1 * b_anycancer * 197.7976434381271200000000000
    a += age_1 * b_carehome * 8.7645882901669339000000000
    a += age_1 * b_corticosteroids * -84.4591681203892650000000000
    a += age_1 * b_cvd * -152.3838753524188700000000000
    a += age_1 * b_dementia * -487.3745694179724000000000000
    a += age_1 * b_legulcer * -18.8046731684082110000000000
    a += age_1 * b_liverpancreas * -198.9966883241830800000000000
    a += age_1 * b_poormobility * -277.2509814649311000000000000
    a += age_1 * b_renal * -324.7882093197725300000000000
    a += age_1 * b_type2 * -338.2992514394883300000000000
    a += age_1 * c_hb * -276.0898116311615800000000000
    a += age_1 * high_lft * -49.2301078035400510000000000
    a += age_1 * s1_dyspnoea * -302.9575553942258400000000000
    a += age_1 * town * -30.9214522323932110000000000
    a += age_2 * (hes_admitprior_cat == 1) * 38.3704628590155390000000000
    a += age_2 * (hes_admitprior_cat == 2) * 124.5624518720805200000000000
    a += age_2 * (hes_admitprior_cat == 3) * 301.5614530259237500000000000
    a += age_2 * b_CCF * 35.6954151435173590000000000
    a += age_2 * b_antipsychotic * 108.8453013528351900000000000
    a += age_2 * b_anycancer * -67.1545110002867460000000000
    a += age_2 * b_carehome * 35.0125181870904710000000000
    a += age_2 * b_corticosteroids * 84.3464059491397080000000000
    a += age_2 * b_cvd * 107.4067357534877400000000000
    a += age_2 * b_dementia * 366.2255288273296400000000000
    a += age_2 * b_legulcer * 43.7856895954169260000000000
    a += age_2 * b_liverpancreas * 175.3944326624610100000000000
    a += age_2 * b_poormobility * 201.4412389111520800000000000
    a += age_2 * b_renal * 249.2372907754739200000000000
    a += age_2 * b_type2 * 228.4257899683014400000000000
    a += age_2 * c_hb * 207.0135783712442500000000000
    a += age_2 * high_lft * 63.1507149099797970000000000
    a += age_2 * s1_dyspnoea * 220.4008767640308700000000000
    a += age_2 * town * 22.5388366303935900000000000

    print(a)
    print(math.exp(a))
    print(survivor[surv])
    print(pow(survivor[surv], math.exp(a)))

    # == Calculate the score ==
    score = 100.0 * (1 - pow(survivor[surv], math.exp(a)))
    return round(score, 6)


s = qmortality_female(
    75,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    40,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    2
)

print(s)
print(round(s,6))

def qmortality_male() -> int:
    return 0
