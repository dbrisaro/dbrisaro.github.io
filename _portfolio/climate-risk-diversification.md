---
layout: default
title: "Climate Risk Diversification Tool"
excerpt: "An interactive tool for reinsurers to build and evaluate diversified climate risk portfolios across Latin America, combining historical event data with exposure layers."
date: 2024-05-01
permalink: /portfolio/climate-risk-diversification/
category: "Climate Risk"
tags:
  - Climate Risk
  - Insurance
  - ERA5
  - Python
  - Data Visualization
  - Latin America
---

<div class="project-header">
  <h1>Climate Risk Diversification Tool</h1>
  <div class="project-tags">
    {% for tag in page.tags %}
    <span class="project-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>

## Overview

Climate risk is not uniform across space or time. Hurricanes, floods, droughts, and heatwaves do not all occur simultaneously in the same region, and the large-scale climate drivers that trigger them often affect different parts of Latin America in opposite or uncorrelated ways. This creates a natural diversification opportunity that reinsurers can exploit when building their portfolios.

This tool is designed for reinsurers and climate risk professionals who want to understand and quantify that diversification. It combines historical climate event data with exposure layers to show not just where extreme events occur, but where they matter, and how combining different regions and perils reduces aggregate risk.

## What you can do

- Select regions across Latin America and types of climate risk (hurricanes, floods, droughts, heatwaves)
- See the correlation structure between the risks you selected
- Build your portfolio interactively and visualize how your aggregate exposure changes as you add or remove regions and perils
- Understand which combinations offer the most diversification benefit

## Why exposure weighting matters

A heatwave in an uninhabited area is not the same risk as a heatwave in a dense urban center. The tool weights climate events by exposure layers including population density, agricultural land use, and insurable assets, so the analysis reflects real-world risk rather than raw climatology. This distinction is critical for reinsurers: what matters is not the physical event itself, but its intersection with exposed value.

## Methodology

Climate events are estimated from ERA5 reanalysis data across Latin America. Exposure layers are derived from global population and land use datasets (GPW, WorldPop, ESA CCI). Diversification is quantified through event correlation matrices and aggregate loss metrics across the selected portfolio. The underlying hypothesis is that large-scale climate drivers such as ENSO affect different regions in opposite or uncorrelated ways, generating natural diversification across a geographically spread portfolio.

## Target audience

- Reinsurers building or evaluating parametric climate risk portfolios
- Insurance companies assessing aggregate exposure across regions
- Public institutions and development banks working on climate risk finance in Latin America

**Status:** under development.
