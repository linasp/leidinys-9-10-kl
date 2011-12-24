Intuityvios algoritmo ir algoritmo sudėtingumo sąvokos
======================================================

.. todo:: Sutvarkyti, kad ši citata būtų normaliai vaizduojama.

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

.. todo:: Žemiau sutvarkyti nuorodą į knygą.

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

.. todo:: Žemiau sutvarkyti nuorodą į knygą.

Iš tiesų skyrelio pradžioje pateiktas algoritmo apibrėžimas tėra intuityvi ir matematiškai
netiksli algoritmo sąvoka [1]. Tačiau mums jos pakaks.


Algoritmo sudėtingumas
----------------------

Kaip jau minėjome, yra uždavinių, kurių kompiuteris negali išspręsti per priimtiną laiką, ir būtų neišmintinga viltis, kad kompiuteriai gali greitai atlikti *bet kokius* skaičiavimus.  Todėl svarbu mokėti įvertinti algoritmo sudėtingumą, t. y. nustatyti, kiek laiko ir atminties išteklių prireiks algoritmo vykdymui.

Kas gi yra spartus algoritmas?  Kuo didesnis pradinių duomenų kiekis (arba dydis), tuo ilgiau veikia programos, apdorojančios šiuos duomenis. Taigi algoritmas yra spartus, jei ganėtinai greitai apdoroja *didelius duomenų kiekius*. Negalime sakyti, kad vienas rikiavimo algoritmas spartesnis už kitą, jei pirmasis 10 skaičių išrikiavo greičiau nei antrasis. Kas kita, jei tenka rikiuoti labai daug skaičių.  Apskritai konkretūs laiko įverčiai dažniausiai neteikia naudos, kadangi priklauso nuo daugybės veiksnių -- techninių kompiuterio parametrų, algoritmo realizacijos, kompiliatoriaus nustatymų ir panašiai.

Daug svarbiau žinoti, kaip algoritmo vykdymui reikalingi laiko ir atminties ištekliai priklauso nuo pradinių duomenų kiekio. Žinodami, kad rikiavimo algoritmo atliekamų veiksmų skaičius didėja proporcingai rikiuojamos sekos ilgio kvadratui, galėsime nuspręsti, ar toks efektyvumas priimtinas.  Algoritmo sudėtingumas laiko atžvilgiu vertinamas funkcija, apibrėžiančia atliekamų veiksmų skaičiaus priklausomybę nuo pradinių duomenų dydžio. Algoritmo sudėtingumas atminties atžvilgiu vertinamas funkcija, apibrėžiančia reikalingos atminties kiekio priklausomybę nuo pradinių duomenų dydžio.

Kas yra pradinių duomenų dydis? Tai priklauso nuo paties algoritmo. Pavyzdžiui, dažnam rikiavimo algoritmui duomenų dydį apibrėžia rikiuojamų skaičių kiekis, bet ne patys skaičiai. Tačiau yra rikiavimo algoritmų, kurių efektyvumas priklauso ir nuo pačių rikiuojamų skaičių, todėl šiuo atveju duomenų dydis papildomas ir maksimalia rikiuojamų skaičių reikšme.


Kaip įvertinti algoritmo sudėtingumą
------------------------------------

.. todo:: Žemiau sutvarkyti nuorodą į knygą.

Natūralus būdas įvertinti algoritmo sudėtingumą -- apskaičiuoti, kiek elementarių veiksmų (aritmetinių operacijų, kreipimųsi į atmintį) jis atlieka. Susitarsime, kad visi elementarūs veiksmai įvykdomi vienodai greitai [2]. Žinodami, kiek vidutiniškai elementarių veiksmų per sekundę atlieka kompiuteris, galėsime įvertinti vykdymui reikalingą laiką. Panagrinėkime programos fragmentą, randantį kvadratinėje :math:`n \times n` lentelėje surašytų skaičių sumą, ir suskaičiuokime atliekamų elementarių veiksmų skaičių.

