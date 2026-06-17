# RAD_REQ_CONTROLS

> The Rad_Req_Controls table contains system level settings related to the patient packet / requisition.

**Description:** Radiology Requisition Controls  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `KEEP_NBR_DAYS` | DOUBLE |  |  | The Keep_Nbr_Days column contains the number of days that the requisition should be kept on-line |
| 2 | `PREVIOUS_EXAMS_FLAG` | DOUBLE |  |  | The Previous_Exams_Flag indicates how previous exams should be handled on the requisition. |
| 3 | `PRINT_ADVANCE_NBR_DAYS` | DOUBLE |  |  | The Print_Advance_Nbr_Days indicates how many days in advance of the requested date that the requisition should print. |
| 4 | `PRINT_CANCEL_NOTICE_IND` | DOUBLE |  |  | The Print_Cancel_Notice_Ind indicates if cancellation notices will be utilized |
| 5 | `PRINT_MODIFIED_IND` | DOUBLE |  |  | This column indicates if a requisition should be printed when an order is modified. |
| 6 | `PRINT_REPLACED_IND` | DOUBLE |  |  | The Print_Replaced_Ind indicates if requisitions are to print when a procedure is replaced. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Service Resource table. It uniquely identifies the Department for which the settings are for. |
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

