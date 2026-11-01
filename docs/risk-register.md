# Risk register — Lakefront Retail cloud migration

The risks below are extracted from and organized around the academic report. Severity labels are **qualitative discussion aids**, not results of a completed formal risk assessment.

| Risk | Why it matters | Proposed mitigation | Gate/owner |
|:--|:--|:--|:--|
| Legacy application incompatibility | ERP or inventory software may fail or need costly changes | Obtain vendor confirmation; test real workflows before commitments | Application owners / IT lead |
| Lease deadline miss | Delayed cutover may force unplanned hosting or downtime | Stage migration; finish by month eight; preserve one-month buffer and alternate-hosting option | Project sponsor |
| RPO mismatch | Once-daily backups cannot reliably meet a one-hour recovery point objective | Evaluate more frequent data protection, replication, and restore tests | IT operations / business sponsor |
| Recovery not validated | A low estimated cloud bill does not guarantee operational resilience | Confirm acceptable RTO/RPO and run recovery drills | Business continuity owner |
| Unclear PCI scope | Outsourced payment processing does not eliminate all internal obligations | Document data flows, systems, access, and in-scope controls | Security/compliance owner |
| Incomplete like-for-like pricing | Storage tiers, data restoration windows, and backup coverage differ by provider | Normalize configurations and rerun costs before purchase | Finance / cloud lead |
| Limited internal capacity | Six-person team may lack cloud architecture and migration experience | Training, staged migration, documented runbooks, specialist support | IT manager |
| Narrow SLA service credits | Database credits may not compensate business losses | Confirm exclusions, claim window, monitoring, and resilience strategy | Procurement / IT |
| Vendor lock-in and exit costs | Future change may incur technical and transfer costs | Maintain data-export procedures and exit-cost assumptions | Architecture / finance |

No vulnerabilities were exploited and no live business environment was assessed as part of this project.
