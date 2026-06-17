# LH_CNT_PATIENT_EXTENSION

> Store patient/encounter extension information used within the Lighthouse Content space.

**Description:** lh_cnt_patient_extension  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter identifier which indicates the encounter that the extension value will apply to. |
| 3 | `EXTENSION_TYPE_MEAN` | VARCHAR(12) |  |  | Type of extension to be applied to the patient/encounter |
| 4 | `EXTENSION_VALUE_TXT` | VARCHAR(255) |  |  | The value associated with the mean |
| 5 | `LH_CNT_PATIENT_EXTENSION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_PATIENT_EXTENSION table. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The patient identifier which indicates the patient that the extension value will apply to. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

