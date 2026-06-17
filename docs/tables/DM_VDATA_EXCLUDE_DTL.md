# DM_VDATA_EXCLUDE_DTL

> Store reasons a table cannot be compared by a data compare process between 2 databases

**Description:** DM_VDATA_EXCLUDE_DTL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_VDATA_EXCLUDE_DTL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `DM_VDATA_MASTER_ID` | DOUBLE | NOT NULL | FK→ | FK to DM_VDATA_MASTER |
| 3 | `EXCLUDE_REASON_FLAG` | DOUBLE | NOT NULL |  | Reasons a table is excluded from the compare process. 10= 'Table does not have a single, numeric, uniquely indexed column'. 20 = 'Table has an unsupported data type.' 30 = 'Table marked for downtime Migration'. |
| 4 | `EXCLUDE_REASON_TXT` | VARCHAR(1000) |  |  | Text will contain the description as specified above. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_VDATA_MASTER_ID` | [DM_VDATA_MASTER](DM_VDATA_MASTER.md) | `DM_VDATA_MASTER_ID` |

