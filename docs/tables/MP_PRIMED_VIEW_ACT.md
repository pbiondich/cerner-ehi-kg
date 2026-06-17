# MP_PRIMED_VIEW_ACT

> Used to store primed data for Patients based on population and reference views.

**Description:** Mpages Primed Views Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_BLOB` | LONGBLOB |  |  | The JSON blob that is consumed by the Mpages front end. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter ID from Encounter Table. |
| 3 | `LOAD_DT_TM` | DATETIME | NOT NULL |  | Time Data was loaded into the table |
| 4 | `LONG_BLOB_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 5 | `MP_PRIMED_VIEW_ACT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MP_PRIMED_VIEW_ACT table. |
| 6 | `MP_PRIMED_VIEW_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique ID from MP_DPV_REF table |
| 7 | `PENDING_UPDT_IND` | DOUBLE | NOT NULL |  | Indicates if this row is pending for the update script to complete execution. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person ID from person table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MP_PRIMED_VIEW_REF_ID` | [MP_PRIMED_VIEW_REF](MP_PRIMED_VIEW_REF.md) | `MP_PRIMED_VIEW_REF_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

