# MIC_QC_SCHEDULE_SEGMENT

> This reference table contains a record for each microbiology QC schedule segment defined for a segment.

**Description:** Microbiology Quality Control Schedule Segment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMPONENT1_NBR` | DOUBLE |  |  | This field stores the first component of a schedule segment. |
| 6 | `COMPONENT2_NBR` | DOUBLE |  |  | This field stores the second component of a schedule segment. |
| 7 | `COMPONENT3_NBR` | DOUBLE |  |  | This field stores the third component of a schedule segment. |
| 8 | `DAYS_OF_WEEK_BIT` | DOUBLE |  |  | This bit map field indicates which days of the week have been selected for the schedule segment. |
| 9 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key used to join to schedule segments to a specific schedule. |
| 10 | `SCHEDULE_SEGMENT_ID` | DOUBLE | NOT NULL |  | This field contains the unique value that identifies the QC schedule segment. |
| 11 | `SEGMENT_SEQ` | DOUBLE | NOT NULL |  | This field uniquely identifies a segment within a specific schedule. |
| 12 | `SEGMENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field indicates the type of schedule segment. |
| 13 | `TIME_NBR` | DOUBLE | NOT NULL |  | This field stores the time for a schedule segment. (Stored as a number) |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCHEDULE_ID` | [MIC_QC_SCHEDULE](MIC_QC_SCHEDULE.md) | `SCHEDULE_ID` |

