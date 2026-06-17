# RAD_IMAGE_SYS_CONTROLS

> The Rad_Image_Sys_Controls table contains system

**Description:** Rad Image System Controls  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEF_EX_RM_LOAN_INTERVAL` | DOUBLE |  |  | The Def_Ex_Rm_Loan_Interval contains the default number of days that an exam room may keep loaned folders/films. |
| 2 | `DEF_FOREIGN_LIB_FLAG` | DOUBLE |  |  | The Def_Foreign_Lib_Flag indicates whether the foreign library should default from the users profile or from the library group. |
| 3 | `DEF_LOAN_INTERVAL` | DOUBLE |  |  | The Def_Loan_Interval keeps the default number of days that a loan may exist. |
| 4 | `DEF_PAT_LOAN_INTERVAL` | DOUBLE |  |  | The Def_Pat_Loan_Interval indicates the default amount of days that a patient can borrow their folders/films. |
| 5 | `FOREIGN_RETURN_INTERVAL` | DOUBLE |  |  | The Foreign_Return_Interval indicates the maximum amount of time, in days, that foreign folders should be kept. |
| 6 | `HIST_DOWNLOAD_IND` | DOUBLE |  |  | The Hist_Download_Ind indicates whether or not a historical download of information has bee performed. |
| 7 | `HIST_LABELS_IND` | DOUBLE |  |  | The Hist_Labels_Ind indicates whether or not labels from a historical download should print or not. |
| 8 | `IEX_UNREAD_FLAG` | DOUBLE |  |  | The IEX_Unread_Flag indicates if unread exams are to be included, excluded, or handled separately on the incomplete exam report. |
| 9 | `LOAN_INTERESTING_CASE_IND` | DOUBLE |  |  | This column indicates if exams that reside in interesting case files are allowed to be loaned out. |
| 10 | `LOAN_MED_LEGAL_IND` | DOUBLE |  |  | The Loan_Med_Legal_Ind indicates if folders that are marked as medical legal are available to be loaned. |
| 11 | `LOAN_UNREAD_FILMS_IND` | DOUBLE |  |  | The Loan_Unread_Films_Ind indicates if unread exams are available to be loaned. |
| 12 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Library_Group table. It identifies the library group that these system controls are for. |
| 13 | `SUSPEND_TAT_UNREAD_IND` | DOUBLE |  |  | The Suspend_TAT_Unread_Ind indicates if unread exams are to be included on the turnaround time report. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_PREV_MASTERS_IND` | DOUBLE | NOT NULL |  | The Updt_Prev_Masters_Ind indicates if previous master folders should have their current location updated, along with the active master, when an exam is completed. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `URS_UNREAD_FLAG` | DOUBLE |  |  | The URS_Unread_Flag indicates if unread films are to be included, excluded, or handled separately on the unsigned reports listing. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

