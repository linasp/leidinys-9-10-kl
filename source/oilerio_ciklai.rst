Oilerio ir Hamiltono ciklai
===========================

    *The whole branch of mathematics was born out of the game.* 

    Iš žaidimų kilo net atskira matematikos šaka.

    -- Nežinomas autorius apie grafų teorijos atsiradimą

Pažintį su grafais pradėjome nuo istorijos apie septynių Karaliaučiaus tiltų uždavinį. Šiame skyrelyje papasakosime, kaip tą uždavinį išsprendė Oileris, taip pat išspręsime jau ne kartą sutiktą Hamiltono ciklų uždavinį.
Tam prireiks keleto naujų grafų teorijos sąvokų, tad nuo jų ir pradėkime.

Kelios grafų teorijos sąvokos
-----------------------------

Briaunų, jungiančių viršūnę :math:`v` su kokia nors kita viršūne, skaičius vadinamas viršūnės :math:`v` **laipsniu**. Paprastuose grafuose viršūnės laipsnis yra jai gretimų viršūnių skaičius, tačiau multigrafuose (grafuose, kuriuose dvi viršūnes gali jungti daugiau nei viena briauna), šie du skaičiai gali skirtis.

Briauna, kurią pašalinus iš grafo padidėtų jungumo komponentų skaičius, vadinama **tiltu**. Kitaip tariant, jei norėtume iš kurios nors viršūnės pasiekti kitą, ir tam **būtinai** turėtume eiti briauna :math:`(u, v)`, ši briauna ir būtų tiltas.


Oilerio keliai ir ciklai
------------------------

Jau minėjome, kad Oileris neigiamai atsakė į Karaliaučiaus gyventojus dominantį klausimą: nėra maršruto, kuris prasidėtų viename iš krantų, pereitų kiekvienu iš septynių tiltų lygiai vieną kartą ir baigtųsi tame pačiame krante. Išnagrinėjęs tokių maršrutų galimybę, Oileris padėjo grafų teorijos pagrindus.

Jam pavyko išspręsti šį uždavinį: Oileris nustatė, kokios sąlygos yra būtinos ir pakankamos, kad grafe egzistuotų toks maršrutas, be to, pateikė algoritmą jam rasti. Maršrutai, prasidedantys ir užsibaigiantys toje pačioje viršūnėje bei apeinantys visas grafo briaunas po vieną kartą, nuo tada vadinami **Oilerio ciklais** arba (jei baigiasi kitoje viršūnėje negu prasideda) **Oilerio keliais**.

.. todo:: pataisyti nuorodą į paveikslą žemiau.

Nėra sudėtinga Karaliaučiaus tiltų atveju įrodyti, kad neegzistuoja Oilerio ciklas. Prisiminkime, kaip atrodė grafas, kurio viršūnės -- Karaliaučiaus salos ir krantai, o briaunos -- juos jungiantys tiltai (50 pav.).

Ieškome maršruto, kuris kiekviena briauna pereitų vieną kartą. Panagrinėjus kurią nors vieną viršūnę, nesunku pastebėti, jog ieškomas maršrutas neįmanomas, jei viršūnės laipsnis nelyginis: juk išeiti iš šios viršūnės turėsime lygiai tiek kartų, kiek ir atėjome, ir kiekvienąkart vis kita briauna, taigi visas briaunų skaičius turi būti dviejų kartotinis, lyginis. Tačiau šiame grafe visų viršūnių laipsniai nelyginiai (3, 3, 3 ir 5), taigi ir toks maršrutas tikrai neįmanomas.

Įrodėme, kad toks maršrutas negalimas, jei bent vienos viršūnės laipsnis nelyginis. Oileris įrodė griežtesnį teiginį: *Oilerio ciklas egzistuoja tada ir tik tada, kai visų viršūnių laipsniai yra lyginiai*.

