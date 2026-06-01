# Projekt në Modelime në Fizikë: Personalized PageRank

**Studenti:** Donaldo Shtjefni  
**Lënda:** Modelime në Fizikë  
**Mjedisi i Zhvillimit:** JupyterLab (I optimizuar për Python 3.13)  

---

## 📌 Përshkrimi i Projektit

Ky projekt implementon algoritmën **Personalized PageRank (PPR)** nga gërvishtja (*from scratch*) pa përdorur librari komplekse rrjetesh si NetworkX. Qëllimi është modelimi i një sistemi rekomandimi për materiale kursi akademike bazuar në strukturuar e lidhjeve midis tyre dhe preferencave tematike të një studenti (Vektori i Personalizimit $v$).

Në fizikën e sistemeve komplekse dhe mekanikën statistiko-kuantike, ky model përfaqëson një **Random Walk (Ecje Rastësore)** me mundësi "teleportimi" drejt gjendjeve (nyjeve) të preferuara, duke ndjekur një proces Markovian stokaotik.

### Rrjeti i Materialeve të Kursit (5 Nyje):
0. **Mekanika Analitike**
1. **Termodinamika**
2. **Fizika Kvantike**
3. **Metodat Matematikore**
4. **Modelime në Fizikë**

---

## 🛠️ Teknologjitë dhe Libraritë

Projekti është ndërtuar për të qenë plotësisht i pajtueshëm me **Python 3.13** në mjedise JupyterLab online/lokale. Libraritë e përdorura janë:
* `numpy` — Për llogaritjet matricore, shumëzimin pikësor (`np.dot`) dhe normat e konvergjencës.
* `matplotlib` — Për vizualizimin e të dhënave në mjedise 2D dhe 3D.

---

## 📐 Metodologjia Matematikore dhe Fizike

Modeli bazohet në metodën iterative të fuqisë (**Power Iteration Method**). Ekuacioni themelor i tranzicionit për PageRank-un e Personalizuar është:

$$p^{(t+1)} = \alpha \cdot p^{(t)} M + (1 - \alpha) \cdot v$$

Ku:
* $p^{(t)}$ është vektori i probabilitetit të rëndësisë në hapin $t$.
* $M$ është matrica e tranzicionit e normalizuar sipas rreshtave (probabilitetet e kalimit).
* $\alpha$ është faktori i dämpingut (rrezatimit), i vendosur si standard në `0.85`.
* $v$ është vektori i personalizimit që përcakton interesat specifike të studentit.

---

## 📊 Struktura e Jupyter Notebook

Notebook-u është i ndarë në celula logjike si vijon:

1.  **Celula 1 (Markdown):** Hyrje dhe informacionet gjenerale të projektit.
2.  **Celula 2 (Code):** Përcaktimi i nyjeve dhe ndërtimi i Matricës së Adjacencës ($A$).
3.  **Celula 3 (Code):** Normalizimi i matricës për të krijuar Matricën e Tranzicionit Stastik ($M$).
4.  **Celula 4 (Code):** Algoritmi kryesor i PPR me ruajtjen e historikut të hapave për vizualizim.
5.  **Celula 5 (Code):** Skenari 1 (Studenti i fokusuar tek *Fizika Kvantike*).
6.  **Celula 6 (Code):** Skenari 2 (Studenti i fokusuar tek *Modelimet* dhe *Metodat Matematikore*).
7.  **Celula 7 (Code):** Paneli i përbashkët i grafikëve (Grafiku me Shtylla 2D krahasues dhe Grafiku Surface 3D i konvergjencës).

---

## 📈 Vizualizimet e Përfshira

Në fund të notebook-ut gjenerohen dy grafikë paralelë:
* **Grafiku A (Majtas):** Krahasimi 2D me shtylla i shpërndarjes finale të peshës për të dy skenarët e preferencave.
* **Grafiku B (Djathtas):** Evolucioni 3D i sistemit (`plot_surface`), i cili tregon dinamikën se si konvergjojnë vlerat e rëndësisë hap pas hapi përgjatë iteracioneve drejt gjendjes së ekuilibrit.

---

## 🚀 Si ta ekzekutoni projektin

1. Hapni mjedisin tuaj **JupyterLab**.
2. Krijoni një Notebook të ri me kernel **Python 3.13**.
3. Kopjoni kodet e secilës celulë sipas radhës kronologjike.
4. Ekzekutoni celulat me radhë duke përdorur kombinimin e tasteve `Shift + Enter`.
