# BR_CONTR_SEG_R

> This table stores the HL7 segments chosen for each contributor system/interface type

**Description:** Bedrock Control Segment Relationships  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CONTR_SEG_R_ID` | DOUBLE | NOT NULL |  | Unique ID |
| 2 | `BR_CONTR_TYPE_R_ID` | DOUBLE | NOT NULL |  | ID of the row on the BR_CONTR_TYPE_R table with which this row is associated |
| 3 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | value of 1 indicates that this segment is required for the contributor system/interface type |
| 4 | `SEGMENT_NAME` | VARCHAR(10) | NOT NULL |  | the name of the HL7 segment chosen for the interface type, i.e. PID, PV1, NTE |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

