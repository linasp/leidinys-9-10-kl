Pirmasis algoritmas -- Euklido algoritmas didžiausiam bendrajam dalikliui rasti
===============================================================================

    Kartą mokinys, išmokęs savo pirmąją geometrijos teoremą, paklausė Euklido: „Kokia man nauda, kad šitai išmoksiu?“. Euklidas pakvietė savo vergą ir tarė: „Duok šiam žmogui drachmą, nes jis turi turėti naudos iš to, ką išmoksta.“

    -- J. Stobijus (Joannes Stobaeus), V a. pr. Kr.

Šiame skyrelyje susipažinsime su seniausiu netrivialiu algoritmu, išlikusiu iki šių dienų. Tai algoritmas didžiausiam bendrajam dalikliui rasti. Nėra žinoma, kas šį algoritmą sugalvojo (ir ar tai buvo vienas žmogus). Dar prieš Euklidui (graikų k. Eukleidhx, *Eukleides*) aprašant šį algoritmą, jį savo veikale cituoja Aristotelis. Euklidas algoritmą kruopščiai aprašė garsiajame veikale *„Pradmenys“* (apie 300 m. pr. Kr.), todėl algoritmui ir prigijo Euklido vardas.



Didžiausias bendrasis daliklis ir mažiausias bendrasis kartotinis
-----------------------------------------------------------------

Prisiminkime *didžiausio bendrojo daliklio* (DBD) ir *mažiausio bendrojo kartotinio* (MBK) sąvokas.

Sakome, kad skaičius :math:`a` dalija skaičių :math:`b`, jei egzistuoja toks sveikasis skaičius :math:`k`, kad :math:`b = ka` (žymima :math:`a|b`).

Pavyzdžiui, :math:`5|30`, nes :math:`30 = 6 \cdot 5`. Skaičius 1 dalija visus skaičius (:math:`1|a`, visiems sveikiesiems :math:`a`), o skaičių 0 dalija visi skaičiai, išskyrus patį 0 (:math:`a|0`, visiems sveikiesiems :math:`a`, :math:`a \neq 0`).

Dviejų neneigiamų skaičių :math:`a` ir :math:`b` didžiausiu bendruoju dalikliu (DBD) vadinamas didžiausias skaičius, dalijantis :math:`a` ir :math:`b`. Pavyzdžiui, :math:`DBD(12, 8) = 4`, :math:`DBD(3, 6) = 3`, :math:`DBD(7, 9) = 1`.

Neneigiamų skaičių :math:`a` ir :math:`b` mažiausiu bendruoju kartotiniu (MBK) vadinamas mažiausias teigiamas skaičius, kurį dalija :math:`a` ir :math:`b`. Pavyzdžiui, :math:`MBK(12, 8) = 24`, :math:`MBK(3, 6) = 6`, :math:`MBK(7, 9) = 63`.

Natūralus būdas rasti :math:`DBD(a, b)` -- išskaidyti skaičius :math:`a` ir :math:`b` pirminiais daugikliais ir išrinkti visus bendruosius šių skaičių pirminius daugiklius. Pavyzdžiui, :math:`12 = 2 \cdot 2 \cdot 3`, :math:`8 = 2 \cdot 2 \cdot 2`, bendrieji daugikliai yra :math:`2 \cdot 2`, taigi :math:`DBD(12, 8) = 4`. Šiuo būdu tarsi konstruojame DBD, stengdamiesi jį padaryti kuo didesnį (rinkdami kuo daugiau skaičiaus a pirminių daugiklių), tačiau žiūrėdami, kad DBD dalytų ir skaičių :math:`b`.

:math:`MBK(a, b)` taip pat galime rasti išskaidę skaičius :math:`a` ir :math:`b` į pirminius daugiklius. Kadangi :math:`a|MBK(a, b)`, tai MBK turi priklausyti visi a pirminiai daugikliai. Tačiau ir :math:`b|MBK(a, b)`, todėl pridedame skaičiaus :math:`b` pirminius daugiklius, kurių trūksta (būtent,  daugiklius, kurie nėra bendrieji skaičiams :math:`a` ir :math:`b`). Pavyzdžiui, :math:`MBK(12, 8) = 2 \cdot 2 \cdot 3 \cdot 2 = 24`.

Šie DBD ir MBK konstravimo būdai paaiškina ir šiuos skaičius siejančią lygybę: :math:`DBD(a, b) \cdot MBK(a, b) = a \cdot b`.


Euklido algoritmas
------------------

    *An algorithm must be seen to be believed.*

    Algoritmą reikia pamatyti, kad juo patikėtum.

    -- Donaldas Knutas (Donald Knuth)

