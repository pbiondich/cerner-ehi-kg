# MAMMO_STUDY_PRSNL

> Radiology personnel associated with the study.

**Description:** Mammography Study Personnel  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PHYSICIAN_IDENTIFIER_FLAG` | DOUBLE | NOT NULL |  | As part of BIRADs 5.0 Enhancements, a mammo study can have information on more than one radiologist. This is called double read physicians. This column indicates the role played. |
| 2 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This identifies the personnel that was involved with the case. This is a foreign key to the Prsnl table. |
| 3 | `PRSNL_RELATION_FLAG` | DOUBLE | NOT NULL |  | Identifies the role that the personnel had in regards to the case. |
| 4 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | This identifies the study that the personnel are associated with. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |

