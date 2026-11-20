---
name: make-banner
description: Make an ad banner for an AdsAnyway slot, from an image file or from a headline, and add it to the user's account. Use when someone needs a banner, creative or ad image for a booking, or a banner was rejected for its size.
---

# Make a banner

Check the size first: `get_listing` for the slot gives `accepted_sizes` and `ad_types`. Common sizes are 728x90 and 300x250.

Pick the first route that works:

1. **An image the user already hosts**: `create_creative` with `image_url` (a permanent public URL), `click_url`, `width`, `height`.
2. **An image file you made or the user gave you**:
   - With a shell: call `upload_link`, then send the file with curl to the URL it returns, as it describes. The upload returns `creative_id`.
   - Without a shell: `create_creative` with `image_base64`.
   Make the file exactly the slot size, PNG, JPG, GIF or WebP, 5 MB max.
3. **No image**: `create_text_banner` with `headline` (60 chars max), `click_url`, an optional `subline` and `cta`, the slot `width` and `height`, and colors that suit the product (`background`, `color`, `accent` as hex). Keep the headline short enough to read at a glance.

Show the user the banner's `image_url` before booking. Every banner goes through AdsAnyway review (`ad_policy` lists what is accepted); `list_creatives` shows `review_status`.

The click URL must be the user's own page. Do not use someone else's trademark or claims you cannot back up.
