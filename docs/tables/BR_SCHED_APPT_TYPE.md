# BR_SCHED_APPT_TYPE

> Stores proposed scheduling appointment types.

**Description:** Bedrock Scheduling Appointment Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPT_TYPE_DISPLAY` | VARCHAR(40) | NOT NULL |  | Name of the appointment type |
| 2 | `APPT_TYPE_ID` | DOUBLE | NOT NULL |  | identifier of the appointment type |
| 3 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 4 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Catalog type of the default orders the department type can be scheduled for |
| 5 | `DEPT_TYPE_ID` | DOUBLE | NOT NULL |  | ID of the department type |
| 6 | `MATCH_APPT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value from 14230 if the proposed appointment type is created |
| 7 | `ORDERS_BASED_IND` | DOUBLE |  |  | Indicates if the appointment type will have orders attached to it |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

