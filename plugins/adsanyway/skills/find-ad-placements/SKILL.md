---
name: find-ad-placements
description: Find and book banner ad slots on niche and gaming sites for the user's game, app or product with AdsAnyway. Use when someone wants to advertise, buy ads, find sites for their audience, or plan an ad budget.
---

# Find slots and get them booked

1. Learn what is being promoted: the URL, who it is for, the budget in dollars (if any) and how many days.
2. Call `search_marketplace` with `q` (audience words such as "cozy fishing game"), and `days`. With a budget, pass `budget_cents` (the total) and `days`; each row's `total_cents` then fits it and `next_open_date` is the first day the run is free.
3. Pick 3 to 5 slots. Match the audience first (category, site description), then prefer low `cost_per_1k_loads_cents` and early open dates. For each give the site, slot size, why it fits, price per day and total in dollars, and expected views from `forecast` when present. Never promise clicks or sales.
4. A banner is needed at a size the slot accepts (`get_listing` -> `accepted_sizes`). Use `list_creatives` for existing banners, or the make-banner skill.
5. For each slot the user picks, call `prepare_booking` with `zone_id`, `creative_id`, and `start_date` (use `next_open_date`) plus `days`. It checks size, ad type, dates and price and holds nothing.
6. Give the user each `review_url` with the slot, dates and total in dollars. They book and pay on AdsAnyway, from their balance or by card (`pays_from` says which). Never say a slot is booked until `list_campaigns` shows it.

If the seller approves bookings (`require_seller_approval`), say the booking starts once they approve.
