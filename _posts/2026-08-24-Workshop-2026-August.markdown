---
layout: post
title:  "August 2026 Workshop Summary: Common Workflows for Unstructured Data"
date:   2026-08-24 18:00:00 +0000
categories: news
---

<img src="/img/2026-BlogPictures/Feb2026-BlogPic.jpg" alt="Citizen Science Sketch" width=350px align = "right"> 

Diana Bowler (_UK Centre for Ecology and Hydrology_, <diabow@ceh.ac.uk>) gave a
great presentation for August’s workshop on workflows for unstructured data. Unstructured data, like some [citizen science datasets](https://www.inaturalist.org/), are collected without a consistent, documented protocol. Compared to more structured datasets, they typically cover a larger spatial area, temporal period and range of taxa, as well as having a larger quantity of data. For ecology, they have become a key data source for understanding patterns at large scale. However, they are also influenced by a variety of biases, like no recording of absences, inconsistent collection efforts, misidentifications, and no spatial or temporal design.

Workflows have been developed to account for some of these biases, with Diana presenting a typical workflow for biodiversity monitoring:
  1. Data preparation – experts remove likely false positives and infer absences based on an assumed target group, surveys are reverse engineered, and proxies of sampling effort calculated
  2. Data modelling – try to account for detection and reporting variability, usually using hierarchical state space model with the true state represented by a latent variable
  3. Communicating uncertainty – understanding which sources of uncertainty and bias are unaccounted for, and how much uncertainty could have been introduced by the methods and assumptions used

Opportunities for improvement include sensitivity analysis of different workflow methods, integration with more structured datasets, and improving the reporting of metadata so that sampling variability can be modelled.
