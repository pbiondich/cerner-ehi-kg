# MSG_FYI_FILTER_DTL

> Holds detailed information on a results FYI filter. These filters determine which new results will automatically display in the physician's inbox.

**Description:** MSG_FYI_FILTER_DTL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FILTER_TYPE_CD` | DOUBLE | NOT NULL |  | Value from code set 3414 that represents the type of filter. Can be lifetime relation, encounter relation, encounter, or event. |
| 3 | `FILTER_VALUE_CD` | DOUBLE | NOT NULL |  | Holds the encounter or relation code value from code sets 331, 333, or 71 to be filtered. Will be zero when the filter type code is event. |
| 4 | `FILTER_VALUE_TXT` | VARCHAR(100) |  |  | Holds the event set name being filtered. Only populated when the filter type code is event. |
| 5 | `MSG_FYI_FILTER_DTL_ID` | DOUBLE | NOT NULL |  | Primary key |
| 6 | `MSG_FYI_FILTER_ID` | DOUBLE | NOT NULL | FK→ | The filter associated with this detail |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MSG_FYI_FILTER_ID` | [MSG_FYI_FILTER](MSG_FYI_FILTER.md) | `MSG_FYI_FILTER_ID` |

