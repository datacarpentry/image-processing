## Contributing

[The Carpentries][cp-site] ([Software Carpentry][swc-site], [Data
Carpentry][dc-site], and [Library Carpentry][lc-site]) are open source
projects, and we welcome contributions of all kinds: new lessons, fixes to
existing material, bug reports, and reviews of proposed changes are all
welcome.

### Contributor Agreement

By contributing, you agree that we may redistribute your work under [our
license](LICENSE.md). In exchange, we will address your issues and/or assess
your change proposal as promptly as we can, and help you become a member of our
community. Everyone involved in [The Carpentries][cp-site] agrees to abide by
our [code of conduct](CODE_OF_CONDUCT.md).

### Who Should Contribute?

Contributions to this lesson are welcome from anyone with an interest in the project.

### How to Contribute

The easiest way to get started is to file an issue to tell us about a spelling
mistake, some awkward wording, or a factual error. This is a good way to
introduce yourself and to meet some of our community members.

1. If you do not have a [GitHub][github] account, you can [send us comments by
   email][contact]. However, we will be able to respond more quickly if you use
   one of the other methods described below.

2. If you have a [GitHub][github] account, or are willing to [create
   one][github-join], but do not know how to use Git, you can report problems
   or suggest improvements by [creating an issue][issues]. This allows us to
   assign the item to someone and to respond to it in a threaded discussion.

