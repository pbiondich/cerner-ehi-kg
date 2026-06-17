# APPLICATION_ACCESS

> Allows discrete application access for user groups.

**Description:** Application Access  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | The date at which the relationship between the application and the application group became active. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who activated the relationship between the application and the application group. |
| 4 | `APPLICATION_ACCESS_ID` | DOUBLE | NOT NULL |  | A unique number to identify a specific application to application group relationship in the table. |
| 5 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | The number of the application for which the application group is being granted access to. |
| 6 | `APP_GROUP_CD` | DOUBLE | NOT NULL |  | The code representing the application group that has access to the application. |
| 7 | `INACTIVE_DT_TM` | DATETIME |  |  | The date at which the relationship between the application group and the application is no longer valid. |
| 8 | `INACTIVE_PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the person who inactivated the relationship between the application and the application group. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

