---
layout: default
title: CV
permalink: /cv/
redirect_from:
  - /resume
---

## CV

## Education

<div class="cv-entry">
  <div class="cv-entry__date">Dec 2024</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Master of Public Policy</p>
    <p class="cv-entry__sub">Universidad Torcuato Di Tella</p>
    <p class="cv-entry__detail">Thesis: The influence of climate variability on Argentina's fishing industry based on future climate projections.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Dec 2020</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Ph.D. in Atmospheric and Oceanic Sciences</p>
    <p class="cv-entry__sub">University of Buenos Aires</p>
    <p class="cv-entry__detail">Thesis: Long-term trends of the sea surface temperature around South America and its ecological impact.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Mar 2015</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Master in Physical Oceanography</p>
    <p class="cv-entry__sub">University of Buenos Aires</p>
    <p class="cv-entry__detail">Thesis: Analysis of sea surface temperature trends on the Patagonian shelf based on satellite observations.</p>
  </div>
</div>

## Work Experience

<div class="cv-entry">
  <div class="cv-entry__date">Jan 2024 – Present</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Principal Climate Scientist</p>
    <p class="cv-entry__sub">Suyana – Climate Insurance</p>
    <p class="cv-entry__detail">Developed parametric models for climate risk insurance. Integrated field and satellite data for high-accuracy climate risk assessments. Conducted detection and analysis of extreme weather events.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Jul 2022 – Present</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Senior Data Scientist</p>
    <p class="cv-entry__sub">Fundar – Foundation for Argentinean Development</p>
    <p class="cv-entry__detail">Led development of open-source climate data. Applied advanced data analysis for evidence-based policy. Authored technical documentation for clients and stakeholders.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Aug 2020 – Jul 2022</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Scientific Advisor</p>
    <p class="cv-entry__sub">Secretary of Science and Technology, Province of Buenos Aires</p>
    <p class="cv-entry__detail">Led open data initiatives for a public observatory. Coordinated with public sector stakeholders on data management and policy formulation.</p>
  </div>
</div>

## Skills

<div class="cv-entry">
  <div class="cv-entry__date">Programming</div>
  <div class="cv-entry__body">
    <p class="cv-entry__sub">Python · MATLAB · R · C++</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">ML & Data</div>
  <div class="cv-entry__body">
    <p class="cv-entry__sub">Pandas · NumPy · scikit-learn · SciPy · Matplotlib · Seaborn · Plotly · Cartopy · SVM · Random Forests · regression · clustering · anomaly detection</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">GIS & RS</div>
  <div class="cv-entry__body">
    <p class="cv-entry__sub">QGIS · ArcGIS · Google Earth Engine · Geopandas · Pysal · Xarray · MODIS · Landsat · Sentinel-2 · ERA5 · NCEP/NCAR · CFSR</p>
  </div>
</div>

## Publications

{% assign pubs = site.publications | sort: "date" | reverse %}
{% for post in pubs %}
{% unless post.title == "" or post.title contains "paper-title" %}
<div class="cv-entry">
  <div class="cv-entry__date">{{ post.date | date: "%Y" }}</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">{% if post.paperurl %}<a href="{{ post.paperurl }}" target="_blank" rel="noopener">{{ post.title }}</a>{% else %}{{ post.title }}{% endif %}</p>
    <p class="cv-entry__sub"><em>{{ post.category }}</em> · {{ post.venue }}</p>
  </div>
</div>
{% endunless %}
{% endfor %}

## Teaching

{% assign teaching = site.teaching | sort: "date" | reverse %}
{% for post in teaching %}
{% unless post.title == "" %}
<div class="cv-entry">
  <div class="cv-entry__date">{{ post.date | date: "%Y" }}</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">{{ post.title }}</p>
    <p class="cv-entry__sub">{{ post.venue }}</p>
  </div>
</div>
{% endunless %}
{% endfor %}

## Service & Leadership

<div class="cv-entry">
  <div class="cv-entry__date">2024</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Host, IFAECI Days</p>
    <p class="cv-entry__sub">Franco-Argentine Institute for Climate Studies and Its Impacts, coordinating working groups and facilitating dialogue.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">2020&ndash;2022</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Youth Ambassador, European Union</p>
    <p class="cv-entry__sub">Argentine representative in the All-Atlantic Ocean Youth Ambassadors programme, promoting sustainable ocean development and stewardship through science diplomacy, community outreach, and policy engagement. Participated in the Youth Ambassador Forum in Brussels, the Summer School in Washington D.C., and the All-Atlantic Data Enterprise 2030 Stakeholders Workshop in Buenos Aires, contributing to dialogue on Atlantic ocean data infrastructure and data sharing across the scientific community.</p>
  </div>
</div>
