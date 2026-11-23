# OSIQ 30: the public record

**OSIQ 30** (the OpenStrategy Institutional Quality Index) is a public research benchmark of 30 externally operated onchain trading strategies on Hyperliquid, selected under our rules and measured on the whole account every day. Inception 1 July 2026 at 100.00; published daily since 17 July 2026. Every observation is published, drawdowns included, and corrections are issued under a published policy.

It is the selection and measurement method, on record. It is research evidence: not investable, and not client returns.

## Figures at this snapshot

From the daily publication of 23 November 2026. The live numbers are always at the endpoints below; this table goes stale by one observation a day.

| Fact | Value |
| --- | --- |
| Latest level | 130.18 (146 daily observations) |
| Since inception (1 Jul 2026) | +30.18% |
| Maximum drawdown (daily observations) | 11.03%, 16 Aug 2026 peak to 22 Aug 2026 trough, each observation published on its date |
| Daily-return correlation to bitcoin | 0.06 over the record: 145 matched daily-return pairs, 1 Jul to 23 Nov 2026, OSIQ 30 daily returns against Hyperliquid BTC daily-open-to-daily-open returns by UTC date |
| Realised volatility, annualised | 23.7% |
| Corrections issued | 1, under the public corrections policy |
| Classification | Public research benchmark · Not investable |

Drawdown is measured on daily observations; intraday losses may be larger. The correlation describes this research window and may change.

Canonical endpoints, no login:

- [Daily history CSV](https://openstrategy.trade/api/index/history.csv)
- [Record JSON](https://openstrategy.trade/api/index/record.json)
- [Full public record](https://openstrategy.trade/index/)

The snapshot in [`data/`](data/) mirrors the live history and record for 23 November 2026, with the record trimmed to the fields this page and the verifier use. Verify it, or the live record, with `python3 ../tools/verify_osiq_record.py [--live]`.

## What the record shows

- **The whole account, not a slice of it.** Each trader's record is rebuilt across perpetuals, spot, lending and staking, with deposits and withdrawals separated from returns, so risk is measured against everything the trader holds.
- **Drawdowns are left in.** The index fell 11.03% from its 16 August peak to its 22 August trough, and every observation of it was published on its date.
- **Suspensions are published.** Suspensions are recorded on the public record alongside results.
- **Corrections are published.** One correction has been issued, for the 25 August 2026 observation, with the reason, under the published corrections policy.

Research behind the method:

- [October 2026 monthly note](https://openstrategy.trade/research/index/monthly-note-2026-10/)
- [September 2026 monthly note](https://openstrategy.trade/research/index/monthly-note-2026-09/)
- [July 2026 monthly note](https://openstrategy.trade/research/index/monthly-note-2026-07/)
- [Correlation in an asset is a condition. In a strategy, it is behaviour.](https://openstrategy.trade/research/index/correlation-notes-2026-08/)
- [Onchain has two ways to tell you a trader is good. Neither one is ever re-tested.](https://openstrategy.trade/research/measurement/two-labels-never-re-tested/)
- [Collateral-basis valuation: what a wallet is actually worth.](https://openstrategy.trade/research/measurement/what-a-wallet-is-actually-worth/)
- [Methodology](https://openstrategy.trade/methodology/) · [Corrections log](https://openstrategy.trade/corrections/)

## Boundaries

OpenStrategy observes the strategies in OSIQ 30. It does not trade them. Clients never buy the basket: they use the research to choose traders and build their own portfolios. Index data is published for research citation with attribution; see the [terms](https://openstrategy.trade/terms/). Index inclusion does not constitute an investment recommendation, institutional approval, or a conclusion that a strategy is accessible or investable. Constituent identities are not published. Research and information only. Not investment advice.
