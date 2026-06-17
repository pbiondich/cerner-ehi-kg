# TIME_SCALE_OP

> Defines operations on the time scale

**Description:** TIME SCALE OP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OPERATION_DISP_NAME` | VARCHAR(100) |  |  | The name of the operation to be displayed. i.e. Shift 1 Total, Grand total |
| 2 | `OPERATION_END_INTERVAL` | DOUBLE | NOT NULL |  | The last interval to operate on |
| 3 | `OPERATION_FLAG` | DOUBLE | NOT NULL |  | Defines what operation to perform on the a range of intervals |
| 4 | `OPERATION_PLACEMENT_FLAG` | DOUBLE |  |  | Where to place the operation |
| 5 | `OPERATION_START_INTERVAL` | DOUBLE | NOT NULL |  | The interval to start operating on |
| 6 | `TIME_SCALE_ID` | DOUBLE | NOT NULL |  | foreign key to time_scale |
| 7 | `TIME_SCALE_OP_IDX` | DOUBLE | NOT NULL |  | Operation number on the specific time scale. A time scale can have one or more operations |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

