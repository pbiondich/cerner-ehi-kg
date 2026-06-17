# SA_REF_MACRO_PARAMETER

> Contains detail records about parameters for a macro Based on the # of Macros they have built. Estimate a 2:1 with SA_REF_MACRO. 200

**Description:** SA Ref Macro Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `EXECUTE_IND` | DOUBLE |  |  | Indicates whether this record is executed by default. 1=by default, execute this detail record when the macro is executed, the user will have to uncheck the record if they do not want this detail record executed. 0=by default, do not execute this detail record when the macro is executed. This detail record still shows up under the macro, but the user will have to mark this record if they want this record executed. |
| 6 | `MONITOR_IND` | DOUBLE |  |  | Indicates whether the values associated with the parameter (sa_ref_parameter_id) should be pulled into the anesthesia record. |
| 7 | `SA_REF_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The macro id that this parameter detail belongs to |
| 8 | `SA_REF_MACRO_PARAMETER_ID` | DOUBLE | NOT NULL |  | Unique value that identifies each macro parameter record |
| 9 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Code from CODE_VALUE |
| 10 | `TODO_IND` | DOUBLE | NOT NULL |  | Indicates whether the item defaults to be put on the ToDo list when the macro is executed |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_REF_MACRO_ID` | [SA_REF_MACRO](SA_REF_MACRO.md) | `SA_REF_MACRO_ID` |

