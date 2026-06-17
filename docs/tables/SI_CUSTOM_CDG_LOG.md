# SI_CUSTOM_CDG_LOG

> Stores a custom log of requests that CDG server failed to process

**Description:** System Integration Custom CCD document generator Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key To The Encounter Table |
| 3 | `ERROR_FLAG_TXT` | VARCHAR(2) |  |  | REASON/TYPE OF ERROR |
| 4 | `ERROR_TEXT` | VARCHAR(500) |  |  | ERROR TEXT MESSAGE |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key To The Person Table |
| 6 | `SI_CUSTOM_CDG_LOG_ID` | DOUBLE | NOT NULL |  | Primary Key Of The Table |
| 7 | `TRIGGER_DT_TM` | DATETIME |  |  | When the request was triggered for the CCD. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

