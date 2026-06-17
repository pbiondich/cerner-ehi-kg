# ACCESSION_ASSIGNMENT

> This is the actual accession bucket used to generate accession numbers.

**Description:** Accession Assignment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_SEQ_NBR` | DOUBLE |  |  | The current sequence number of an accession bucket. |
| 2 | `ACC_ASSIGN_DATE` | DATETIME | NOT NULL |  | The date the accession bucket was created. |
| 3 | `ACC_ASSIGN_POOL_ID` | DOUBLE | NOT NULL | FK→ | A system generated number that uniquely identifies an accession bucket. |
| 4 | `INCREMENT_VALUE` | DOUBLE |  |  | The increment value of an accession bucket. |
| 5 | `LAST_INCREMENT_DT_TM` | DATETIME |  |  | The date and time the accession bucket was increment. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACC_ASSIGN_POOL_ID` | [ACCESSION_ASSIGN_POOL](ACCESSION_ASSIGN_POOL.md) | `ACCESSION_ASSIGNMENT_POOL_ID` |

