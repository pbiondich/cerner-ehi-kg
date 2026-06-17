# RAD_CRITICAL_RESOLVE

> Contains the resolution details provided by the physician for exams with normalcy indicators.

**Description:** RadNet Criticality Resolution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This column is a foreign key to the order_radiology table. It uniquely identifies the order/procedure that the resolution is for. |
| 2 | `RAD_CRITICAL_RESOLVE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_CRITICAL_RESOLVE table. |
| 3 | `RESOLUTION_CD` | DOUBLE | NOT NULL |  |  |
| 4 | `RESOLUTION_COMMENT_TXT` | VARCHAR(255) |  |  |  |
| 5 | `RESOLUTION_DT_TM` | DATETIME |  |  | the date/time stamp when the physician marked procedure's cruciality as resolved. |
| 6 | `RESOLUTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `RESOLUTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

