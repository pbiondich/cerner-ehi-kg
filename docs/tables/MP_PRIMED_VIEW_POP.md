# MP_PRIMED_VIEW_POP

> Contains the patients currently active in Primed view Population

**Description:** MP_PRIMED_VIEW_POP  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MP_PRIMED_VIEW_POP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MP_PRIMED_VIEW_POP table. |
| 2 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | PERSON_ID from person table |
| 3 | `POP_NAME` | VARCHAR(20) | NOT NULL |  | The named population. |
| 4 | `POP_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains ID from referenced table e.g. TRACK_GROUP_ID |
| 5 | `POP_PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains table name of referenced table e.g. TRACK_GROUP. This identifies for a patient what caused them to be added to population |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VIEW_ERROR_IND` | DOUBLE | NOT NULL |  | Indicates if an error in priming has occurred for the patient. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

