---
layout: default
title: "Agricultural Drought Monitor"
excerpt: "An interactive tool combining multiple drought indices and remote sensing products to monitor agricultural drought across key regions of South America."
date: 2024-03-01
permalink: /portfolio/agro-application/
category: "Applications"
tags:
  - Agriculture
  - Drought
  - Remote Sensing
  - NDVI
  - Satellite
  - Python
---

<div class="project-header">
  <h1>Agricultural Drought Monitor</h1>
  <div class="project-tags">
    {% for tag in page.tags %}
    <span class="project-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>

## Overview

Drought is one of the most complex and costly climate risks for agricultural systems in South America. Unlike floods, it develops slowly and its impacts are hard to capture with a single metric. This tool brings together multiple drought indices and remote sensing products to provide a comprehensive view of drought conditions across key agricultural regions.

The platform is designed for anyone who needs to monitor, assess, or make decisions around agricultural drought: insurers developing parametric products, producers tracking conditions on the ground, and public institutions managing climate risk.

## What you will find here

- Multiple drought indices: SPI, SPEI, NDVI anomalies, soil moisture
- Data from multiple sources: ERA5, CHIRPS, MODIS, Sentinel
- Interactive maps and time series by region
- Current conditions and historical evolution
- Focus regions: Buenos Aires Province and Bolivia

## Why multiple indices?

No single index captures drought fully. Meteorological drought (lack of rainfall), agricultural drought (soil moisture deficit), and vegetation stress can develop at different times and intensities. Combining indices gives a more complete and reliable picture.

**Status:** under development.
