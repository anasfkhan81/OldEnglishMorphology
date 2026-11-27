# Modelling Old English Strong Verbs in OntoLex-Lemon

## Introduction

The aim of this project is to use OntoLex-lemon, its Morphology module (Morph), and LexInfo to encode the morphological information contained in the Clark–Hall Old English dictionary as RDF. Our main objective overall is to use Semantic Web standards to make the morphological information contained in traditional lexicographic resources more machine-actionable, facilitating its querying, reuse and integration with other linguistic resources;  this is part of a wider project which seeks to make other kinds of linguistic similarly more accessible via Semantic Web technologies.

Further objectives include:

- Exploring interoperability with Paralex, including the possibility of working directly in Paralex and subsequently mapping the results into OntoLex-lemon.
- Integrating morphological information from other resources, in particular UniMorph.
- Exploring the use of RDF 1.2 to represent the provenance of morphological descriptions and classifications, including cases where different sources provide different analyses of the same lexical entry.

## Ontology of Old English Strong Verbs

We have developed a small OWL ontology (CHM) that extends OntoLex-lemon and LexInfo with classes and properties for the representation of Old English strong verb morphology.

The following prefixes are used in the ontology and the accompanying examples:

```turtle
@prefix chm:     <https://example.org/chm#> .
@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:     <http://www.w3.org/2002/07/owl#> .
@prefix chsample: <https://example.org/clarkhall/sample/> .
```

### The Basic Classes

The core class of the ontology is `chm:StrongVerb`, defined as a subclass of both `ontolex:LexicalEntry` and `lexinfo:Verb`.

```turtle
chm:StrongVerb a owl:Class ;
    rdfs:label "Strong verb (Clark–Hall morphology)"@en ;
    rdfs:subClassOf ontolex:LexicalEntry, lexinfo:Verb .
```

We define seven subclasses of `chm:StrongVerb`, corresponding to the seven traditional classes of Old English strong verbs.

```turtle
chm:StrongVerbI a owl:Class ;
    rdfs:label "Strong verb class I"@en ;
    rdfs:subClassOf chm:StrongVerb .

chm:StrongVerbII a owl:Class ;
    rdfs:label "Strong verb class II"@en ;
    rdfs:subClassOf chm:StrongVerb .

chm:StrongVerbIII a owl:Class ;
    rdfs:label "Strong verb class III"@en ;
    rdfs:subClassOf chm:StrongVerb .

chm:StrongVerbIV a owl:Class ;
    rdfs:label "Strong verb class IV"@en ;
    rdfs:subClassOf chm:StrongVerb .

chm:StrongVerbV a owl:Class ;
    rdfs:label "Strong verb class V"@en ;
    rdfs:subClassOf chm:StrongVerb .

chm:StrongVerbVI a owl:Class ;
    rdfs:label "Strong verb class VI"@en ;
    rdfs:subClassOf chm:StrongVerb .

chm:StrongVerbVII a owl:Class ;
    rdfs:label "Strong verb class VII"@en ;
    rdfs:subClassOf chm:StrongVerb .
```

We introduce further subclasses where necessary. Our intention is that the classification should be sufficiently granular for the members of each leaf-level class to share a characteristic morphological pattern.

The current class hierarchy is as follows:

```text
StrongVerb
├── StrongVerbI
├── StrongVerbII
│   ├── StrongVerbIIa
│   └── StrongVerbIIb
├── StrongVerbIII
│   ├── StrongVerbIIIa
│   ├── StrongVerbIIIb
│   ├── StrongVerbIIIc
│   ├── StrongVerbIIId
│   └── StrongVerbIIIe
├── StrongVerbIV
├── StrongVerbV
├── StrongVerbVI
└── StrongVerbVII
    ├── StrongVerbVIIa
    └── StrongVerbVIIb
```

### Describing Strong Verb Classes Using OWL Punning

In addition to classifying lexical entries, we want to be able to describe the morphological characteristics of the strong verb classes themselves, in particular their characteristic vowel series.

To this end, we make use of **OWL 2 punning**, which allows the same IRI to be used both as an OWL class and as an individual.

For example, `chm:StrongVerbI` can be used:

- As an OWL class whose instances are lexical entries belonging to strong verb class I.
- As an individual to which we can attach information concerning the characteristic vowel series of strong verb class I.

We have introduced four datatype properties for the latter purpose:

```turtle
chm:infinitive_vowel a owl:DatatypeProperty ;
    rdfs:label "infinitive vowel"@en .

chm:pret_sing_vowel a owl:DatatypeProperty ;
    rdfs:label "preterite singular vowel"@en .

chm:pret_pl_vowel a owl:DatatypeProperty ;
    rdfs:label "preterite plural vowel"@en .

chm:past_part_vowel a owl:DatatypeProperty ;
    rdfs:label "past participle vowel"@en .
```

