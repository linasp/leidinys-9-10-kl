Perrinkimas ir grįžimo metodas
==============================

    *Modern computers are so fast that brute force can be an effective and honourable way to solve problems.*

    Šiuolaikiniai kompiuteriai yra tokie spartūs, kad perrinkimas gali būti efektyvus ir garbingas būdas uždaviniams spręsti.

    -- Steven S. Skienna, Miguel A. Revilla, „Programming Challenges“

1852 metais matematikas F. Gatris (*Francis Guthrie*) paskelbė hipotezę, teigiančią, jog kiekvienam žemėlapiui nuspalvinti taip, kad jokios dvi gretimos valstybės nebūtų nuspalvintos ta pačia spalva, pakanka keturių spalvų. Daugelis matematikų siūlė šios hipotezės įrodymus, tačiau vis išaiškėdavo, kad jie neteisingi. Keletas tokių įrodymų buvo paneigti praėjus tik 11 metų po jų paskelbimo. Hipotezė pagaliau tapo teorema (buvo įrodyta) 1976 metais, o dalis įrodymo rėmėsi kompiuteriu išnagrinėtomis 1476 situacijomis. Kompiuterio programa veikė šimtus valandų, o žmonėms nepakako ir šimto metų. Taigi nors perrinkimo metodai dažnai būna neefektyvūs, spartėjant kompiuteriams šis sprendimo būdas (visų galimų sprendinių išbandymas) tam tikrais atvejais gali būti priimtinas, ypač jei perrinkimą pavyksta optimizuoti.

Formaliai **perrinkimą** galima apibrėžti kaip uždavinių sprendimo metodą, kai išbandomi visi galimi sprendiniai.

Šiame skyrelyje susipažinsime su patogiu metodu perrinkimui realizuoti -- grįžimo metodu. **Grįžimo metodas** (angl. *Backtracking*) -- tai sistemingas būdas spręsti uždaviniams, kurių sprendinys yra kintamųjų :math:`p_1, p_2, \ldots, p_n` reikšmių rinkinys, tenkinantis kokius nors reikalavimus. Prisiminkime, pavyzdžiui, :ref:`Keliaujančio pirklio uždavinį <keliaujancio-pirklio-uzdavinys>`: šiuo atveju kintamųjų :math:`p_1, p_2, \ldots, p_n` reikšmėms reikia priskirti skirtingus miestų numerius taip, kad ši miestų aplankymo tvarka ir būtų pageidaujamas maršrutas.

Pagrindinė grįžimo metodo idėja tokia: paeiliui renkamos visų galimų kintamųjų reikšmės ir tikrinama, ar tenkinami reikalavimai, o radus sprendinį arba situaciją, kai reikalavimai netenkinami, grįžtama per vieną žingsnį atgal ir parenkama nauja atitinkamo kintamojo reikšmė.

Programuojant grįžimo metodą dažnai naudojama rekursija. Panagrinėsime abstrakčių kombinatorinių uždavinių sprendimų schemas bei porą konkrečių uždavinių.


.. _keliniu-generavimas:

Kėlinių generavimas
-------------------

Sakykime, parduotuvės lentynoje vienoje eilėje reikia išdėlioti :math:`n` skirtingų prekių. Raskime visus skirtingus būdus, kaip tai padaryti. Uždavinys yra ekvivalentus visų :math:`n` ilgio kėlinių be pasikartojimų generavimo uždaviniui.

Kas gi tas kėlinys be pasikartojimų? Tarkime, turime aibę iš :math:`n` elementų. Kiekviena visų (skirtingų) :math:`n` elementų seka vadinama **kėliniu be pasikartojimų**. Taigi kėliniai vienas nuo kito skiriasi tik elementų išsidėstymu vienas kito atžvilgiu.

Parašykime algoritmą, kuris išspausdintų visus prekių išdėstymo būdus. Prekes laikysime sunumeruotomis nuo 1 iki :math:`n`.

