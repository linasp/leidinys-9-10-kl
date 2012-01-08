Pirma pažintis su grafais: paieška platyn ir gilyn
==================================================

   *Mathematicians are like Frenchmen: whenever you say something to them, they translate it into their own language, and at once it is something entirely different.* 

    Matematikai --- kaip prancūzai: kad ir ką jiems bepasakytum, jie iškart išverčia tai į savo kalbą, ir tai iškart tampa visiškai skirtingu dalyku.

    -- Johanas Volfgangas fon Gėtė (*Johann Wolfgang von Goethe*)

Per Karaliaučių tekančioje Priegliaus upėje yra dvi gražios salos. Septyni tiltai jungia krantus su šiomis salomis, taip pat abi salas tarpusavyje. Maždaug prieš tris šimtus metų Karaliaučiaus gyventojus sudomino klausimas: ar galimas toks maršrutas, kuris prasidėtų viename iš krantų, kad per kiekvieną tiltą būtų pereinama tik vieną kartą, o pasivaikščiojimas pagaliau baigtųsi ten, kur ir prasidėjo.

1736 m. šio uždavinio ėmėsi garsus šveicarų matematikas Leonardas Oileris (*Leonhard Euler*). Krantai, salos, tiltai --- visa tai jam buvo tik uždavinio „apvalkalas“: salos buvo tam tikri objektai, o tiltai --- šiuos objektus siejantys ryšiai. Krantus bei salas Oileris sutapatino su taškais, o tiltus --- su linijomis. Jis paprastai įrodė, jog maršruto, tenkinančio minėtus kriterijus, nėra ir negali būti. Šitaip buvo pradėta grafų teorija. Tačiau apie tai vėliau.

Šiame skyrelyje išsiaiškinsime, kas tie grafai, kam jie reikalingi, taip pat susipažinsime su dviem pirmaisiais grafų teorijos algoritmais.


Grafo sąvoka
------------

**Grafas** yra sąsajų struktūra, nurodanti, kad yra objektų grupė, ir kad šie objektai yra tarpusavy susiję (arba nesusiję).

Objektai vadinami grafo **viršūnėmis**, o jų ryšius apibūdina grafo **briaunos**. Jei grafe briauna jungia dvi viršūnes, tai šios viršūnės vadinamos **gretimomis**. Viršūnei gretimos viršūnės dar vadinamos jos **kaimynėmis**. Jei briauna jungia viršūnę su ja pačia, tai ta briauna vadinama **kilpa**.

    31 pav. Karaliaučiaus tiltų brėžinys, kai krantai sutapatinti su taškais, o tiltai --- su linijomis

Labai svarbi yra grafų geometrinė interpretacija: grafo viršūnes patogu vaizduoti plokštumos taškais, o briaunas --- linijomis, jungiančiomis viršūnių (taigi taškų) porą. Viršūnių (taškų) ir briaunų (linijų) geometrinis išdėstymas nesvarbus, svarbus tik pačių sąsajų pavaizdavimas. Tą patį grafą galima nupiešti daugybe skirtingų būdų.

    32 pav. Tas pats grafas, pavaizduotas dviem skirtingais būdais, grafo viršūnės žymimos skaičiais

.. todo:: pataisyti nuorodą į iliustraciją.

Matematiškai grafas apibrėžiamas kaip dviejų aibių --- viršūnių ir briaunų --- rinkinys: :math:`G = (V, B)`. Briaunų aibės elementai --- tai viršūnių poros. Pavyzdžiui, 33 pav. pavaizduotą grafą atitinka tokios viršūnių ir briaunų aibės: :math:`V = \{ a, b, c, d, e, f, g \}`, :math:`B = \{ (a, c), (a, f), (b, f), (c, f), (d, e), (d, g) \}`.

    33 pav. Grafas, jo viršūnės žymimos raidėmis

Pastabesni galėtų prikibti --- aibėje negali būti pasikartojančių elementų. Tačiau skyrelio pradžioje sutikome grafą, kurio dvi viršūnes jungia **kelios briaunos** (salą su tuo pačiu krantu jungia keli tiltai).

Grafai su pasikartojančiomis briaunomis vadinami **multigrafais**. Tokių grafų matematiniame modelyje aibė pakeičiama multiaibe (aibe, kurioje elementai gali kartotis). Daugelyje uždavinių vietoj multigrafo pakanka nagrinėti paprastą grafą, gautą iš multigrafo, iš kelių dvi viršūnes jungiančių briaunų paliekant tik vieną, tinkamiausią uždaviniui spręsti.

