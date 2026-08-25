---
layout: default
title: CV
permalink: /cv/
redirect_from:
  - /resume
---

## CV

<p><a href="/files/CV_Risaro_aug_2026.pdf" target="_blank" rel="noopener">Download as PDF</a></p>

## Education

<div class="cv-entry">
  <div class="cv-entry__date">2021&ndash;2025</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Master of Public Policy</p>
    <p class="cv-entry__sub">Universidad Torcuato Di Tella</p>
    <p class="cv-entry__detail">Thesis: The Argentine fishing industry and its relationship with climate variability and change, covering environmental, economic and institutional perspectives. Selected among the best final dissertations of 2025.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">2015&ndash;2020</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Ph.D. in Atmospheric and Oceanic Sciences</p>
    <p class="cv-entry__sub">University of Buenos Aires</p>
    <p class="cv-entry__detail">Thesis: Long-term trends of the sea surface temperature around South America and its ecological impact.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">2009&ndash;2015</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Licenciatura in Physical Oceanography (equivalent to MSc)</p>
    <p class="cv-entry__sub">University of Buenos Aires</p>
    <p class="cv-entry__detail">Thesis: Analysis of sea surface temperature trends on the Patagonian shelf based on satellite observations.</p>
  </div>
</div>

## Work Experience

<div class="cv-entry">
  <div class="cv-entry__date">Jan 2025 – Present</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Principal Climate Scientist</p>
    <p class="cv-entry__sub">Suyana – Climate Insurance</p>
    <p class="cv-entry__detail">Lead a team of data scientists and set hazard index design across all parametric products, from trigger definition to threshold calibration and basis risk validation. Built a satellite sargassum monitoring system combining optical and infrared imagery (MODIS, VIIRS, Sentinel-2, Landsat) with deep learning segmentation, and forecast coastal arrival daily in production through Lagrangian drift modelling. Designed the portfolio construction methodology behind the move to Managing General Agent, and delivered a multi-hazard risk and infrastructure loss assessment for CAF using CLIMADA with ERA5 and CHIRPS hazard layers.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Jan 2024 – Dec 2024</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Senior Climate Scientist</p>
    <p class="cv-entry__sub">Suyana – Climate Insurance</p>
    <p class="cv-entry__detail">Built the first five parametric products end to end (storm surge, heatwaves, cold spells, drought and sea surface temperature anomalies), implemented in Peru, Bolivia, Argentina and Colombia. Ran wave and storm surge simulations (SWAN) for 89 ports along 3,000 km of the Peruvian coast, and co-developed a flood detection method training a CNN on MODIS, VIIRS and IMERG with Sentinel-1 SAR-derived labels. Defended model design and assumptions to reinsurers, securing up to USD 5 million in risk capital for the first programme placed.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Jun 2022 – Dec 2024</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Senior Data Scientist</p>
    <p class="cv-entry__sub">Fundar – Foundation for Argentine Development</p>
    <p class="cv-entry__detail">Delivered Argendata, the national climate change indicator database, combining ERA5 reanalysis with AVHRR satellite records as an open public resource. Produced a report on the Argentine fishing sector and its exposure to climate variability, linking MODIS sea surface temperature and chlorophyll with CMIP6 projections to 35 years of landings. Built two subnational composite indices on gender inequality, published with open source code and data, and wrote for national press on climate, fisheries and planetary boundaries.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Aug 2020 – May 2022</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Scientific Advisor</p>
    <p class="cv-entry__sub">Secretariat of Science, Technology and Innovation, Province of Buenos Aires</p>
    <p class="cv-entry__detail">Defined climate and development policy indicators for ORBITA, the province's regional technology and innovation observatory. Co-designed FITBA, the provincial technology innovation fund, and evaluated 30 proposals in its first call. Worked with the provincial statistics office to develop and publish gender indicators for the science and technology sector, adding them to official statistics.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">Apr 2015 – Aug 2020</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">PhD Researcher, Climate and Ocean Sciences</p>
    <p class="cv-entry__sub">CONICET – Argentine National Scientific and Technical Research Council</p>
    <p class="cv-entry__detail">Detected and validated long-term regional warming and cooling trends in the South Atlantic using Mann-Kendall testing, spectral analysis and EOF and PCA decomposition on AVHRR and OISSTv2 records, reanalysis and in-situ data. Isolated coupled ocean and atmosphere modes through singular value decomposition, linking observed trends to ENSO and SAM teleconnections. Developed reproducible Python workflows (xarray, Dask, pandas) on remote Linux servers, and participated in three oceanographic cruises aboard FS Meteor and RV Puerto Deseado.</p>
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

## Conferences & Workshops

<div class="cv-entry">
  <div class="cv-entry__date">2020</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Penguin exposure to climate change inferred through CMIP6 projections</p>
    <p class="cv-entry__sub">Oral presentation, British Ornithologists' Union Conference. Lois, N., Risaro, D. B., and Raya Rey, A.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">2018</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Trends and variability of sea surface temperature in the Argentine Patagonian Shelf</p>
    <p class="cv-entry__sub">Oral presentation, X Jornadas Nacionales de Ciencias del Mar, Buenos Aires. Risaro, D. B., Chidichimo, M. P., and Piola, A. R.</p>
  </div>
</div>

<div class="cv-entry">
  <div class="cv-entry__date">2017</div>
  <div class="cv-entry__body">
    <p class="cv-entry__title">Strong gradients and currents, mixing, blooms and internal waves in the Brazil-Malvinas confluence and Patagonian shelf break</p>
    <p class="cv-entry__sub">GEOMAR Summer School, Kiel. Manta, G., Risaro, D. B., Bonelli, G., and Handmann, P.</p>
  </div>
</div>

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
