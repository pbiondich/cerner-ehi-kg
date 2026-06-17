# TRACK_TRIGGER_ACTIVITY

> This table stores the patients trigger activities

**Description:** TRACK TRIGGER ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE` | VARCHAR(50) | NOT NULL |  | what action type triggers this actionColumn |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 3 | `NEW_VALUE` | VARCHAR(50) |  |  | What value got stored due to the trigger action.Column |
| 4 | `OLD_VALUE` | VARCHAR(50) |  |  | what was before the trigger actionColumn |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 6 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking Id of the patientColumn |
| 7 | `TRACK_TRIGGER_ACTIVITY_ID` | DOUBLE | NOT NULL |  | auto generated key for the tableColumn |
| 8 | `TRACK_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | from track_triggers table to validate the trigger actionColumn |
| 9 | `TRIGGER_DT_TM` | DATETIME | NOT NULL |  | when the trigger happened.Column |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `USER_ID` | VARCHAR(50) |  |  | who triggered this actionColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |
| `TRACK_TRIGGER_ID` | [TRACK_TRIGGERS](TRACK_TRIGGERS.md) | `TRACK_TRIGGER_ID` |

