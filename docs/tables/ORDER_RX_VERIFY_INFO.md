# ORDER_RX_VERIFY_INFO

> Stores information about pharmacy verification for orders.

**Description:** Order Rx Verify Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICAL_REVIEW_COMPLETED_CNT` | DOUBLE |  |  | The number of clinical reviews a pharmacist has completed for the order. |
| 2 | `CLINICAL_REVIEW_REQD_PREF_CD` | DOUBLE |  |  | The preference code defining the multiple pharmacy verification behavior currently assigned to the order. |
| 3 | `CLINICAL_REVIEW_REQUIRED_CNT` | DOUBLE |  |  | The number of clinical reviews required by a pharmacist for the order to be considered fully verified. |
| 4 | `LATEST_ORIGINATING_ACTION_SEQ` | DOUBLE |  |  | The latest action sequence on an order from which an rx verify group originated. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the associated order. |
| 6 | `ORDER_RX_VERIFY_INFO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_RX_VERIFY_INFO table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

