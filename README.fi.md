# Career Gap Navigator

**Lue tämä README eri kielellä:** [English](README.md) | [简体中文](README.zh-CN.md) | [Suomi](README.fi.md)

**Näyttöön perustuva työnhaun ja uramahdollisuuksien ohjaustyökalu, jota voi käyttää GitHub Agent Skill -taitona tai erillisenä kehotteena.**

Career Gap Navigator auttaa eri alojen työnhakijoita vertaamaan ansioluetteloaan **todellisiin, jäljitettävissä oleviin uramahdollisuuksiin**. Se erottaa toisistaan osoitetun osaamisen, ansioluettelosta puuttuvat tiedot ja taidot, joita olisi perusteltua kehittää. Työkalu esittää kohdennettuja tarkentavia kysymyksiä ja laatii vastausten perusteella oppimisvaihtoehtoja sekä henkilökohtaisen **30/60/90 päivän urakehityssuunnitelman**.

> **Pilottivaihe.** Saman hakijan eri CV-versioilla tehdyssä rajatussa vertailussa luokittelutulosten yhdenmukaisuus parani sääntöjen tarkentamisen jälkeen. Tämä **ei todista luokittelun oikeellisuutta** eikä työkalun soveltuvuutta kaikkiin ammatteihin. Koko työnkulkua, mukaan lukien tutkimusrahoitusmahdollisuuksien ja koulutusten suosittelu, ei ole vielä arvioitu laajasti todellisilla käyttäjillä.

## Kaksi käyttötapaa

