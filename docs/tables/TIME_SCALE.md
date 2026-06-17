# TIME_SCALE

> Time scale definition for some Powerchart components. Used in IO2G

**Description:** TIME SCALE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERVAL_LABEL_FLAG` | DOUBLE |  |  | determines how to label an interval |
| 2 | `INTERVAL_LENGTH` | DOUBLE |  |  | length of an interval |
| 3 | `INTERVAL_UNITS_CD` | DOUBLE | NOT NULL | FK→ | time unit for interval |
| 4 | `NBR_OF_INTERVALS` | DOUBLE |  |  | defines the number of intervals in a day |
| 5 | `TIME_SCALE_ID` | DOUBLE | NOT NULL |  | primary key to the time scale table |
| 6 | `TIME_SCALE_NAME` | VARCHAR(60) | NOT NULL |  | Name of the time scale |
| 7 | `TIME_SCALE_NAME_KEY` | VARCHAR(60) | NOT NULL |  | Uppercase name as index |
| 8 | `TIME_SCALE_START_TM` | DATETIME |  |  | Start time for time scale |
| 9 | `TIME_SCALE_START_TM_LONG` | DOUBLE |  |  | Time scale start time stored as a long datatype |
| 10 | `TIME_SCALE_TYPE_FLAG` | DOUBLE | NOT NULL |  | time scale type |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERVAL_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

