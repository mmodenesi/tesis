from functools import partial

LANG, IAMEAN, SLOTTED, CH_UTILIZATION, SIM_DELAY = range(5)
PYTHON, CPP = 'python', 'c++'

DATA = [
    ['c++', 0.1, True, 0.006466311480521, 0.5848276320002697],
    ['python', 0.1, True, 0.006466311480521, 119.21491560300001],
    ['c++', 0.2, True, 0.037610105670009, 0.4584900680001738],
    ['python', 0.2, True, 0.037610105670009, 88.72029479499997],
    ['c++', 0.3, True, 0.098827804181821, 0.3809897589999309],
    ['python', 0.3, True, 0.098827804181821, 72.0835129140005],
    ['c++', 0.4, True, 0.16064480261995, 0.32006621599975915],
    ['python', 0.4, True, 0.16064480261995, 58.36702549600068],
    ['c++', 0.5, True, 0.21978882360328, 0.2715306320005766],
    ['python', 0.5, True, 0.21978882360328, 50.37430065300032],
    ['c++', 0.6, True, 0.26590445965143, 0.26100987900008477],
    ['python', 0.6, True, 0.26590445965143, 42.77850106799997],
    ['c++', 0.7, True, 0.30069543988558, 0.21912263300055201],
    ['python', 0.7, True, 0.30069543988558, 37.25045305599997],
    ['c++', 0.8, True, 0.32841614300196, 0.19208460500067304],
    ['python', 0.8, True, 0.32841614300196, 33.3296159420006],
    ['c++', 0.9, True, 0.35030633100803, 0.1798737869994511],
    ['python', 0.9, True, 0.35030633100803, 32.00576179299969],
    ['c++', 1, True, 0.3620135096168, 0.15734090299974923],
    ['python', 1, True, 0.3620135096168, 29.37238604600043],
    ['c++', 1.5, True, 0.37417182276006, 0.12501570099993842],
    ['python', 1.5, True, 0.37417182276006, 21.154129888999705],
    ['c++', 2, True, 0.35808126966332, 0.09409088400025212],
    ['python', 2, True, 0.35808126966332, 15.896753297000032],
    ['c++', 2.5, True, 0.32315465311504, 0.08267888499995024],
    ['python', 2.5, True, 0.32315465311504, 13.319568406999679],
    ['c++', 3, True, 0.29777006758858, 0.07369433799976832],
    ['python', 3, True, 0.29777006758858, 11.031811740999728],
    ['c++', 4, True, 0.25638056059959, 0.05768032499963738],
    ['python', 4, True, 0.25638056059959, 8.387699105999673],
    ['c++', 5, True, 0.21972448797673, 0.05032164899967029],
    ['python', 5, True, 0.21972448797673, 6.728005928999664],
    ['c++', 6, True, 0.19226166810694, 0.045464001999789616],
    ['python', 6, True, 0.19226166810694, 5.965362578000168],
    ['c++', 7, True, 0.16888638161703, 0.039412827999512956],
    ['python', 7, True, 0.16888638161703, 4.820465584999511],
    ['c++', 8, True, 0.15047976608798, 0.03712264900059381],
    ['python', 8, True, 0.15047976608798, 4.209939122000833],
    ['c++', 9, True, 0.13547151185145, 0.03749758800040581],
    ['python', 9, True, 0.13547151185145, 3.5890565689996947],
    ['c++', 10, True, 0.124433562124, 0.03290581700002804],
    ['python', 10, True, 0.124433562124, 3.4924967070001003],
    ['c++', 11, True, 0.11527294248685, 0.03088372000001982],
    ['python', 11, True, 0.11527294248685, 3.1877669390005394],
    ['c++', 12, True, 0.10688476729002, 0.031212740000228223],
    ['python', 12, True, 0.10688476729002, 2.8483696450002753],
    ['c++', 13, True, 0.098825058505501, 0.03161678299966297],
    ['python', 13, True, 0.098825058505501, 2.701907260000553],
    ['c++', 14, True, 0.093616973912472, 0.027711645000636054],
    ['python', 14, True, 0.093616973912472, 2.4378241889999117],
    ['c++', 15, True, 0.088037337300734, 0.026821356999789714],
    ['python', 15, True, 0.088037337300734, 2.4747979300000225],
    ['c++', 0.1, False, 0, 0.7302508539996779],
    ['python', 0.1, False, 0, 145.31575596400035],
    ['c++', 0.2, False, 0, 0.5210480169998846],
    ['python', 0.2, False, 0, 101.02737987899945],
    ['c++', 0.3, False, 0.00076325300354625, 0.3756052059998183],
    ['python', 0.3, False, 0.00076325300354625, 72.07944632700037],
    ['c++', 0.4, False, 0.0039588643604514, 0.3123093889989832],
    ['python', 0.4, False, 0.0039588643604514, 59.69938408300004],
    ['c++', 0.5, False, 0.011682838306187, 0.2664828619999753],
    ['python', 0.5, False, 0.011682838306187, 48.79803602100037],
    ['c++', 0.6, False, 0.025603452468452, 0.23273999100092624],
    ['python', 0.6, False, 0.025603452468452, 44.44012174099953],
    ['c++', 0.7, False, 0.039420787497505, 0.21011473699945782],
    ['python', 0.7, False, 0.039420787497505, 39.112202779000654],
    ['c++', 0.8, False, 0.056545297349915, 0.17592885900012334],
    ['python', 0.8, False, 0.056545297349915, 35.348774288999266],
    ['c++', 0.9, False, 0.072230508946743, 0.17366348799987463],
    ['python', 0.9, False, 0.072230508946743, 30.71674825699847],
    ['c++', 1, False, 0.087666903783682, 0.15758263200041256],
    ['python', 1, False, 0.087666903783682, 26.81410339300055],
    ['c++', 1.5, False, 0.14858681850652, 0.12107748500056914],
    ['python', 1.5, False, 0.14858681850652, 19.10262854999928],
    ['c++', 2, False, 0.17922565762884, 0.09663343200008967],
    ['python', 2, False, 0.17922565762884, 15.320787870999993],
    ['c++', 2.5, False, 0.18868286038616, 0.08128265099912824],
    ['python', 2.5, False, 0.18868286038616, 12.419898019001266],
    ['c++', 3, False, 0.19206834134435, 0.07034532000034233],
    ['python', 3, False, 0.19206834134435, 11.003627136999057],
    ['c++', 4, False, 0.18305322477005, 0.05974540800161776],
    ['python', 4, False, 0.18305322477005, 7.984181870999237],
    ['c++', 5, False, 0.16710512686259, 0.05028533099903143],
    ['python', 5, False, 0.16710512686259, 6.520586059999914],
    ['c++', 6, False, 0.15294315842394, 0.04651024399936432],
    ['python', 6, False, 0.15294315842394, 5.483925722999629],
    ['c++', 7, False, 0.13886721388324, 0.0404815130004863],
    ['python', 7, False, 0.13886721388324, 4.905973154000094],
    ['c++', 8, False, 0.12723940926008, 0.03751071900114766],
    ['python', 8, False, 0.12723940926008, 4.3254758639996],
    ['c++', 9, False, 0.11648069652152, 0.034700645999691915],
    ['python', 9, False, 0.11648069652152, 3.870026284999767],
    ['c++', 10, False, 0.1087283587839, 0.032678042000043206],
    ['python', 10, False, 0.1087283587839, 3.3397165300011693],
    ['c++', 11, False, 0.10134104010002, 0.03193541699874913],
    ['python', 11, False, 0.10134104010002, 3.0784308909987885],
    ['c++', 12, False, 0.094900113189545, 0.029999125999893295],
    ['python', 12, False, 0.094900113189545, 2.9317122180000297],
    ['c++', 13, False, 0.090550009969597, 0.028916971999933594],
    ['python', 13, False, 0.090550009969597, 2.700906940001005],
    ['c++', 14, False, 0.085604136965468, 0.02776208700015559],
    ['python', 14, False, 0.085604136965468, 2.5422813530003623],
    ['c++', 15, False, 0.080802896018396, 0.02700130499943043],
    ['python', 15, False, 0.080802896018396, 2.188418952000575],
]


def generic_filter(field, data_in, arg):
    for elem in data_in:
        if elem[field] == arg:
            yield elem

filter_by_lang = partial(generic_filter, LANG)
filter_by_slotted = partial(generic_filter, SLOTTED)


def generic_selector(field, data_in, lang, slotted):
    by_lang = filter_by_lang(data_in, lang)
    data = filter_by_slotted(by_lang, slotted)
    for point in data:
        yield (point[IAMEAN], point[field])


channel_utilization = partial(generic_selector, CH_UTILIZATION)
sim_delay = partial(generic_selector, SIM_DELAY)


if __name__ == '__main__':
    # print(*sim_delay(DATA, CPP, True))
    # print(*sim_delay(DATA, CPP, False))
    print(*sim_delay(DATA, PYTHON, True))
    print(*sim_delay(DATA, PYTHON, False))

    # print(*channel_utilization(DATA, CPP, True))
    # print(*channel_utilization(DATA, CPP, False))
    # print(*channel_utilization(DATA, PYTHON, True))
    # print(*channel_utilization(DATA, PYTHON, False))
