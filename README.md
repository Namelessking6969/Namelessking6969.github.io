# Nameless Blog

A personal blog powered by [**Chirpy**](https://github.com/cotes2020/jekyll-theme-chirpy), a minimal and responsive Jekyll theme.

## Getting Started

### Prerequisites

- Ruby >= 2.7
- Bundler
- Node.js >= 16

### Running Locally

1. Install dependencies:

   ```shell
   bundle install
   ```

2. Start the development server:

   ```shell
   bundle exec jekyll serve
   ```

3. Open `http://localhost:4000` in your browser.

## Writing Posts

New posts go in the `_posts/` directory using the naming convention:

```
YYYY-MM-DD-title.md
```

Each post should include front matter at the top:

```yaml
---
title: "Post Title"
date: 2026-01-01
categories: [category]
tags: [tag1, tag2]
---
```

## Configuration

Site-wide settings are in `_config.yml`. Key options to customize:

- `title` and `tagline`
- `url` and `social` links
- `comments` and `analytics` providers
- `theme_mode` (light/dark)

## License

MIT
