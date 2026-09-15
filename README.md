# TTS Model Comparison — Demo Page

A GitHub Pages (Jekyll) site listing generated audio samples from five text-to-speech
models — Conv, LSTM, Mamba-Attn, Mamba-Mamba, and Transformer — side by side for the
same 10 text inputs, one sample per row.

## Structure

```
.
├── _config.yml              # site title/description, uses jekyll-theme-cayman
├── index.md                 # the page itself (header + samples table)
├── assets/css/style.scss    # theme overrides (table/audio-player styling)
├── resources/
│   └── audios/
│       ├── conv/01.wav ... 10.wav
│       ├── lstm/01.wav ... 10.wav
│       ├── mamba-attn/01.wav ... 10.wav
│       ├── mamba-mamba/01.wav ... 10.wav
│       └── transformer/01.wav ... 10.wav
├── texts.tsv                 # sample -> text (used to regenerate the table)
└── generate_index.py         # regenerates the table in index.md from texts.tsv
```

This mirrors the layout of [NQMT_IS26](https://github.com/alexdemartos/NQMT_IS26).

## Editing content

- **Title / abstract / authors / links**: edit the header block at the top of `index.md`
  and the `title:` / `description:` fields in `_config.yml`.
- **Samples**: edit `texts.tsv` (columns: `sample`, `src_idx`, `text`), drop the matching
  `.wav` files into `resources/audios/<model>/<sample>.wav`, then regenerate the table:

  ```bash
  python3 generate_index.py
  ```

  This rewrites the `<table>...</table>` block inside `index.md` — replace it manually
  with the freshly generated `_table_include.html` output if you don't want to script it.
- **Models / column order**: edit the `MODELS` list at the top of `generate_index.py`
  (folder name → display name), then regenerate.

## Deploying to GitHub Pages

1. Push this repository to GitHub (e.g. `your-username/your-repo-name`).
2. In the repo settings, go to **Pages** and set the source to the `main` branch
   (root folder).
3. GitHub will build the Jekyll site automatically — no build step needed on your end.
4. The site will be live at `https://your-username.github.io/your-repo-name/`.

## Local preview (optional)

```bash
bundle exec jekyll serve
```

requires Ruby + Bundler + Jekyll (`gem install bundler jekyll`).
