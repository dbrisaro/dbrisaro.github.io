---
layout: default
title: "SAR Flood Detection"
excerpt: "Using synthetic aperture radar imagery to identify and map flooded areas during extreme events."
date: 2024-01-01
permalink: /portfolio/sar-flood-detection/
category: "Remote Sensing"
tags:
  - SAR
  - Satellite
  - Flood
  - Remote Sensing
  - Python
---

<div class="project-header">
  <h1>SAR Flood Detection</h1>
  <div class="project-tags">
    {% for tag in page.tags %}
    <span class="project-tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>

## Overview

Flood events are among the most damaging natural disasters in Latin America, yet accurately mapping their extent in real time remains a challenge. Optical satellites struggle with cloud cover during heavy rainfall, precisely when floods occur. This project tackles that problem by combining SAR imagery, which sees through clouds, with optical sensors to estimate flooded areas and build a flood prediction model for climate risk applications.

## How it works

SAR (Synthetic Aperture Radar) satellites emit their own microwave signals and detect how the surface reflects them back. Water appears distinctively dark in SAR images because flat water scatters the signal away from the sensor. This makes SAR a reliable ground truth for flood mapping regardless of weather conditions.

We combine that ground truth with optical imagery from MODIS, VIIRS, and Sentinel to train a model that can estimate flooded areas even when SAR data is not available. The goal is a scalable tool for climate risk assessment and parametric insurance applications.

## Data sources

- SAR: ground truth for flood extent
- MODIS, VIIRS, Sentinel: optical imagery for model training and estimation
- Target region: pilot area in Latin America (TBD)

**Status:** pilot in development.
