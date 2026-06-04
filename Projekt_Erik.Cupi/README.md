# Atraktorët Lorenz dhe Rössler

## Përshkrimi

Ky projekt simulon dy sisteme kaotike klasike: sistemin Lorenz dhe sistemin Rössler.

Qëllimi është të tregohet forma e atraktorëve dhe ndjeshmëria ndaj kushteve fillestare. Kjo do të thotë se dy trajektore që nisin shumë afër njëra-tjetrës mund të largohen me kalimin e kohës.

## Modeli Lorenz

Sistemi Lorenz përshkruhet nga tre ekuacione diferenciale:

dx/dt = sigma(y - x)

dy/dt = x(rho - z) - y

dz/dt = xy - beta z

## Modeli Rössler

Sistemi Rössler përshkruhet nga:

dx/dt = -y - z

dy/dt = x + ay

dz/dt = b + z(x - c)

## Struktura e projektit

- `src/attractors.py` – funksionet për sistemet Lorenz dhe Rössler dhe metoda Runge-Kutta 4.
- `Scripts/Lorenz_Rossler.py` – ekzekutimi i simulimit dhe gjenerimi i figurës.
- `figures/lorenz_rossler.png` – figura e gjeneruar nga programi.

## Instalimi

```bash
pip install -r requirements.txt

## Punoi: Erik Cupi



