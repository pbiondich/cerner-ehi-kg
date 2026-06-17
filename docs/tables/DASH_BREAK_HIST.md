# DASH_BREAK_HIST

> Tracks the BREAK History of a given Provider

**Description:** DASHBOARD BREAK HISTORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXCLUDE_IND` | DOUBLE | NOT NULL |  | Indicates if the provider should be excluded from the chart data |
| 2 | `POSITION_IDENT` | VARCHAR(100) |  |  | A string value showing the positon for each provider put in the table |
| 3 | `PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | A Foreign Key value from the PRSNL table |
| 4 | `PROVIDER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies type of provider. 1 = Anesthesia Provider. |
| 5 | `RECORD_DT_TM` | DATETIME |  |  | Indicator of what day the row is relevant to |
| 6 | `STATUS_DT_TM` | DATETIME |  |  | Date and Time the status was updated |
| 7 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the current break status of the provider. 0 = A break is needed, 1 = The provider has received their break, 2 = The provider can break themselves |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

