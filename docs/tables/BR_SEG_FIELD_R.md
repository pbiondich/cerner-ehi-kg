# BR_SEG_FIELD_R

> This table stores the HL7 fields and code sets that are available for the HL7 interface type/interface direction/segment

**Description:** Bedrock Segment Field Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_SEG_FIELD_R_ID` | DOUBLE | NOT NULL |  | Unique id |
| 2 | `BR_TYPE_SEG_R_ID` | DOUBLE | NOT NULL |  | ID of the row on the BR_TYPE_SEG_R table with which this row is associated |
| 3 | `CODESET` | DOUBLE | NOT NULL |  | the code set associated to the HL7 field |
| 4 | `FIELD_NAME` | VARCHAR(20) | NOT NULL |  | the name of the HL7 field, i.e. PID 2.5, PID 3.3, PV1 2 |
| 5 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | value of 1 indicates that this code set is required for the segment |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

