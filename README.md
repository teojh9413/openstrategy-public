# OpenStrategy

**Investment intelligence for onchain markets.**
The trader intelligence layer for onchain markets, for funds and family offices.

OpenStrategy starts with trader discovery and assessment. We rebuild whole-account records from public onchain data so funds and family offices can understand performance and risk before deciding who merits capital and, with automated execution routing next, back the traders they choose from their own exchange account, under their own limits.

**Website:** [openstrategy.trade](https://openstrategy.trade/) · **Investor deck:** [openstrategy.trade/investordeck](https://openstrategy.trade/investordeck) · **Investor appendix:** [openstrategy.trade/investor-appendix](https://openstrategy.trade/investor-appendix) · **Live record:** [OSIQ 30](https://openstrategy.trade/index/) · **Platform:** [terminal.openstrategy.trade](https://terminal.openstrategy.trade/)

## The investment case

- **Opportunity.** Institutions seeking alpha already pay for investment expertise: in-house teams carry recruiting and fixed costs, external managers and funds of funds carry minimum tickets and capacity constraints, private-bank portfolios delegate the decisions. Onchain markets open a new route: a broader universe of strategies with public trading records, across stocks, commodities, currencies and crypto. Markets that reference stocks, commodities and currencies are perpetual futures, not ownership of the underlying assets.
- **Product.** Find traders, back their strategies. The research platform is available now: curated traders, comparable whole-account records and paper portfolios. Clients choose traders and set allocations. Automated execution routing is next, from the client's own exchange account under limits the client sets. Hyperliquid today; more venues and market intelligence later.
- **Method.** What other platforms show is insufficient for real capital. We measure the whole account, including spot, lending and staking, and test whether skill persists: an independent study of 935,000 wallets over one year (July 2026) found only 19% of the top 10% by PnL stayed there the following month. The OpenStrategy method: whole-account risk, cash-flow-adjusted returns, published selection rules, daily monitoring.
- **Working proof.** OSIQ 30, a public research index of onchain traders selected under our rules, measured since 1 July 2026 and published daily. Drawdowns, suspensions and corrections published. Figures and the check in [`openstrategy/README.md`](openstrategy/README.md).
- **Business model.** AUM-based revenue without taking custody. Free research, free paper portfolios, then a 1% annual service fee on allocated AUM for live allocation, with negotiated institutional rates. No performance fee. No trader pays to be listed.
- **Market.** Singapore, then Hong Kong and Dubai: hubs where institutional capital is concentrated and onchain allocation is still early. In UBS's 2026 global survey, 24% of family offices hold digital assets, and those invested typically allocate about 1%.
- **Ambition.** Our ambition: the MSCI of onchain trading strategies. One intelligence foundation that could power institutional workflows, support financial products built around assessed strategies, and set benchmarks issuers license. Long-term opportunities, subject to commercial and regulatory feasibility; no commercial agreements implied.
- **Moat.** Public data, proprietary intelligence that compounds: whole-account reconstruction that took months of financial engineering; a proprietary selection engine (O.P.E.N.: published principles, proprietary assessment logic); an operating history of selections, suspensions and corrections since July 2026, made before the later outcomes; and, next, execution feedback from client fills.

Client capital never leaves the client's own exchange account. OpenStrategy never runs a fund or holds money.

## What is available and what is next

| Surface | Status | Public evidence |
| --- | --- | --- |
| Research platform: curated traders, comparable whole-account records, paper portfolios | Available now | [Platform](https://terminal.openstrategy.trade/) |
| OSIQ 30 daily public record | Live | [Record](https://openstrategy.trade/index/) · [CSV](https://openstrategy.trade/api/index/history.csv) · [JSON](https://openstrategy.trade/api/index/record.json) |
| Methodology, research and corrections | Live | [Methodology](https://openstrategy.trade/methodology/) · [Research](https://openstrategy.trade/research/) · [Corrections](https://openstrategy.trade/corrections/) |
| Automated execution routing from the client's own exchange account, under the client's limits | Next | [Fees](https://openstrategy.trade/pricing/) |
| Suggested Portfolios: AI-assisted selection and rebalancing | Later release | |
| More venues and market intelligence | Later release | |

## Check the record in three minutes

1. **Open the live record:** [OSIQ 30](https://openstrategy.trade/index/), published daily since 17 July 2026, measured from 1 July 2026, every drawdown included.
2. **Pull the data:** [daily history CSV](https://openstrategy.trade/api/index/history.csv) · [record JSON](https://openstrategy.trade/api/index/record.json). No login, no email required.
3. **Verify the published numbers yourself:** `python3 tools/verify_osiq_record.py --live` recomputes the return and maximum drawdown from the daily series and checks them against the published figures.
4. **Read how it is done:** [methodology](https://openstrategy.trade/methodology/) · [corrections log](https://openstrategy.trade/corrections/) · [research](https://openstrategy.trade/research/).

## Founder

Teo Jun Hao. FX dealer, banker, venture capital, then co-founder of a crypto family office with a quant crypto hedge fund. Built and took two protocols to public token listings and supported US$10m+ in fundraising as COO. Product experience across AI and agentic trading infrastructure. Built OpenStrategy and OSIQ 30. Team: the founder, one technical contributor and two in business development. OpenStrategy is a member of the NVIDIA Inception program.

Pre-seed closing December 2026. Contact: [junhao@openstrategy.trade](mailto:junhao@openstrategy.trade)

## Public proof, not public source

This is a public showcase and verification repository, not the application source.

Included here:

- dated snapshots of the OSIQ 30 public record;
- a zero-dependency verifier for the public record;
- logo files and palette.

Not included here:

- credentials, private evidence or constituent wallet identities;
- selection implementation and internal assessment logic;
- the execution engine or any per-trader dataset;
- private application, infrastructure or customer information.

No open-source licence is granted by this repository. Public index-data use is governed by the [OpenStrategy terms](https://openstrategy.trade/terms/).

## Repository map

- [`openstrategy/README.md`](openstrategy/README.md): OSIQ 30, what it is, the figures at this snapshot and what the record shows.
- [`openstrategy/data/`](openstrategy/data/): public-record snapshot through the 23 November 2026 observation.
- [`tools/verify_osiq_record.py`](tools/verify_osiq_record.py): deterministic public-record verification, local or live.
- [`brand/`](brand/): logo files and palette.

Research and information only. Not investment advice. OSIQ 30 is a public research benchmark and is not investable. It demonstrates the selection and measurement method and does not represent client returns. Index inclusion is not an investment recommendation.

© 2026 NVIDIA, the NVIDIA logo, and NVIDIA Inception are trademarks and/or registered trademarks of NVIDIA Corporation in the U.S. and other countries.