Atkreipkite dėmesį -- šis uždavinys priskiriamas įžangoje minėtai uždavinių klasei: :math:`m`-ojoje vietoje padėtą prekę (prekės numerį) pažymėjus :math:`p_m`, reikia rasti kintamųjų :math:`p_1, \ldots, p_n` reikšmių (kintančių nuo 1 iki :math:`n`) rinkinius, tenkinančius vieną reikalavimą -- visos reikšmės turi būti skirtingos; tuos rinkinius atspausdinti.

Uždavinį galima išreikšti rekursyviai, t. y. suskaidyti į tokius pat, tik mažesnius, uždavinius. Tegu procedūra ``generuok(m, n)`` priskirs reikšmes kintamiesiems nuo :math:`p_m`-ojo iki :math:`p_n`-ojo. Tuomet jos veikimas galėtų būti toks:

* Jei :math:`m \le n`, imti po vieną visas dar lentynoje nepadėtas prekes ir su kiekviena atlikti tokius veiksmus:

    * Prekę padėti į :math:`m`-ąją poziciją lentynoje (:math:`p_m \gets \text{prekės numeris}`).
    * Sudėti į lentyną likusias prekes (priskirti reikšmes kintamiesiems nuo :math:`p_{m+1}` iki :math:`p_n`) -- toks pat uždavinys, taigi iškviesti ``generuok(m + 1)``.
    * Prekę, esančią :math:`m`-ojoje pozicijoje, paimti nuo lentynos.

* Jei :math:`m > n`, tai ši procedūra iškviesta jau išdėliojus visas prekes lentynoje, todėl atspausdiname kintamųjų :math:`p_1, p_2, \ldots, p_n` reikšmes.

Norint patikrinti, kurios prekės jau sudėtos į lentyną, galima peržiūrėti jau priskirtas reikšmes. Tačiau paprasčiau ir efektyviau paskirti globalų loginį masyvą panaudotas, ir, padėjus į lentyną prekę su numeriu :math:`i`, pažymėti, jog šis numeris jau panaudotas (``panaudotas[i] := true``), o paėmus prekę nuo lentynos -- atstatyti buvusią reikšmę (``panaudotas[i] := false``).

.. code-block:: c++

    const int MAXN = 20; // didžiausia n reikšmė

    int p[MAXN];
    bool panaudotas[MAXN + 1];

    void spausdink(int n)
    {
        for (int i = 0; i < n; i++)
            cout << p[i] << " ";
        cout << endl;
    }

    void generuok(int m, // parenkamas elementas m-ajai pozicijai
                  int n)
    {
        // jei m >= n, tai ši procedūra iškviesta jau sugeneravus visą kėlinį
        if (m >= n) {
            spausdink(n);
            return;
        }

        for (int i = 1; i <= n; i++)
            if (!panaudotas[i]) {
                panaudotas[i] = true;
                p[m] = i;
                generuok(m + 1, n);
                panaudotas[i] = false;
            }
    }

Kad galėtume išspausdinti visas trijų prekių išdėliojimo lentynoje tvarkas, įvykdome:

.. code-block:: c++

    n = 3;
    for (int i = 1; i <= n; i++)
        panaudotas[i] = false;
    generuok(0, n);

Parašytą procedūrą nesunku pritaikyti kitiems uždaviniams -- vietoj spausdinimo galima atlikti kokius nors kitus veiksmus. Spausdinimą iškėlėme į atskirą procedūrą norėdami paryškinti sprendimo struktūrą.

Koks gi parašytos programos sudėtingumas, t. y. kaip atliekamų veiksmų skaičius priklauso nuo :math:`n`? Algoritmas generuoja visus įmanomus skaičių nuo :math:`1` iki :math:`n` išdėstymo į eilę būdus. Kiek jų yra? Pirmąjį skaičių galima parinkti :math:`n` būdų, antrąjį skaičių -- :math:`(n - 1)` būdu (kadangi vienas skaičius jau pasirinktas), trečiąjį skaičių -- :math:`(n - 2)` būdais (du skaičiai jau parinkti) ir t. t. Gauname, kad yra :math:`n \cdot (n - 1) \cdot (n - 2) \cdot \ldots \cdot 2 \cdot 1 = n!` skirtingų būdų išdėstyti :math:`n` skaičių į eilę. Taigi procedūros generuok sudėtingumas yra :math:`O(n!)`. Pavyzdžiui, kai :math:`n = 13`, tai vieną atspausdintą eilutę sudaro apie :math:`30` simbolių, o eilučių yra :math:`13! = 6227020800` ir programa spausdintų daugiau nei 150 gigabaitų teksto... (jei, žinoma, sulauktume veikimo pabaigos).


Aštuonių valdovių uždavinys
---------------------------

Išspręsime klasikinį aštuonių valdovių uždavinį.

.. _astuoniu-valdoviu-uzdavinys:

    **Užduotis.** :math:`8 \times 8` dydžio šachmatų lentoje reikia išdėlioti :math:`8` valdoves taip, kad jokiu būdu neatsidurtų dvi vienoje eilutėje, stulpelyje arba įstrižainėje (t. y. nė viena negalėtų nukirsti kitos tolesniu ėjimu). Uždavinio formuluotę išplėsime ir ieškosime, kaip :math:`n` valdovių surikiuoti :math:`n \times n` dydžio lentoje.

Šį uždavinį taip pat spręsime grįžimo metodu. Pavyzdžiui, lentos langelius sunumeravę nuo :math:`1` iki :math:`n^2`, kiekvienai valdovei galime skirti po vieną langelį (numerį) taip, kad būtų tenkinama uždavinio sąlyga. Tačiau spręsdami uždavinį šiuo būdu, turėtume išnagrinėti labai didelį variantų skaičių. Variantų skaičius, kuriuo aštuonioms valdovėms galima paskirstyti langelių numerius nuo :math:`1` iki :math:`64` yra :math:`64 \cdot 63 \cdot 62 \cdot 61 \cdot 60 \cdot 59 \cdot 58 \cdot 57 = 178\ 462\ 987\ 637\ 760` būdų.

Be abejo, didžioji dalis šių variantų visiškai neįdomūs, nes labai tikėtina, kad kurios nors dvi valdovės atsidurs toje pačioje eilutėje, stulpelyje arba įstrižainėje. Atkreipkime dėmesį -- kiekviename stulpelyje turės atsidurti lygiai viena valdovė; stulpelių yra tiek, kiek ir valdovių, o viename stulpelyje dvi valdovės stovėti negali.

Taigi galima šiek tiek kitaip vykdyti perrinkimą. Tegu :math:`p_k` yra valdovės, stovinčios :math:`k`-ajame stulpelyje, eilutės numeris. Kintamiesiems :math:`p_1, p_2, \ldots, p_n` reikia priskirti reikšmes nuo :math:`1` iki :math:`n` taip, kad jokios dvi valdovės neatsidurtų vienoje eilutėje arba įstrižainėje.

Šitaip atliekant perrinkimą, net nepaisant įstrižainių apribojimo, nagrinėjamų variantų bus tik :math:`n!`. Palyginkite -- aštuonių valdovių atveju teks išnagrinėti :math:`8! = 40\ 320` variantų vietoj :math:`178\ 462\ 987\ 637\ 760`.

Perrenkant valdovių rikiavimo būdus, visai nesudėtinga sekti, kuriose eilutėse valdovės jau pastatytos -- tam galima skirti loginį masyvą.

Tačiau kaip elgtis su įstrižainėmis? Patikrinti, ar dvi valdovės nestovi vienoje įstrižainėje, galima sustačius visas valdoves. Tačiau išsisuksime paprasčiau (ir efektyviau) pastebėję, kad įstrižaines taip pat nesunku sunumeruoti: vienoje įstrižainėje esančių langelių eilutės ir stulpelio numerių suma arba skirtumas yra pastovus.

