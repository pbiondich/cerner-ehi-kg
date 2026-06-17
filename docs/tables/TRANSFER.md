# TRANSFER

> Contains a record for every time a product is transferred to another facility or refrigerated location.

**Description:** Transfer  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `LOGIN_COND_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 6 | `LOGIN_DT_TM` | DATETIME |  |  | Table is not used yet. Possibly obsolete |
| 7 | `LOGIN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Table is not used yet. Possibly obsolete |
| 8 | `LOGIN_QTY` | DOUBLE |  |  | Table is not used yet. Possibly obsolete |
| 9 | `LOGIN_VIS_INSP_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 10 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Table is not used yet. Possibly obsolete |
| 11 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Table is not used yet. Possibly obsolete |
| 12 | `RETURN_COND_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 13 | `RETURN_DT_TM` | DATETIME |  |  | Table is not used yet. Possibly obsolete |
| 14 | `RETURN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Table is not used yet. Possibly obsolete |
| 15 | `RETURN_QTY` | DOUBLE |  |  | Table is not used yet. Possibly obsolete |
| 16 | `RETURN_REASON_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 17 | `RETURN_VIS_INSP_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 18 | `TRANSFERRING_LOCN_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 19 | `TRANSFER_COND_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 20 | `TRANSFER_QTY` | DOUBLE |  |  | Table is not used yet. Possibly obsolete |
| 21 | `TRANSFER_REASON_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 22 | `TRANSFER_VIS_INSP_CD` | DOUBLE | NOT NULL |  | Table is not used yet. Possibly obsolete |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGIN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `RETURN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

