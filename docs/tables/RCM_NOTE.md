# RCM_NOTE

> Stores notes for Care Management solution.

**Description:** RevWorks Care Management - Note  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | Date and time the note was created. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person who created the note. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely Identifies the related encounter. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that last updated the note. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related long text row where additional information is stored. |
| 9 | `NOTE_PRIORITY_CD` | DOUBLE | NOT NULL |  | Identifies the importance of this note. |
| 10 | `NOTE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of note. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related person. |
| 12 | `PREV_RCM_NOTE_ID` | DOUBLE | NOT NULL |  | Used to track versions of the note. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 13 | `RCM_NOTE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a note recorded for Care Management. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