Taigi žinodami langelio koordinates (stulpelio ir eilutės numerius), galime pasakyti, kuriai įstrižainei priklauso šis langelis. Įstrižainėms skiriame du loginius masyvus su indeksais atitinkamai :math:`[2 \ldots 2n]` ir :math:`[–n + 1 \ldots n – 1]`, kuriuose žymėsime, ar įstrižainės jau užimtos.

.. todo:: Lentos lentelė/iliustracija.

    Kairėje pavaizduotos įstrižainės numeruojamos eilutės ir stulpelio numerių suma, dešinėje -- skirtumu

Parašysime procedūrą ``statyk(k, n)``, perrenkančią sprendinius grįžimo metodu, kuri visais įmanomais būdais sudėlios lentoje valdoves nuo :math:`k`-osios iki :math:`n`-osios. :math:`k`-oji valdovė bus statoma :math:`k`-ajame stulpelyje. Taigi procedūra turi bandyti pastatyti :math:`k`-ąją valdovę nepažeisdama apribojimų, o pastačius -- pažymėti užimtas eilutę ir įstrižaines, ir iškviesti ``statyk(k + 1, n)``.

Jei iškvietus procedūrą parametro :math:`k` reikšmė viršija :math:`n` (:math:`k > n`), tai reiškia, kad ši procedūra buvo iškviesta sudėliojus visas :math:`n` valdovių, taigi radus sprendinį. Viena vertus, sudėliojus visas :math:`n` valdovių, procedūros statyk būtų galima nebekviesti, tačiau dėl šio papildomo iškvietimo programa tampa paprastesnė ir aiškesnė. Tai dažnai naudojama rekursyviose procedūrose.

Procedūroje skaičiuosime, kiek yra sprendinių, t. y. būdų išdėlioti valdoves lentoje. Tačiau nesunku modifikuoti procedūrą taip, kad ši rastus sprendinius išspausdintų -- tuomet dar reikėtų saugoti, kur lentoje statomos valdovės.

.. code-block:: pascal

    const MAXN = 12;

    var eilute : array [1..MAXN] of boolean;
        istr1 : array [2..2 * MAXN] of boolean;
        istr2 : array [-MAXN + 1..MAXN - 1] of boolean;
        sprendiniu_sk : longint;

    procedure statyk(k, { valdovė statoma k-ajame stulpelyje }
                    n : integer { reikia pastatyti n valdovių });
    var i : integer;
    begin
        if k > n then { rastas sprendinys }
            sprendiniu_sk := sprendiniu_sk + 1
        else
            for i := 1 to n do
                if not (eilute[i] or
                        istr1[i + k] or
                      istr2[i - k])
                then begin
                    eilute[i] := true;
                    istr1[i + k] := true;
                    istr2[i - k] := true;
                    { bandoma pastatyti likusias valdoves }
                    statyk(k + 1, n);
                    eilute[i] := false;
                    istr1[i + k] := false;
                    istr2[i - k] := false;
                end;
    end;

..

    Valdovių uždavinio rekursijos medis, kai :math:`n = 4`.


Gretiniai, deriniai ir poaibiai
-------------------------------

Skyriuje :ref:`keliniu-generavimas` nagrinėjome, kiek ir kokių kombinacijų galima sudaryti iš įvairių objektų, kad būtų tenkinamos vienokios ar kitokios sąlygos. Šitai nagrinėja matematikos šaka, vadinama *kombinatorika*, kuri atsirado XVI amžiuje išpopuliarėjus azartiniams žaidimams. Pirmieji kombinatorikos uždaviniai ir buvo susiję su šiais žaidimais, pavyzdžiui, buvo tiriama, keliais būdais galima išmesti kokį nors taškų skaičių, žaidžiant dviem arba trimis kauliukais.