O kaip su Oilerio keliais? Jei maršrutas turi baigtis ne toje pačioje viršūnėje kur prasidėjo, tai minėta taisyklė turi galioti visoms viršūnėms, išskyrus pradinę ir galinę. *Oilerio kelias egzistuoja tada ir tik tada, kai lygiai dviejų viršūnių laipsniai yra nelyginiai*.

Be abejo, grafai, turintys Oilerio ciklą arba kelią, turi pasižymėti dar viena natūralia savybe -- jie turi būti jungūs [#jungus_pastaba]_.


Flerio algoritmas
-----------------

Žinome, kas yra Oilerio kelias ir ciklas, ir netgi mokame duotame grafe nustatyti, ar toks egzistuoja. Tačiau kaip ieškoti Oilerio kelio? Pasirodo, tai labai paprasta. Flerio algoritmas, skirtas Oilerio ciklų ir kelių paieškai, gali būti nusakytas trimis žodžiais: *venk eiti tiltu*.

Flerio algoritmą, ieškantį Oilerio ciklo, galime išskaidyti į tokius žingsnius:

#. pradedame bet kurioje viršūnėje,
#. jei įmanoma, einame briauna, kuri nėra tiltas (jei tokios briaunos nėra, tai einame tiltu),
#. briauną, kuria jau ėjome, pašaliname iš grafo,
#. kartojame nuo antro žingsnio, o jei nėra kur eiti, baigiame.

.. todo:: iliustracija

Oilerio kelio paieška skiriasi tik pradinės viršūnės pasirinkimu: pradedame viršūnėje su nelyginiu laipsniu.

Flerio algoritmą Oilerio ciklo arba kelio paieškai multigrafe (t. y. grafe, kuriame dvi viršūnes gali jungti daugiau negu viena briauna) užrašysime programavimo kalba. Multigrafą vaizduosime kaimynystės matrica -- kiekvienai porai viršūnių įsiminsime, kelios briaunos jas jungia:

.. code-block:: pascal

    type grafas = record
            n : integer;
            briaunu_sk : array [1..MAXN,
                                1..MAXN] of integer;
            laipsnis : array [1..MAXN] of integer;
         end;

Tarsime, kad masyvas ``laipsnis`` užpildomas sudarant grafą.

Prieš pradedant ieškoti svarbu įsitikinti, ar tenkinamos būtinos ir pakankamos sąlygos. Paprastumo dėlei tarsime, kad grafas jungus, arba jį sudaro tik vienas nevienetinio dydžio jungumo komponentas. Šias sąlygas nesunku patikrinti pasinaudojus paieška gilyn, kaip tai darėme skyrelyje :ref:`jungumo-tikrinimas`.

Viršūnių laipsnių ribojimą patikrinti dar paprasčiau: tereikia suskaičiuoti, kiek viršūnių grafe turi nelyginius laipsnius. Jei tokios bus dvi, tai ieškosime Oilerio kelio ir turėsime pradėti vienoje iš nelyginio laipsnio viršūnių, priešingu atveju galėsime pradėti bet kurioje viršūnėje.

Patikrinus, ar tenkinamos abi sąlygos, galima pradėti vykdyti Flerio algoritmą: įsiminti pradinę viršūnę, pasirinkti tolesnę ir briauną, kuria jau ėjome, išbraukti iš grafo. Tolesnę lankomą viršūnę renkamės pagal minėtą sąlygą -- stengiamės neiti tiltu, jei tik įmanoma.

.. code-block:: pascal

    const MAXB = ...; { maksimalus briaunų skaičius }
    type  masyvas = array [1..MAXB+1] of integer;

    procedure Flerio(var g : grafas;
                     var kelio_ilgis : integer;
                     var kelias : masyvas);
    { jei Oilerio ciklas/kelias grafe neegzistuoja, tai „kelio_ilgis“ reikšmė lygi
       nuliui, kitu atveju Oilerio ciklas/kelias įrašomas į masyvą „kelias“ }
    var k, p, v, u, nelyg : integer;
    begin
        nelyg := 0;
        { suskaičiuojama, kiek yra nelyginio laipsnio
        viršūnių, ir parenkama pradinė (v) }
        v := 1;
        for k := 1 to g.n do
            if odd(g.laipsnis[k]) then begin
                nelyg := nelyg + 1;
                { jei randama bent viena nelyginio laipsnio viršūnė,
                  tai v priskiriamas jos numeris }
                v := k;
            end;
        kelio_ilgis := 0;

        if ((nelyg = 0) or (nelyg = 2))
        { jei tenkinamos būtinos Oilerio ciklo/kelio egzistavimo sąlygos }
        then begin { vykdomas Flerio algoritmas }
            while v > 0 do begin
                inc(kelio_ilgis);
                kelias[kelio_ilgis] := v;
                p := v; { paskutinė pereita viršūnė }
                v := 0;
                { pagal Flerio algoritmą pasirenkama sekanti viršūnė }
                for u := 1 to g.n do
                    if (g.briaunu_sk[p, u] > 0) and
                    ((v = 0) or not tiltas(g, p, u))
                    then
                        v := u;
                if v > 0 then begin { ištrinama briauna }
                    dec(g.briaunu_sk[p, v]);
                    dec(g.briaunu_sk[v, p]);
                end;
            end;
        end;
    end;

Liko nerealizuota funkcija ``tiltas``. Ji turėtų grąžinti reikšmę ``true``, jei grafe :math:`g` briauna :math:`(u, v)` yra tiltas. Tai patikrinti nesunku: jei :math:`(u, v)` yra tiltas, tai pašalinus šią briauną viršūnės :math:`u` ir :math:`v` atsidurs skirtinguose jungumo komponentuose. Taigi pašalinkime šią briauną, paieška gilyn patikrinkime, ar v pasiekiama iš :math:`u`, ir sugrąžinę pašalintą briauną pateikime rezultatą.

.. code-block:: pascal

    function tiltas(var g : grafas;
                    u, v : integer) : boolean;
    var k : integer;
    begin
        if g.briaunu_sk[u, v] > 1 then
            tiltas := false
        else begin
            for k := 1 to g.n do
                spalva[k] := balta;

            g.briaunu_sk[u, v] := 0; { pašalinama briauna }
            g.briaunu_sk[v, u] := 0;
            ieskok_gilyn(g, u);
            g.briaunu_sk[u, v] := 1; { atstatoma briauna }
            g.briaunu_sk[v, u] := 1;

            tiltas := spalva[v] = balta;
        end;
    end;

Atkreipiame dėmesį, kad procedūra ``ieskok_gilyn`` buvo pateikta skyrelyje :ref:`paieska-gilyn`, tačiau kitaip pavaizduotam grafui, taigi prieš taikant ją būtina modifikuoti.


Uždavinys *Domino kauliukai* 
----------------------------

Pritaikykime Flerio algoritmą spręsdami uždavinį *Domino kauliukai* [#uzd_domino_kauliukai]_:

    Yra krūvelė domino kauliukų. Kiekvienas domino kauliukas perskirtas pusiau, kiekvienoje pusėje užrašytas skaičius nuo 0 iki 6. Du kauliukus galima sujungti, jei sutampa skaičiai, užrašyti ant sujungiamų kauliukų pusių.

    **Užduotis.** Reikia nustatyti, ar krūvelėje esančius kauliukus galima sudėlioti į nenutrūkstamą liniją.

Uždavinį modeliuosime grafais. Grafas turės septynias viršūnes, sunumeruotas nuo 0 iki 6 (mat nuo 0 iki 6 taškų gali būti ant domino kauliuko puselės). Kauliukus atitiks grafo briaunos.

.. todo:: Įkelti iliustraciją.

52 pav. Kauliukų rinkinys ir juos atitinkantis grafas; grafe Oilerio kelias yra toks: 6--4--2--1--3--6--2, tad kauliukus galima sudėlioti į vieną eilę: [6,4] [4,2] [2,1] [1,3] [3,6] [6,2] [2,4]

Kauliukų dėliojimas į liniją atitinka kelią, kai visomis grafo briaunomis apeinama po vieną kartą, t. y. Oilerio kelią. Norint išspręsti šį uždavinį tereikia patikrinti, ar grafe egzistuoja Oilerio kelias.


Hamiltono keliai ir ciklai
--------------------------

    *O brooding Spirit of Wisdom and of Love,
    Whose mighty wings even now o'ershadow me,
    Absorb me in thine own immensity,
    And raise me far my finite self above!*

    Mąslioji išminties ir meilės siela,
    kurios eiklių sparnų šešėlyje slepiuos,
    leisk prisiliesti prie gelmės tavos
    ir peržengt savo ribotumo sieną! [#eiliu_vertimas]_

    -- Seras Viljamas Rovanas Hamiltonas (*Sir William Rowan Hamilton*)

.. todo:: Sutvarkyti eilutes.

Ieškodami visų Hamiltono kelių grafe, kurio viršūnės sunumeruotos nuo :math:`1` iki :math:`n`, galėtume generuoti visus skaičių nuo :math:`1` iki :math:`n` kėlinius (t. y. visas galimas viršūnių apėjimo tvarkas) :math:`k_1, k_2, \ldots, k_n`, o sugeneravę patikrinti, ar egzistuoja visos briaunos :math:`(k_i, k_{i + 1}), (i = 1, 2, \ldots, n - 1)`.

Tačiau retuose (t. y. tokiuose, kurie turi nedaug briaunų) grafuose Hamiltono kelių galima ieškoti kur kas efektyviau. Viršūnių seką galima iškart sudaryti taip, kad gretimas sekos viršūnes jungtų briauna. Naudodami grįžimo metodą parašysime procedūrą, spausdinančią visus konkrečioje viršūnėje :math:`v` prasidedančius Hamiltono kelius. Grafą vaizduosime kaimynystės sąrašais.

.. code-block:: pascal

    const MAXN = ...;
    var seka : array [1..MAXN] of integer;
        aplankyta : array [1..MAXN] of boolean;

    procedure ieskok(var g : grafas;
                    k,      	{ kiek viršūnių apeita }
                    v : integer { kurioje viršūnėje sustota } );
    var i, u : integer;
    begin
        seka[k] := v;
        {aplankytomis žymimos konstruojamame kelyje esančios viršūnės}
        aplankyta[v] := true;
        if (k = g.n) then
            { jei apeitos visos viršūnės – tai rastas Hamiltono kelias}
            spausdink(g.n)
        else
            { bandoma toliau eiti į visas neaplankytas v kaimynes }
            for i := 1 to g.vir[v].k do begin
                u := g.vir[v].ksarasas[i];
                if (not aplankyta[u]) then
                    ieskok(g, k + 1, u);
            end;
        { pabaigus, v pažymima kaip neaplankyta }
        aplankyta[v] := false;
    end;

Procedūra ``spausdink`` išveda masyvo elementus nuo :math:`1` iki :math:`m`; ji analogiška procedūrai, pateiktai skyrelyje :ref:`keliniu-generavimas`.

Norint rasti Hamiltono kelius, prasidedančius visose viršūnėse, reikia įvykdyti:

.. code-block:: pascal

    for v := 1 to g.n do
        ieskok(g, 1, v);

Jei ieškotume ne kelių, o ciklų, tuomet sugeneravus visą seką reiktų papildomai patikrinti, ar egzistuoja briauna, jungianti pirmą ir paskutinę kelyje esančias viršūnes.


.. rubric:: Išnašos

.. [#jungus_pastaba] Išimtis, jei grafe yra izoliuotų (t.y. iš kurių neišeina nė viena briauna) viršūnių; tokiu atveju Oilerio ciklas gali egzistuoti, nors grafas ir nejungus.

.. [#uzd_domino_kauliukai] Šis uždavinys buvo pateiktas Lietuvos informatikos olimpiados III etape 1995 metais.

.. [#eiliu_vertimas] Eiles vertė Gediminas Pulokas.

