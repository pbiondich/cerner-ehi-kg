# BB_QC_SCHEDULE_SEGMENT

> This reference table contains a record for each blood bank QC schedule segment defined for a segment.

**Description:** Blood Bank Quality Control Schedule Segment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT1_NBR` | DOUBLE | NOT NULL |  | This field stores the first component of a schedule segment. |
| 2 | `COMPONENT2_NBR` | DOUBLE | NOT NULL |  | This field stores the second component of a schedule segment. |
| 3 | `COMPONENT3_NBR` | DOUBLE | NOT NULL |  | This field stores the third component of a schedule segment. |
| 4 | `DAYS_OF_WEEK_BIT` | DOUBLE | NOT NULL |  | This bit map field indicates which days of the week have been selected for the schedule segment. |
| 5 | `SCHEDULE_CD` | DOUBLE | NOT NULL |  | This field contains the code value used to join to schedule segments to a specific schedule. |
| 6 | `SCHEDULE_SEGMENT_ID` | DOUBLE | NOT NULL |  | This field contains the unique value that identifies the QC schedule segment. |
| 7 | `SEGMENT_SEQ` | DOUBLE | NOT NULL |  | This field uniquely identifies a segment within a specific schedule. |
| 8 | `SEGMENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field indicates the type of schedule segment. |
| 9 | `TIME_NBR` | DOUBLE | NOT NULL |  | This field stores the time for a schedule segment. (Stored as a number) |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