These properties correspond to the four principal forms traditionally used to describe the vowel alternations of Old English strong verbs.

For example, the characteristic vowel series of strong verb class I can be represented as follows:

```turtle
chm:StrongVerbI a owl:NamedIndividual ;
    chm:infinitive_vowel "ī" ;
    chm:pret_sing_vowel "ā" ;
    chm:pret_pl_vowel "i" ;
    chm:past_part_vowel "i" .
```

This approach allows us to represent both the classification of individual verbs and the morphological characteristics of the classes themselves without introducing a separate set of identifiers for the latter.

It should be noted that, under OWL 2 punning, the class and individual interpretations of an IRI are semantically independent. The properties associated with a strong verb class as an individual are therefore not automatically inherited by the lexical entries that instantiate that class.

The vowel-series properties have been defined in the current ontology; their systematic population for all classes and subclasses remains work in progress.

### Representing Paradigm Cells and Morphological Variants

A lexical entry may have more than one form corresponding to a particular combination of grammatical features, i.e. more than one form occupying the same cell in its inflectional paradigm.

In order to explicitly represent the relationship between such forms, we introduce a new object property, `chm:cellmate`.

```turtle
chm:cellmate a owl:ObjectProperty, owl:SymmetricProperty ;
    rdfs:label "cellmate"@en ;
    rdfs:domain ontolex:Form ;
    rdfs:range ontolex:Form ;
    rdfs:comment "Relates two distinct morphological forms that occupy the same cell in the inflectional paradigm of a lexical entry, irrespective of their orthographic or phonological differences."@en .
```

The property is symmetric: if form A is a cellmate of form B, then form B is also a cellmate of form A.

The property is deliberately underspecified with respect to the nature of the variation between the forms. The differences may be orthographic, phonological, dialectal or morphological.

The use of `chm:cellmate` is compatible with the OntoLex-lemon distinction between forms and their written representations. Where variants are modelled as different written representations of a single `ontolex:Form`, there is no need to introduce a cellmate relation. Where they are modelled as distinct instances of `ontolex:Form`, the property allows us to explicitly represent their paradigmatic relationship.

The property can also be used to relate prefixed and unprefixed forms of the same lexical entry, where these occupy the same paradigm cell.

We do not define the property as transitive. Instead, where a paradigm cell contains several distinct forms, we explicitly relate each pair of forms.

## Representing Lexical Entries and Their Forms

Individual verbs are represented as instances of `ontolex:LexicalEntry` and of the relevant strong verb class.

Their morphological forms are represented as instances of `ontolex:Form`, linked to the corresponding lexical entry via the OntoLex-lemon properties `ontolex:canonicalForm` and `ontolex:otherForm`.

We use existing LexInfo properties to describe the grammatical features associated with each form.

| Property | Description |
|---|---|
| `lexinfo:tense` | Grammatical tense |
| `lexinfo:person` | Grammatical person |
| `lexinfo:number` | Grammatical number |
| `lexinfo:verbFormMood` | Verbal form or mood |
| `ontolex:writtenRep` | Written representation of a form |
| `chm:cellmate` | Relation between forms occupying the same paradigm cell |

The morphological information associated with individual forms is thus represented separately from the characteristic vowel series associated with the strong verb class as a whole.

## Example Entries

### bīdan — Strong Verb Class I

The following example illustrates the representation of the Old English verb *bīdan*.

The forms currently represented in the example are:

| Paradigm cell | Forms |
|---|---|
| Infinitive | bīdan |
| Present indicative, second person singular | bīst, bīdst, bītst |
| Present indicative, third person singular | bīt |
| Preterite indicative, third person singular | bād |
| Preterite indicative, plural | beodan, bidon |

The lexical entry is represented as follows:

```turtle
chsample:biidan a ontolex:LexicalEntry,
                 chm:StrongVerb,
                 chm:StrongVerbI ;
    rdfs:label "bīdan"@ang ;
    ontolex:canonicalForm chsample:biidan_inf ;
    ontolex:otherForm
        chsample:biidan_pret-3sg,
        chsample:biidan_pret-pl_1,
        chsample:biidan_pret-pl_2,
        chsample:biidan_pres-2sg_1,
        chsample:biidan_pres-2sg_2,
        chsample:biidan_pres-2sg_3,
        chsample:biidan_pres-3sg .
```

The infinitive is represented as the canonical form:

```turtle
chsample:biidan_inf a ontolex:Form ;
    ontolex:writtenRep "bīdan"@ang ;
    lexinfo:verbFormMood lexinfo:infinitive .
```

The three variants of the present indicative second person singular are represented as distinct instances of `ontolex:Form`, each associated with the same set of grammatical features.

