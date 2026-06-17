# AP_DC_STUDY

> This reference table includes the parameters established for diagnostic correlation studies. Every study contains parameters regarding a specific set of events or information to be evaluated and correlated.

**Description:** Diagnostic Correlation Study  
**Table type:** REFERENCE  
**Primary key:** `STUDY_ID`  
**Columns:** 13  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACROSS_CASE_IND` | DOUBLE | NOT NULL |  | This field contains a value indicating that the study is defined as "within case" (value = "0") or "across case (value = "1"). Study elements to be evaluated for "within case" studies must reside on the same PathNet Anatomic Pathology case number (or must be associated with a case or accession that will not be tracked as an "across case" study). Study elements to be evaluated for "across case" studies must reside on different PathNet Anatomic Pathology case numbers. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `DEFAULT_TO_GROUP_IND` | DOUBLE | NOT NULL |  | This field indicates whether assignment of new correlation events involving this study type will be defaulted to a group (value=1) or an individual (value=0). |
| 4 | `DESCRIPTION` | VARCHAR(100) |  |  | This field includes the long description, up-to-60 characters, defined for the diagnostic correlation study. |
| 5 | `INCLUDE_CYTOTECHS_IND` | DOUBLE | NOT NULL |  | This field indicates whether to include cytotechnologists in assignment of correlation events involving this study. A value of 1 indicates that they will be included. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the work area at which the study will be performed for access control. |
| 7 | `SLIDE_COUNTS_PROMPT_IND` | DOUBLE | NOT NULL |  | This field indicates whether to prompt to tally cytology slide counts for correlation events involving this study type. |
| 8 | `STUDY_ID` | DOUBLE | NOT NULL | PK | This field includes the internal identification code assigned to the diagnostic correlation study. This value would be referenced on other tables, such as the AP_DC_EVENT activity table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [AP_DC_EVENT](AP_DC_EVENT.md) | `STUDY_ID` |
| [AP_DC_STUDY_RPT_PROC](AP_DC_STUDY_RPT_PROC.md) | `STUDY_ID` |
| [AP_SYS_CORR](AP_SYS_CORR.md) | `STUDY_ID` |

