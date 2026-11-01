# Proposed migration and decision gates

**Context:** Fictional Lakefront Retail scenario. The data-center lease ends at the end of month nine. The original recommendation sought completion by month eight, leaving a one-month contingency buffer.

The phase breakdown below is an **illustrative portfolio elaboration** of the risk-gated strategy described in the October 2026 report; it is not evidence of an implemented migration.

| Window | Workstream | Evidence for go/no-go |
|:--|:--|:--|
| Months 1–2 | Inventory systems and dependencies; consult application vendors; test inventory and accounting workflows | Vendor compatibility signoff and validated critical workflows |
| Months 3–4 | Pilot noncritical workloads; confirm identity, permissions, storage performance, logging, and backup options | Pilot performance and security review |
| Months 5–6 | Stage data migration and validate store connectivity, reporting, backup schedules, and rollback procedures | Successful data integrity checks and recovery tests |
| Month 7 | Conduct cutover rehearsal and confirm staffing, operational runbooks, and escalation contacts | Approved rehearsal and rollback checkpoints |
| Month 8 | Execute production cutover in waves; monitor errors, recovery, and business operations | Business owner acceptance and completion checklist |
| Month 9 | Reserve contingency time for remediation or fallback before lease expiry | Lease exit or approved alternate hosting strategy |

## Mandatory decision gates

- **Compatibility:** Inventory, ERP/accounting, and reporting must run acceptably on the proposed Azure environment.
- **Recovery:** The business must approve downtime and data-loss limits, then verify that the chosen design actually meets them.
- **Security:** Identity, access control, monitoring, data protection, and PCI responsibilities must be defined and tested.
- **Cost:** Include backup, storage performance, support, migration, staffing, and egress—not only compute pricing.
- **Fallback:** Preserve a rollback/temporary hosting plan until the new environment passes acceptance testing.

## Operating model

A small internal IT team would need documented responsibilities for access management, patching, backup checks, cost review, incident escalation, and vendor coordination. Each critical responsibility should have backup coverage.

**Decision rule:** If application compatibility, recovery, or the lease deadline cannot be satisfied within acceptable cost and risk, reconsider Azure and compare alternatives or lease-extension options.
