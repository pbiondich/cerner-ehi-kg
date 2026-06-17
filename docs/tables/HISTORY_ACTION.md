# HISTORY_ACTION

> Track users reviewing the patient's history data captured through powerforms or powernote in the Social, Family, Past Medical, Procedure and Pregnancy history components.

**Description:** HISTORY ACTION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Review action taken date time |
| 2 | `ACTION_DT_TZ` | DOUBLE | NOT NULL |  | Review action taken date time zone |
| 3 | `COMP_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Name of the history component that review action was taken |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 5 | `HISTORY_ACTION_ID` | DOUBLE | NOT NULL |  | this is the table's primary key. the unique identifier for a history_action table. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | this is the value of the unique primary identifier of the person table. it is an internal system assigned number. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | prsnl id. this is the value of the unique primary identifier of the person table. it is an internal system assigned number |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VIEW_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | History view type when the review action was taken |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

