# Projekt 1: Model SIR Hapësinor në Rrjet, Difuzion Lokal dhe Karantinë

**Autori:** Klaus Dragjoshi

**Lënda:** Modelim ne Fizike

---

## 1. Përshkrimi i Projektit
Ky projekt synon ndërtimin dhe simulimin e modelit **SIR** (Susceptible-Infected-Recovered) në një mjedis dydimensional. Ndryshe nga modelet klasike me përzierje homogjene, ky model fokusohet në **difuzionin lokal**, ku infektimi përhapet te fqinjët e drejtpërdrejtë, duke simuluar një përhapje më reale gjeografike të një epidemie.

## 2. Objektivat
* Modelimi i gjendjeve epidemiologjike (S, I, R) në një rrjetë diskrete.
* Studimi i ndikimit të parametrave $\beta$ ) dhe $\gamma$ 
* Analizimi i efektit të **karantinës globale** kur kalohet një prag i caktuar i të infektuarve.

## 3. Implementimi Algoritmik
Projekti është realizuar në Python duke përdorur libraritë `NumPy` për llogaritjet numerike dhe `Matplotlib` për vizualizimin e të dhënave.

### Funksionalitetet kryesore:
- **Inicimi:** Krijimi i një rrjete me individë të shëndetshëm (S) dhe vendosja e një vatre infeksioni (I) në qendër.
- **Logjika e Fqinjësisë:** Përdorimi i fqinjëve Moore (8 fqinjët rrethues) për të llogaritur probabilitetin e infektimit sipas formulës:
  $$P(S \to I) = 1 - (1 - \beta)^{n_i}$$
  ku $n_i$ është numri i fqinjëve të infektuar.
- **Karantina:** Reduktimi i parametrit $\beta$ me 80%  nëse numri total i të infektuarve kalon pragun `quarantine_threshold`.

## 4. Analiza e Rezultateve
Nga simulimet e kryera :
- **Pa Karantinë:** Infeksioni përhapet me shpejtësi në formë rrethore nga vatra qendrore, duke arritur një kulm të lartë (pik) përpara se të ulet.
- **Me Karantinë:** Kurba e të infektuarve "shtohet" , duke reduktuar ngarkesën maksimale në sistem dhe duke zgjatur kohëzgjatjen e epidemisë por me intensitet më të ulët.

## 5. Udhëzime për Ekzekutim
1. Sigurohuni që keni instaluar `numpy` dhe `matplotlib`.
2. Hapni skedarin `Raport.ipynb` ose ekzekutoni script-in në një ambient Jupyter.
3. Parametrat si $N$, $\beta$, dhe $\gamma$ mund të modifikohen në fillim të kodit për të parë skenarë të ndryshëm.

---
*Punoi: Klaus Dragjoshi*
