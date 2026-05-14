#  Projekti 3 : Lorenz & Rössler Attractors: Chaos Analysis

Ky projekt shqyrton sjelljen e sistemeve dinamike jolineare në hapësirën tridimensionale. Përmes simulimeve numerike, ne analizojmë se si ligje matematike deterministike prodhojnë sjellje kaotike dhe të paparashikueshme, duke vërtetuar matematikisht **"Efektin Flutur"**.

---

## Qëllimi i Projektit
Ndërtimi i një pakete simulimi për dy sisteme klasike kaotike (**Lorenz** dhe **Rössler**) për të krahasuar gjeometrinë e atraktorëve dhe për të matur ndjeshmërinë e tyre ndaj kushteve fillestare.

##  Hapat Metodologjikë

### 1. Implementimi i Modeleve
Kemi koduar ekuacionet diferenciale për të dy sistemet me parametra të kontrollueshëm:
* **Sistemi Lorenz:** - $\dot{x} = \sigma(y - x)$
  - $\dot{y} = x(\rho - z) - y$
  - $\dot{z} = xy - \beta z$
* **Sistemi Rössler:** - $\dot{x} = -y - z$
  - $\dot{y} = x + ay$
  - $\dot{z} = b + z(x - c)$

### 2. Vizualizimi 3D i Atraktorëve
Gjenerimi i trajektoreve në hapësirën e fazave për të vëzhguar "Atraktorët e Çuditshëm". Këto struktura tregojnë se trajektorja mbetet brenda një zone të kufizuar pa u përsëritur asnjëherë (aperiodicitet).

### 3. Analiza e Ndjeshmërisë (Efekti Flutur)
Simulimi i dy kushteve fillestare me një diferencë infinitesimale prej $\delta_0 = 10^{-9}$. Përmes matjes së distancës $d(t)$, vërtetohet se gabimi rritet në mënyrë eksponenciale në kohë.

### 4. Skanimi i Parametrave
Realizimi i skanimeve për parametrat $\rho$ (te Lorenz) dhe $c$ (te Rössler) për të vëzhguar tranzicionin e sistemit nga orbita periodike në kaos të plotë.

### 5. Diskutimi Kritik
Analiza e faktit pse vizualizimi estetik 3D nuk mjafton si provë shkencore. Kaosi vërtetohet përmes **Eksponentit të Lyapunov-it** (pjerrësia e divergjencës në shkallë logaritmike).

---

##  Struktura e Projektit
```text
lorenz_rossler_attractors/
├── README.md
├── src/
│   ├── models/
│   │   ├── lorenz.py
│   │   └── rossler.py
│   ├── analysis/
│   │   └── sensitivity.py
│   └── visualization/
│       └── phase3d.py
└── scripts/
    └── compare_sensitivity.py
