# REPORT_TASK

> This activity table contains parameters associated with pathology case reports. Information such as the hold status (and hold reason and comment), last edit date and time, and responsible pathologist and resident (for the report) are included.

**Description:** Report Task  
**Table type:** ACTIVITY  
**Primary key:** `REPORT_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENTS` | VARCHAR(100) |  |  | This field is no longer used. Refer to the COMMENTS_LONG_TEXT_ID for information regarding the order comment. |
| 2 | `COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the report order comment. |
| 3 | `EDITING_DT_TM` | DATETIME |  |  | This field contains the last date and time this report was viewed in a 'result entry application'. |
| 4 | `EDITING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the user who is currently viewing/modifying this report in a 'result entry application'. |
| 5 | `HOLD_CD` | DOUBLE | NOT NULL |  | If the report is currently associated with a hold status, this field contains the internal identification code associated with the hold reason. Hold reasons are stored on codeset 1300. |
| 6 | `HOLD_COMMENT` | VARCHAR(100) |  |  | This field is no longer used. Refer to the COMMENTS_LONG_TEXT_ID for information regarding the report hold comment. |
| 7 | `HOLD_COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the report hold comment. |
| 8 | `HOLD_DT_TM` | DATETIME |  |  | If the report is currently associated with a hold status, this field contains the date and time the hold status was assigned to the report. |
| 9 | `HOLD_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | If the report is currently associated with a hold status, the internal identification code of the user who updated the report to a hold status is contained in this field. This value could be used to join to information on the PRSNL and PERSON tables. |
| 10 | `LAST_EDIT_DT_TM` | DATETIME |  |  | This field contains the date and time that text was added to the report. |
| 11 | `LAST_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the report component (discrete task) for which text was last added. |
| 12 | `ORDER_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key value representing the report order. |
| 13 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | This field contains the identification code of the priority (stat, routine, for example) currently assigned to the report. |
| 14 | `REPORT_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the foreign key value used to represent the report. This is used to join to report information stored on the CASE_REPORT activity table. |
| 15 | `RESPONSIBLE_PATHOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the user designated as the responsible pathologist for the report. This may, or may not, be the same as the responsible pathologist assigned to the case (stored on the PATHOLOGY_CASE table). |
| 16 | `RESPONSIBLE_RESIDENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the user designated as the responsible resident for the report. This may, or may not, be the same as the responsible resident assigned to the case (stored on the PATHOLOGY_CASE table). |
| 17 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the service resource to which the report is assigned. This could be used to join to the service_resource table. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENTS_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `EDITING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `HOLD_COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `HOLD_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LAST_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `REPORT_ID` | [CASE_REPORT](CASE_REPORT.md) | `REPORT_ID` |
| `RESPONSIBLE_PATHOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESPONSIBLE_RESIDENT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REPORT_DETAIL_TASK](REPORT_DETAIL_TASK.md) | `REPORT_ID` |