Tarkime, reikia rasti skaičių a ir b didžiausiąjį bendrą daliklį. Atliekame tokius veiksmus:

* jei :math:`b = 0`, tai :math:`DBD(a, b)` lygus :math:`a`, priešingu atveju :math:`a_2 = b`, :math:`b_2 = a mod b` (lygus liekanai, gautai padalijus :math:`a` iš :math:`b`)
* jei :math:`b_2 = 0`, tai :math:`DBD(a, b)` lygus :math:`a_2`, priešingu atveju :math:`a_3 = b_2`,:math:`b_3 = a_2 mod b_2` 
* ...
* jei :math:`b_k = 0`, tai :math:`DBD(a, b)` lygus :math:`a \cdot k`, priešingu atveju :math:`a \cdot k + 1 = b \cdot k`, :math:`b \cdot k + 1 = a \cdot k \mod b \cdot k`.

Kadangi dalydami iš skaičiaus :math:`n` galime gauti liekaną nuo 0 iki :math:`n - 1`, tai :math:`b > b_2 > \ldots > b_k > \ldots > b_n = 0`, ir algoritmas atliks baigtinį skaičių veiksmų (anksčiau ar vėliau :math:`b_i` taps lygus 0, tad algoritmas baigs darbą).

Raskime skaičių :math:`a = 12` ir :math:`b = 8` DBD naudodamiesi Euklido algoritmu:

* :math:`b > 0`, taigi skaičiuojame :math:`a_2 = b = 8`, :math:`b_2 = a \mod b = 12 \mod 8 = 4`.
* :math:`b_2 > 0`, taigi skaičiuojame :math:`a_3 = b_2 = 4`, :math:`b_3 = a_2 mod b_2 = 8 mod 4 = 0`.
* :math:`b_3 = 0`, taigi :math:`DBD(a, b) = a_3 = 4`.

Gavome :math:`DBD(12, 8) = 4`. Užrašysime Euklido algoritmą Paskalio kalba:

.. code-block:: c++

    int DBD(int a, int b)
    {
        int c = a;
        while (b > 0) {
            a = b;
            b = c % b;
            c = a;
        }
        return c;
    }

Jei reikia rasti dviejų skaičių DBD, tačiau nežinome, ar jie teigiami, funkciją iškviečiame perduodami skaičių modulius: ``DBD(abs(a), abs(b))``.

.. todo:: perrašyti lygybę žemiau.

Euklido algoritmas yra teisingas, nes remiasi sąryšiu: :math:`DBD(a, b) = DBD(b, a \mod b)`. Šio sąryšio teisingumu nesunku įsitikinti pasinaudojus lygybe: :math:`a = (a div b) · b + a mod b`.

Du skaičiai turi vieną ir tik vieną didžiausiąjį bendrą daliklį. Tarkime, :math:`DBD (a, b) = d`. Daliklis :math:`d` dalija skaičių :math:`a` ir taip pat dalija jo dalį :math:`(a div b) · b`, todėl turi dalyti ir likusią skaičiaus :math:`a` dalį – :math:`a \mod b`. Taigi skaičių :math:`a` ir :math:`b` didžiausias bendrasis daliklis yra ir (mažesnių) skaičių poros :math:`b` ir :math:`a \mod b` didžiausias bendrasis daliklis, t. y. :math:`DBD(a, b) = d = DBD(b, a \mod b)`.

.. todo:: pasitikslinti pastraipą žemiau.

Pamėginkime įvertinti Euklido algoritmo sudėtingumą. Pasiremsime nelygybe :math:`n \mod m < \frac{n}{2}`, kur :math:`n` ir :math:`m` -- sveikieji neneigiami skaičiai ir :math:`n \ge m`.
Nelygybė teisinga, nes:

* jei :math:`m \le frac{n}{2}`, tuomet :math:`n mod m < m \le n/2`;
* jei :math:`m > frac{n}{2}`, tuomet :math:`n div m = 1`; tada lygybę :math:`n = (n div m) m + n mod m` perrašome: :math:`n = m + n mod m`; gauname :math:`n mod m = n – m < n – n/2 = n/2`.

Tarkime, kad :math:`a > b` (jei taip nėra, tai atliekant ciklą pirmąjį kartą, šie skaičiai bus sukeisti vietomis). Ciklo viduje atliekamas operacijas galime laikyti elementariomis, tad Euklido algoritmo sudėtingumas tiesiog proporcingas tam, kiek kartų bus atliekamas ciklas while.

