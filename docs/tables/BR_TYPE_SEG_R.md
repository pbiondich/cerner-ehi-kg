# BR_TYPE_SEG_R

> This table stores the HL7 segments that are available for the HL7 interface type/interface direction

**Description:** Bedrock Type Segment Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_TYPE_SEG_R_ID` | DOUBLE | NOT NULL |  | Unique id |
| 2 | `INBOUND_IND` | DOUBLE | NOT NULL |  | value of 1 indicates that this segment is available for the inbound interface direction |
| 3 | `INTERFACE_TYPE` | VARCHAR(60) |  |  | the type of HL7 interface, i.e. ADT, Orders, Results |
| 4 | `OUTBOUND_IND` | DOUBLE | NOT NULL |  | value of 1 indicates that this segment is available for the outbound interface direction |
| 5 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | value of 1 indicates that this segment is required for the interface type/direction |
| 6 | `SEGMENT_NAME` | VARCHAR(10) |  |  | the name of the HL7 segment, i.e. PID, PV1, NTE |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

