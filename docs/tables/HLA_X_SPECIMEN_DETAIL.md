# HLA_X_SPECIMEN_DETAIL

> Stores detail information related to a cross specimen antibody screen analysis.

**Description:** HLA Cross Specimen Analysis Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies the tray selected for use in the cross specimen analysis. |
| 2 | `CROSS_SPECIMEN_DETAIL_ID` | DOUBLE | NOT NULL |  | A column used to create a unique identifier for the HLA__X_SPECIMEN_DETAIL table. |
| 3 | `CROSS_SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Relates information to a saved cross specimen analysis. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order id that is related to the tray used in the cross specimen analysis. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_ID` | [HLA_AB_SCREEN_BATCH](HLA_AB_SCREEN_BATCH.md) | `BATCH_ID` |
| `CROSS_SPECIMEN_ID` | [HLA_X_SPECIMEN_ANALYSIS](HLA_X_SPECIMEN_ANALYSIS.md) | `CROSS_SPECIMEN_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

