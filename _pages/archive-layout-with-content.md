---
title: "Archive Layout with Content"
layout: archive
permalink: /archive-layout-with-content/
---

# Archive of Daniela Risaro’s Work

This page serves as a showcase of various types of content on my website, including key projects, publications, talks, and more.

## Projects

Here are some of the key projects I’ve worked on:

| Project Name      | Year   | Description                                                      |
| ----------------- | ------ | ---------------------------------------------------------------- |
| Climate Risk Model | 2024   | Development of parametric models for climate insurance, integrating satellite and field data to assess risks. |
| Sea Surface Trends | 2020   | Analyzed long-term sea surface temperature trends in South America using satellite imagery. |
| Open Climate Data  | 2022   | Developed open-source climate datasets for public policy applications in Argentina. |

## Publications

<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

## Talks

<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html  %}
{% endfor %}</ul>

## Teaching

<ul>{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

## Skills & Tools

Some of the tools and techniques I frequently use:

- **Programming & Scripting:** Python, R, MATLAB
- **Data Analysis & Visualization:** Pandas, NumPy, Matplotlib, Seaborn, scikit-learn
- **Machine Learning:** SVM, Random Forest, clustering, anomaly detection
- **Remote Sensing & GIS Tools:** Google Earth Engine, QGIS, ArcGIS, Sentinel, MODIS
- **Technical Writing:** Research proposals, publications, policy briefs

## Contact & Links

If you’d like to collaborate or learn more about my work, feel free to [contact me](mailto:dbrisaro@gmail.com).

<ul>{% for post in site.pages %}
  {% include archive-single.html %}
{% endfor %}</ul>
