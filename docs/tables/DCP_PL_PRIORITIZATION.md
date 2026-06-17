# DCP_PL_PRIORITIZATION

> Identifies priority of a patient in the context of a given patient list.

**Description:** DCP PL PRIORITIZATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter that will no longer be displayed on the PowerChart patient list. |
| 2 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | identifier of patient list. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 4 | `PRIORITY` | DOUBLE |  |  | Patient priority. |
| 5 | `PRIORITY_ID` | DOUBLE | NOT NULL |  | unique identifier. |
| 6 | `REMOVE_DT_TM` | DATETIME |  |  | Date and time this encounter information was removed from the PowerChart patient list. |
| 7 | `REMOVE_IND` | DOUBLE | NOT NULL |  | Indicates removed encounter information on the PowerChart patient list. If remove ind is set to 1, encounter will no longer display on the powerchart patient list. |
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
| `PATIENT_LIST_ID` | [DCP_PATIENT_LIST](DCP_PATIENT_LIST.md) | `PATIENT_LIST_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

