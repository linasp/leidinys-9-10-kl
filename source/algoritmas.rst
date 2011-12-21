Intuityvios algoritmo ir algoritmo sudėtingumo sąvokos
======================================================

.. todo::

     Sutvarkyti, kad ši citata būtų normaliai vaizduojama.

..

    Languages come and go, but algorithms stand the test of time.

    Programavimo kalbos atsiranda ir išnyksta, bet algoritmai išlieka ilgam.

    -- Donaldas Knutas (Donald Knuth)

Algoritmas
----------

Algoritmo sąvoka atsirado daugiau kaip prieš tūkstantį metų,
o pats žodis kilo iš IX a. persų matematiko Mohamedo ibn Musos al Chorezmio (*Al-Khwarizmi*) vardo.
Algoritmu sutarta vadinti seką elementarių veiksmų, pradinius duomenis paverčiančių rezultatais.
Algoritmas yra teisingas, jei su visais pradiniais duomenimis baigia darbą ir gaunami teisingi rezultatai.

.. todo::

    Žemiau sutvarkyti nuorodą į knygą.

Koks algoritmas yra geras?
Į šį klausimą puikiai atsakyta jau klasika tapusioje knygoje „Įvadas į algoritmus“ [2]:

    Geras algoritmas -- kaip aštrus peilis -- atlieka tiksliai tai, ką turi atlikti,
    su minimaliomis pastangomis.
    Netinkamo algoritmo naudojimas problemai spręsti primena bandymą perpjauti kepsnį
    atsuktuvu: anksčiau ar vėliau gali pavykti pasiekti patenkinamą rezultatą, tačiau
    teks išnaudoti daug daugiau pastangų negu būtina, ir pats rezultatas nekels
    estetinio pasigėrėjimo.

Geras algoritmas turi būti teisingas ir efektyvus laiko ir atminties požiūriu.
Jis taip pat turi būti lengvai realizuojamas, t. y. užrašomas realia programavimo kalba.
Dažniausiai visų tikslų pasiekti nepavyksta ir tenka nusileisti iki kompromiso.
Mokslininkai teoretikai linkę skirti dėmesį teisingumui ir efektyvumui, nes jie retai
patys programuoja savo algoritmus.
Tuo tarpu industrija renkasi vadinamąjį *greitą ir purviną* (angl. *Quick and Dirty*)
darbo principą: bet kokia programa, kuri pateikia priimtinus rezultatus ir pernelyg
nesulėtina darbo, yra tinkama, nepaisant to, kad gali būti ir geresnis algoritmas.

Atskirai paminėsime euristinius algoritmus.
Ne visiems uždaviniams spręsti sugalvoti efektyvūs algoritmai, o teisingi,
bet neefektyvūs algoritmai praktiškai nepritaikomi, nes jų vykdymas užtruktų per ilgai,
pavyzdžiui, kelis šimtmečius. Jei uždavinį vis dėlto reikia spręsti, galvojami spartūs
algoritmai, kurie nebūtinai suranda tikslų sprendinį, tačiau rastasis sprendinys
*dažniausiai* yra *artimas* ieškomajam. Tokie optimizmu grįsti algoritmai vadinami
euristiniais algoritmais arba tiesiog euristikomis.

.. todo::

    Žemiau sutvarkyti nuorodą į knygą.

Iš tiesų skyrelio pradžioje pateiktas algoritmo apibrėžimas tėra intuityvi ir matematiškai
netiksli algoritmo sąvoka [1]. Tačiau mums jos pakaks.
