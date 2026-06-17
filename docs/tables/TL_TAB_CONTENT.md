# TL_TAB_CONTENT

> Hold the values to the tab content fields for a specific tab for the tasklist.

**Description:** TL TAB CONTENT  
**Table type:** REFERENCE  
**Primary key:** `TL_TAB_ID`  
**Columns:** 36  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLSTATUS_IND` | DOUBLE |  |  | An indicator that identifies whether tasks of any status should be included on this tab. |
| 2 | `ALLTIMEPARAM_IND` | DOUBLE |  |  | An indicator that identifies whether tasks of any time parameter should be included on this tab. |
| 3 | `COMPLETE_IND` | DOUBLE |  |  | An indicator that identifies whether completed tasks should be included on this tab. |
| 4 | `CONTINUOUS_IND` | DOUBLE |  |  | An indicator that identifies whether continuous tasks should be included on this tab. |
| 5 | `DISCONTINUED_IND` | DOUBLE |  |  | An indicator that identifies whether discontinued tasks should be included on this tab. |
| 6 | `INPROCESS_IND` | DOUBLE |  |  | An indicator that identifies whether inprocess tasks should be included on this tab. |
| 7 | `IV_IND` | DOUBLE |  |  | An indicator that identifies whether iv tasks should be included on this tab.Column |
| 8 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location_cd of the task group view location group associated with this task view. |
| 9 | `MED_FLAG` | DOUBLE |  |  | An indicator that identifies whether no meds, all meds, or some meds are being defined (0 = none, 1= all meds, 2 = selected meds). |
| 10 | `NONPATIENT_IND` | DOUBLE |  |  | An indicator that identifies whether non patient tasks should be included on this tab. |
| 11 | `NONPHYSORDER_IND` | DOUBLE |  |  | An indicator that identifies whether nonphysician ordered tasks should be included on this tab. |
| 12 | `NONSCHEDULED_IND` | DOUBLE |  |  | An indicator that identifies whether nonscheduled tasks should be included on this tab. |
| 13 | `OUTCOMES_IND` | DOUBLE |  |  | An indicator that identifies whether outcomes tasks should be included on this tab. |
| 14 | `OVERDUE_IND` | DOUBLE |  |  | An indicator that identifies whether overdue tasks should be included on this tab. |
| 15 | `PENDINGVALIDATION_IND` | DOUBLE |  |  | An indicator that identifies whether tasks in a pending validation status should be displayed in this tab. |
| 16 | `PENDING_IND` | DOUBLE |  |  | An indicator that identifies whether pending tasks should be included on this tab. |
| 17 | `PHYSORDER_IND` | DOUBLE |  |  | An indicator that identifies whether physician ordered tasks should be included on this tab. |
| 18 | `POSITION_CD` | DOUBLE | NOT NULL |  | A position_cd that corresponds with who can perform an action against a task and is used when determining which tasks will be represented in a task list. |
| 19 | `POSITION_FLAG` | DOUBLE |  |  | An indicator that identifies whether no positions, all positions, or some positions are being defined (0 = none, 1 = all, 2 = selected positions). |
| 20 | `PRN_IND` | DOUBLE |  |  | An indicator that identifies whether prn tasks should be included on this tab.Column |
| 21 | `RESPONSE_IND` | DOUBLE |  |  | An indicator that identifies whether response tasks should be included on this tab. |
| 22 | `SCHEDULED_IND` | DOUBLE |  |  | An indicator that identifies whether scheduled tasks should be included on this tab. |
| 23 | `SUSPEND_IND` | DOUBLE |  |  | This column defines whether suspended tasks are displayed in the task list. |
| 24 | `TAB_NAME` | VARCHAR(25) |  |  | The name of the specific tab.Column |
| 25 | `TL_TAB_ID` | DOUBLE | NOT NULL | PK | A unique, generated number that identifies a specific tab.Column |
| 26 | `TPN_IND` | DOUBLE |  |  | An indicator that identifies whether tpn tasks should be included on this tab.Column |
| 27 | `TYPE_FLAG` | DOUBLE |  |  | An indicator that identifies whether no task types, all types, or some types are being defined (0 =none, 1 = all, 2 = selected task types). |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 33 | `VIEW_COMP_PREFS_ID` | DOUBLE | NOT NULL |  | This column is a foreign key to the view_comp_prefs table. |
| 34 | `VIEW_MODE_FLAG` | DOUBLE |  |  | This field defines whether the task list will display in task view or order view. |
| 35 | `VIEW_PREFS_MP_ID` | DOUBLE | NOT NULL |  | This column is a foreign key to the view_prefs table for multi-patient tasklist. |
| 36 | `VIEW_PREFS_SP_ID` | DOUBLE | NOT NULL |  | This column is a foreign key to the view_prefs table.Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [TL_COLUMN_CONTENT](TL_COLUMN_CONTENT.md) | `TL_TAB_ID` |
| [TL_ELIGIBLE_TASK_CODE](TL_ELIGIBLE_TASK_CODE.md) | `TL_TAB_ID` |
| [TL_MASTER_TAB_SET_XREF](TL_MASTER_TAB_SET_XREF.md) | `TL_TAB_ID` |
| [TL_TAB_MEDICATION](TL_TAB_MEDICATION.md) | `TL_TAB_ID` |
| [TL_TAB_POSITION_XREF](TL_TAB_POSITION_XREF.md) | `TL_TAB_ID` |
| [TL_USER_XREF](TL_USER_XREF.md) | `TL_TAB_ID` |

