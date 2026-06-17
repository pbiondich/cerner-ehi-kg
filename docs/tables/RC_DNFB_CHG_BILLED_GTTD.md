# RC_DNFB_CHG_BILLED_GTTD

> This is a per-session temp table used by the DNFB evaluation process in determining billed charges for the encounters being evaluated.

**Description:** Revenue Cycle DNFB Charge Billed Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_ID` | DOUBLE | NOT NULL |  | This id references the row on the trans_log table that corresponds to the initial posting of the charge that this row represents. |
| 2 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | This id references a specific charge on the charge table that has been included on a bill related to the pft_encntr_id. |
| 3 | `NET_CHARGE_AMT` | DOUBLE | NOT NULL |  | This field represents the net charge amount for the current charge, taking credits into consideration. |
| 4 | `OFFSET_CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | This id references a specific row on charge table represents a credit of a charge that has been included on a bill related to the pft_encntr_id. |
| 5 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL |  | This id references the pft_charge row associated with this charge. |
| 6 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL |  | This id identifies a specific financial encounter in the pft_encntr table for which the DNFB evaluation service is currently being executed for a specified date. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