.. code-block:: pascal

    suma := 0;                      // atliekamas vieną kartą
    read(n);                        // vieną kartą
    for i := 1 to n do              // n kartų
        for j := 1 to n do begin    // n^2 kartų
            read(a);                // n^2 kartų
            suma := suma + a;       // n^2 kartų (priskyrimas ir sumavimas)
        end;
    writeln(suma);                  // vieną kartą

Elementarių veiksmų skaičius lygus :math:`1 + 1 + n + n^2 + n^2 + 2n^2 + 1 = 4n^2 + n + 3`. Jį nusako funkcija :math:`f(n) = 4n2 + n + 3`. Tai ir yra šio fragmento sudėtingumas laiko atžvilgiu.

Jei paimtumėte kurią nors savo programą ir pabandytumėte pakartoti šiuos žingsnius, tikriausiai susiimtumėte už galvos! Kaip skaičiuoti, jei programoje yra ciklas ``while`` ar naudojama rekursija, jei priklausomai nuo įvairių sąlygų vieną kartą atliekami vieni, o kitą -- kiti veiksmai.

Panagrinėkime kurį nors rikiavimo algoritmą. Jei pradiniai duomenys sudaro surikiuotą seką, tikriausiai bus atliekama mažiau veiksmų, negu rikiuojant atsitiktinę seką. Tad atliekamų elementarių veiksmų skaičius gali priklausyti ne tik nuo pradinių duomenų kiekio, bet ir nuo pačių duomenų.

Dėl šių priežasčių dažnai skaičiuojama, kiek veiksmų bus atliekama blogiausiu atveju, t. y. kiek *daugiausiai* elementarių veiksmų gali tekti atlikti vykdant algoritmą.

Kiekvienos programos veikimą nusakys vis kitokia funkcija. Tiksliai suskaičiuoti elementarių veiksmų kiekį didesnėms programoms būtų sudėtinga. Laimei, to daryti neteks! Panagrinėkime, kaip didėjant :math:`n` auga kiekvienas iš dėmenų. Kai :math:`n = 1`, dėmenys lygūs 4, 1 ir 3, kai :math:`n = 10`, jie atitinkamai lygūs 400, 10 ir 3, kai :math:`n = 1000`, gauname 4 000 000, 1000 ir 3. Matome, kad didėjant :math:`n` labiausiai didėja tik pirmasis dėmuo, o kiti dėmenys -- labai nežymiai. Kadangi kiekvienas dėmuo tiesiogiai reiškia elementarių veiksmų skaičių, du mažesniuosius dėmenis galime atmesti. Laikas, sugaištas atlikti 1003 veiksmams, yra nereikšmingas palyginti su laiku, reikalingu atlikti keturiems milijonams veiksmų.

Taigi, augant pradiniams duomenims (:math:`n`), algoritmo atliekamų elementarių veiksmų skaičius vis labiau priklausys nuo greičiausiai augančio funkcijos dėmens, t. y. nuo :math:`4n^2`. Natūralu vietoj funkcijos :math:`f(n) = 4n^2 + n + 3` toliau nagrinėti paprastesnę funkciją :math:`g(n) = 4n^2`.

Tai dar ne viskas. Padidinus :math:`n` dešimt kartų, vykdymo laikas padidės šimtąkart. Palyginus su tuo, vykdymo laiko padidėjimas keturis kartus yra neesminis. Taigi galime atmesti konstantą prie :math:`n^2` ir tarti, kad elementarių veiksmų skaičių pakankamai gerai nusako dar paprastesnė funkcija :math:`h(n) = n^2`.

Mokslininkai rašytų, kad nagrinėto programos fragmento sudėtingumas yra :math:`O(n^2)`. Mat visur, kur kalbama apie algoritmų sudėtingumą, naudojamas didžiosios :math:`O` žymėjimas.


Didžiosios :math:`O` žymėjimas
------------------------------

Formaliai algoritmo sudėtingumas apibrėžiamas taip:

    Tarkime, pradinių duomenų dydis yra :math:`n`, o algoritmo atliekamų elementarių veiksmų skaičius -- :math:`g(n)`. Sakysime, jog algoritmo sudėtingumas yra :math:`O(f(n))` (rašome :math:`g(n) = O(f(n))`), jei egzistuoja tokie skaičiai :math:`c` ir :math:`n_0`, su kuriais visiems :math:`n > n_0` galioja nelygybės: :math:`0 \le g(n) \le c \cdot f(n)`.

