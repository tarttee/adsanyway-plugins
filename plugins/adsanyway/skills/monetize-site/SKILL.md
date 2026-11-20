---
name: monetize-site
description: Put a paid ad slot on the user's website or blog with AdsAnyway and get it listed for advertisers. Use when someone wants to earn from their site, sell ad space, add a banner slot, or asks "how do I monetize my site".
---

# Sell ad space on a site

AdsAnyway sells a site's ad slot by the day to advertisers who want that audience. The owner keeps 85% of each booking.

1. Ask for the site URL if you do not have it. Pass `monthly_visits` only if the owner gives it or you read it from their analytics. Never estimate it.
2. Call `monetize_site` with the URL (and `monthly_visits`, `category`, `description` when known). It creates the site and a 728x90 daily slot and returns the embed snippet, the WordPress plugin link, `price_per_day` and `next_steps`.
   - For a sidebar or square slot, pass `width` and `height` (300x250 is the common one). Call `create_zone` for a second slot on the same site.
3. Install the snippet:
   - If you can edit the site's code, paste `snippet` into the page template where the ad should show, right where the slot should appear. Do not change the snippet.
   - On WordPress, give the owner `wordpress_plugin_url`; `get_embed` also returns a `shortcode`.
   - Otherwise show the snippet and say where it goes.
4. After the page is live, call `check_install`. `installed` turns true on the first ad load and the slot appears on the marketplace. If false, open the page once and check again.
5. Tell the owner the price per day in dollars, that unsold days show a house ad pointing buyers to the slot, and that they can change the price with `update_zone`.

Selling quarter shares of a day: `update_zone` with `share_price_cents`. Auto pricing: `auto_price` with `price_floor_cents` and `price_ceiling_cents`.

Prices are in cents in the API; show dollars to people.
