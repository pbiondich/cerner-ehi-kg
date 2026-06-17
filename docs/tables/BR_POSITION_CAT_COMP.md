# BR_POSITION_CAT_COMP

> the positions within the categories

**Description:** BEDROCK POSITION CAT COMP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `CATEGORY_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 3 | `DEFAULT_SELECTED_IND` | DOUBLE |  |  | Defined as 1 the default positions selected. |
| 4 | `PHYSICIAN_IND` | DOUBLE | NOT NULL |  | Defined as 1 the position is defined as a physician. |
| 5 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position associated to the position category |
| 6 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 7 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies which version of start has been loaded |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

