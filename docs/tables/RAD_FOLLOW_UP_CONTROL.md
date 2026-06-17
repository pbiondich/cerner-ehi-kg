# RAD_FOLLOW_UP_CONTROL

> The Rad_Follow_Up_Control table contains general information about patient follow up.

**Description:** Rad Follow Up Control  
**Table type:** REFERENCE  
**Primary key:** `FOLLOW_UP_CONTROL_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADVANCE_PRINT_INTERVAL` | DOUBLE |  |  | The Advance_Print_Interval indicates how many days in advance that the follow up letter should be sent. |
| 3 | `ALLOW_SUPPRESS_NOTIFY_LETT_IND` | DOUBLE | NOT NULL |  | Indicates if a user can suppress patient notification letters from printing. |
| 4 | `ASSESSMENT_4_DEFAULT_INTERVAL` | DOUBLE |  |  | Stores the default recall interval in months for studies with Assessment 4. A value of -1 indicates "Now". |
| 5 | `ASSESSMENT_5_DEFAULT_INTERVAL` | DOUBLE |  |  | Stores the default recall interval in months for studies with Assessment 5. A value of -1 indicates "Now". |
| 6 | `AUDIT_REPORT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The audit report type set in the domain |
| 7 | `COMPLETE_FOLLOW_UP_IND` | DOUBLE |  |  | This column indicates whether radiology exam management does mammography follow-up processing |
| 8 | `DAYS_BEFORE_SURVEY` | DOUBLE | NOT NULL |  | Sets the number of days after the study date that the physician survey letter would qualify to print. |
| 9 | `DAYS_BEFORE_WARNING` | DOUBLE |  |  | Number of days after recall date at which to send OVERDUE warning |
| 10 | `DAYS_BETWEEN_WARNING` | DOUBLE |  |  | If repeated warnings are sent, number of days between warnings |
| 11 | `DUAL_BREAST_DENSITY_STMT_IND` | DOUBLE | NOT NULL |  | If 1, indicates that separate density statements will be used for dense and non-dense breast types. |
| 12 | `FOLLOW_UP_CONTROL_ID` | DOUBLE | NOT NULL | PK | This column serves as the primary key. It serves no other purpose other than to uniquely identify a row. |
| 13 | `MAMMO_TAG_LTR_IND` | DOUBLE |  |  | The determining factor if the mammography letters were defined using the tagging tool. |
| 14 | `MAX_WARNING_LETTER_PRINTS` | DOUBLE | NOT NULL |  | Sets the maximum number of times that a patient or physician warning letter will be printed. |
| 15 | `NO_FOL_UP_REQ_DEFAULT_IND` | DOUBLE | NOT NULL |  | No longer used. |
| 16 | `ONLINE_BREAST_DIAGRAM_IND` | DOUBLE | NOT NULL |  | If 1, indicates that online breast diagram will be used for all mammography exams ordered from that point forward. |
| 17 | `PRINT_MAMMO_HDR_IND` | DOUBLE | NOT NULL |  | If this indicator is 1 then the Facility information will print on the mammography letters, if it is 0 then it won't. The default is 1. |
| 18 | `PROC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the mammography procedure group that is to be used for follow up |
| 19 | `SIGNOUT_FOLLOW_UP_IND` | DOUBLE |  |  | No longer used. |
| 20 | `TRANS_FOLLOW_UP_IND` | DOUBLE |  |  | The Signout_Follow_Up_Ind indicates if follow up information should be captured from the transcription application. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROC_GROUP_ID` | [RAD_PROCEDURE_GROUP](RAD_PROCEDURE_GROUP.md) | `PROC_GROUP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_FOLLOW_UP_DEFAULT](RAD_FOLLOW_UP_DEFAULT.md) | `FOLLOW_UP_CONTROL_ID` |
| [RAD_FOLLOW_UP_PRINT_CTRL](RAD_FOLLOW_UP_PRINT_CTRL.md) | `FOLLOW_UP_CONTROL_ID` |

