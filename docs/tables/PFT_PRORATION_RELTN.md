# PFT_PRORATION_RELTN

> This table stores information on all modifications made to the Proration tables.

**Description:** This table stores information on all modifications made to the Proration tables  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Related activity that caused the difference. |
| 6 | `AMOUNT_CHANGED_CD` | DOUBLE | NOT NULL |  | This is the type of value modified. (Current, Original, Deductible, Original Deductible) - See New Code Set - Amount_Changed_CD |
| 7 | `AMOUNT_DIFFERENCE` | DOUBLE | NOT NULL |  | Difference between New and Old Amount from the perspective of the Old Amount |
| 8 | `AMOUNT_DIFFERENCE_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag associated with the Amount_Difference. |
| 9 | `MODIFICATION_FLAG` | DOUBLE |  |  | This flag states whether the modification was manual (1) or automatic (0) |
| 10 | `MODIFICATION_REASON_CD` | DOUBLE | NOT NULL |  | Reason for the modification - See New Code Set - Modification_Reason_CD |
| 11 | `NEW_AMOUNT` | DOUBLE | NOT NULL |  | New Amount after modification |
| 12 | `NEW_AMOUNT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag associated with the New Amount. |
| 13 | `OLD_AMOUNT` | DOUBLE | NOT NULL |  | Old Amount before modification |
| 14 | `OLD_AMOUNT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag associated with the Old Amount. |
| 15 | `PFT_PRORATE_DEDUCT_ID` | DOUBLE | NOT NULL |  | Pft Proration Deduct Identifier |
| 16 | `PFT_PRORATION_ID` | DOUBLE | NOT NULL | FK→ | PFT Proration Identifier |
| 17 | `PFT_PRORATION_RELTN_ID` | DOUBLE | NOT NULL |  | Primary Key: Built from pft_charge_seq |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `PFT_PRORATION_ID` | [PFT_PRORATION](PFT_PRORATION.md) | `PFT_PRORATION_ID` |

