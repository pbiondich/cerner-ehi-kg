# PDOC_AUTOSAVE

> This table stores details about auto saved entries

**Description:** Physicial Documentation Auto Save  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | Contains the id of the author that created the content being auto saved. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Identifies the encounter to which the auto saved content belongs. |
| 3 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the auto saved content. |
| 4 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient to which the auto saved content belongs. |
| 5 | `PDOC_AUTOSAVE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information about an auto saved document. |
| 6 | `REFERENCE_TXT` | VARCHAR(255) | NOT NULL |  | Identifies the type of content being auto saved. Should not contain user, patient, or encounter identifiers or patient combines will not work. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

