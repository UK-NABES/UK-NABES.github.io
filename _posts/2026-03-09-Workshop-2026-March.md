---
layout: post
title: "March 2026 Workshop Summary: Consultancy Corner"
date: 2026-03-09 17:26:00 -0000
categories: news
---


<img src="/img/2025-BlogPictures/NABES blog picture - 25-08 - consultancy corner.svg" alt="Consultancy Corner Sketch" width=300px align = "right"> 

For this month’s Consultancy Corner workshop, Mike Dunbar (*Environment Agency*), <mike.dunbar@environment-agency.gov.uk>) presented some challenges of fitting statistical models of pollutant concentrations using spot sample water quality monitoring data from rivers:
* General Additive Models (GAMs) are a robust approach for modelling seasonality, multi-year trends (arising e.g. changing effluent treatment regulations) and datasets with concentrations below analytical limits of detection. River flow can be added as a covariate – allowing bivariate smoothing with time for longer-term dynamics, such as regulation changes. However, this approach doesn’t explicitly distinguish between contributions from different sources of pollution e.g. point or diffuse sources

   * The [Load Apportionment Model](https://doi.org/10.1016/j.scitotenv.2008.01.054) (LAM) does explicitly model the contributions of point and diffuse sources as power law functions of flow. It could benefit from more robust statistical formulation for limits of detection, uncertain/time-varying parameters and explicit residual distributions, and comparison with the above GAM approach.
* We are planning a masters project to investigate these topics further. 
