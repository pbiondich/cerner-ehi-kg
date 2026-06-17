# DISP_PRIORITY_SR_R

> Disp_priority_sr_r - Relates Dispense Priority to Service Resource.

**Description:** DISPENSE PRIORITY SERVICE RESOURCE RELATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE |  |  | NOT IN USE |
| 2 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 4513 - Dispense Priority |
| 3 | `FIXED_TIME` | DOUBLE |  |  | TIME (0000 TO 2359). indicates the default fixed time to display during order entry for the priority/service resource combination |
| 4 | `SERV_RES_CD` | DOUBLE | NOT NULL |  | CODE VALUE FROM CODE SET 221 - Service Resource |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

