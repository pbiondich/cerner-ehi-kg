# PM_POST_DOC_REF

> Stores the reference data of ERM post document actions.

**Description:** Person Misc Post Doc Reference  
**Table type:** REFERENCE  
**Primary key:** `PM_POST_DOC_REF_ID`  
**Columns:** 31  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_OBJECT_NAME` | VARCHAR(30) |  |  | Custom script object name for updating values for client defined workflows. Script object is executed when the associated rule returns true. |
| 2 | `ACTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time that this row became active, usually the date and time that it was inserted. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `BATCH_PRINT_IND` | DOUBLE | NOT NULL |  | Indicator to determine if a generated document is printed in batch out of an ops job or printed real time. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `COPIES_NBR` | DOUBLE | NOT NULL |  | Number of document copies to be printed when the associated document is generated. |
| 10 | `DOCUMENT_OBJECT_NAME` | VARCHAR(30) |  |  | Custom script object name for client defined document. Script object is executed when the associated rule returns true. |
| 11 | `DOCUMENT_TYPE_CD` | DOUBLE | NOT NULL |  | Post document type code used to identify the type of document that was generated. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | Output destination code for the generated document. |
| 14 | `PM_POST_DOC_REF_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a row on the PM_POST_DOC_REF table. |
| 15 | `PREV_PM_POST_DOC_REF_ID` | DOUBLE | NOT NULL |  | This field is used to track versions of the post documents. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 16 | `PRIMARY_CARE_DOC_OBJ_NAME` | VARCHAR(30) |  |  | Primary care physician organization custom script object name for client defined document. script object is executed when the associated rule returns true. |
| 17 | `PRIMARY_CARE_DOC_TYPE_CD` | DOUBLE |  |  | primary care physician organization post document type code used to identify the type of document that was generated. |
| 18 | `PROCESS_NAME` | VARCHAR(250) |  |  | Contains the name of the post process. |
| 19 | `REF_ORG_DOC_OBJ_NAME` | VARCHAR(30) |  |  | Referring organization custom script object name for client defined document. script object is executed when the associated rule returns true. |
| 20 | `REF_ORG_DOC_TYPE_CD` | DOUBLE | NOT NULL |  | Referring organization post document type code used to identify the type of document that was generated. |
| 21 | `RELATED_PERSON_DOC_OBJ_NAME` | VARCHAR(30) |  |  | Related person custom script object name for client defined document. script object is executed when the associated rule returns true. |
| 22 | `RELATED_PERSON_DOC_TYPE_CD` | DOUBLE | NOT NULL |  | Related person post document type code used to identify the type of document that was generated. |
| 23 | `REQUEST_NUMBER_CD` | DOUBLE | NOT NULL |  | Request processing number to identify request number from which the rule should be executed from. A NULL value indicates that the rule should be execute from all valid requests. |
| 24 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | This column relates the post document to a specific entry on the sch_flex_list table |
| 25 | `TIME_BASED_OBJECT_NAME` | VARCHAR(30) |  |  | Custom script object name for client defined select statements. Script object is executed through an ops job to qualify persons/encounters for the associated document. |
| 26 | `TIME_BASED_OPS_IND` | DOUBLE | NOT NULL |  | Time Based Operations job Indicator for identifying which rules are time based. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `FACESHEET_ID` |
| [PM_POST_DOC](PM_POST_DOC.md) | `PM_POST_DOC_REF_ID` |
| [PM_POST_DOC_ORG_RELTN](PM_POST_DOC_ORG_RELTN.md) | `PM_POST_DOC_REF_ID` |