**Keliu** grafe vadinama gretimų viršūnių seka, kai ta pati briauna kelyje sutinkama tik vieną kartą, o ta pati viršūnė gali būti kelyje sutinkama kelis kartus. Jei kelias prasideda ir baigiasi toje pačioje viršūnėje, jis vadinamas **ciklu**. Kelio ilgis lygus pereitų briaunų skaičiui.

Tačiau kam gi reikalinga grafų teorija? Pasirodo, grafų teorijos „kalba“ galima išreikšti daugelį svarbių (dažnai praktinių) uždavinių. Vieną jų ką tik matėme --- tai maršruto, kai kiekviena briauna pereinama lygiai vieną kartą, paieška. Grafu galima pavaizduoti ir miesto planą, briaunomis žymint jo gatves. Tuomet, kiekvienai briaunai priskyrę po teigiamą skaičių --- gatvės ilgį, galime klausti: koks trumpiausias kelias iš viršūnės :math:`a` į viršūnę :math:`b`? Šio uždavinio sprendimui taip pat yra efektyvus algoritmas, kurį pateiksime vėliau.

Ne visuomet ryšys tarp uždavinio ir jo sumodeliavimo grafų teorijos terminais toks akivaizdus. Štai dar vieno uždavinio pavyzdys: tarkime, kad :math:`n` vaikų pasirinko mokytis kai kuriuos iš :math:`m` dalykų. Reikia sudaryti optimalų (kuo glaustesnį) užsiėmimų tvarkaraštį. Sudarykime grafą, kurio :math:`m` viršūnių atitiks visus dalykus, o briauna, jungianti viršūnes :math:`a` ir :math:`b`, reikš, kad bent vienas vaikas pasirinko abu dalykus :math:`a` ir :math:`b`.

    35 pav. Viršūnių spalvinimo uždavinys. Sudarę ir nuspalvinę pasirinkimų grafą, darome išvadą, kad fizikos ir biologijos užsiėmimai gali vykti vienu metu

Dabar galime spręsti *grafo viršūnių spalvinimo uždavinį*: kaip, panaudojant kuo mažiau spalvų, nuspalvinti grafo viršūnes, kad jokios dvi gretimos grafo viršūnės nebūtų nuspalvintos ta pačia spalva. Viena spalva nuspalvintomis viršūnėmis pažymėtų dalykų užsiėmimai gali vykti vienu metu: tai netrukdys nė vienam moksleiviui. Taigi svarbioji uždavinio dalis bus išspręsta. Deja, viršūnių spalvinimo uždaviniui nežinomas joks efektyvus algoritmas.


Grafų vaizdavimas
-----------------

