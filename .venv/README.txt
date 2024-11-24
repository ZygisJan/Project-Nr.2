# Paveikslėlių Karpymas ir Transformacija su Python (PP2 Project)

Šis projektas susideda iš dviejų dalių, kurios kartu realizuoja paveikslėlio karpymą ir juostų pertvarkymą tiek horizontaliai, tiek vertikaliai. Programa yra padalinta į dvi dalis:

- Pirmoji dalis (PP2_part_1.py): Supjausto paveikslėlį horizontaliomis juostomis ir išskirsto jas į lygines bei nelygines grupes.
- Antroji dalis (PP2_part_2.py): Kombinuoja gautas juostas ir supjausto jas vertikaliai, sukuriant naujus rezultatus.

---

# Projekto Tikslai
1. Pademonstruoti paveikslėlio segmentavimą ir transformavimą.
2. Naudoti Python `Pillow` biblioteką paveikslėlio pjaustymui, pertvarkymui ir kombinavimui.
3. Vizualizuoti kiekvieną tarpinių rezultatų etapą.

---

# Failų Struktūra

PP2_project/
├── collage_even_slices.jpg        # Paveikslėlis su lyginėmis juostomis (pirmos dalies rezultatas).
├── collage_odd_slices.jpg         # Paveikslėlis su nelyginėmis juostomis (pirmos dalies rezultatas).
├── combined_image.jpg             # Paveikslėlis, kuris apjungia lygines ir nelygines juostas.
├── Ice_age.jpg                    # Pradinis paveikslėlis, naudojamas projekte.
├── PP2_part_1.py                  # Pirmos dalies Python kodas (pjausto horizontaliai, lyginiai/nelyginiai).
├── PP2_part_2.py                  # Antros dalies Python kodas (kombinuoja, pjausto vertikaliai).
├── pyvenv.cfg                     # Virtualios aplinkos konfigūracijos failas.
├── README.txt                     # Projekto dokumentacija.
├── sliced_combined_image_even.jpg # Galutinis rezultatas: lyginės juostos vertikaliai apdorotos.
├── sliced_combined_image_odd.jpg  # Galutinis rezultatas: nelyginės juostos vertikaliai apdorotos.
└── requirements.txt               # Naudojamų bibliotekų sąrašas.

# Instrukcijos Paleidimui:
# Reikalingos Bibliotekos
Projektas naudoja šias Python bibliotekas:
-Pillow: Biblioteka vaizdų karpymui ir apdorojimui.

Visos reikalingos bibliotekos išvardytos faile `requirements.txt`.

# Kaip Įdiegti Bibliotekas?
1. Atsisiųskite projektą.
2. Paleiskite šią komandą terminale, kad įdiegtumėte visas priklausomybes:
   ```bash
   pip install -r requirements.txt

