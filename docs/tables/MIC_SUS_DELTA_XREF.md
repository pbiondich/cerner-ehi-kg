# MIC_SUS_DELTA_XREF

> Contains delta check information between susceptibility details based on susceptibility delta checking criteria.

**Description:** Microbiology Susceptibility Delta Checking Parameter Cross Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL | FK→ | Code_value of the antibiotic used to define susceptibility delta checking parameter criteria. |
| 2 | `SUS_DELTA_PARAM_ID` | DOUBLE | NOT NULL | FK→ | Unique value that identifies susceptibility delta checking parameter criteria. |
| 3 | `SUS_DETAIL1_CD` | DOUBLE | NOT NULL |  | Code_value of the first susceptibility detail to be cross referenced. |
| 4 | `SUS_DETAIL2_CD` | DOUBLE | NOT NULL |  | Code_value of the second susceptibility detail to be cross referenced. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANTIBIOTIC_CD` | [MIC_SUS_DELTA_PARAMETER](MIC_SUS_DELTA_PARAMETER.md) | `ANTIBIOTIC_CD` |
| `SUS_DELTA_PARAM_ID` | [MIC_SUS_DELTA_PARAMETER](MIC_SUS_DELTA_PARAMETER.md) | `SUS_DELTA_PARAM_ID` |

