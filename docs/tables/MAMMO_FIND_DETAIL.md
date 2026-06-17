# MAMMO_FIND_DETAIL

> This table stores the details of the mammography findings.

**Description:** Mammography Finding Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIELD_ID` | DOUBLE | NOT NULL | FK→ | This identifies the follow-up field that is being valued. |
| 2 | `FIND_DETAIL_ID` | DOUBLE | NOT NULL |  | This is a meaningless number that is used to uniquely identify the row. |
| 3 | `FIND_ID` | DOUBLE | NOT NULL | FK→ | This identifies the finding that this detail information is a part of. |
| 4 | `NUMERIC_VALUE` | DOUBLE |  |  | if the field is numeric, then this is the value assigned by the user. |
| 5 | `TEXT_VALUE` | VARCHAR(255) |  |  | if the field is textual, this is the text that was assigned by the user. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALUE_DT_TM` | DATETIME |  |  | If the field is a date/time, then this is the date and time that the user assigned. |
| 12 | `VALUE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `FIND_ID` | [MAMMO_FIND](MAMMO_FIND.md) | `FIND_ID` |