Grafus vaizduoti aibėmis pagal jų matematinį apibrėžimą dažniausiai nėra patogu. Tarus, kad grafas turi :math:`n` viršūnių, sunumeruotų nuo :math:`1` iki :math:`n`, viršūnių aibės nurodyti nebūtina --- pakanka žinoti viršūnių skaičių :math:`n`. Grafo briaunas paprasčiausia pavaizduoti dvimačiu :math:`n \times n` loginiu masyvu: elementus :math:`[u, v]` ir :math:`[v, u]` pažymint reikšme ``true``, jei viršūnes su numeriais :math:`u` ir :math:`v` grafe jungia briauna. Šis masyvas visuomet yra simetrinis įstrižainės atžvilgiu [#orientuoti_grafai]_.

.. code-block:: pascal

    const MAXN = ...; { maksimalus grafo viršūnių skaičius }

    type grafas = record
             n : integer;
             briauna : array [1..MAXN,
                            1..MAXN] of boolean;
        end;

Kol visos masyvo briauna reikšmės lygios false, grafe nėra nė vienos briaunos. Priklausomai nuo uždavinio pradinių duomenų, kai kurias viršūnes reikės sujungti briauna. Tai atlieka tokia procedūra:

.. code-block:: pascal

    procedure papildyk_briauna(var g : grafas;
                            u, v : integer);
    begin
        g.briauna[u, v] := true;
        g.briauna[v, u] := true;
    end;

Toks grafo vaizdavimas vadinamas **kaimynystės matrica**. Tokio vaizdavimo kompiuteryje privalumai --- jo paprastumas ir galimybė sparčiai patikrinti, ar dvi viršūnes jungia briauna. Deja, yra ir svarbus trūkumas --- norėdami rasti visas viršūnės :math:`v` kaimynes, turime patikrinti visą :math:`v`-ąją masyvo briauna eilutę, tikrindami sąlygą, ar ``briauna[v, u] = true``. Jei grafas yra **retas** (t. y. jame palyginti nedaug briaunų), tai atmintis, skiriama beveik tuščiam masyvui, neefektyviai išnaudojama. Kai grafe briaunų daug (grafas **tankus**), tai šis paprastas vaizdavimo būdas labai patogus.

Iš anksto žinant, kad grafas bus retas, geriau naudoti kitą vaizdavimo būdą --- **kaimynystės sąrašus** --- t. y. kiekvienai viršūnei saugoti jai gretimų viršūnių (jos kaimynių) sąrašą.

Naudojant sudėtingesnes dinamines duomenų struktūras šiems sąrašams saugoti, galima sutaupyti atminties. Tačiau olimpiadose, jei tik įmanoma, geriau vengti dinaminių duomenų struktūrų --- jas kur kas sudėtingiau teisingai realizuoti per trumpą laiką.

Savo pavyzdžiuose paprastumo dėlei kaimynių sąrašą saugosime masyvu. Kadangi iš anksto nežinome, kiek daugiausiai kaimynių gali turėti kiekviena viršūnė, tai šių masyvų ilgis bus toks, koks gali būti didžiausias viršūnių skaičius.

.. code-block:: pascal

    const MAXN = ...; { maksimalus grafo viršūnių skaičius }

    type virsune = record
             k : integer;           	{ kaimynių skaičius }
             ksarasas : array [1..MAXN] of integer;
                                        { kaimynių sąrašas }
        end;

        grafas = record
             n : integer;             	{ viršūnių skaičius }
             vir : array [1..MAXN] of virsune;
                                        { viršūnių sąrašas }
        end;

Kai grafe nėra briaunų, visų viršūnių kaimynių skaičiaus atributas lygus nuliui. Įterpti briauną :math:`(u, v)` į šitaip vaizduojamą grafą reiškia papildyti viršūnių :math:`u` ir :math:`v` kaimynių sąrašus. Tai atlieka tokia procedūra:

.. code-block:: pascal

    procedure papildyk_briauna(var g : grafas; u, v : integer);
    begin
        with g do begin
            inc(vir[u].k);
            vir[u].ksarasas[vir[u].k] := v;
            if v <> u then begin { jei tai ne kilpa }
                inc(vir[v].k);
               vir[v].ksarasas[vir[v].k] := u;
            end;
        end;
    end;

Nors surasti vienos viršūnės kaimynes galime labai greitai, patikrinti, ar viršūnes :math:`u` ir :math:`v` grafe jungia briauna tapo sudėtingiau: tam reikia perbėgti vienos iš šių viršūnių kaimynių sąrašą, ieškant antrosios.

Kurį iš aptartų vaizdavimo būdų pasirinkti? Tai priklauso nuo sprendžiamo uždavinio. Daugelyje algoritmų tenka surasti duotosios viršūnės kaimynes, o rečiau --- patikrinti, ar viršūnes jungia briauna. Kai reikalingas abiejų šių operacijų efektyvumas, tą patį grafą gali tekti vaizduoti dviem būdais.

Galimas ir dar kitoks grafo pavaizdavimo būdas. Jei grafe viršūnių labai daug, o briaunų nedaug, galime saugoti briaunų (viršūnių porų) sąrašą. Tuomet briauną, jungiančią viršūnes :math:`u` ir :math:`v`, verta vaizduoti dviem poromis: :math:`(u, v)` ir :math:`(v, u)`. Išrikiavę tokį sąrašą, konkrečios briaunos paiešką galime atlikti per :math:`O(\log b)` laiko (:math:`b` --- briaunų skaičius), pasitelkę dvejetainę paiešką. Praktikoje šis būdas retai naudojamas.


.. _paieska-gilyn:

Paieška gilyn
-------------

    Karalaitė slapta padavė Tesėjui kamuoliuką siūlų ir pamokė, ką reikia daryti, kad nepaklystų vingiuotuose paslaptingojo statinio koridoriuose. Tesėjas pririšo siūlo galą prie labirinto angos ir, eidamas priekin, vyniojo rankoje laikomą kamuoliuką.

    (Iš graikų mitų)

Pirmieji grafų algoritmai, su kuriais susipažinsime, --- tai paieška grafe gilyn ir platyn. Pradėjus nuo kažkurios viršūnės, aplankomos visos kitos briaunomis pasiekiamos viršūnės. Dvi skirtingos viršūnių aplankymo strategijos -- paieška gilyn ir platyn --- dažnai yra kitų algoritmų sudėtinė dalis.

Pradėsime nuo **paieškos gilyn** (angl. *Depth-First Search*, *DFS*), jos principas panašus į grįžimo metodo. Algoritmo parametras yra pradžios viršūnė :math:`v_0`, iš jos aplankomos kitos viršūnės: aplankius viršūnę :math:`v_0`, aplankoma dar neaplankyta :math:`v_0` kaimynė :math:`v_1`, tada ieškoma dar neaplankyta :math:`v_1` kaimynė :math:`v_2` ir taip toliau, kol pasiekiama viršūnė :math:`v_m`, kuri nebeturi neaplankytų kaimynių. Tuomet grįžtama vieną žingsnį ir žiūrima, ar viršūnė :math:`v_{m - 1}` dar turi nors vieną neaplankytą kaimynę :math:`v_{m\`}`. Jei turi, --- ieškoma gilyn, jei ne --- grįžtama dar per vieną žingsnį ir t. t. Paiešką gilyn, kaip ir grįžimo metodu pagrįstus algoritmus, paprasta realizuoti naudojant rekursiją.

Skirtingai negu grįžimo metodas, paieška gilyn yra efektyvus algoritmas, kadangi kiekviena grafo viršūnė aplankoma tik vieną kartą. Tuo tarpu jei taikytume grįžimo metodą, ta pati viršūnė galėtų būti aplankyta daug kartų, nes būtų išbandomi visi įmanomi keliai grafe, prasidedantys viršūnėje :math:`v_0`.

Paieškos gilyn algoritmas veikimo metu kiekvieną viršūnę nuspalvina tam tikra spalva --- balta, pilka arba juoda. Viršūnių spalvoms žymėti aprašysime specialų duomenų tipą:

.. code-block:: pascal

    type spalvos = (balta, pilka, juoda);

Prieš pradedant vykdyti algoritmą visos viršūnės nuspalvinamos baltai (pažymimos neaplankytomis). Algoritmo veikimo metu, aplankant viršūnę, ji nuspalvinama pilkai, o įvykdžius algoritmą su visomis neaplankytomis jos kaimynėmis --- juodai.

    38 pav. Paieškos gilyn veikimo iliustracija, kai pradine viršūne pasirinkta viršūnė :math:`a`.

Algoritmas taip pat išsaugo paieškos į gylį pirminumo medį, t. y. kiekvienai viršūnei įsimena, iš kurios ši buvo aplankyta.

Žemiau pateiktas algoritmo tekstas Paskalio kalba. Algoritmo veikimo metu dažnai reikės rasti kurios nors viršūnės kaimynes, todėl grafą vaizduosime kaimynystės sąrašais.

.. code-block:: pascal

    type spalvos = (balta, pilka, juoda);

        sp_masyvas = array [1..MAXN] of spalvos;
        masyvas = array [1..MAXN] of integer;

    var spalva : sp_masyvas;  { pradinės reikšmės – balta}
        pirmine : masyvas;	{ pradinės reikšmės – 0}

    procedure ieskok_gilyn(var g: grafas; v : integer { aplankoma viršūnė });
    var u, i : integer;
    begin
        spalva[v] := pilka;
        with g do
            { toliau paieška iš eilės vykdoma visose neaplankytose
              (baltose) kaimynėse }
            for i := 1 to vir[v].k do begin
                u := vir[v].ksarasas[i];
                if spalva[u] = balta then begin
                    pirmine[u] := v;
                   ieskok_gilyn(g, u);
                end;
            end;
        spalva[v] := juoda;
    end;

Iškvietus ``ieškok_gilyn(v)``, visos viršūnės, kurias galima pasiekti briaunomis iš viršūnės :math:`v`, bus pažymimos juodai. Atspausdinti kelią, kuriuo buvo pasiekta viršūnė :math:`u`, nesunku pasinaudojus masyve ``pirmine`` išsaugota informacija:

.. code-block:: pascal

    procedure spausdink_kelia(u : integer);
    begin
        if pirmine[u] <> 0 then
            spausdink_kelia(pirmine[u]);
        writeln(u);
    end;

Iš tiesų algoritme pakaktų viršūnes spalvinti tik dviem spalvomis: atskirti aplankytas nuo neaplankytų. Tačiau naudojant tris spalvas algoritmas tampa aiškesnis. Be to, gali būti naudinga atskirti viršūnes, kuriose pradėtas vykdyti paieškos gilyn algoritmas, bet nebaigtas (pilkas viršūnes), pavyzdžiui, norint pritaikyti paieškos gilyn algoritmą ciklo paieškai.

Procedūros ``ieskok_gilyn`` sudėtingumas yra :math:`O(b)`, kur :math:`b` yra grafo briaunų skaičius. Tokiam efektyvumui pasiekti grafą būtina vaizduoti kaimynystės sąrašais. Jei grafą vaizduotume kaimynystės matrica, galėtume pasiekti tik :math:`O(n^2)` sudėtingumą.

Kaip tik paieška gilyn ir naudojosi Tesėjas, ieškodamas labirinte Minotauro. Kiekvienoje koridorių sankirtoje jis pasirinkdavo tolimesnę kryptį ir jei prieidavo aklavietę, grįždavo atgal iki praeitos sankirtos bandyti kitos krypties. O jei toje sankirtoje visi koridoriai jau išbandyti --- grįždavo į dar ankstesnę sankirtą ir taip toliau. Siūlas padėjo Tesėjui rasti Minotaurą.


Patikrinimas, ar grafas jungus
------------------------------

Grafas yra **jungus**, jei iš bet kurios viršūnės galima pasiekti bet kurią kitą viršūnę einant briaunomis. Priešingu atveju grafas vadinamas **nejungiu**.

Nejungus grafas yra sudarytas iš jungių dalių, vadinamų **jungumo komponentais**.

Grafo jungumą tenka tikrinti sprendžiant įvairiausius uždavinius. Paprasčiausia tai padaryti taikant paiešką į gylį grafe. Pritaikysime praeitame skyrelyje pateiktą algoritmą, grafą vaizduosime kaimynystės sąrašais. Šiuo atveju viršūnes užteks spalvinti tik dviem spalvomis (t. y. atskirti aplankytas nuo neaplankytų), tad tam naudosime loginį masyvą. Pirminės viršūnės taip pat nesvarbios, taigi paiešką gilyn realizuoti bus paprasčiau. Tačiau paieškos gilyn procedūrą papildysime skaičiavimu, kiek viršūnių aplankyta. 

Grafas yra jungus tada ir tik tada, jei įvykdžius paiešką gilyn iš bet kurios jo viršūnės, bus aplankytos **visos** grafo viršūnės.

.. code-block:: pascal

    function jungus(var g : grafas) : boolean;
    var aplankyta : array [1..MAXN] of boolean;

        procedure ieskok_gilyn(v : integer;
                              var sk : integer);
        { v - aplankoma viršūnė, sk – aplankytų viršūnių skaičius }
        var u, i : integer;
        begin
            aplankyta[v] := true;
            inc(sk);
            with g do
                for i := 1 to vir[v].k do begin
                    u := vir[v].ksarasas[i];
                    if not aplankyta[u] then
                        ieskok_gilyn(u, sk);
                end;
        end;

    var v, sk : integer;
    begin
        for v := 1 to g.n do
            aplankyta[v] := false;
        sk := 0;
        ieskok_gilyn(1, sk);
        { jei buvo aplankytos visos viršūnės – tai grafas jungus }
        jungus := sk = g.n;
    end;


Uždavinys *Epidemijos modeliavimas*: grafo jungumo komponentų paieška
---------------------------------------------------------------------

Taikydami grafų teoriją išspręsime pirmą konkretų uždavinį Epidemijos modeliavimas [#epidemijos_modeliavimas]_:

    Plinta pavojinga paukščių liga. Jeigu paukštis užsikrečia šia liga, tai nuo jo užsikrės visi kiti paukščiai, turintys su juo nuolatinius kontaktus, po to nuo jų užsikrės dar kiti (turintys nuolatinius kontaktus su naujai užsikrėtusiais) ir t. t. Paukščiai, neturintys tarpusavyje nuolatinių kontaktų, tiesiogiai vienas nuo kito užsikrėsti negali.

    **Užduotis:** Žinoma, kad :math:`m` paukščių jau yra užsikrėtę liga, ir žinomos visos paukščių poros, turinčios nuolatinius kontaktus. Deja, nežinoma, kurie iš visų :math:`n` paukščių jau yra užsikrėtę. Reikia nustatyti, kiek daugiausiai šios rūšies paukščių gali užsikrėsti dėl epidemijos.

Paukščiai atitiks grafo viršūnes, o nuolatiniai kontaktai --- briaunas. Grafas gali būti nejungus, t. y. jame gali egzistuoti keletas jungių komponentų, kuriuos toliau sprendimo aprašyme vadinsime paukščių šeimomis. Atskiru atveju šeimą gali sudaryti tik vienas paukštis.

Jei užsikrės nors vienas paukštis iš šeimos, tai nuo šio paukščio užsikrės visa šeima. Tad užsikrėtusių paukščių bus daugiausiai, jei iš pradžių bus užsikrėtę po vieną paukštį iš kuo gausesnių šeimų.

Taigi norint išspręsti šį uždavinį, reikia rasti viršūnių skaičių kiekviename **jungumo komponente**, tuomet jas išrikiuoti nedidėjimo tvarka ir suskaičiuoti, kiek yra viršūnių didžiausiuose :math:`m` komponentų.

Piešinyje pateiktame pavyzdyje yra penkios paukščių šeimos: tris šeimas sudaro vieniši paukščiai, vieną šeimą sudaro paukščių pora, o dar vieną --- penki paukščiai. Išrikiavę gautume: :math:`5, 2, 1, 1, 1`.

Sakykime, užsikrėtė :math:`3` paukščiai. Tad didžiausias galimų užsikrėtusių paukščių skaičius lygus: :math:`5 + 2 + 1 = 8`.

Tačiau kaip ieškoti jungumo komponentų? Pasirinkime bet kurią grafo viršūnę --- ji priklauso kažkokiam grafo jungumo komponentui. Jei pradėdami joje įvykdysime paiešką gilyn, tai bus aplankomos visos komponento viršūnės. Todėl norėdami suskaičiuoti, kiek jungumo komponentų sudaro grafą, galime iteruoti per visas grafo viršūnes ir radę neaplankytą, vykdyti paiešką gilyn (aplankančią visas aptikto komponento viršūnes). Kiek kartų iteruodami aptiksime neaplankytą viršūnę, tiek ir jungumo komponentų yra grafe.

Šiame uždavinyje svarbu sužinoti ir pačių komponentų dydžius, todėl panaudosime paieškos gilyn procedūrą, kurią naudojome grafo jungumo tikrinimui --- įsimenančią, kiek viršūnių buvo aplankyta paieškos metu.

.. code-block:: pascal

    type log_mas = array [1..MAXN] of boolean;
         masyvas = array [1..MAXN] of integer;

    function uzsikres(var g : grafas; m : integer): integer;
    { m – jau užsikrėtusių paukščių skaičius;
      g – grafas, vaizduojamas kaimynystės sąrašais }

    var aplankyta : log_mas;
        i, komp_sk, iki : integer;
        komp_dydis : masyvas;

    begin
        for i := 1 to g.n do
            aplankyta[i] := false;
        komp_sk := 0;

        for i := 1 to g.n do
            if not aplankyta[i] then begin
                komp_sk := komp_sk + 1;
                komp_dydis[komp_sk] := 0;
                ieskok_gilyn(i, komp_dydis[komp_sk]);
            end;
        rikiuok(komp_sk, komp_dydis);

        uzsikres := 0;
        { užsikrėtusių paukščių gali būti daugiau
          nei jungumo komponentų }
        if m > komp_sk then
            iki := 1
        else
            iki := komp_sk - m + 1;
        for i := komp_sk downto iki do
            uzsikres := uzsikres + komp_dydis[i];
    end;

Čia naudojama procedūra ``rikiuok`` yra aprašyta skyriuje :ref:`rikiavimas-iterpimu`, o procedūra ``ieskok_gilyn`` --- :ref:`paieska-gilyn`.


Paieška platyn
--------------

**Paieškos platyn** (angl. *Breadth-First Search*, *BFS*) algoritmas aplanko viršūnes pagal griežtą taisyklę: pradėjus nuo pasirinktos viršūnės (tarkime, :math:`p`), aplankomos visos viršūnės, kurios pasiekiamos iš :math:`p` viena briauna (vienu ėjimu), tuomet --- pasiekiamos iš :math:`p` dvejomis briaunomis (dviem ėjimais) ir t. t.

Kaip užtikrinti tokią viršūnių lankymo tvarką? Algoritmas naudoja aplankytų viršūnių eilę: pirmiausia į eilę įrašoma pradinė viršūnė; kol eilė netuščia, iš jos pradžios imama viršūnė ir visos neaplankytos jos kaimynės įrašomos į eilės galą. Šitaip eilėje pirmiausia atsiduria viršūnės, pasiekiamos viena briauna, tada --- dviem briaunomis ir t. t.

Programuodami paiešką gilyn panaudojome rekursiją, tad nekonstravome savo dėklo [#deklas]_ duomenų struktūros. Paieškai platyn jau reikalinga *eilės* duomenų struktūra:

.. code-block:: pascal

    type eile = record
            duom : array [1..MAXN] of integer;
            pradzia, pabaiga : integer;
        end;

Nauji elementai dedami į eilės galą, o imami iš eilės pradžios. Žemiau pateiktos procedūros su eile atlieka veiksmus, kurių reikės paieškos platyn algoritmui:

.. code-block:: pascal

    procedure isvalyk(var eil : eile);
    begin
        eil.pradzia := 0;
        eil.pabaiga := 0;
    end;

    function tuscia(var eil : eile) : boolean;
    begin
        tuscia := eil.pradzia = eil.pabaiga;
    end;

    procedure idek(var eil : eile; x : integer);
    begin
        eil.pabaiga := eil.pabaiga + 1;
        eil.duom[eil.pabaiga] := x;
    end;

    function isimk(var eil : eile) : integer;
    begin
        eil.pradzia := eil.pradzia + 1;
        isimk := eil.duom[eil.pradzia];
    end;

Kaip ir paieškos gilyn atveju, algoritmo vykdymo metu viršūnės spalvinamos balta, pilka ir juoda spalvomis, nors užtektų ir dviejų spalvų. Balta spalva nuspalvintos dar neaplankytos viršūnės, pilka --- viršūnės, kurios įtrauktos į eilę, o juoda --- jau išnagrinėtos (pašalintos iš eilės) viršūnės.

Paieškos platyn viršūnių aplankymo strategija garantuoja, kad kiekviena viršūnė iš pradinės bus aplankyta **trumpiausiu keliu** (jį sudaro mažiausias briaunų skaičius). Taigi paieška platyn --- tinkamas algoritmas trumpiausio kelio paieškai grafuose, kurių visos briaunos yra lygiavertės (grafų teorijos terminais, **besvorės**).

    44 pav. Paieškos platyn veikimo iliustracija, kai pradine viršūne pasirinkta viršūnė :math:`a`.

Trumpiausi atstumai iki kiekvienos viršūnės saugomi atskirame masyve. Kol nerastas kelias iki viršūnės, šis atstumas laikomas begaliniu. Grafas vaizduojamas kaimynystės sąrašais.

.. code-block:: pascal

    const BEGALINIS = MAXINT;
    type spalvos = (balta, pilka, juoda);

    var atstumas, { saugomi atstumai nuo pradinės iki
                  visų kitų viršūnių }
        pirmine : array [1..MAXN] of integer;
        spalva : array [1..MAXN] of spalvos;

    procedure ieskok_platyn(var g : grafas;
                            p : integer { pradinė viršūnė } );
    var eil  : eile;
        i, u, v : integer;
    begin
        for v := 1 to g.n do begin
            atstumas[v] := BEGALINIS;
            pirmine[v] := 0;
            spalva[v] := balta;
        end;

        isvalyk(eil);
        { į eilę įtraukiama pradinė viršūnė }
        spalva[p] := pilka;  atstumas[p] := 0;
        pirmine[p] := 0;     idek(eil, p);

        while not tuscia(eil) do begin
            v := isimk(eil);
            with g do
            { dar neaplankytos (baltos) v kaimynės įtraukiamos į eilę }
                for i := 1 to vir[v].k do begin
                    u := vir[v].ksarasas[i];
                   if spalva[u] = balta then begin
                        spalva[u] := pilka;
                        pirmine[u] := v;
                        atstumas[u] := atstumas[v] + 1;
                        idek(eil, u);
                    end;
                end;
            spalva[v] := juoda;
        end;
    end;

Jei reikia išspausdinti trumpiausią kelią nuo pradinės viršūnės iki viršūnės :math:`u`, naudojamės sudarytu pirminumo medžiu ir kreipiamės į procedūrą ``spausdink_kelia(u)`` --- ji pateikta skyrelyje :ref:`paieska-gilyn`.

    45 pav. Paieškos platyn pirminumo medis

Algoritmo sudėtingumas yra toks pat kaip ir paieškos gilyn: :math:`O(n + b)`, jei grafas vaizduojamas kaimynystės sąrašais, ir :math:`O(n^2)`, jei grafas vaizduojamas kaimynystės matrica. Čia :math:`n` --- grafo viršūnių, :math:`b` --- briaunų skaičius.


Uždavinys Nykštukai
-------------------

Panagrinėsime uždavinį *Nykštukai* [#nykstukai]_:

    Nykštukai gyvena vienaukščiame name, kuriame yra daug kambarių. Jei tarp dviejų kambarių yra durys, tai galima pereiti iš vieno kambario į kitą. Įėjimas iš namo yra tik pro vienintelį kambarį. Namas stebuklingas ir durys gali būti tarp bet kurių kambarių. Išėjimas pro duris į kitą kambarį arba į lauką užtrunka vieną laiko vienetą.

    Netikėtai nykštukai sužinojo, kad po t laiko vienetų iš aikštelės šalia namo išvažiuoja autobusas į NKL (Nykštukų krepšinio lygos) finalines varžybas. Žinoma, kiek nykštukų yra name ir kokiuose kambariuose. Kiekvienas nykštukas žino greičiausią kelią iki išėjimo ir iš namo bėgs būtent tuo keliu.

    46 pav. Namo išplanavimo pavyzdys; parodyta, kuriuose kambariuose pradiniu momentu yra nykštukai

    **Užduotis.** Reikia nustatyti, kurie nykštukai suspės į autobusą, jeigu kiekvienas bėgs greičiausiu keliu.


Uždavinį modeliuojame grafu: kambariai bei išėjimas laikomi grafo viršūnėmis, o durys --- briaunomis.

Reikia sužinoti, per kiek mažiausiai laiko vienetų kiekvienas nykštukas gali išbėgti laukan. Laiko vienetų skaičius lygus perbėgamų durų skaičiui, t. y. briaunų skaičiui mūsų sudarytame grafe. Taigi ieškome trumpiausių kelių iš viršūnių, kuriose „stovi“ nykštukai, iki išėjimo viršūnės. Nepamirškime --- mus domina ne patys keliai, o tik jų ilgiai.

Trumpiausio kelio paieškai galime panaudoti ką tik išmoktą paieškos platyn algoritmą, ir vykdyti jį iš kiekvienos viršūnės, kurioje „stovi“ bent vienas nykštukas. Tačiau galima uždavinį išspręsti efektyviau: įsivaizduokime, kad lauke stovi vienas nykštukas (pavyzdžiui, autobuso vairuotojas?); jei rasime visus nykštukus, pas kuriuos šis nykštukas gali atbėgti per :math:`t` ar mažiau laiko vienetų, tai ir išspręsime uždavinį. Pakanka **vieną kartą** įvykdyti paieškos platyn algoritmą iš išėjimo viršūnės. Žinant trumpiausių kelių ilgius nuo išėjimo iki kiekvieno kambario, nesunku baigti spręsti uždavinį.

Toliau pateiktame programos fragmente paieška platyn realizuota paprasčiau, kadangi mus domina ne patys keliai, o tik atstumai. Neaplankytas viršūnes atpažinsime ne pagal spalvą, o pagal tai, kad atstumas iki jų yra pažymėtas begaliniu. Grafas vaizduojamas kaimynystės sąrašais.

.. code-block:: pascal

    const BEGALINIS = MAXINT;
        MAXN = ...; {maksimalus kambarių (grafo viršūnių) skaičius}
        MAXK = ...; {maksimalus nykštukų skaičius}

    type masyvas = array [1..MAXK] of integer;
         loginis = array [1..MAXK] of boolean;

    var atstumas : array [1..MAXN] of integer;



    procedure ieskok_platyn(var g : grafas; p : integer { pradinė viršūnė } );

    var eil : eile;
        i, u, v : integer;

    begin
        for v := 1 to g.n do
            atstumas[v] := BEGALINIS;
        isvalyk(eil);
        { į eilę įtraukiama pradinė viršūnė }
        atstumas[p] := 0;
        idek(eil, p);
        while not tuscia(eil) do begin
            v := isimk(eil);
            with g do
            { visos dar neaplankytos (pažymėtos begaliniu atstumu)
              v kaimynės įtraukiamos į eilę }
                for i := 1 to vir[v].k do begin
                    u := vir[v].ksarasas[i];
                    if atstumas[u] = BEGALINIS then begin
                        atstumas[u] := atstumas[v] + 1;
                        idek(eil, u);
                    end;
                end;
        end;
    end;

    procedure kas_spes(var g : grafas;
                    var kamb : masyvas;
                    { kamb[i] – i-ojo nykštuko kambario numeris }
                    isejimas, t : integer;
                    var spes : loginis);
    begin
        ieskok_platyn(g, isejimas);
        for i := 1 to nyk_sk do
        spes[i] := atstumas[kamb[i]] <= t;
    end;



.. rubric:: Išnašos

.. todo:: pataisyti nuorodą į skyrius žemiau.

.. [#orientuoti_grafai] 9 skyriuje nagrinėsime orientuotus grafus, kurie vaizduojami nesimetriškais dvimačiais masyvais.

.. [#epidemijos_modeliavimas] Šis uždavinys buvo pateiktas Lietuvos moksleivių informatikos olimpiados III etape 2006 metais.

.. [#deklas] Žr. 4.1 skyrelį.

.. [#nykstukai] Analogiškas uždavinys buvo pateiktas Lietuvos informatikos olimpiados III etape 2005 metais.
