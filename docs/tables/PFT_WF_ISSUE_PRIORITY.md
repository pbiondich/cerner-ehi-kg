# PFT_WF_ISSUE_PRIORITY

> This table stores the information that is needed to determine the work item priority.

**Description:** ProFit Workflow Issue Priority  
**Table type:** REFERENCE  
**Primary key:** `PFT_WF_ISSUE_PRIORITY_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANALYSIS_STATUS_FLAG` | DOUBLE | NOT NULL |  | The analysis status flag, used to determine the type of update for the analysis. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `IMPACT_LOWER_BOUND_VALUE` | DOUBLE | NOT NULL |  | This column stores the lower bound value of the data point on the impact graph. |
| 5 | `IMPACT_UPPER_BOUND_VALUE` | DOUBLE | NOT NULL |  | This column stores the upper bound value of the data point on the impact graph. |
| 6 | `ORIG_PFT_WF_ISSUE_PRIORITY_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the workflow issue priority information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 7 | `PFT_WF_ISSUE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a row on the PFT_WF_ISSUE_ID table. |
| 8 | `PFT_WF_ISSUE_PRIORITY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a row on the PFT_WF_ISSUE_PRIORITY table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `URGENCY_LOWER_BOUND_VALUE` | DOUBLE | NOT NULL |  | This column stores the lower bound value of the data point on the urgency graph. |
| 15 | `URGENCY_UPPER_BOUND_VALUE` | DOUBLE | NOT NULL |  | This column stores the upper bound value of the data point on the urgency graph. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_PFT_WF_ISSUE_PRIORITY_ID` | [PFT_WF_ISSUE_PRIORITY](PFT_WF_ISSUE_PRIORITY.md) | `PFT_WF_ISSUE_PRIORITY_ID` |
| `PFT_WF_ISSUE_ID` | [PFT_WF_ISSUE](PFT_WF_ISSUE.md) | `PFT_WF_ISSUE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_WF_ISSUE_PRIORITY](PFT_WF_ISSUE_PRIORITY.md) | `ORIG_PFT_WF_ISSUE_PRIORITY_ID` |
| [PFT_WF_ISSUE_PRIORITY_LT](PFT_WF_ISSUE_PRIORITY_LT.md) | `PFT_WF_ISSUE_PRIORITY_ID` |

