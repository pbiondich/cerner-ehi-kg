# RETRIES

> This table defines the criteria for retrying a transmission for each station defined. The retry type indicates what to do for each type of transmission failure.

**Description:** Retries  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IMMEDIATE_DELAY` | DOUBLE |  |  | The time to wait between transmission attempts. No other stations will be able to be sent out of the port while the immediate delay is in effect. |
| 2 | `IMMEDIATE_RETRIES` | DOUBLE |  |  | The number of immediate retries to attempt before giving up the port to another fax. |
| 3 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL |  | Foreign Key into the station table. |
| 4 | `QUEUED_DELAY` | DOUBLE |  |  | The amount of time that the report has to wait in the report queue prior to attempting another transmission. |
| 5 | `QUEUED_RETRIES` | DOUBLE |  |  | The number of times a queued retry will be attempted |
| 6 | `RETRY_PRIORITY` | DOUBLE |  |  | The priority assigned to the report if it has been returned to the delivery class queue. This can be either 0 or 1. 0 = re-queue at priority zero, 1 = no change |
| 7 | `RETRY_TYPE_CD` | DOUBLE | NOT NULL |  | Unique system assigned value that identifies the type of retry I.e. Busy, NoConnect etc. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

