# Clark Hall: TEI \+ RDFa modelling

This document connects selected Clark Hall entries in TEI with proposed morphological descriptions expressed through RDFa.

## 1\. Scope

- Focus on verbs, including strong and weak verbs.  
- Begin with morphological forms cited in CH.  
- Use the latest available TEI and the current encoding policy as the baseline.  
- Distinguish information recorded in the dictionary from additional analysis.  
- &nbsp;

## 2\. Materials

| Title | Link |
| :---- | :---- |
| Latest TEI input for enrichment | (fixing a few things, will parse the whole dictionary shortly) |
| Current TEI encoding policy | [CAS and SWEET encoding policy.ipynb](https://drive.google.com/open?id=1CBBjcU-5Jip4t3y22ygM66-_Nu0li-qp) |
| Existing Modelling Document | [Modelling Document](https://docs.google.com/document/u/0/d/1WqetwdEJPn5fM6HpVnzyZgzIw51ykNU8GsDg_QQ8uLA/edit) |
| Existing research questions document | [Research Questions](https://docs.google.com/document/u/0/d/1-WVl-zcK3Ahe-oMSl_leAN53qX54Kes7TEhpEhkMTHU/edit) |
| Verb spreadsheet | [CH Verb classes spreadsheet](https://docs.google.com/spreadsheets/d/1gi1RXsZjCGHZpJRpHfiLiG9XH7oEzBxA0ZWPxILDiIA/edit?usp=sharing) |
| Existing RDFa prototype | [Existing TEI \+ RDFa prototype](https://github.com/Serg078/Conversion-of-The-Clark-Hall-Dictionary-of-Old-English-to-TEI)&nbsp; |
| Existing interface | [Live dictionary and SPARQL interface](https://clark-hall-tei-rdfa.netlify.app/) |
| New enrichment repository | (creating shortly) |

&nbsp;

## 3\. Worked examples

### E01 — lācan

```
lācan^7 pret. 3 sg. leolc _to move up and down, leap, jump, swing, fly_,
_Jul_: _play (instrument)_: (†) _fight, contend_, _B_: (+) _incite to_,
AO: _be rewarded_. [‘_lake_’]
```

#### A. Current automatically generated TEI

```xml
<entry xml:id="CAS2.lācan" type="mainEntry" xml:lang="ang">
        <form type="lemma">
          <orth>lācan</orth>
        </form>
        <gramGrp>
          <gram type="pos" value="strong verb"/>
          <gram type="inflectionType">
            <hi rend="superscript">7</hi>
          </gram>
        </gramGrp>
        <form type="inflected">
          <gramGrp>
            <gram type="pos" value="verb"/>
            <gram type="tense" value="preterite">pret.</gram>
            <gram type="person" value="third">3</gram>
            <gram type="number" value="singular">sg.</gram>
          </gramGrp>
          <orth>leolc</orth>
        </form>
        <sense xml:id="CAS2.lācan.1">
          <sense xml:id="CAS2.lācan.1.1">
            <cit type="translationEquivalent" xml:lang="en">
              <quote>to move up and down, leap, jump, swing, fly,</quote>
              <bibl type="attestation" source="#Jul">
                <title>Jul</title>
              </bibl>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.2">
            <cit type="translationEquivalent" xml:lang="en">
              <quote>play</quote>
              <gloss>(instrument)</gloss>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.3">
            <usg type="textType" norm="attested in poetic texts only">†</usg>
            <cit type="translationEquivalent" xml:lang="en">
              <quote>fight, contend,</quote>
              <bibl type="attestation" source="#B">
                <title>B</title>
              </bibl>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.4">
            <form type="variant">
              <orth expand="ge-lācan">
                <lbl expand="ge-">(+)</lbl>
              </orth>
            </form>
            <cit type="translationEquivalent" xml:lang="en">
              <quote>incite to,</quote>
              <bibl type="attestation" source="#AO">
                <title>AO</title>
              </bibl>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.5">
            <cit type="translationEquivalent" xml:lang="en">
              <quote>be rewarded</quote>
            </cit>
          </sense>
        </sense>
        <etym>
          <pc>[</pc>
          <xr type="related">
            <ref type="entry" target="OED_lake">'lake'</ref>
          </xr>
          <pc>]</pc>
        </etym>
        <metamark>.</metamark>
      </entry>
```

&nbsp;

#### B. TEI+RDFa

```xml
<entry xmlns="http://www.tei-c.org/ns/1.0"
       xml:id="CAS2.lācan" type="mainEntry" xml:lang="ang"
       prefix="ontolex: http://www.w3.org/ns/lemon/ontolex#
               lexinfo: http://www.lexinfo.net/ontology/3.0/lexinfo#
               chm: https://example.org/chm#"
       about="https://example.org/ch/lacan"
       typeof="ontolex:LexicalEntry chm:StrongVerbVII">
        <form type="lemma"
              rel="ontolex:canonicalForm"
              resource="https://example.org/ch/lacan#lemma"
              typeof="ontolex:Form">
          <orth property="ontolex:writtenRep">lācan</orth>
        </form>
        <gramGrp>
          <gram type="pos" value="strong verb"
                property="lexinfo:partOfSpeech" resource="lexinfo:verb"/>
          <gram type="inflectionType">
            <hi rend="superscript">7</hi>
          </gram>
        </gramGrp>
        <form type="inflected"
              rel="ontolex:otherForm"
              resource="https://example.org/ch/lacan#leolc-pret-3sg"
              typeof="ontolex:Form">
          <gramGrp>
            <gram type="pos" value="verb"/>
            <gram type="tense" value="preterite"
                  property="lexinfo:tense" resource="lexinfo:past">pret.</gram>
            <gram type="person" value="third"
                  property="lexinfo:person" resource="lexinfo:thirdPerson">3</gram>
            <gram type="number" value="singular"
                  property="lexinfo:number" resource="lexinfo:singular">sg.</gram>
          </gramGrp>
          <orth property="ontolex:writtenRep">leolc</orth>
        </form>
        <sense xml:id="CAS2.lācan.1">
          <sense xml:id="CAS2.lācan.1.1">
            <cit type="translationEquivalent" xml:lang="en">
              <quote>to move up and down, leap, jump, swing, fly,</quote>
              <bibl type="attestation" source="#Jul">
                <title>Jul</title>
              </bibl>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.2">
            <cit type="translationEquivalent" xml:lang="en">
              <quote>play</quote>
              <gloss>(instrument)</gloss>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.3">
            <usg type="textType" norm="attested in poetic texts only">†</usg>
            <cit type="translationEquivalent" xml:lang="en">
              <quote>fight, contend,</quote>
              <bibl type="attestation" source="#B">
                <title>B</title>
              </bibl>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.4">
            <form type="variant">
              <orth expand="ge-lācan">
                <lbl expand="ge-">(+)</lbl>
              </orth>
            </form>
            <cit type="translationEquivalent" xml:lang="en">
              <quote>incite to,</quote>
              <bibl type="attestation" source="#AO">
                <title>AO</title>
              </bibl>
            </cit>
          </sense>
          <metamark function="senseSeparator">:</metamark>
          <sense xml:id="CAS2.lācan.1.5">
            <cit type="translationEquivalent" xml:lang="en">
              <quote>be rewarded</quote>
            </cit>
          </sense>
        </sense>
        <etym>
          <pc>[</pc>
          <xr type="related">
            <ref type="entry" target="OED_lake">'lake'</ref>
          </xr>
          <pc>]</pc>
        </etym>
        <metamark>.</metamark>
      </entry>
```

C. Extracted RDF and query result

```
@prefix ex: <https://example.org/ch/> .
@prefix f: <https://example.org/ch/lacan#> .
@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#> .
@prefix chm: <https://example.org/chm#> .

ex:lacan a ontolex:LexicalEntry, chm:StrongVerbVII ;
    lexinfo:partOfSpeech lexinfo:verb ;
    ontolex:canonicalForm f:lemma ;
    ontolex:otherForm f:leolc-pret-3sg .

f:lemma a ontolex:Form ;
    ontolex:writtenRep "lācan"@ang .

f:leolc-pret-3sg a ontolex:Form ;
    ontolex:writtenRep "leolc"@ang ;
    lexinfo:tense lexinfo:past ;
    lexinfo:person lexinfo:thirdPerson ;
    lexinfo:number lexinfo:singular .
```

&nbsp;

**Question:** Which forms belong to a class VII verb and are past, third person and singular?

```
PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
PREFIX lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#>
PREFIX chm: <https://example.org/chm#>

SELECT ?lemma ?form
WHERE {
  ?entry a chm:StrongVerbVII ;
         ontolex:canonicalForm/ontolex:writtenRep ?lemma ;
         ontolex:otherForm ?f .
  ?f ontolex:writtenRep ?form ;
     lexinfo:tense lexinfo:past ;
     lexinfo:person lexinfo:thirdPerson ;
     lexinfo:number lexinfo:singular .
}
```

&nbsp;

| lemma | form |
| :---- | :---- |
| lācan | leolc |

## 4\. Questions/discussion

| Topic | Question to resolve | Status |
| :---- | :---- | :---- |

&nbsp;

## 5\. ...