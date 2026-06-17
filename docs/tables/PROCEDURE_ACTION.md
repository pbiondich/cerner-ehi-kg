# PROCEDURE_ACTION

> Each row on the table represents an action (Create, Review, etc.) that a particular clinician performed on a procedure record.

**Description:** procedure action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Action date & time |
| 2 | `ACTION_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Indicates the type of action performed by clinician. In the initial release it will be REVIEW. |
| 3 | `PROCEDURE_ACTION_ID` | DOUBLE | NOT NULL |  | Sequence: REFERENCE_SEQ Unique key for the table. |
| 4 | `PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for a clinical PROCEDURE record from PROCEDURE table. |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the clinician who performed a particular action on the PROCEDURE. |
| 6 | `UPDATE_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique primary identifierof the encounter table. Represents the last encounter id on which the procedure was modified. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROCEDURE_ID` | [PROCEDURE](PROCEDURE.md) | `PROCEDURE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `UPDATE_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

