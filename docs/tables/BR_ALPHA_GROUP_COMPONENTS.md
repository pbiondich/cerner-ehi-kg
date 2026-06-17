# BR_ALPHA_GROUP_COMPONENTS

> Alpha responses contained within the alpha groups

**Description:** BEDROCK ALPHA GROUP COMPONENTS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Used to indicate which alpha response should be used as the default in result entry applications |
| 3 | `GROUP_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 4 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The alpha response associated to the alpha group |
| 5 | `REFERENCE_IND` | DOUBLE | NOT NULL |  | Indicates if the alpha response selected will be printed on hard-copy charts as the typical "reference" value. |
| 6 | `RESULT_PROCESS_CD` | DOUBLE | NOT NULL |  | Used to store processing codes that would flag alpha responses |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `USE_UNITS_IND` | DOUBLE | NOT NULL |  | Used to indicate whether or not units of measure will be appended to the alpha response. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

