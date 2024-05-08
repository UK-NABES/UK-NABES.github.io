# `UK-NABES`

Join us or attend a meeting to see what we are all about! We have a [JISCM@il email list](https://www.jiscmail.ac.uk/cgi-bin/webadmin?A0=UKNABES) which you can [Subscribe/Unsubscribe to here](https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?SUBED1=UKNABES&A=1).

The files for the NABES website are hosted here. You can look at the rendered site at https://uk-nabes.github.io.

## Contributing to the site

The NABES website uses github actions to automatically build and redelopy the https://uk-nabes.github.io site when changes are made to the `main` branch of the repository. 

You can etiher edit a file locally and upload files, or add files in the web interface to github. Either way is fine!

### Some details about the site setup

The site uses [Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll), a simple way to build a site using only [markdown](https://daringfireball.net/projects/markdown/basics) (plain text) files.

You can edit any page by simply clicking on it in this repository and clicking the edit button (pen icon, top right). If you have permissions this will lead you to be able to edit in situ, else you will be asked to "fork" the site, make changes then create a "pull request" to submit your changes back here for review.

### Adding "blog" posts

Adding a new post is dead easy - just write a new post in [markdown](https://www.markdownguide.org/tools/jekyll/) under the `_posts` directory (remembering to use the file naming convention *YYYY-MM-DD-post-title-with-hyphens-not-spaces.markdown*), commit your changes locally, and push the changes back up to the repository. The post should then just go live automatically after a few minutes.

### Adding people or organisations

To add a new person or organisation, go to the `_people/` or `_organisations/` directory (respectively) and make a copy of the `template.md` file (e.g. as `myorg.md`, the filename isn't used anywhere, it just needs to be descriptive and unique). Then edit that file, ensuring you fill in the [YAML](https://jekyllrb.com/docs/front-matter/) at the top of the file, then the content below. Add a logo or photo to that directory too. Once you have that as you like, don't forget to add the new `.md` file and logo/photo, commit the changes and push.

### Testing the site

You can test whether your post will work and look OK first, of you want, by following the installation and build instructions from [here](https://jekyllrb.com/docs/step-by-step/01-setup/) (I think you'll need linux, windows subsystem linux, or macos for this), but remembering not to follow the 'create a site' section, but instead just be int he root path of the git checkout of this repository.


### Some useful pages

Click the links here to see the corresponding page in github for editing

- [about page](https://github.com/UK-NABES/UK-NABES.github.io/blob/main/about.markdown)
- [resources page](https://github.com/UK-NABES/UK-NABES.github.io/blob/main/resources.markdown)


