# CALENDAR_EXCEPTION

> Individual dates that are an exception to the resource's calendar.

**Description:** Calendar Exception  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AVAIL_IND` | DOUBLE |  |  | Whether the resource is available or not. |
| 2 | `CLOSE_TIME` | DOUBLE |  |  | The time of day that the resource is no longer available. 24 hour clock. Valid values are 0 through 2359. |
| 3 | `EXCEPTION_SEQ` | DOUBLE | NOT NULL |  | The relative sequence of the calendar exception. The lowest sequence would be considered first followed the next highest, etc. |
| 4 | `EXC_DATE` | DATETIME | NOT NULL |  | The date of the exception for the calendar |
| 5 | `OPEN_TIME` | DOUBLE |  |  | The time of day that the resource begins to be available. 24 hour clock. Valid values are 0 through 2359. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The resource for which the calendar exception is being defined |
| 7 | `TEXT_DESCRIPTION` | VARCHAR(200) |  |  | The description which explains the calendar exception. Expected examples include "Christmas Day" |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

