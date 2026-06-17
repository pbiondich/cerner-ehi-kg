# SCH_EVENT_RECUR_COMM

> Scheduling comments for event recurring instances.

**Description:** Scheduling Event recur comment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_RECUR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the SCH_EVENT_RECUR_COMM table |
| 2 | `SCH_EVENT_RECUR_COMM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_EVENT_RECUR_COMM table. |
| 3 | `SUB_TEXT_CD` | DOUBLE | NOT NULL |  | The identifier for the scheduling text sub-type. |
| 4 | `TEXT_ID` | DOUBLE | NOT NULL | FK→ | Text Identifier |
| 5 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL |  | The identifier for the scheduling text type |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_RECUR_ID` | [SCH_EVENT_RECUR](SCH_EVENT_RECUR.md) | `EVENT_RECUR_ID` |
| `TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

