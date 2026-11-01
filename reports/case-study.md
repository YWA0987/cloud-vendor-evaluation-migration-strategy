# Cloud Vendor Evaluation — Consulting Case Study

**Author:** Wafi Ahmed  
**Course:** MGS 402, University at Buffalo  
**Original memo date:** October 25, 2026  
**Client:** Lakefront Retail (**fictional academic case**)

## Recommendation

I recommended Microsoft Azure for a regional retailer's planned cloud transition because it had the lowest estimated three-year total cost in the modeled scenario and fit the organization's Microsoft-centric IT skills. The recommendation was **conditional** on testing legacy application compatibility, verifying storage and recovery capabilities, confirming security responsibilities, and meeting the lease deadline.

## Business scenario

Lakefront operates about 25 stores and employs about 600 people. A six-person IT team supports Windows Server, Active Directory, SQL Server, Microsoft 365, accounting/ERP, inventory, shared files, and business reporting. Its data-center lease ends in nine months. A poorly documented inventory application presents a key migration risk. A third party processes card payments, but Lakefront still needs to determine its PCI-related responsibilities.

## Decision process

I weighted deadline feasibility at 30% and three-year cost at 25%. Reliability and security each received 15%, team skills 10%, and exit/lock-in 5%.

| Provider | Weighted total |
|:--|--:|
| Azure | 3.90 / 5 |
| Google Cloud | 3.16 / 5 |
| AWS | 2.97 / 5 |

Several non-cost scores were intentionally equal because the data did not demonstrate a provider advantage. This makes the reason for the recommendation more transparent: **modeled price and operational fit**, not an unverified claim of superior security or reliability.

## Cost model

| Provider | Three-year modeled total |
|:--|--:|
| Azure | $243,741 |
| Google Cloud | $333,382 |
| AWS | $423,343 |

The model included a three-year cloud services estimate, $31,000 for migration/training, and $62,400 for internal staff operations. Storage-related spending was assumed to grow 20% each year while other variables remained constant. The model was based on October 2026 pricing assumptions and was not a firm quote.

Azure's estimate was approximately $89.6K below Google Cloud and $179.6K below AWS. This was a **scenario comparison**, not realized savings. The configurations had material differences in storage, performance, and recovery coverage.

## Business continuity, security, and recovery

The study reviewed Microsoft's database SLA and explained why billing credits are not the same as operational recovery. It identified that a once-daily backup does not meet a proposed one-hour RPO and that the organization would have to validate a four-hour RTO through testing. It also identified possible PCI scope, staff skill, storage performance, and application-compatibility gaps.

The project proposed evaluating legacy system compatibility in the first two months, migrating in stages, aiming for month-eight completion, and leaving one month for risk remediation or alternative hosting.

## Key judgment

Azure won the modeled comparison, but a failed inventory or ERP compatibility test could invalidate that recommendation despite the lower cost. The report prioritized decision gates and an explicit fallback rather than presenting a single provider as universally best.

## Portfolio note

This case study summarizes the original **six-page October 25, 2026 academic submission**. It does not represent a live implementation or client engagement. The original document includes pricing calculator evidence in an appendix; the source PDF may be added separately to this folder.
