---
title: About Twitter (X) Cards
keywords:
  - Twitter Cards
  - X Cards
  - Tweets
  - Markup
  - Sample Code
description: "With X Cards, you can attach rich photos, videos and media experiences to Tweets, helping to drive traffic to your website. Simply add a few lines of markup to your webpage, and users who Tweet links to your content will have a “Card” added to the Tweet that’s visible to their followers."
created: 2025-02-05 05:54:00
updated: 2025-02-05 05:54:00
---

## About

With X Cards, you can attach rich photos, videos and media experiences to Tweets, helping to drive traffic to your website. Simply add a few lines of markup to your webpage, and users who Tweet links to your content will have a “Card” added to the Tweet that’s visible to their followers.

## Cards Markup Tag Reference

- `<meta name="twitter:card" content=""`
  - Required: Yes
  - `content`. e.g. `summary`, `summary_large_image`
  - Used with all cards
- `twitter:title`
  - Required: Yes
  - A concise title for the related content
  - Title of content (max 70 characters)
  - Used with summary, summary_large_image, player cards
- `twitter:site`
  - Required: No
  - The Twitter @username the card should be attributed to
  - Used with summary, summary_large_image, app, player cards
- `twitter:description`
  - Required: No
  - A description that concisely summarizes the content as appropriate for presentation within a Tweet
  - Description of content (maximum 200 characters)
  - Used with summary, summary_large_image, player cards
- `twitter:image`
  - Required: No
  - A URL to a unique image representing the content of the page
  - Images must be less than 5MB in size
  - JPG, PNG, WEBP and GIF formats are supported. Only the first frame of an animated GIF will be used
  - SVG is not supported
  - Used with summary, summary_large_image, player cards
- `twitter:image:alt`
  - Required: No
  - A text description of the image conveying the essential nature of an image to users who are visually impaired.
  - Maximum 420 characters.
  - Used with summary, summary_large_image, player cards

## Card types

### Summary Card

Sample Code

```html
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="About Twitter (X) Cards - chrisding.xyz" />
<meta name="twitter:site" content="@chris1ding1" />
<meta name="twitter:description" content="Description." />
<meta name="twitter:image" content="https://" />
<meta name="twitter:image:alt" content="" />
```

### Summary with large image

Sample Code

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="About Twitter (X) Cards - chrisding.xyz">
<meta name="twitter:site" content="@chris1ding1">
<meta name="twitter:description" content="">
<meta name="twitter:image" content="https://">
<meta name="twitter:image:alt" content="" />
```
