from rake_nltk import Metric, Rake

# To use it with a specific language supported by nltk.
r = Rake(language="icelandic")

# If you want to provide your own set of stop words and punctuations to
#r = Rake(
    #stopwords= ,
#    punctuations=[";", ",", ".", ":", "?", "„", "“"]
#)

# If you want to control the metric for ranking. Paper uses d(w)/f(w) as the
# metric. You can use this API with the following metrics:
# 1. d(w)/f(w) (Default metric) Ratio of degree of word to its frequency.
# 2. d(w) Degree of word only.
# 3. f(w) Frequency of word only.

r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
r = Rake(ranking_metric=Metric.WORD_DEGREE)
r = Rake(ranking_metric=Metric.WORD_FREQUENCY)

# If you want to control the max or min words in a phrase, for it to be
# considered for ranking you can initialize a Rake instance as below:

r = Rake(min_length=1, max_length=4)

# TODO: nota lemmaðan texta
text = "Heildargreiðslur taka til beingreiðslna, býlisstuðnings, gæðastýringargreiðslna samkvæmt gildandi reglugerð um gæðastýrða sauðfjárframleiðslu með síðari breytingum, greiðslna fyrir ullarnýtingu og greiðslna vegna svæðisbundins stuðnings. Heildargreiðslur ársins verður deilt í 12 jafna hluta. Tvöföld greiðsla skal greidd í febrúar, mars og apríl en fellur þó niður á móti í janúar, nóvember og desember. Matvælastofnun er heimilt að halda eftir 7% af framlögum vegna gæðastýringar og ullarnýtingar og 2% vegna beingreiðslna, svæðisbundins stuðnings og býlisstuðnings við gerð ársáætlunar sem verða greidd þegar heildarframleiðsla liggur fyrir. Ef fjárveiting yfirstandandi fjárlagaárs nægir ekki fyrir uppgjöri stuðningsgreiðslna er Matvælastofnun heimilt að draga mismuninn frá fjárveitingu næsta fjárlagaárs. Heildargreiðslur til nýliða skal áætla út frá ærgildum og fjölda vetrarfóðraðra kinda samkvæmt haustskýrslu í Bústofni. Miða skal við að hver vetrarfóðruð ær tveggja vetra og eldri skili 20 kg af lambakjöti og hver veturgömul ær 10 kg. Jafnframt skal miða við að sérhver vetrarfóðruð kind skili 1,6 kg af hreinni ull. Skiptingu framleiðslu í flokka skal miða við framleiðslu á landsvísu árið á undan. Ef nýliði tekur við búi í fullum rekstri er Matvælastofnun heimilt að áætla greiðslur miðað við síðasta framleiðsluár fyrri eiganda. Ársáætlun um heildargreiðslur skal kynnt framleiðanda eigi síðar en 15. febrúar ár hvert. Athuga­semdir við áætlunina skulu berast stofnuninni innan 20 daga frá dagsetningu þeirra. Matvæla­stofnun skal svara öllum athugasemdum eigi síðar en 15. apríl ár hvert. Matvælastofnun er heimilt að leiðrétta áætlun um heildargreiðslur til framleiðenda ef forsendur greiðslna breytast. Stuðningsgreiðslur eru inntar af hendi með fyrirvara um að framleiðandi fullnægi skilyrðum um stuðningsgreiðslur samkvæmt reglugerð þessari. Uppgjör á heildargreiðslur fyrra árs skal fara fram í febrúar árið eftir. Þá verða greiðslur til fram­leiðenda leiðréttar í samræmi við raunverulega framleiðslu ársins og vegna annarra breytinga á for­sendum heildargreiðslur, svo sem ef þeir standast ekki skilyrði fyrir álagsgreiðslu í gæðastýrðri sauð­fjár­framleiðslu. Ef bú uppfyllir ekki skilyrði fyrir stuðningsgreiðslum samkvæmt reglugerð þessari er Matvæla­stofnun heimilt að endurkrefja nýjan framleiðanda um allar ofgreiddar stuðningsgreiðslur fyrir búið ef skipt hefur verið um handhafa á árinu. Ef handhafaskipti eru ekki tilkynnt til Matvælastofnunar með réttum hætti áður en lokauppgjör fer fram þá ber Matvælastofnun ekki að endurkrefja fyrri handhafa um ofgreiddar stuðningsgreiðslur fyrir búið. Matvælastofnun er heimilt að skuldajafna endurgreiðslukröfu vegna greiðslna af öðrum stuðn­ings­greiðslum skv. samningi um starfsskilyrði í sauðfjárrækt."

r.extract_keywords_from_text(text)
print(r.get_ranked_phrases_with_scores())