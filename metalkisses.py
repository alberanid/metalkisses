#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markovify

BACI = 'baci.txt'
METAL = 'metal.txt'
QUANTI_BACI = 24000


def baciniFratturati():
    with open(BACI) as f:
        baci = f.read()
    baciModel = markovify.NewlineText(baci)

    with open(METAL) as f:
        metal = f.read()
    metalModel = markovify.NewlineText(metal)

    bmModel = markovify.combine([baciModel, metalModel], [1, 1.3])
    for i in range(QUANTI_BACI):
        amorMetallo = bmModel.make_short_sentence(max_chars=140,
                                                  max_overlap_ratio=.35,
                                                  tries=200) or 'il mio cuore è ruggine sanguinante!'
        print('%s\n' % amorMetallo)


if __name__ == '__main__':
    try:
        baciniFratturati()
    except KeyboardInterrupt:
        print('\n\nMA SEI SENZA CUORE!')
