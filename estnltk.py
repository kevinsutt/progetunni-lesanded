# siin importitakse pakette
from estnltk import Text
from estnltk.taggers import NerTagger
# siin on tekst
text = Text('''Projekt “KV korterite andmebaas”
Ajahinnang tööle
Analüüs ja senise koodi läbivaatus: 7 tundi
Dokumenteerimine: 0,5 tundi
Testimine: 2 tundi
Paigaldus: 0,5 tundi
Töö tasu
Tunni hind on 35 € arendaja kohta.
Juhul kui ajakulu on suurem kui tegelikkuses, ei arvestata lisatunde.
Töö teostamise ajakulu on kokku 10 tundi. Hind 599 eurot + km.
Töö oleks valmis neljapäevaks, 30. märts 2022.
Töö sisukirjeldus
Persoona: Andrus, 43-aastane, soovib korterit Tartusse.
● Andrus soovib osta omale korteri Tartusse ja soovib leida parimat hinda. Ta soovib
näha kinnisvarade hindu, et mõista, palju Tartus korterid maksavad.
Persoona: Käo Jaan, 31-aastane, investor.
● Käo Jaan on kogenud kinnisvarainvestor ning ta soovib jälgida erinevaid kinnisvara
üksuseid Tartus, Pärnus ja Tallinnas hinna poolest.
Persoona: Triin, 37-aastane.
● Triin soovib müüa oma korterit, kes pole hindaja tulemusega rahul - ta soovib tutvuda
võimalikult efektiivselt kõigi korterite hindadega eri paikades.
Muu
Andmete importimiseks kasutatakse KV veebilehte: https://www.kv.ee/
Tarkvaraarendajad projektis: Kermo Nurmeoja ja Kevin Sutt
    ''')
# erinevad tagid tekstist
text.tag_layer(['tokens', 'words', 'morph_analysis', 'sentences'])
# teksti osadega töötlemine
nertagger = NerTagger()
nertagger.tag(text)
# for tsükkel
namedentities = text.ner
for n in namedentities:
    if n.nertag == 'LOC':
        print(n.enclosing_text)

print("TEGUSÕNAD ja NIMISÕNAD")
# sõnade leidmine ja printimine
text.tag_layer(['morph_analysis_est'])
for w in text['morph_analysis_est']:
    if w.morph_analysis.partofspeech[0] == "V":
        print(w.lemma[0])
    elif w.morph_analysis.partofspeech[0] == "S":
        print(w.lemma[0])

