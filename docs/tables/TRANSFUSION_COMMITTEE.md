# TRANSFUSION_COMMITTEE

> Defines the criteria by which the Transfusion Committee Report determines what products to track and report.

**Description:** Transfusion Committee  
**Table type:** REFERENCE  
**Primary key:** `TRANS_COMMIT_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALL_RESULTS_IND` | DOUBLE |  |  | Indicates whether all of the patient's results for this discrete task assay should be printed on the transfusion committee report. |
| 6 | `INV_AREA_CD` | DOUBLE | NOT NULL |  | The location (inventory area) of products to which this transfusion committee parameter applies. |
| 7 | `OWNER_CD` | DOUBLE | NOT NULL |  | The location (owner area) of products to which this transfusion committee parameter applies. |
| 8 | `POST_HOURS` | DOUBLE |  |  | Defines the number of hours before the transfusion for which results of this discrete task assay should print for the patient transfused. (NO LONGER USED) |
| 9 | `PRE_HOURS` | DOUBLE |  |  | Defines the number of hours before the transfusion for which results of this discrete task assay should print for the patient transfused. (NO LONGER USED in Rev 5) |
| 10 | `PRODUCT_CD` | DOUBLE | NOT NULL | FK→ | The code value that represents the type of product for which transfusion committee criteria is defined. An example of a product type is "Red Blood Cells". |
| 11 | `SINGLE_HOURS` | DOUBLE |  |  | NO LONGER USED IN REV 5. Replaced with SINGLE_PRE_HOURS and SINGLE_POST_HOURS. Will be removed completely in Rev 6. |
| 12 | `SINGLE_POST_HOURS` | DOUBLE | NOT NULL |  | Identifies the number of hours post-transfusion that define this type of product as being a "single transfusion". |
| 13 | `SINGLE_PRE_HOURS` | DOUBLE | NOT NULL |  | Identifies the number of hours pre-transfusion that define this type of product as being a "single transfusion". |
| 14 | `SINGLE_TRANS_IND` | DOUBLE | NOT NULL |  | Indicates whether single transfusions should be reported for this type of product transfused. |
| 15 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The code value representing the discrete task assay defined that should be reported for transfusions of a certain type of product. |
| 16 | `TRANS_COMMIT_ID` | DOUBLE | NOT NULL | PK | An internal system-assigned number that is the primary key to this table, and ensures the uniqueness of each row. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_CD` | [PRODUCT_INDEX](PRODUCT_INDEX.md) | `PRODUCT_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRANS_COMMIT_ASSAY](TRANS_COMMIT_ASSAY.md) | `TRANS_COMMIT_ID` |