Kombinatorikos žinių prireikia sprendžiant įvairius olimpiadinius uždavinius. Šiame skyrelyje glaustai išdėstysime, kaip generuoti kitus junginius rekursiniais algoritmais [#pastaba_rekursijai]_.


Gretiniai
^^^^^^^^^

Grįžkime prie pavyzdžio su parduotuve. Sakykime, turime :math:`n` skirtingų prekių, kurias reikia išdėlioti lentynoje; deja, lentynoje telpa tik :math:`k` prekių ir visų prekių iš karto parodyti pirkėjams nepavyks. Reikia rasti visus būdus, kuriais galima išdėlioti prekes lentynoje. Tuščių vietų likti lentynoje negali.

Kitaip sakant, reikia rasti visus **gretinius be pasikartojimų** iš :math:`n` elementų po :math:`k`. Uždavinys labai panašus į jau nagrinėtą kėlinių be pasikartojimų generavimo uždavinį, tiesiog iš :math:`n` elementų renkame tik :math:`k (k \le n)`.

.. code-block:: c++

    const int MAX = 20; // didžiausia n ir k reikšmė

    int p[MAX];
    bool panaudotas[MAX + 1];


    void generuok(int m, // parenkamas elementas m-ajai pozicijai
                  int n, int k)
    {
        // jei m >= k, tai ši procedūra iškviesta jau sugeneravus
        // visą gretinį
        if (m >= k) {
            spausdink(k);
            return;
        }

        for (int i = 1; i <= n; i++)
            if (!panaudotas[i]) {
                panaudotas[i] = true;
                p[m] = i;
                generuok(m + 1, n, k);
                panaudotas[i] = false;
            }
    }

Norėdami gauti visus gretinius iš :math:`5` po :math:`3`, į procedūrą kreipiamės:

.. code-block:: c++

    n = 5;
    k = 3;
    for (int i = 1; i <= n; i++)
        panaudotas[i] = false;
    generuok(0, n, k);

Suskaičiuosime, kiek gali būti skirtingų gretinių be pasikartojimų, tuo pačiu įvertinsime ir algoritmo sudėtingumą. Pirmąją prekę galime rinktis iš visų :math:`n` prekių, antrąją prekę -- iš :math:`(n - 1)` prekės ir t. t. :math:`k`-ąją prekę galime rinktis iš :math:`(n - k + 1)` prekių. Gretinių be pasikartojimų iš :math:`n` elementų po :math:`k` skaičius žymimas :math:`A_n^k` ir lygus:

.. math::

    A_n^k = n \cdot (n - 1) \cdot (n – 2) \cdot ... \cdot (n - k + 1) = \frac{n!}{(n - k)!}


Deriniai
^^^^^^^^

Generuodami gretinius atsižvelgėme į prekių išdėstymą lentynose. Pamėginkime rasti visus būdus, kuriais galima išdėstyti :math:`n` skirtingų prekių lentynoje, kurioje telpa tik :math:`k` prekių (lentynoje neturi likti tuščių vietų) nekreipiant dėmesio į prekių išdėstymą, t. y. kai rūpi tik tai, kokios prekės yra lentynoje, tačiau nesvarbu, kokia tvarka jos ten išdėliotos. Kitaip sakant, reikia sugeneruoti visus **derinius be pasikartojimų** iš :math:`n` elementų po :math:`k`.

Derinius galima generuoti kaip gretinius, laikantis vienos papildomos taisyklės: prekės dėliojamos taip, kad jų numeriai sudarytų didėjančią seką, t. y. :math:`p_1 < p_2 < p_3 < \ldots < p_k`. Derinius generuojančiai rekursinei procedūrai prireiks vieno papildomo parametro, kuris rodytų, nuo kurio elemento galime rinkti tolesnius elementus.

    Keletas derinių iš penkių prekių po tris (tvarka deriniuose nesvarbi)

.. code-block:: c++

    const int MAX = 20; // didžiausia n ir k reikšmė

    int p[MAX];
    bool panaudotas[MAX + 1];

    void generuok(int m, int n, int k, int s)
    {
        // jei m >= k, tai ši procedūra iškviesta jau sugeneravus visą derinį
        if (m >= k) {
            spausdink(k);
            return;
        }
        // bus renkamasi tik iš elementų, didesnių arba lygių „s“
        // parenkamas elementas m-ajai pozicijai
        for (int i = s; i <= n; i++)
            if (!panaudotas[i]) {
                panaudotas[i] = true;
                p[m] = i;
                generuok(m + 1, n, k, i + 1);
                panaudotas[i] = false;
            }
    }

Norėdami gauti visus skirtingus derinius iš :math:`5` elementų po :math:`3`, į procedūrą kreipiamės:

.. code-block:: c++

    n = 5;
    k = 3;
    for (int i = 1; i <= n; i++)
        panaudotas[i] = false;
    generuok(0, n, k, 1);

Beliko apskaičiuoti, kiek gali būti skirtingų derinių be pasikartojimų iš :math:`n` po :math:`k`. Šį skaičių pažymėkime :math:`C_n^k`.

Sakykime, turime konkretų derinį. Jei paimtume visus jo perstatymus, gautume visus kėlinius be pasikartojimų iš tų :math:`k` derinį sudarančių elementų. Tokių kėlinių gali būti :math:`k!`.

O jei kartu paimtume visus kiekvieno galimo derinio perstatymus, gautume visus gretinius be pasikartojimų iš n elementų po :math:`k`. Žinome, kad jų gali būti :math:`A_n^k = \frac{n!}{(n - k)!}`. Gauname:

.. math::

    C_n^k = \frac{n!}{(n - k)! \cdot k!}

Pavyzdžiui, jei turime :math:`10` prekių, o lentynoje telpa :math:`7` prekės, tai nepaisydami prekių išdėstymo tvarkos šias prekes galime išdėlioti lentynoje :math:`\ldots` būdų.


Poaibiai
^^^^^^^^

Visus galimus :math:`n` elementų aibės poaibius galime gauti generuodami iš eilės :math:`0, 1, 2, \ldots, n` ilgio derinius be pasikartojimų. Galimas ir dar paprastesnis būdas: pakanka sugeneruoti visus įmanomus žodžius, kurių ilgis :math:`n` iš abėcėlės :math:`\{\text{true}, \text{false}\}`.

    21 pav. Abėcėlės :math:`\{\text{true}, \text{false}\}` žodžių transformavimo į poaibius pavyzdys

.. code-block:: c++

    const int MAXN = 20; // didžiausia n reikšmė

    bool parinktas[MAXN + 1];
        
    void spausdink(int n)
    {
        cout << "{ ";
        for (int i = 0; i < n; i++)
            if (parinktas[i])
                cout << i << " ";
        cout << "}" << endl;
    }

    void generuok(int k, int n)
    {
        // Nagrinėjamas k-asis n elementų aibės narys.
        // Jei k >= n, tai ši procedūra iškviesta jau sugeneravus visą poaibį.
        if (k >= n) {
            spausdink(k);
            return;
        }

        // Generuojame poaibius, kuriuose nėra k-ojo elemento
        parinktas[k] = false;
        generuok(k + 1, n);

        // Generuojame poaibius, kuriuose yra k-asis elementas
        parinktas[k] = true;
        generuok(k + 1, n);
    }

Norėdami gauti visus poaibius iš 4 elementų, į procedūrą generuok kreipiamės:

.. code-block:: c++

    generuok(0, 4);

Suskaičiuosime, kiek skirtingų poaibių turės aibė iš :math:`n` elementų, o tuo pačiu ir algoritmo sudėtingumą. Poaibių skaičius lygus visų įmanomų :math:`n` ilgio žodžių iš abėcėlės :math:`\{\text{true}, \text{false}\}` skaičiui. Kadangi kiekvieną tokio žodžio raidę galime parinkti dviem būdais (atitinkamas elementas arba įtraukiamas į poaibį, arba ne), tai tokių žodžių (ir galimų poaibių) skaičius lygus :math:`2^n`.


Uždavinys *Pakyla*
------------------

Panagrinėsime vieną uždavinį, kurio sprendimui reikia taikyti kombinatorikos žinias ir perrinkti visus įmanomus variantus.

    Tarp dviejų taškų :math:`A` ir :math:`B` norime pastatyti pakylą, kurios aukštis :math:`H` metrų. Į pakylos viršų tiek iš taško :math:`A`, tiek iš taško :math:`B` turi vesti kylantys laiptai. Laiptų pakopos aukštis yra :math:`1` metras. Nesunku apskaičiuoti, kad pakylą turi sudaryti :math:`(2H - 1)` pakopų -- po :math:`(H – 1)` iš kiekvienos pusės bei viršutinė. Pirmoji laiptų, kylančių iš taško :math:`A` (taško :math:`B`), pakopa turi prasidėti taške :math:`A` (atitinkamai taške :math:`B`).
    Atstumas tarp taškų :math:`A` ir :math:`B` lygus :math:`P` metrų. O kiekvienos pakopos plotis turi būti lygus sveikajam metrų skaičiui. Aukščiausioje dalyje esančios pakopos plotis turi būti lygus :math:`V` metrų.
    **Užduotis.** Reikia rasti visus galimus skirtingus būdus pakylai įrengti. Dvi pakylos laikomos skirtingomis, jei jų aukštis skiriasi bent vienoje pozicijoje tarp taškų :math:`A` ir :math:`B`.
    Galioja ribojimai: pradiniai duomenys tokie, kad galimų variantų skaičius pakylai įrengti neviršija :math:`20000`.

Prieš sprendžiant uždavinį, svarbu tiksliai apibrėžti, ko iš tiesų ieškome. Kiekvieną galimą pakylą atitinka didėjanti skaičių nuo :math:`0` iki :math:`P` seka :math:`\{S_i\}`, kurią sudaro lygiai :math:`2H` skaičių ir kuri tenkina papildomus ribojimus:

* :math:`S_1 = 0`
* :math:`S_{2H} = P`
* :math:`S_{H + 1} – S_H = V`.

Kiekvienas šios sekos elementas rodo vietą (koordinatę :math:`x`), kurioje keičiasi pakopos aukštis. Pavyzdžiui, paveiksle pavaizduotą pakylą atitinka skaičių seka :math:`0, 2, 3, 4, 7, 8, 10, 12`.

Taigi pirmojo ir paskutinio nario reikšmės yra fiksuotos, o :math:`(H + 1)`-ojo nario reikšmė priklauso nuo :math:`H`-ojo nario: :math:`S_{H + 1} = S_H + V`. Nesunku apriboti :math:`k`-ojo nario reikšmę:

.. math::

    S_{k–1} < S_k \le P – (V – 1) – (2H – k) , \text{ jei } 2 \le k \le H,
    S_{k–1} < S_k \le P – (2H – k) , \text{ jei } H + 2 \le k \le 2H – 1.

Apatinis ribojimas išplaukia iš to, kad seka yra didėjanti, o viršutinis -- kad nepritrūktų skaičių sekai užbaigti.

Gavome derinių generavimo uždavinį, tik tam tikrais ribojimais maksimalioms pozicijų reikšmėms.

Pasinaudosime jau žinomu derinių generavimo algoritmu, kurį pritaikysime šio uždavinio sprendimui. Beje, sutarsime, kad sprendinys egzistuoja.

.. code-block:: pascal

    const MAXH = 100; { maksimalus pakylos aukštis }

    var s : array [1..2*MAXH] of integer;
        P, H, V : integer;

    procedure generuok(k : integer);
    { generuoja sekos narį, kurio numeris k }
    var i, max : integer;
    begin
        if k = 2*H then
            { sugeneruoti visi nariai (paskutinis žinomas iš anksto) }
            spausdink(2*H)[21]
        else if k = H+1 then begin
            { (H+1)-osios pakopos viršūnės plotis fiksuotas }
            s[k] := s[k-1]+V;
            generuok(k+1);
        end
        else begin
            { nagrinėjamos visos galimos k-ojo nario reikšmės }
            if k <= H then
                max := P-(2*H-k)-(V-1)
            else
                max := P-(2*H-k);
            for i := s[k-1]+1 to max do begin
                s[k] := i;
                generuok(k+1);
            end;
        end;
    end;

Į procedūrą generuok turi būti kreipiamasi tokiu būdu:

.. code-block:: pascal

    S[1] := 0;
    S[2*H] := P;
    generuok(2);


Perrinkimo optimizavimas
------------------------

Panagrinėkime dar vieną pavyzdį. Sakykime, saugos kodą, kurį reikia surinkti įeinant į laiptinę, sudaro :math:`3` skaitmenys. Norint jį atspėti, reikia išbandyti :math:`10^3 = 1000` variantų. Jei vieną kodą galima surinkti ir pabandyti atidaryti duris per :math:`3` sekundes, tai visus variantus pavyks išbandyti per :math:`50` minučių. Tačiau jei saugos kodą sudarytų :math:`4` skaitmenys, tai visiems :math:`10^4 = 10000` variantams išbandyti prireiktų daugiau nei :math:`8` valandų. Matome, kad pradiniams duomenims (t. y. skaitmenų skaičiui) padidėjus :math:`33\%`, galimų sprendinių skaičius padidėja :math:`900\%`. Toks staigus sprendinių skaičiaus augimas vadinamas **kombinatoriniu sprogimu**.

Vienas didžiausių perrinkimo trūkumų yra tai, kad susiduriama su kombinatoriniu sprogimu. Generuojant kombinatorinius objektus kitaip ir negali būti: reikia rasti visus objektus, o jų yra daug, taigi ir algoritmų sudėtingumas turi būti didelis. Tačiau dažniau tenka ieškoti tam tikros kombinacijos, t. y. sprendinio, tenkinančio konkrečias sąlygas.

Todėl daugelyje tokių uždavinių stengiamasi **optimizuoti paiešką**. Vienas galimų optimizavimo būdų -- paanalizuoti sprendinio struktūrą ir sumažinti galimų sprendinių paieškos erdvę. Taip darėme :ref:`Aštuonių valdovių uždavinyje <astuoniu-valdoviu-uzdavinys>`. Pradinė sprendinių erdvė buvo gana didelė: buvo sutarta, kad kiekviena valdovė gali stovėti bet kuriame lentos langelyje (po vieną valdovę langelyje), ir galimų variantų skaičius viršijo :math:`4 \cdot 10^9`. Tačiau jei perrenkant variantus, kiekviena valdovė statoma tik į tuščią eilutę -- tai išnagrinėjamų variantų skaičius iš karto sumažėja iki :math:`8! = 40320`.

Gali pavykti sumažinti ir skyrelio pradžioje pateikto uždavinio paieškos erdvę. Jei žinoma, kad visi skaičiai turi būti paspausti vienu metu, tai saugos kode nebus pasikartojančių skaitmenų. Be to, šitaip parenkant kodą nenustatoma skaitmenų tvarka, todėl galime dar sumažinti sprendinių erdvę: pakanka išbandyti visus derinius. Pavyzdžiui, bandant atspėti keturių skaitmenų saugos kodą, mus domina visi deriniai iš :math:`10` po :math:`4`. Jų skaičius yra :math:`C_10^4 = 210` (palyginkite su :math:`10000`).

Jei reikalingas tik vienas sprendinys, paiešką verta optimizuoti parenkant sprendinių nagrinėjimo tvarką taip, kad tikėtini sprendiniai būtų nagrinėjami pirmiausia, jei tik tai įmanoma padaryti.

Yra įvairiausių kitų metodų paieškai pagreitinti, dažnai priimtinų tik konkrečiam uždaviniui Pavyzdžiui, ieškant geriausio ėjimo stalo žaidimuose, naudojama *Minimax* paieška su *Alfa-Beta* atkirtimu; šis metodas leidžia anksčiau atkirsti daug neperspektyvių paieškos medžio šakų


.. rubric:: Išnašos

.. [#pastaba_rekursijai] Yra efektyvesnių (nerekursinių) kombinatorinius objektus generuojančių algoritmų, tačiau rekursiniai algoritmai yra intuityvesni ir lengviau realizuojami.
