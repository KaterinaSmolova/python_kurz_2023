teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]



ranni_teploty = [hodnoty[0] for hodnoty in teploty]

print(ranni_teploty)

nocni_teploty = [hodnoty[3] for hodnoty in teploty]

print(nocni_teploty)

poledni_nocni_teploty = [[hodnoty[1], hodnoty[3]] for hodnoty in teploty]

print(poledni_nocni_teploty)

prumerne_teploty = [round(sum(hodnoty)/len(hodnoty), 2) for hodnoty in teploty]

print(prumerne_teploty)
