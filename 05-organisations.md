---
title: Organisations

---

Here is a list of affiliated organisations.


{% for organisation in site.organisations %}
  <h2 id="{{organisation.shortname}}">{{ organisation.name }}</h2>
  <p><img src="organisations/{{organisation.logo}}" alt="{{organisation.name}} logo" width=200px hspace="20" vspace="20" style="float:left"> {{ organisation.content | markdownify }}</p>
  <p>More information on the {{organisation.name}} <a href="{{ organisation.website }}">website</a>.</p>
  <br/>
  <br/>
{% endfor %}
