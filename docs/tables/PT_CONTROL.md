# PT_CONTROL

> This table dcuments the status of a patient. If he was enrolled on a protocol, if not the reason why he was not enrolled etc.

**Description:** PT CONTROL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CHANGE_DT_TM` | DATETIME |  |  | The date and time on which the patient status changed |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FOLLOW_UP_STATUS_CD` | DOUBLE | NOT NULL |  | %followup% |
| 5 | `INITIAL_PROT_ENROLL_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates whether the patient was initially enrolled on a protocol. If so what type |
| 6 | `NOT_ON_PROT_COMMENT_TXT` | LONGBLOB |  |  | Comments indicating why the patient was not on a protocol |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 8 | `PT_CONTROL_ID` | DOUBLE | NOT NULL |  | Primary key of the pt_control table |
| 9 | `PT_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the patient. If he is alive, active , discharged etc. |
| 10 | `REASON_FOR_NO_PROT_ENROLL_CD` | DOUBLE | NOT NULL |  | Indicates the reason why the patient was not enrolled on any protocol |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

