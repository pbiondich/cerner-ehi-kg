# PP_AUDIT_EVENT

> This table is used to log auditing event information for specific system events encountered through regular PowerPlans solution workflow.

**Description:** PowerPlan Audit Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APP_NBR` | DOUBLE | NOT NULL |  | Application number that was used to trigger the event being audited |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the encounter affected by the event being audited |
| 3 | `EVENT_DT_TM` | DATETIME | NOT NULL |  | Date & time of the event occurrence |
| 4 | `EVENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier for the entity affected by the event being audited |
| 5 | `EVENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the database table used to store the entity affected by the event being audited |
| 6 | `EVENT_ENUM` | DOUBLE | NOT NULL |  | This is a logical flag. An asynchronous call to populate the table from the solution will also have an enumeration defined in the front end C++ code for the values in this field |
| 7 | `EVENT_MESSAGE` | VARCHAR(255) | NOT NULL |  | Free-text message used to provide additional context for the event. |
| 8 | `EVENT_NAME` | VARCHAR(12) | NOT NULL |  | Event name identifier, used to mark recurring events. |
| 9 | `EVENT_TYPE` | VARCHAR(12) | NOT NULL |  | Event type identifier. This field can be used to sort/group events together. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the patient affected by the event being audited |
| 11 | `PP_AUDIT_EVENT_ID` | DOUBLE | NOT NULL |  | Unique Identifier. Primary Key |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `USER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the user who triggered the event being audited |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