.. todo:: Sutvarkyti nuorodą į paveikslą.

Geriau suprasti šį apibrėžimą padės 2 paveiksle pateikti funkcijų :math:`f` ir :math:`g` grafikai.

Šis formalus apibrėžimas reiškia, kad, augant :math:`n`, funkcija :math:`g(n)` auga ne sparčiau nei funkcija :math:`f(n)`.

Sutartiniu didžiosios :math:`O` žymėjimu paprastai parodoma, kaip elgsis algoritmas didėjant pradiniams duomenims, t. y. kaip augs algoritmui reikalingos atminties dydis arba vykdymo laikas.

Panagrinėkime dar keletą pavyzdžių:

* :math:`3n2 + 2n + 20 = O(n2)`,
* :math:`n + 10 000 = O(n)`,
* :math:`n + 10 000 = O(n2)` (pagal apibrėžimą teisingas teiginys, tačiau parankesnė praeita lygybė),
* :math:`2n + n10 = O(2n)`.

Jei algoritmo sudėtingumas nepriklauso nuo duomenų kiekio (t. y. jis pastovus, konstantinis), tai jį žymėsime :math:`O(1)`. Pavyzdžiui, atminties, kurią naudoja nagrinėtas programos fragmentas, dydis lygus :math:`O(1)`.

Pradinių duomenų dydį gali nusakyti ne vienas, o keli kintamieji. Tokiu atveju didžiosios :math:`O` žymėjimas aprašo sudėtingumo augimą didėjant visiems parametrams. Pavyzdžiui, galimi tokie algoritmo sudėtingumo variantai: :math:`O(2n+m)`, :math:`O(L^2W + W^2L)`.

.. todo:: Sutvarkyti išnašas žemiau.

Nusakant algoritmų sudėtingumą dažnai teks susidurti su šiomis funkcijomis:
:math:`O(1)` (konstantinis), :math:`O(\log n)` (logaritminis [3]), :math:`O(\sqrt(n))` (šakninis[4]), :math:`O(n)` (tiesinis), :math:`O(n \log n)`, :math:`O(n^2)` (kvadratinis), :math:`O(n^3)` (kubinis), :math:`O(2^n)` (eksponentinis), :math:`O(n!)` (faktorialinis[5]).


Kaip tai pritaikyti olimpiadoje
-------------------------------

Olimpiadose ribojamas programų veikimo laikas ir naudojamoji atmintis. Taigi apmąstant įvairius sprendimo būdus reikia mokėti įvertinti, ar programa bus pakankamai efektyvi (ar suspės įveikti uždavinį su visais pradiniais duomenimis per leistiną laiką). Tačiau kiek gi veiksmų gali atlikti kompiuteris per, pavyzdžiui, vieną sekundę? Tai priklauso nuo daugelio dalykų: nuo procesoriaus, kompiliatoriaus, pačių veiksmų, kuriuos programa atlieka. Atliekamų veiksmų skaičių mums padės įvertinti paprasta programa:

.. code-block:: pascal

    uses windows;

    var pradzia, veiksmuSk : longint;

    begin
        veiksmuSk := 0;
        pradzia := GetTickCount;
        while GetTickCount - pradzia < 1000 do
            inc(veiksmuSk);
        writeln(veiksmuSk);
    end.

Ši programa suskaičiuoja, kiek elementarių veiksmų kompiuteris gali atlikti per vieną sekundę (suprantama, jei programą pradėjote ir baigėte vykdyti tą pačią parą). Be abejo, matavimai nėra visiškai tikslūs, tačiau jų pakanka įvertinti kompiuterio spartai.

