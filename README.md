Tuesmon Contrib Let's Chat
========================

Tuesmon plugin for Let's Chat (https://sdelements.github.io/lets-chat/) integration.

> **NOTE: Let's Chat team is working to add markdown support, please use this branch for testing: https://github.com/sdelements/lets-chat/tree/try-md**

Installation
------------
### Production env

#### Tuesmon Back

In your Tuesmon back python virtualenv install the pip package `tuesmon-contrib-letschat` with:

```bash
  pip install tuesmon-contrib-letschat
```

Modify in `tuesmon-back` your `settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["tuesmon_contrib_letschat"]
```

Then run the migrations to generate the new need table:

```bash
  python manage.py migrate tuesmon_contrib_letschat
```

#### Tuesmon Front

Download in your `dist/plugins/` directory of Tuesmon front the `tuesmon-contrib-letschat` compiled code (you need subversion in your system):

```bash
  cd dist/
  mkdir -p plugins
  cd plugins
  svn export "https://github.com/tuesmoncom/tuesmon-contrib-letschat/tags/$(pip show tuesmon-contrib-letschat | awk '/^Version: /{print $2}')/front/dist" "letschat"
```

Include in your 'dist/conf.json' in the 'contribPlugins' list the value `"/plugins/letschat/letschat.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/letschat/letschat.json"
    ]
...
```

### Dev env

#### Tuesmon Back

Clone the repo and

```bash
  cd tuesmon-contrib-letschat/back
  workon tuesmon
  pip install -e .
```

Modify in `tuesmon-back` your `settings/local.py` and include the line:

```python
  INSTALLED_APPS += ["tuesmon_contrib_letschat"]
```

Then run the migrations to generate the new need table:

```bash
  python manage.py migrate tuesmon_contrib_letschat
```

#### Tuesmon Front

After clone the repo link `dist` in `tuesmon-front` plugins directory:

```bash
  cd tuesmon-front/dist
  mkdir -p plugins
  cd plugins
  ln -s ../../../tuesmon-contrib-letschat/dist letschat
```

Include in your 'dist/conf.json' in the 'contribPlugins' list the value `"/plugins/letschat/letschat.json"`:

```json
...
    "contribPlugins": [
        (...)
        "/plugins/letschat/letschat.json"
    ]
...
```

In the plugin source dir `tuesmon-contrib-letschat/front` run

```bash
npm install
```

and use:

- `gulp` to regenerate the source and watch for changes.
- `gulp build` to only regenerate the source.
