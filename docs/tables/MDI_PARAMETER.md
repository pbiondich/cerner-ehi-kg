# MDI_PARAMETER

> This table will store MDI demographic parameters

**Description:** MDI PARAMETER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MDI_PARAMETER_CD` | DOUBLE | NOT NULL |  | MDI PARAMETER CODE from code set 4002311 |
| 2 | `MDI_PARAMETER_DEF` | VARCHAR(12) |  |  | CDF MEANING of the MDI_PARAMETER code value (from code set 4002311) |
| 3 | `MDI_PARAMETER_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `SELECTED_IND` | DOUBLE | NOT NULL |  | Indicates if the parameter was selected |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Code Set 221: Internal identifier for the instrument. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

