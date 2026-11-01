# Evaluation methodology and assumptions

**Source:** Final MGS402 cloud vendor recommendation memo, dated October 25, 2026. This document explains the original analysis rather than representing a new production assessment.

## Fictional client and decision objective

Lakefront Retail operates 25 stores with approximately 600 employees and a six-person IT team. The existing data-center lease ends in nine months. Most internal IT experience is in Microsoft 365, SQL Server, Windows Server, and Active Directory.

The decision objective was to recommend an affordable, operationally feasible migration destination without ignoring compatibility, backup, and security requirements.

## Weighted criteria

| Criterion | Weight | Azure | AWS | Google Cloud |
|:--|--:|--:|--:|--:|
| Lease deadline | 30% | 4.00 | 3.00 | 3.00 |
| Three-year cost | 25% | 5.00 | 2.88 | 3.66 |
| Reliability/SLA | 15% | 3.00 | 3.00 | 3.00 |
| Security/PCI responsibilities | 15% | 3.00 | 3.00 | 3.00 |
| Team skills | 10% | 4.00 | 3.00 | 3.00 |
| Exit costs and lock-in | 5% | 3.00 | 3.00 | 3.00 |
| **Weighted total** | **100%** | **3.90** | **2.97** | **3.16** |

The model used a scale of 1 (major weakness) to 5 (strong fit). Cost scores were computed as:

**Cost score = 5 × lowest modeled three-year TCO ÷ provider modeled three-year TCO**

Weighted totals sum each criterion score multiplied by its weight. Totals should be calculated using **unrounded cost scores**, so a displayed Google Cloud cost score of 3.66 still produces a weighted total of about 3.16.

The other providers' reliability, security, and lock-in scores were deliberately tied at 3 because the available evidence did not establish meaningful differences on those criteria. A tied score does not establish identical real-world security or reliability.

## Three-year TCO components

| Component | Azure | AWS | Google Cloud |
|:--|--:|--:|--:|
| Year 1 cloud services | $47,918 | $104,293 | $73,093 |
| Year 2 cloud services | $49,976 | $109,625 | $79,563 |
| Year 3 cloud services | $52,447 | $116,024 | $87,326 |
| Cloud services subtotal | $150,341 | $329,943 | $239,982 |
| Migration/training | $31,000 | $31,000 | $31,000 |
| Internal staff time | $62,400 | $62,400 | $62,400 |
| **Total modeled TCO** | **$243,741** | **$423,343** | **$333,382** |

Annual values are rounded; the AWS subtotal is $1 higher than the sum of the displayed annual values because of rounding in the original report.

**Assumptions:** Pricing estimates were collected around October 24, 2026. Storage-related spending was assumed to grow 20% annually. Compute needs, network usage, and other prices were held constant. Migration/training and internal staff-time allocations were modeled rather than sourced from firm vendor bids.

## What the model does not prove

1. The service configurations are **not fully like-for-like**, including storage and recoverability.
2. Real-world workloads, performance, backup coverage, and application dependencies were not measured.
3. Pricing is a dated estimate, not a purchase commitment or guaranteed future cost.
4. The security and PCI scores are provisional; requirements remain to be scoped and validated.
5. A production choice requires formal compatibility, cost, security, and recovery gates.

**Interpretation:** Azure ranked highest for this scenario, but the recommendation is contingent on tests and approvals rather than a general claim that Azure is always cheapest or best.
