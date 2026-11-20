# AdsAnyway plugins

[AdsAnyway](https://adsanyway.com) is a marketplace for banner ad slots on niche and gaming sites. Advertisers reach engaged, relevant audiences; site owners keep 85% of each booking.

These plugins connect your AI app to AdsAnyway. Your agent does the work: it sets up ad slots on your site, finds slots for your product, makes banners, checks bookings and reads results. You book, top up and withdraw on adsanyway.com.

## Claude Code

```
/plugin marketplace add tarttee/adsanyway-plugins
/plugin install adsanyway@adsanyway
```

Then run `/mcp`, pick **adsanyway** and sign in with your AdsAnyway account.

## Claude and ChatGPT apps

Find **AdsAnyway** in the Claude connector directory or in ChatGPT's plugins and connect it. Until the listing is live, add a custom connector with the address `https://adsanyway.com/mcp`. See [adsanyway.com/agents](https://adsanyway.com/agents).

## What is inside

| Path | What it is |
| --- | --- |
| `.claude-plugin/marketplace.json` | Claude Code marketplace |
| `plugins/adsanyway` | Claude plugin: the AdsAnyway MCP server and skills |
| `plugins/adsanyway/skills` | Skills shared by both plugins: monetize-site, find-ad-placements, make-banner, check-results |
| `chatgpt/` | ChatGPT plugin manifest and MCP config |
| `build.py` | Builds `dist/adsanyway-chatgpt.zip` |

The MCP server is `https://adsanyway.com/mcp/app` (OAuth sign-in). It shows interactive cards in Claude and ChatGPT. The full server at `https://adsanyway.com/mcp` also lets an agent book from your AdsAnyway balance.

## Privacy and support

- Privacy: https://adsanyway.com/privacy
- Terms: https://adsanyway.com/terms
- Support: hello@adsanyway.com

## License

MIT
