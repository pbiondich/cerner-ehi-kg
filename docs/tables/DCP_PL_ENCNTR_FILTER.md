# DCP_PL_ENCNTR_FILTER

> Stores the information about encounter type and encounter class for patients in given patient list.

**Description:** DCP PL ENCNTR FILTER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter class defines how this encounter row is being used in relation to the person table. |
| 2 | `ENCNTR_FILTER_ID` | DOUBLE | NOT NULL |  | Unique identifier for encounter type filter. |
| 3 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter type code to be included within the patient list. |
| 4 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | Identifier of patient list filter is for. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATIENT_LIST_ID` | [DCP_PATIENT_LIST](DCP_PATIENT_LIST.md) | `PATIENT_LIST_ID` |

