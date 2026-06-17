# TRANS_COMMIT_ASSAY

> Contains the discrete task assays applicable to each product with transfusion committee criteria defined. Used by the transfusion committee report.

**Description:** Transfusion Committee Assay table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALL_RESULTS_IND` | DOUBLE | NOT NULL |  | Indicates whether all of the patient's results for this discrete task assay should be printed on the transfusion committee report. |
| 6 | `POST_HOURS` | DOUBLE | NOT NULL |  | Defines the number of hours after the transfusion for which results of this discrete task assay should print for the patient transfused. |
| 7 | `PRE_HOURS` | DOUBLE | NOT NULL |  | Defines the number of hours before the transfusion for which results of this discrete task assay should print for the patient transfused. |
| 8 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The code value representing the discrete task assay defined that should be reported for transfusions of a certain type of product. |
| 9 | `TRANS_COMMIT_ASSAY_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number. The primary key to this table that ensures the uniqueness of each row. |
| 10 | `TRANS_COMMIT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the row on the transfusion_committee table for which this row is associated. This is done to link the discrete task assay information defined on this table to the transfusion_committee table, where the product type is defined. It is an internal system-assigned number. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `TRANS_COMMIT_ID` | [TRANSFUSION_COMMITTEE](TRANSFUSION_COMMITTEE.md) | `TRANS_COMMIT_ID` |

