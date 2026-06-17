# BR_DTA_RELATIONSHIP

> legacy dta relationships

**Description:** BEDROCK DTA RELATIONSHIP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `DTA_ID` | DOUBLE | NOT NULL |  | Legacy assay id. |
| 3 | `INTERVAL_MIN` | DOUBLE | NOT NULL |  | Defined as 1 the interval minutes associated to the assay for this order catalog item. |
| 4 | `OC_ID` | DOUBLE | NOT NULL |  | Legacy order catalog item. |
| 5 | `PENDING_IND` | DOUBLE | NOT NULL |  | Defined as 1 the pending indicator is defined. |
| 6 | `REPEAT_IND` | DOUBLE | NOT NULL |  | Defined as 1 the repeat indicator is defined. |
| 7 | `RESTRICT_DISPLAY_IND` | DOUBLE | NOT NULL |  | Defined as 1 the restrict display indicator is defined. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

