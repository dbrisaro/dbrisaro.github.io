---
layout: default
title: "Is there a feminist approach to statistical data collection?"
excerpt: "Assessing gender dimensions in National Household Survey design using feminist epistemology, comparative analysis, and large language models."
date: 2024-03-01
permalink: /portfolio/feminist-surveys/
category: "Data Science"
tags:
  - Feminist Economics
  - Survey Design
  - LLMs
  - Quantitative Methods
  - Data Science
---

<div class="project-header">
  <h1>Is there a feminist approach to statistical data collection?</h1>
  <p class="project-subtitle">Assessing gender dimensions in National Household Survey design</p>
  <div class="project-tags">
    {% for tag in page.tags %}
    <span class="project-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>

**Co-authors:** Daniela Belén Risaro (Faculty of Exact and Natural Sciences, UBA; School of Government, UTDT) and Micaela Fernández Erlauer (School of Accounting, Finance and Economics, University of Greenwich).

**Status:** Working paper. Submission expected October 2025.

---

## Motivation

Feminist scholarship on quantitative methods has focused predominantly on analytical decisions: how researchers model, interpret, and report findings once datasets are available. Recent contributions have begun to formalise guidelines for feminist econometric practice, addressing survey weighting, intersectional modelling, and non-binary measures of gender. Both the gender bias in data analysis and the lack of gender-disaggregated data are widely recognised as key factors limiting evidence-based policy.

Yet these efforts largely presuppose the existence of usable data. Considerably less attention has been paid to an earlier and arguably more consequential stage: the design of the statistical instruments through which data are collected in the first place.

This paper argues that the problem of gender data gaps is systematically misdiagnosed. It is usually framed as a data availability problem when it is, more precisely, a design problem. Household surveys, a primary source of data in feminist economics, carry their design assumptions forward into every analysis conducted on them. Instruments designed without feminist intent produce data whose limitations cannot be fully corrected at the modelling stage.

---

## Research questions

1. What criteria define a feminist statistical instrument?
2. How do existing national household surveys perform when assessed against a feminist statistical framework?
3. Can LLMs reliably operationalise feminist epistemological criteria at scale?

---

## Conceptual framework

Drawing on feminist epistemology and decolonial theory, the paper proposes a framework to assess what it means for a data collection instrument to be feminist. This framework moves beyond the presence of gender-disaggregated variables, a shallow but common proxy, toward a deeper assessment of design choices:

- Question wording and embedded categorical assumptions
- Sampling design and population coverage
- Measurement frequency and reference periods
- Theoretical assumptions in instrument construction
- Binary gender assumptions and their structural effects on analysis

---

## Methodology

**Case selection.** The analysis compares national official household surveys from countries representing varied institutional contexts across Latin America and Europe, with Argentina as the anchor case.

**Data collection.** A systematic and large-scale corpus is constructed through automated scraping of publicly available documentation from national statistics offices, including questionnaires, methodological notes, and sampling frame documents.

**LLM-assisted classification.** In a second stage, large language models are applied to this documentation to:
- Classify survey questions and design choices against the feminist evaluation framework
- Identify embedded binary gender assumptions
- Surface systematic absences in coverage

Prompt design is treated as an explicit methodological instrument, following feminist principles of transparency and replicability. All procedures and decisions are made fully available.

---

## Contributions

**Typology of feminist incorporation.** Applying the framework across surveys in Latin America and Europe, the paper produces a typology of statistical instruments along a spectrum ranging from instruments entirely silent on gender dynamics to those reflecting explicit feminist design principles.

**Non-neutrality at the design stage.** The comparative analysis demonstrates that apparent neutrality is itself a feminist consideration. Survey objectives constrain design, and those constraints are carried forward into all downstream analysis. Argentina's household survey is examined as a concrete case: it lacks the statistical power to capture key feminist economic variables at the subnational level.

**Open-access database.** All evaluated instruments and assessments are made publicly available to support replicability and further research.

---

## Implications

Framing gender data gaps solely as an availability problem obscures a more fundamental issue: data that were never intended to be collected cannot meaningfully be described as a gap. Addressing this requires methodological transparency, reflexivity among those producing official data, and explicit criteria for evaluating instruments before analysis begins. This paper proposes actionable criteria that researchers, national statistics offices, and feminist advocates can apply to evaluate and improve statistical instruments.
