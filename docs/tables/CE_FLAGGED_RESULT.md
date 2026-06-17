# CE_FLAGGED_RESULT

> Stores flagged result information that will be related to a specific clinical event and a discipline or list of disciplines. The event_id will identify the active clinical event row that this flagged result is associated with.

**Description:** Clinical Event Flagged Result  
**Table type:** ACTIVITY  
**Primary key:** `CE_FLAGGED_RESULT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_FLAGGED_RESULT_ID` | DOUBLE | NOT NULL | PK | A unique, generated number that is used to identify an individual CE_FLAGGED_RESULT row. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter of the clinical event that was flagged. |
| 3 | `EVENT_CD` | DOUBLE | NOT NULL |  | The code that identifies the most basic unit of storage, i.e. RBC, discharge summary, image. |
| 4 | `EVENT_END_DT_TM` | DATETIME |  |  | Clinical date time for the end of the event. |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event that has been flagged. |
| 6 | `FLAGGED_DT_TM` | DATETIME |  |  | Date and time that the clinical event row became flagged. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person who's Clinical Event has been flagged. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CE_FLAGGED_RESULT_ROLE](CE_FLAGGED_RESULT_ROLE.md) | `CE_FLAGGED_RESULT_ID` |

