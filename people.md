---
title: People

---

Here is a list of affiliated people.

{% for person in site.people %}
  <h2 id="{{person.shortname}}">{{ person.name }}</h2>
  <p><img src="people/{{person.image}}" alt="Photo of {{person.name}}" width=200px hspace="20" vspace="20" style="float:left"> {{ person.content | markdownify }}</p>
  <p>More information on {{person.name}}'s <a href="{{ person.website }}">website</a>.</p>
  <br/>
  <br/>
{% endfor %}
