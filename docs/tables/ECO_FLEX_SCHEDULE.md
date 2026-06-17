# ECO_FLEX_SCHEDULE

> Stores all of the flexes that the ECO server will honor.

**Description:** Explode Continuing Orders Flex Schedule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDITIONAL_EXPLOSION_HOURS` | DOUBLE |  |  | Number of hours that the ECO server will explode child orders after the initial explosion. |
| 3 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Flexing option #2. What group the orderable falls into. |
| 4 | `ECO_FLEX_SCHEDULE_ID` | DOUBLE | NOT NULL |  | The unique identifier for this table. |
| 5 | `INITIAL_EXPLOSION_HOURS` | DOUBLE |  |  | The number of hours the eco will explode child orders at initial order time. |
| 6 | `NEXT_EXPLOSION_TIME_FRAME` | DOUBLE |  |  | Tells us how many hours prior to the last instance that is exploded, that the ECO server should explode additional instances. |
| 7 | `PROCESSING_FLAG` | DOUBLE | NOT NULL |  | This is a flexing parameter that can make the ECO server explode orders for different types of orders .0 - Normal Processing; 1 - Inpatient Processing; 2 - Outpatient Processing; 3 - Outpatient Scheduable Processing |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

