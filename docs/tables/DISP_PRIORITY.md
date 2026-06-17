# DISP_PRIORITY

> Disp_priority - Stores Dispensing priorities used for Prescriptions.

**Description:** DISPENSE PRIORITY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLOW_TIME_CHG_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). Indicates whether or not to allow the dispense time to be changed during order entry / refill process. |
| 2 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4513 - Dispense Priority. |
| 3 | `DISP_SEQ_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4507 - Indicates sequence of dispense events. |
| 4 | `FIXED_TIME` | DOUBLE |  |  | TIME (0000 TO 2359). Time which will default in the dispense time field during order entry / refill process. If Use_time_ind = 0, then the fixed time will default in for this Dispense Priority. The more specific default value from Dispense Priority / Service Resource will override this default value. |
| 5 | `HIGH_PRIORITY_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). Indicates whether or not the highest consideration should be given orders with this dispense priority |
| 6 | `NEXT_DAY_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). If using Fixed_time option, and current time is after fixed time in Order Entry / Refill process, this indicates whether or not to automatically switch the dispense priority date to the next day. |
| 7 | `ONFILE_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). Indicates that prescription is considered "On File". No dispense events will occur. |
| 8 | `ONHOLD_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). Indicates that prescription is "On Hold". No dispense events will occur, and order does not have to be complete to be saved. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `USE_TIME_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). Indicates if Dispense Priority Date/Time should default to current time (Use_time_ind = 1), or default to fixed time (Use_time_ind = 0). |
| 15 | `WARN_USER_IND` | DOUBLE |  |  | INDICATOR (0 OR 1). Indicates whether or not to warn user when dispense date automatically changes because of Next_day_ind options. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

