# Model SIR hapesinor ne rrjet, difuzion lokal dhe karantine

## Përshkrimi

Ky projekt simulon një model SIR hapësinor në një rrjet dy-dimensional.

Qëllimi është të tregohet përhapja e një infeksioni në një rrjet lokal, ku çdo qelizë mund të jetë në një nga tre gjendjet:

- S: susceptible
- I: infected
- R: recovered

Në ndryshim nga modeli klasik SIR me përzierje homogjene, këtu infektimi ndodh lokalisht nga fqinjët më të afërt.

## Modeli

Në çdo hap kohor:

- Një qelizë e shëndetshme mund të infektohet nga fqinjët infektivë.
- Një qelizë infektive mund të kalojë në gjendjen recovered.
- Karantina modelohet duke ulur probabilitetin e infektimit.

## Struktura e projektit

- `src/sir_model.py` – funksionet kryesore të modelit SIR.
- `Scripts/Spatial_SIR.py` – ekzekutimi i simulimit dhe gjenerimi i figurës.
- `figures/spatial_sir.png` – figura e gjeneruar nga programi.

## Instalimi

```bash
pip install -r requirements.txt

##Punoi: Klaus Dragjoshi
