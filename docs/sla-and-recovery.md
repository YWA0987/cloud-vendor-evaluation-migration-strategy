# Service-level agreement and recovery analysis

## What the report examined

The October 2026 recommendation evaluated a selected Microsoft database service's published availability commitment of **99.995%**, subject to configuration and service agreement conditions. It also considered credits, claim deadlines, and what those credits do **not** protect.

The original memo illustrated a **qualifying one-hour outage within a 30-day month**, resulting in an approximately **$225 service credit** for eligible database charges under the stated scenario. The memo identified a **60-day claim window** and noted exclusions, including some planned maintenance and customer-caused failures.

> This is a dated interpretation of the agreement as discussed in the original academic report, **not a guarantee that a real outage would qualify or produce this credit**. Verify current service terms before relying on it.

## Why the credit is insufficient

- Credits may apply only to the **eligible database service**, not all systems used by stores.
- Credits reduce fees; they do not reimburse lost sales, wages, or customer disruption.
- An availability commitment is not the same as a tested disaster-recovery capability.
- Eligibility depends on deployment configuration, observed outage details, documentation, exclusions, and submission timing.

## Business recovery targets

The report proposed the following limits for management to approve and validate:

| Metric | Proposed target | Meaning |
|:--|:--|:--|
| Recovery Time Objective (RTO) | 4 hours | Longest acceptable service interruption |
| Recovery Point Objective (RPO) | 1 hour | Maximum acceptable loss of recent work |

**Critical gap:** A daily-only backup schedule leaves up to roughly 24 hours of potential data loss and does **not** satisfy a one-hour RPO. More frequent protection, replication, or a different recovery architecture must be tested and costed.

## Recommended validation

1. Define business-approved RTO/RPO by workload, not as a blanket assumption.
2. Map backup/replication options to those targets and include recurring storage costs.
3. Test restores and failover with realistic datasets.
4. Confirm identity and network dependencies do not undermine restoration.
5. Document owner responsibilities, alerting, and evidence retention for SLA claims.