.. todo:: pasitikslinti latex logaritmų ir mod sintaksę.

Panagrinėkime, kaip keičiasi kintamųjų :math:`a` ir :math:`b` reikšmės vykdant while ciklą. Sakykime, pradinės šių kintamųjų reikšmės yra :math:`a_0` ir :math:`b_0`. Po pirmos ciklo iteracijos :math:`a_1 = b_0`, o :math:`b_1 = a_0 \mod b_0 < frac{a_0}{2}`. Po antros iteracijos :math:`a_2 = b_1 < frac{a_0}{2}`, o :math:`b_2 = a_1 \mod b_1 < a_2`. Gavome, kad atlikus dvi ciklo iteracijas, pirmojo kintamojo reikšmė sumažėja daugiau negu dvigubai ir dar vis galioja :math:`a \ge b`. Po keturių iteracijų pirmojo kintamojo reikšmė bus daugiau nei keturis kartus mažesnė už pradinę ir t. t. Taigi matyti, kad ciklas bus vykdomas ne daugiau kaip :math:`2 \cdot \log a` kartų. Dabar jau nesunku įvertinti, kad Euklido algoritmo sudėtingumas yra :math:`O(\log a)`.

Kadangi Euklido algoritmas apibrėžiamas rekurentiniais sąryšiais:
* :math:`DBD(a, b) = a`, jei :math:`b = 0` 
* :math:`DBD(a, b) = DBD(b, a \mod b)`, jei :math:`b > 0` 
tai Euklido algoritmą nesunku užrašyti rekursyvia [#rekursyvia]_ funkcija:

.. code-block:: c++

    int DBD(int a, int b)
    {
        if (b == 0)
            return a;
        else
            return DBD(b, a % b);
    }

Pastebėkime, kad jei :math:`a < b`, algoritmas pirmu žingsniu šiuos skaičius sukeičia vietomis, pavyzdžiui, :math:`DBD(24, 54) = DBD(54, 24) = DBD(24, 6) = DBD(6, 0) = 6`.

Beje, pats Euklidas šį algoritmą aprašė kiek kitaip. Mat graikų matematikai nelaikė, kad vienetas dalija kitą teigiamą skaičių. Buvo galimi trys variantai: arba du teigiami sveikieji skaičiai yra abu lygūs vienetui, arba tarpusavyje pirminiai, arba turi bendrą didžiausią daliklį. Vienetas netgi nebuvo laikomas skaičiumi, o nulis apskritai neegzistavo.


Euklido algoritmo taikymas, mažiausio bendrojo kartotinio (MBK) radimas
-----------------------------------------------------------------------

Didžiausiojo bendrojo daliklio gali prireikti sprendžiant įvairius skaičiavimo uždavinius. Vienas iš pavyzdžių -- prastinant trupmenas, skaitiklį ir vardiklį reikia padalyti iš didžiausio jų bendrojo daliklio.

Euklido algoritmas leidžia efektyviai apskaičiuoti ir mažiausią bendrąjį kartotinį:

.. todo:: sutvarkyti išnašą.
.. todo:: dalyba prieš daugybą (paaiškinti?).

.. code-block:: c++

    int MBK(int a, int b)
    {
        return a / DBD(a, b) * b;
    }

Naudodamiesi Euklido algoritmu galime rasti ne tik dviejų, bet ir keleto skaičių DBD bei MBK. Kadangi :math:`DBD(a, b, c) = DBD(DBD(a, b), c)`, ir :math:`MBK(a, b, c) = MBK(MBK(a, b), c)`. Šias lygybes suprasti ir įrodyti nesunku įsivaizduojant, kaip konstruotume DBD ir MBK iš skaičių :math:`a`, :math:`b` ir :math:`c` pirminių daugiklių.

Tarkime, masyve :math:`m` yra :math:`k` sveikųjų skaičių. Pateiksime fragmentą, randantį visų :math:`k` skaičių DBD ir MBK:

.. code-block:: c++

    visuDBD = 0; // po pirmo žingsnio taps lygiu m[1]
    for (int i = 1; i <= k; i++)
        visuDBD = DBD(abs(m[i]), visuDBD);
    visuMBK = 1; // po pirmo žingsnio taps lygiu m[1]
    for (int i = 1; i <= k; i++)
        visuMBK = MBK(abs(m[i]), visuMBK);


.. todo:: pataisyti nuorodas į skyrius žemiau.

.. rubric:: Išnašos

.. [#rekursyvia] Su rekursija išsamiai susipažinsime 4 skyriuje.