3. If you are comfortable with Git, and would like to add or change material,
   you can submit a pull request (PR). Instructions for doing this are
   [included below](#using-github).

Note: if you want to build the website locally, please refer to [The Workbench
documentation][template-doc].

### Where to Contribute

1. If you wish to change this lesson, add issues and pull requests here.
2. If you wish to change the template used for workshop websites, please refer
   to [The Workbench documentation][template-doc].


### What to Contribute (General)

There are many ways to contribute, from writing new exercises and improving
existing ones to updating or filling in the documentation and submitting [bug
reports][issues] about things that do not work, are not clear, or are missing.
If you are looking for ideas, please see [the list of issues for this
repository][repo], or the issues for [Data Carpentry][dc-issues], [Library
Carpentry][lc-issues], and [Software Carpentry][swc-issues] projects.

Comments on issues and reviews of pull requests are just as welcome: we are
smarter together than we are on our own. **Reviews from novices and newcomers
are particularly valuable**: it's easy for people who have been using these
lessons for a while to forget how impenetrable some of this material can be, so
fresh eyes are always welcome.

### What to Contribute (This Lesson)

Any contributions are welcome, particularly ideas for how the existing content could be
improved or updated, and/or errors that need to be corrected. Comments on existing issues 
and reviews of pull requests are similarly welcome.

If you plan to submit a pull request, please open an issue
(or comment on an existing thread) first to ensure that effort is not duplicated
or spent making a change that will not be accepted by the Maintainers.

#### Content / style guidelines
- If you add an image / figure that was generated from Python code, please include this 
  code in your PR under `episodes/fig/source`.

- Use the terms in the table below, when referring to Python libraries within the lesson. 
  The table gives two terms for each library: `Term for descriptive text` which should be 
  used when discussing the library in plain English / full sentences and `Term for code` 
  which should be used when referring to code (and within code).

   | Python library  | Term for descriptive text | Term for code  |
   | :-------------  | :-------------            | :------------- | 
   | [scikit-image](https://scikit-image.org/)  | scikit-image  | `skimage` |
   | [NumPy](https://numpy.org/)  | NumPy | `numpy` |
   | [Matplotlib](https://matplotlib.org/) | Matplotlib | `matplotlib` |
   | [imageio](https://imageio.readthedocs.io/en/stable/index.html) | imageio | `imageio` |


- When importing scikit-image use:
   ```python
   import skimage as ski
   ```
   Therefore, to access specific functions, you need to use their submodule name. For example:

   ```python
   import skimage as ski

   rr, cc = ski.draw.rectangle(start=(357, 44), end=(740, 720))
   ```

- For reading and writing images, use the [imageio](https://imageio.readthedocs.io/en/stable/index.html) 
  library and avoid use of `skimage.io`. For example:
   ```python
   import imageio.v3 as iio

   chair = iio.imread(uri="data/chair.jpg")  # read an image
   iio.imwrite(uri="data/chair.tif", image=chair)  # write an image
   ```
  
- Comments providing an overall description of a code snippet should use triple quotes `"""`, e.g.,
   ```python
   """Python script to load a colour image in grayscale"""

   chair = iio.imread(uri="data/chair.jpg")
   gray_chair = ski.color.rgb2gray(chair)
   ```

### What *Not* to Contribute (General)

Our lessons already contain more material than we can cover in a typical
workshop, so we are usually *not* looking for more concepts or tools to add to
them. As a rule, if you want to introduce a new idea, you must (a) estimate how
long it will take to teach and (b) explain what you would take out to make room
for it. The first encourages contributors to be honest about requirements; the
second, to think hard about priorities.

We are also not looking for exercises or other material that only run on one
platform. Our workshops typically contain a mixture of Windows, macOS, and
Linux users; in order to be usable, our lessons must run equally well on all
three.

### What *Not* to Contribute (This Lesson)

Although most contributions will be welcome at this stage of the curriculum's development,
the time available to deliver the content in a training event is strictly limited
and needs to be accounted for when considering the addition of any new content.
If you want to suggest the addition of new content, especially whole new sections or episodes,
please open an issue to discuss this with the Maintainers first and provide the following 
information alongside a summary of the content to be added:

1. A suggested location for the new content.
2. An estimate of how much time you estimate the new content would require in training
   (teaching + exercises).
3. The [learning objective(s)][cldt-lo] of this new content.
4. (optional, but strongly preferred)
   A suggestion of which of the currently-used learning objectives could be
   removed from the curriculum to make space for the new content.

### Using GitHub

If you choose to contribute via GitHub, you may want to look at [How to
Contribute to an Open Source Project on GitHub][how-contribute]. In brief, we
use [GitHub flow][github-flow] to manage changes:

1. Create a new branch in your desktop copy of this repository for each
   significant change.
2. Commit the change in that branch.
3. Push that branch to your fork of this repository on GitHub.
4. Submit a pull request from that branch to the [upstream repository][repo].
5. If you receive feedback, make changes on your desktop and push to your
   branch on GitHub: the pull request will update automatically.

NB: The published copy of the lesson is usually in the `main` branch.

Each lesson has a team of maintainers who review issues and pull requests or
encourage others to do so. The maintainers are community volunteers, and have
final say over what gets merged into the lesson.

#### Merging Policy

Pull requests made to the default branch of this repository
(from which the lesson site is built)
can only be merged after at least one approving review from a Maintainer.
Any Maintainer can merge a pull request that has received at least one approval,
but they may prefer to wait for further input from others before merging.

### Other Resources

The Carpentries is a global organisation with volunteers and learners all over
the world. We share values of inclusivity and a passion for sharing knowledge,
teaching and learning. There are several ways to connect with The Carpentries
community listed at <https://carpentries.org/connect/> including via social
media, slack, newsletters, and email lists. You can also [reach us by
email][contact].

[repo]: https://github.com/datacarpentry/image-processing
[cldt-lo]: https://carpentries.github.io/lesson-development-training/05-objectives.html#learning-objectives
[contact]: mailto:team@carpentries.org
[cp-site]: https://carpentries.org/
[dc-issues]: https://github.com/issues?q=user%3Adatacarpentry
[dc-lessons]: https://datacarpentry.org/lessons/
[dc-site]: https://datacarpentry.org/
[discuss-list]: https://lists.software-carpentry.org/listinfo/discuss
[github]: https://github.com
[github-flow]: https://guides.github.com/introduction/flow/
[github-join]: https://github.com/join
[how-contribute]: https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github
[issues]: https://carpentries.org/help-wanted-issues/
[lc-issues]: https://github.com/issues?q=user%3ALibraryCarpentry
[swc-issues]: https://github.com/issues?q=user%3Aswcarpentry
[swc-lessons]: https://software-carpentry.org/lessons/
[swc-site]: https://software-carpentry.org/
[lc-site]: https://librarycarpentry.org/
[template-doc]: https://carpentries.github.io/workbench/
