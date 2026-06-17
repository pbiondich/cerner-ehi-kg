# MIC_TASK

> This table defines the microbiology tasks and associated attributes.

**Description:** Microbiology Tasks  
**Table type:** REFERENCE  
**Primary key:** `TASK_ASSAY_CD`  
**Columns:** 20  
**Referenced by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BILLABLE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 3 | `BREAKPOINT_IND` | DOUBLE |  |  | This field is not used at this time. |
| 4 | `CHARTABLE_IND` | DOUBLE |  |  | Indicates whether the task_assay_cd can be printed on a patient chart. |
| 5 | `CODE_SET` | DOUBLE |  |  | This field is not used at this time. |
| 6 | `FULL_NAME` | VARCHAR(100) |  |  | This field is not used at this time. |
| 7 | `GROUP_IND` | DOUBLE |  |  | This field is not used at this time. |
| 8 | `MNEMONIC` | CHAR(40) |  |  | This field is not used at this time. |
| 9 | `MNEMONIC_KEY` | CHAR(40) |  |  | This field is not used at this time. |
| 10 | `REPORT_NAME` | VARCHAR(60) |  |  | This field is not used at this time. |
| 11 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | PK | This field identifies a unique value assigned to each task defined on the mic_task table. For sometask types such as reports this field will correspond to the code_value of the report type, but in other tasks such as detail biochemicals it will be a unique value assigned to the task. |
| 12 | `TASK_CLASS_FLAG` | DOUBLE |  |  | This field identifies a value that determines the class associated with the task entered. Tasks are grouped into classes as a means of categorizing the tasks into logical groupings such as reports, biochemicals, etc. Task classes are used to flex how the applications react to particular types of tasks. For most queries the task_type_flag field would be a better field to select. |
| 13 | `TASK_TYPE_FLAG` | DOUBLE |  |  | This field identifies a value that determines the task type associated with the task entered. The task type further categorizes similar tasks within each task class. For example the task class biochemicals has two task type associated: (3)Group Biochemicals and (4)Detail Biochemicals |
| 14 | `TAT_MINUTES` | DOUBLE |  |  | This field identifies the time value for the susceptibility detail procedure. This time value is the expected turn around time for the susceptibility procedure as defined in the susceptibility tool. |
| 15 | `TAT_UNITS_CD` | DOUBLE | NOT NULL |  | This field identifies the unit of time associated with the tat_minutes field. Units are defined on code set 340, Age Units. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (11)

| From table | Column |
|------------|--------|
| [MIC_ABN_SUS_RESULT](MIC_ABN_SUS_RESULT.md) | `SUS_METHOD_CD` |
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `REPORT_CD` |
| [MIC_GROUP_RESPONSE](MIC_GROUP_RESPONSE.md) | `TASK_ASSAY_CD` |
| [MIC_REF_ANG_REPORT](MIC_REF_ANG_REPORT.md) | `REPORT_CD` |
| [MIC_REF_BILLING_SUS](MIC_REF_BILLING_SUS.md) | `SUS_METHOD_CD` |
| [MIC_REF_BIO_FORMAT](MIC_REF_BIO_FORMAT.md) | `TASK_ASSAY_CD` |
| [MIC_REQUIRED_TASK](MIC_REQUIRED_TASK.md) | `TASK_CD` |
| [MIC_REQ_RPT](MIC_REQ_RPT.md) | `TASK_CD` |
| [MIC_RPT_LIMIT](MIC_RPT_LIMIT.md) | `TASK_CD` |
| [MIC_TASK_DETAIL_R](MIC_TASK_DETAIL_R.md) | `TASK_ASSAY_CD` |
| [MIC_VALID_SUS_PANEL](MIC_VALID_SUS_PANEL.md) | `METHOD_CD` |

