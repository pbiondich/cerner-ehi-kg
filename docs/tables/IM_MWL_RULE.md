# IM_MWL_RULE

> Contains information about the configuration rules that affect modality worklist server behavior.

**Description:** im mwl rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALT_PATIENT_ID_TYPE` | VARCHAR(16) | NOT NULL |  | The field that determines which alternate patient id source should be used. |
| 2 | `CONTRIBUTOR_SYS_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. Contributor system for the outbound alias. |
| 3 | `FALLBACK_ID_TYPE` | VARCHAR(16) |  |  | The field that determines which fallback id source should be used when primary id is unavailable. |
| 4 | `GROUP_LEVEL` | VARCHAR(60) | NOT NULL |  | Group level search logic when doing device specific query. Valid values are: SUBSECTION, SECTION, DEPARTMENT, INSTITUTION, and blank. Default is blank. Blank indicates no group level search logic will be used. |
| 5 | `IM_MWL_RULE_ID` | DOUBLE | NOT NULL |  | Unique identifier for this row |
| 6 | `INCLUDE_INSTITUTION_IND` | DOUBLE | NOT NULL |  | The field that determines whether or not institution is included in current patient location. |
| 7 | `MWL_RULE_NAME` | VARCHAR(60) | NOT NULL |  | Unique name of this MWL rule. |
| 8 | `PATIENT_ID_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | The field that determines the alias pool to use for formatting patient id. |
| 9 | `PATIENT_ID_TYPE` | VARCHAR(16) | NOT NULL |  | The field that determines which patient id source should be used. |
| 10 | `RETURN_CODE_VALUE` | DOUBLE | NOT NULL |  | Whether to send canonical value of the requested procedure code or display value. Valid values are: 1 - return canonical value. 0 - return display value. Default is 1. |
| 11 | `RETURN_DEPT_DISPLAY` | DOUBLE | NOT NULL |  | Whether to send display value of the code or department display name for RequestedProcedureId (0040, 1001) field. Valid values: 1 - return department display name; 0 - return display value of the code. Default is 0 |
| 12 | `RETURN_ONE_STEP_IND` | DOUBLE | NOT NULL |  | This field determines whether or not all steps should be returned in MWL queries. |
| 13 | `RETURN_REQDESC_FOR_SPSDESC` | DOUBLE | NOT NULL |  | Whether to send RequestedProcedureDescription (0032, 1060) for the ScheduledStepDescription (0040,0007) instead of sending the step description as built in the database. Valid values: 1 - yes, 0 - No. Default is 0. |
| 14 | `RETURN_REQUEST_AE` | DOUBLE | NOT NULL |  | Always send AE title from the request SCU in the AE title field of the return modality worklist item. Valid values are: 1 - yes, 0 - no. Default is 0. |
| 15 | `SEARCH_DAYS` | DOUBLE | NOT NULL |  | Define the number of days the search will book back and forward from current day if the scheduled procedure start date is not given. Valid values are any integer value. Default is 5. |
| 16 | `SUPPRESS_OPTIONAL_FIELDS_IND` | DOUBLE | NOT NULL |  | Indicates whether optional MWL fields should be returned when not requested. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `USE_CONNECTION_AE` | DOUBLE | NOT NULL |  | Whether to use AE title from the DICOM connection for query purpose if AE title is not specified in the query tags. Valid values are: 1 - use. 0 - no. Default is 0. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

