# See, also

This is a static site, showcasing some of our favorite Wikipedia visualizations, infographics, sonifications, charts, illustrations, or anything particularly cool built on  Wikipedia data. If you want to suggest a Wikipedia-related projects, please [contact us](http://blog.hatnote.com/ask) or [send a pull request](../../pulls).

## Generating static HTML

To install the requirements:

```sh
pip install -r requirements.txt
```

You can build the site from a content file (see [content.yaml](../master/content.yaml)) and a template (see [templates/index.dust](../master/templates/index.dust)) using [generate.py](../master/generate.py):

```sh
python generate.py
```

Optionally, you can specify an input content (YAML) file or output HTML file:

```sh
python generate.py --content content.yaml --output ./static/index.html
```

### Requirements
 - PyYAML==3.10
 - ashes==0.5.3

## About

By Stephen LaPorte and Mahmoud Hashemi. HTML built on [Semantic UI](https://github.com/jlukic/Semantic-UI).

## Copying

Copyright (c) 2013, Stephen LaPorte and Mahmoud Hashemi
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
