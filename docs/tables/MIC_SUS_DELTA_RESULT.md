# MIC_SUS_DELTA_RESULT

> This reference table contains the alpha result values for susceptibility results delta checking.

**Description:** Microbiology Susceptibility Delta Checking Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the antibiotic used to define susceptibility delta checking value criteria. |
| 2 | `RESULT_CD` | DOUBLE | NOT NULL |  | The code_value of the alpha results and interpreted results used to define the susceptibility delta checking value. |
| 3 | `SUS_DELTA_VALUE_ID` | DOUBLE | NOT NULL | FK→ | This field contains a foreign key value used to join susceptibility delta checking value information. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE_NBR` | DOUBLE | NOT NULL |  | This field indicates the delta checking value assigned to the particular result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SUS_DELTA_VALUE_ID` | [MIC_SUS_DELTA_VALUE](MIC_SUS_DELTA_VALUE.md) | `SUS_DELTA_VALUE_ID` |

