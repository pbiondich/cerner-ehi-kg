# ORDER_CATALOG_REVIEW

> Controls routing of nurse review, doctor cosign and pharmacy verify.

**Description:** ORDER CATALOG REVIEW  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Order Action Type: Order, Modify, Cancel, Discontinue |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Unique identifier for orderable items. |
| 3 | `COSIGN_REQUIRED_IND` | DOUBLE |  |  | On hold until doctor cosigns it. |
| 4 | `DOCTOR_COSIGN_FLAG` | DOUBLE |  |  | 0 - No Cosign Needed 1 - Ordering Physician Provider_id 2 - Attending Physician Provider_id 3 - Order detail Provider_id |
| 5 | `NURSE_REVIEW_FLAG` | DOUBLE |  |  | 0 - No verify needed 1 - Location_cd = ordering location 2 - Location _cd = patient location 3 - Order detail defines provider_id 4 - Order detail defines location_cd |
| 6 | `REVIEW_REQUIRED_IND` | DOUBLE |  |  | On Hold until a nurse reviews it |
| 7 | `RX_VERIFY_FLAG` | DOUBLE |  |  | 0 - No verify needed. 2 - Required in On Hold status. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

