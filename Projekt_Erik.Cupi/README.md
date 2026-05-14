#  Analiza e Sistemeve Kaotike: Lorenz & Rössler
### Studimi i Ndjeshmërisë ndaj Kushteve Fillestare (Efekti Flutur)

---

## ## 1. Përshkrimi i Projektit
Ky projekt shqyrton sjelljen e sistemeve dinamike jolineare në hapësirën tridimensionale. Përmes modelimit të atraktorëve të Lorenz dhe Rössler, vërtetohet se në sisteme kaotike, një ndryshim mikroskopik në kushtet fillestare çon në rezultate krejtësisht të ndryshme në një kohë të shkurtër, duke e bërë parashikimin afatgjatë të pamundur.

## ## 2. Objektivat
* **Modelimi Matematik:** Implementimi i ekuacioneve diferenciale tridimensionale.
* **Vizualizimi i Hapësirës së Fazave:** Gjenerimi i atraktorëve 3D aperiodikë.
* **Analiza e Ndjeshmërisë:** Matja e distancës euklidiane $d(t)$ midis dy trajektoreve fqinje.
* **Skanimi i Parametrave:** Identifikimi i kalimit nga stabiliteti në kaos përmes variimit të parametrave kontrollues ($\rho$ dhe $c$).

## ## 3. Implementimi Algoritmik
1. **Definimi i Sistemeve:** Funksionet llogarisin derivatet $(\dot{x}, \dot{y}, \dot{z})$ sipas ligjeve jolineare.
2. **Integrimi Numerik:** Përdorimi i `scipy.integrate.odeint` (metoda Runge-Kutta) për zgjidhjen e sistemeve.
3. **Perturbimi:** Krijimi i një trajektoreje të dytë me diferencë infinitesimale $\delta_0 = 10^{-9}$.
4. **Kalkulimi i Distancës:** Ndjekja e divergjencës euklidiane në kohë për matjen e eksponentit të Lyapunov-it.

## ## 4. Analiza e Rezultateve
* **Gjeometria:** Atraktorët shfaqin struktura fraktale komplekse ku trajektoret nuk priten asnjëherë.
* **Divergjenca Eksponenciale:** Grafiku logaritmik vërteton se gabimi rritet eksponencialisht, duke konfirmuar natyrën kaotike.
* **Prova e Kaosit:** Konfirmohet se vizualizimi estetik 3D është vetëm një tregues, ndërsa prova shkencore mbetet matja numerike e divergjencës.

## ## 5. Udhëzime për Ekzekutim
1. Instalo varësitë: `pip install numpy matplotlib scipy`
2. Hap mjedisin **Jupyter Lab**.
3. Ekzekuto qelizat me radhë për të gjeneruar simulimet dhe grafikët krahasues.

---

##  Përfundime dhe Diskutim Final
Ky projekt vërtetoi se kompleksiteti i një sistemi nuk vjen domosdoshmërisht nga numri i madh i variablave, por nga natyra jolineare e ndërveprimeve midis tyre. Përmes modelimit të sistemit **Lorenz** dhe **Rössler**, pamë se:
1. Sistemet dinamike mund të jenë deterministike (ndjekin rregulla të sakta), por plotësisht të paparashikueshme në afatgjatë.
2. **"Efekti Flutur"** është një fenomen matematikor i matshëm dhe jo thjesht një metaforë teorike.
3. Analiza llogaritëse (computational) është mjeti i vetëm që na lejon të deshifrojmë strukturat e fshehura brenda kaosit.

---

###  Informacion mbi Autorin
* **Punoi:** Erik Cupi  
* **Lënda:** Modelim në Fizikë  
* **Institucioni:** Departamenti i Fizikës  
* **Viti Akademik:** 2026  

---

###  Shënime Shtesë mbi Projektin
* **Saktësia Numerike:** Është përdorur një hap kohor $dt = 0.005$ për të garantuar saktësinë e divergjencës kundrejt zhurmës numerike.
* **Zbatimi në Jetën Reale:** Këto modele aplikohen në parashikimin e motit, dinamikën e lëngjeve, kardiologji dhe tregjet financiare.
* **Sfidat:** Balancimi i kohës së simulimit me rezolucionin e nevojshëm për të kapur kalimin në kaos në shkallën logaritmike.

---
*Ky projekt është pjesë e ciklit të detyrave llogaritëse për lëndën "Modelim në Fizikë".*
