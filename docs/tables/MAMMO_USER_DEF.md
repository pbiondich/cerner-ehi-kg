# MAMMO_USER_DEF

> User defined detail information about the mammo study

**Description:** Mammography User Defined  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIELD_ID` | DOUBLE |  | FK→ | Identifies the follow-up field that is being valued. This is a foreign key to the Rad_Fol_Up_Field table. |
| 2 | `NUMERIC_VALUE` | DOUBLE |  |  | If the field is a numeric field this is the value assigned by the user. |
| 3 | `STUDY_ID` | DOUBLE |  | FK→ | This identifies the study that the field values are a part of. |
| 4 | `TEXT_VALUE` | VARCHAR(255) |  |  | If the field is textual, this is the text assigned by the user |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `USER_VALUE_ID` | DOUBLE | NOT NULL |  | This is meaningless number that is only used to uniquely identify the row. |
| 11 | `VALUE_DT_TM` | DATETIME |  |  | If the field is a date/time, this is the date and time that has been assigned by the user. |
| 12 | `VALUE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |

