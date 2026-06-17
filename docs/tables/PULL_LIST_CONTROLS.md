# PULL_LIST_CONTROLS

> The Pull_List_Controls table contains settings pertaining to how pull lists are to behave within the system.

**Description:** Pull List Controls  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CURRENT_ORDER_NBR_DAYS` | DOUBLE |  |  | The Current_Order_Nbr_Days identifies the number of days beyond today that define an order pull list as current. |
| 2 | `CURRENT_SCHED_NBR_DAYS` | DOUBLE |  |  | The Current_Sched_Nbr_Days identifies the number of days beyond today that a schedule pull list is considered to be current. |
| 3 | `FUTURE_ORDER_NBR_DAYS` | DOUBLE |  |  | The Future_Order_Nbr_Days field identifies the number of days in advance of request that pull listsshould print. |
| 4 | `INCLUDE_EXAMS_IND` | DOUBLE |  |  | The Include_Exams_Ind indicates if exams should be included on an order pull list if they have already appeared on a schedule pull list. |
| 5 | `NBR_DAYS_PRIOR_PULL_LIST` | DOUBLE |  |  | Indicates how many days back to look for a previously printed pull list. |
| 6 | `PREV_EXAMS_BY_LIBGRP_IND` | DOUBLE |  |  | Indicates if the pull list should only show exams within a given library group. |
| 7 | `PRINT_FOR_EVERY_ORDER_IND` | DOUBLE |  |  | Indicates if a pull list should print for every order. |
| 8 | `PRINT_LIB_TRK_PT_FLAG` | DOUBLE |  |  | The Print_Lib_Trk_Pt_Flag field idicates if pull lists should print to the library or tracking point printer. |
| 9 | `PRINT_MASTER_FLAG` | DOUBLE |  |  | The Print_Master_Flag indicates if only the active master or all masters are to print on the order/schedule pull list. |
| 10 | `PRINT_NEW_MASTER_IND` | DOUBLE |  |  | The Print_New_Master_Ind field indicates if new masters are to print on sched/order pull lists. |
| 11 | `PRINT_ORDER_FLAG` | DOUBLE |  |  | The Print_Order_Flag indicates when pull lists will be printed for ordered procedures. |
| 12 | `PULL_LIST_NBR_DAYS` | DOUBLE |  |  | The Pull_List_Nbr_Days field indicates the number of days to keep pull lists on the system. |
| 13 | `SCHED_DAYS_IN_ADVANCE` | DOUBLE |  |  | The Sched_Days_In_Advance field indicates the number of days in advance of the scheduled date that schedule pull lists should print. |
| 14 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Service Resource table. It uniquely identifies theLibrary Group that the pull list controls are set up for. |
| 15 | `UPDATE_SUBSECT_OPTION_IND` | DOUBLE |  |  | The Update_Subsect_Option_Ind indicates if the subsection sort option for order/sched pull lists should be updated. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