**1. Agent Skill.** Repositorio sisältää tiedoston `.github/skills/career-gap-navigator/SKILL.md` sekä siihen liittyvät ohjeet. Taitoa voi käyttää yhteensopivassa Agent Skills -ominaisuutta tukevassa tekoäly-ympäristössä, esimerkiksi tuetussa GitHub Copilot -ympäristössä. Se, milloin taito otetaan käyttöön, riippuu käytetystä agentista. **Repositorion lataaminen GitHubiin ei automaattisesti asenna taitoa ChatGPT:hen.** Katso [GitHubin ohjeet](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) ja [Agent Skills -määritys](https://agentskills.io/specification).

**2. Erillinen keskustelukehote.** Avaa [`Career Gap Navigator.txt`](Career%20Gap%20Navigator.txt), aloita uusi keskustelu, liitä mukaan ansioluettelo ilman tarpeettomia henkilötietoja ja kopioi koko kehote keskusteluun. Tiedosto sisältää projektiin toimitetun uusimman kehotteen **sanatarkasti** ja toimii Skill-paketin ensisijaisena sääntölähteenä. Erillistä testikehotetta tai valmista työpaikkailmoitusaineistoa ei tarvita.

## Mitä käyttäjän on annettava?

| Pakollinen tieto (kysytään vain, jos se puuttuu) | Selitys |
|---|---|
| `CV` | Ajantasainen ansioluettelo ilman tarpeettomia henkilötietoja tai riittävän kattava CV-teksti |
| `Target occupation` | Käyttäjän itse valitsema tavoiteammatti tai urasuunta |
| `Preferred location` | Maa/alue ja etätyötoiveet; rahoitushauissa tarvittaessa myös suunnitellun vastaanottavan organisaation sijainti |
| `Target level` | Aloitteleva / keskitason / kokenut / alanvaihtaja / epävarma (`entry-level / mid-level / senior / career changer / unsure`) |

**Käyttäjän ei tarvitse toimittaa työpaikkailmoituksia tai hakuilmoituksia, jos verkkohaku on käytettävissä.** Työkalu hakee aidot lähteet automaattisesti vahvistettujen tavoitteiden perusteella. Jos verkkohaku ei ole käytettävissä eikä luettavaa alkuperäistä lähdettä ole, työkalu pyytää yhden todellisen työpaikka- tai rahoitushakuilmoituksen ja odottaa vastausta. Opiskeluun käytettävä aika, budjetti, kielet sekä verkko- tai lähiopetuksen toiveet ovat vapaaehtoisia tietoja.

## Millaisia mahdollisuuksia voidaan tarkastella?

Oletuksena etsitään **avoimia työpaikkoja**. Käyttäjän nimenomaisesta pyynnöstä tarkasteluun voidaan lisätä apurahoja, tutkimusrahoitusta, stipendejä tai muita ohjelmia. Kunkin mahdollisuustyypin **pakolliset kelpoisuusehdot ja kilpailulliset valintaperusteet** arvioidaan erikseen. **Rahoitushaku ei ole sama asia kuin työpaikkailmoitus.** Työkalu ei päättele tavoiteammattia pelkkien CV-avainsanojen perusteella eikä lisää rahoitushakuja käyttäjän pyytämättä.

## Kaksivaiheinen työnkulku

```text
CV + käyttäjän valitsema ammatti, sijainti ja tavoitetaso
                         ↓
Todellisten mahdollisuuksien haku (lähteet, päivät, hakutilanne)
                         ↓
Alustava näyttöarvio (yksi tunniste R-ID ja luokka / vaatimus)
                         ↓
3–5 tarkentavaa kysymystä; kukin koskee yhtä selkeää asiaa
                    PYSÄHDY JA ODOTA
                         ↓
Käyttäjän vastaukset (SELF-REPORTED, ellei erikseen todennettu)
                         ↓
Change Log: luokkamuutokset ja perustellusti ennallaan pysyneet luokat
+ päivitetty arvio kaikista alkuperäisistä R-ID-tunnisteista
                         ↓
Enintään 3 painopistettä; tarkistetut kurssit vain, jos perusteltua
                         ↓
30/60/90 päivän suunnitelma + 3–12 kk + seuraavat 7 päivää
```

Kuusi luokittelutunnusta ovat **samat kaikilla kielillä**: `ELIGIBILITY_BARRIER`, `STRENGTH`, `CONFIRMED_SKILL_GAP`, `CV_EVIDENCE_GAP`, `POTENTIAL_EXPERIENCE_GAP` ja `UNKNOWN`.

**Se, ettei ansioluettelossa mainita jotakin taitoa, ei todista taidon puuttumista.** Analyysin perustelujen, epävarmuuden käsittelyn ja ohjeiden yksityiskohtaisuuden on säilyttävä yhtä kattavina riippumatta vastauskielestä.

## Repositorion rakenne

```text
.github/skills/career-gap-navigator/
    SKILL.md
    references/
      opportunity-sourcing.md
      evidence-rules.md
      verification-and-changelog.md
      learning-and-roadmap.md
      output-templates.md
Career Gap Navigator.txt         # Itsenäinen kehote kokonaisuudessaan
README.md                        # English
README.zh-CN.md                  # 简体中文
README.fi.md                     # Suomi
.github/workflows/validate.yml  # Automaattiset rakenne- ja sääntötarkistukset
examples/acceptance-tests.md    # Ihmisen tekemät toimintatestit
examples/fictional-session.md   # Kuvitteellinen esimerkkikeskustelu
examples/source-coverage.md     # Kehotteen ja Skill-ohjeiden vastaavuus
examples/CHANGELOG.md           # Muutoshistoria
scripts/check_policy_sync.py    # Sääntöjen yhtenäisyystarkistus (ei verkkoa)
scripts/validate_privacy.py     # Julkaisun perustason tietosuojatarkistus
tests/test_skill_structure.py
...
```

## Paikalliset tarkistukset

Suorita repositorion juurihakemistossa:

```bash
python tests/test_skill_structure.py
python scripts/check_policy_sync.py
python scripts/validate_privacy.py
```

Skriptit tarkistavat rakenteen, keskeisten sääntöjen esiintymisen, ohjetiedostojen vastaavuuden ja joitakin ilmeisiä tietosuojariskejä. **Ne eivät osoita, että tekoäly noudattaa ohjeita kaikissa tilanteissa, että tietty kurssi on parhaillaan tarjolla tai että suositukset parantavat työllistymistä.** Kokeile myös [ihmisen arvioimia hyväksymistestejä](examples/acceptance-tests.md) erillisissä keskusteluissa synteettisillä tiedoilla tai tiedoilla, joiden käyttöön on saatu suostumus.

## Tietosuoja ja vastuullinen käyttö

- **Älä julkaise todellisten osallistujien ansioluetteloita, alkuperäisiä vastauksia, nimiä, yhteystietoja, rahoitushakemuksia, luottamuksellisia projektitietoja tai työnantajatietoja avoimessa repositoriossa.**
- Hakemiston `examples/` aineisto on kuvitteellista. Poista tarpeettomat henkilötunnisteet ennen verkkohakuja.
- Käyttäjän kertomat lisätiedot merkitään `SELF-REPORTED`, ellei niille ole riippumatonta vahvistusta.
- Älä keksi tietoja avoimista hauista, rahoituskelpoisuudesta, kurssimaksuista tai menestymistodennäköisyyksistä. Työkalu antaa uraohjausta, **ei virallisia pätevyysratkaisuja, oikeudellisia neuvoja tai työnantajan/rahoittajan päätöksiä**.

## Kehitysmenetelmä ja jatkokäyttö

Katso [Development Guide](docs/Development%20Guide.md), jossa kuvataan yleinen tietosuojan huomioiva kehotteen kehitysmenetelmä, sekä [GitHub-julkaisuohje](docs/Publish%20to%20GitHub.md). **Nämä kaksi täydentävää dokumenttia ovat toistaiseksi englanninkielisiä.**

## Lisenssi

Projekti julkaistaan **MIT-lisenssillä**. Katso täydelliset ehdot juurihakemiston [`LICENSE`](LICENSE)-tiedostosta. Käyttö, muokkaaminen ja edelleen jakaminen ovat sallittuja, kun tekijänoikeus- ja lisenssi-ilmoitus säilytetään lisenssiehtojen mukaisesti.
