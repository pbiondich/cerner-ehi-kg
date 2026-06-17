# PBS_AUTHORITY

> Australian Pharmaceutical Benefits Schedule ¿ Authority Method

**Description:** PBS_AUTHORITY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORITY_CD` | DOUBLE | NOT NULL |  | Streamlined Authority Method - CODE SET 28682 |
| 2 | `PBS_AUTHORITY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the PBS_AUTHORITY table. It is an internal system assigned number. |
| 3 | `PBS_INDICATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from PBS_INDICATION table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PBS_INDICATION_ID` | [PBS_INDICATION](PBS_INDICATION.md) | `PBS_INDICATION_ID` |

