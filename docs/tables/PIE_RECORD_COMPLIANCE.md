# PIE_RECORD_COMPLIANCE

> Stores information for documenting compliance of data from outside records

**Description:** RECORD COMPLIANCE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_TYPE_CD` | DOUBLE | NOT NULL |  | Type of the data (ALLERGIES, IMMUNIZATIONS, etc.) from code set 4003507 |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ENCOUNTER for which the Compliance was captured |
| 3 | `PERFORMED_DT_TM` | DATETIME |  |  | The date and time the compliance was captured. |
| 4 | `PERFORMED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Personnel who captured the Compliance |
| 5 | `PERFORMED_TZ` | DOUBLE |  |  | The time zone where the Compliance was performed ( i.e., User Time Zone) |
| 6 | `PIE_RECORD_COMPLIANCE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The compliance status for the encounter. 0 = Complete, 1 = Incomplete |
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
| `PERFORMED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

