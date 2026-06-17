# PULL_LIST

> The Pull_List table contain common information about a pull list.

**Description:** Pull List  
**Table type:** ACTIVITY  
**Primary key:** `PULL_LIST_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PRINT_DT_TM` | DATETIME |  |  | The Print_Dt_Tm contains the date and time that the pull list should print. |
| 2 | `PULL_LIST_ID` | DOUBLE | NOT NULL | PK | The Pull_List_Id uniquely identifies a row within the Pull_List table. This field serves no purpose other than to uniquely identify the row. |
| 3 | `REQ_PULL_DT_TM` | DATETIME |  |  | The Req_Pull_Dt_Tm contains the date and time that the folder(s) should be pulled. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `PULL_LIST_ID` |
| [PULL_ORD_SCHED](PULL_ORD_SCHED.md) | `PULL_LIST_ID` |
| [PULL_TRANS_REQ](PULL_TRANS_REQ.md) | `PULL_LIST_ID` |

