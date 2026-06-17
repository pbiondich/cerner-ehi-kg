# OMF_RADTECH_ORDER_ST

> Summary table storing technician information for radiology mgmt.

**Description:** OMF RADTECH ORDER ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OMF_RADTECH_ORDER_ST_ID` | DOUBLE | NOT NULL |  | Unique identifier for omf_radtech_order_st |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identification number for the order. |
| 3 | `PRIMARY_PRSNL_IND` | DOUBLE | NOT NULL |  | Indicates if the personnel was the primary personnel to start/complete the exam. |
| 4 | `ROLE_CD` | DOUBLE | NOT NULL |  | Stores the role that the personnel performed during the exam. |
| 5 | `TECHNOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | The technologist responsible for the order. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `TECHNOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

