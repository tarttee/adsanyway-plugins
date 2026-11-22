---
name: check-results
description: Show how AdsAnyway ads and ad slots are doing and what to do next, for buyers (ads served, clicks, cost per click, run it again) and sellers (loads, earnings, incoming bookings, price). Use when someone asks how their ads, campaigns, slots or earnings are doing.
---

# Results and next steps

## Buyer
1. `list_campaigns` for their bookings and status.
2. `report` with `campaign_id` for daily ads served, clicks and CTR. Cost per click and per 1,000 ads show once a run ends.
3. Say plainly what worked: the best slots by CTR and cost per click. Compare only like with like (same banner size).
4. To run a good slot again: `prepare_booking` with the same `zone_id` and `creative_id`, `days` = `run_days`, `start_date` = `next_open_date`, then give the `review_url`.
5. A live booking can be paused with `pause_campaign`. A pending one is cancelled on its campaign page on AdsAnyway.

## Seller
1. `list_zones` for each slot's price, open days, loads a day and earnings.
2. `report` with `zone_id` for 30 days of loads, paid loads and clicks.
3. `list_seller_bookings` for incoming bookings. If one waits for approval, show the banner and dates; the owner approves or declines it in the AdsAnyway dashboard.
4. `wallet` shows earnings and what can be withdrawn; withdrawals happen at `wallet_url` on AdsAnyway.
5. If a slot has few open days, suggest a higher price; if it sells nothing for weeks, a lower one or quarter shares (`update_zone`).

Money is cents in the API; show dollars.