Taigi tarkime, kad duomenų dydis yra :math:`n`, :math:`O(f(n))` sudėtingumo algoritmas atlieka lygiai :math:`f(n)` elementarių veiksmų, o atlikę pateiktą programą įvertinome, kad kompiuteris per 1 sekundę atlieka :math:`10^9` tokių veiksmų. Sudarykime lentelę, atspindinčią, kiek laiko trunka įvairaus sudėtingumo algoritmų vykdymas su įvairiais pradiniais duomenimis.

.. todo:: Pertikrinti šitą lentelę su matematika.
          Pagalvoti apie alternatyvą šitai lentelei.


====================  ==========  ==========  ===========================  ===========================  ============  ============  ===========================
:math:`n`             :math:`10`  :math:`20`  :math:`30`                   :math:`100`                  :math:`1000`  :math:`10^6`  :math:`10^9`
====================  ==========  ==========  ===========================  ===========================  ============  ============  ===========================
:math:`O(1)`          ~0          ~0          ~0                           ~0                           ~0            ~0            ~0
:math:`O(\log_2 n)`   ~0          ~0          ~0                           ~0                           ~0            ~0            ~0
:math:`O(\sqrt{n})`   ~0          ~0          ~0                           ~0                           ~0            ~0            ~0,03 ms
:math:`O(n)`          ~0          ~0          ~0                           ~0                           ~0            ~1 ms         ~1 s
:math:`O(n log_2 n)`  ~0          ~0          ~0                           ~0                           ~0            ~20 ms        ~30 s
:math:`O(n^2)`        ~0          ~0          ~0                           ~0                           ~1 ms         ~17 min       ~32 metai
:math:`O(n^3)`        ~0          ~0          ~0.03 ms                     ~1 ms                        ~1 s          ~32 metai     :math:`~32 \cdot 10^9` metų
:math:`O(2^n)`        ~0          ~1 ms       ~1 s                         :math:`~4 \cdot 10^13` metų  –             –             –
:math:`O(n!)`         ~4 ms       ~77 metai   :math:`~8 \cdot 10^15` metų  –                            –             –             –
====================  ==========  ==========  ===========================  ===========================  ============  ============  ===========================

Sunku patikėti, bet tai tiesa: naivus skaičių rikiavimo algoritmas, kuris bando visus įmanomus skaičių išdėstymo būdus (tokių yra :math:`n!`), ir tikrina, ar gautoji skaičių seka yra didėjanti, dvidešimt skaičių „rikiuotų“ daug metų. Toks algoritmas, žinoma, yra neefektyvus.

Efektyviais laikomi polinominio sudėtingumo algoritmai, t. y. tokie, kurių sudėtingumo funkcija yra polinomas -- :math:`O(n^k)`. Pirmieji septyni lentelėje pateikti sudėtingumai yra polinominiai, taigi laikomi efektyviais. Algoritmai, kurių sudėtingumas nepolinominis, laikomi neefektyviais. Tokie yra eksponentinio (pavyzdžiui, :math:`O(2^n)`) ir faktorialinio (:math:`O(n!)`) sudėtingumo algoritmai.

Šią lentelę verta įsidėmėti. Olimpiados metu, sugalvoję uždavinio sprendimą, galime įvertinti jo sudėtingumą ir patikrinti, ar to užteks pradiniams duomenims įveikti per leistiną laiką. Įgijus patirties, algoritmo sudėtingumą dažnai nesunku įvertinti pažvelgus į algoritmo struktūrą: kokie jame yra ciklai, kokie rekursiniai kreipiniai ir panašiai.

Dar daugiau: matydami, jog uždavinio pradiniai duomenys labai maži, žinome, kad pakaks ir neefektyvaus algoritmo uždaviniui spręsti. Ir atvirkščiai: jei uždavinio pradiniai duomenys yra dideli, o leistinas programos veikimo laikas -- mažas, reikia ieškoti efektyvaus būdo, kaip spręsti šį uždavinį.

Beje, beveik visose programose 90% laiko sugaištama vykdant 10% kodo. Ir likusių 90% kodo optimizavimas, deja, neturės didelės įtakos programos efektyvumui. Tad prieš imantis optimizuoti kurią nors algoritmo dalį reikia įsitikinti, ar verta tai daryti.