```turtle
chsample:biidan_pres-2sg_1 a ontolex:Form ;
    ontolex:writtenRep "bīst"@ang ;
    lexinfo:tense lexinfo:present ;
    lexinfo:person lexinfo:secondPerson ;
    lexinfo:number lexinfo:singular ;
    lexinfo:verbFormMood lexinfo:indicative .

chsample:biidan_pres-2sg_2 a ontolex:Form ;
    ontolex:writtenRep "bīdst"@ang ;
    lexinfo:tense lexinfo:present ;
    lexinfo:person lexinfo:secondPerson ;
    lexinfo:number lexinfo:singular ;
    lexinfo:verbFormMood lexinfo:indicative .

chsample:biidan_pres-2sg_3 a ontolex:Form ;
    ontolex:writtenRep "bītst"@ang ;
    lexinfo:tense lexinfo:present ;
    lexinfo:person lexinfo:secondPerson ;
    lexinfo:number lexinfo:singular ;ex
    lexinfo:verbFormMood lexinfo:indicative .
```

Since all three forms occupy the same cell in the inflectional paradigm of *bīdan*, we relate them using `chm:cellmate`.

```turtle
chsample:biidan_pres-2sg_1
    chm:cellmate chsample:biidan_pres-2sg_2,
                 chsample:biidan_pres-2sg_3 .

chsample:biidan_pres-2sg_2
    chm:cellmate chsample:biidan_pres-2sg_3 .
```

Similarly, the two preterite plural forms, *beodan* and *bidon*, are represented as follows:

```turtle
chsample:biidan_pret-pl_1 a ontolex:Form ;
    ontolex:writtenRep "beodan"@ang ;
    lexinfo:tense lexinfo:past ;
    lexinfo:number lexinfo:plural ;
    lexinfo:verbFormMood lexinfo:indicative .

chsample:biidan_pret-pl_2 a ontolex:Form ;
    ontolex:writtenRep "bidon"@ang ;
    lexinfo:tense lexinfo:past ;
    lexinfo:number lexinfo:plural ;
    lexinfo:verbFormMood lexinfo:indicative .

chsample:biidan_pret-pl_1
    chm:cellmate chsample:biidan_pret-pl_2 .
```

The inverse of each cellmate relation can be inferred on the basis of the symmetry of the property.

### cēosan — Strong Verb Class IIa

The verb *cēosan* provides a further example of the use of `chm:cellmate`, particularly in relation to prefixed and unprefixed forms.

Clark–Hall uses the symbol ± to indicate that the verb occurs both with and without the prefix *ge-*.

Rather than introducing a property to represent the optionality of the prefix, we explicitly represent the prefixed and unprefixed forms as separate instances of `ontolex:Form`.

```turtle
chsample:ceosan_inf a ontolex:Form ;
    ontolex:writtenRep "cēosan"@ang ;
    lexinfo:verbFormMood lexinfo:infinitive .

chsample:ceosan_inf_2 a ontolex:Form ;
    ontolex:writtenRep "gecēosan"@ang ;
    lexinfo:verbFormMood lexinfo:infinitive .

chsample:ceosan_inf
    chm:cellmate chsample:ceosan_inf_2 .
```

The same approach is used for the past participles *coren* and *gecoren*.

Other examples of paradigm-cell variation in the entry include:

| Paradigm cell | Forms |
|---|---|
| Infinitive | cēosan, gecēosan |
| Preterite indicative, third person singular | cēas, cǣs, cēs |
| Past participle | coren, gecoren |
| Present indicative, third person singular | cīest, cīesð, cīst, cȳst, cȳsð |

All distinct forms within each of these cells are pairwise related using `chm:cellmate`.

This illustrates how the same property can be used to represent different kinds of morphological variation without committing ourselves to a particular analysis of the differences between the forms.

## Integration with TEI

An important objective of the project is to integrate the RDF representation of morphological information with the existing TEI encoding of the Clark–Hall dictionary.

In particular, we are exploring the use of RDFa to embed RDF statements directly within the TEI representation of dictionary entries.

This is especially relevant in the case of traditional dictionaries such as Clark–Hall, where the morphological information associated with a single lexical entry may be distributed across several dictionary entries. For example, an inflected form may have its own dictionary entry containing a cross-reference to the corresponding lemma.

The RDF representation allows us to bring together this distributed information into a single morphological description of the lexical entry while retaining the structure of the original dictionary in the TEI representation.

## Further Work

The ontology and the accompanying RDF examples constitute a working model. Further work will focus on:

- Extending the coverage of the morphological descriptions to all Old English strong verb classes and subclasses.
- Populating the characteristic vowel series associated with each class.
- Consolidating morphological information distributed across different dictionary entries.
- Further developing the integration of RDF and TEI through RDFa.
- Representing the provenance of morphological information and alternative strong verb classifications using RDF 1.2.
- Investigating interoperability with Paralex and UniMorph.
