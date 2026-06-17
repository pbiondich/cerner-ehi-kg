# ROBOTICS_LIMITS_R

> Robotics Limits relationship

**Description:** Defines time limits to be used for processing specimens on a robotics line.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BARCODE_RETRY_LIMIT` | DOUBLE |  |  | The number of times/container that an auto repeat will be performed due to a barcode that was misread. |
| 2 | `BARCODE_TIME_LIMIT` | DOUBLE |  |  | The length of time allowed for a test to be performed before it is assumed the barcode was misread and an auto repeat is performed by robotics. |
| 3 | `COMPLETION_TIME_LIMIT` | DOUBLE |  |  | The length of time after a test is performed before a container is marked completed and moved to its final destination on the robotics line. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Robotics Line Service Resource code |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

