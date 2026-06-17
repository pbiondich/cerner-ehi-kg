# MIC_REF_ANG_REPORT

> This table contains information regarding the automatic no growth reports that should be issued for each procedure/service resource/source combination and at what time intervals the reports should besent.

**Description:** Microbiology Automatic No Growth Reporting  
**Table type:** REFERENCE  
**Primary key:** `ANG_ID`, `AUTO_NEG_SEQ`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANG_ID` | DOUBLE | NOT NULL | PK FK→ | This field identifies the unique value for each procedure/service resource/source combination assigned on the mic_ref_ang table for which automatic no growth reporting parameters are defined. |
| 2 | `APPEND_TIME_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the current time should be append to the end of the report taskissued. Valid values include: 0 = Do Not Append Time 1 = Append Current Time |
| 3 | `AUTO_NEG_SEQ` | DOUBLE | NOT NULL | PK | If multiple reports are defined for a particular ang_id this field is used to sequence and uniquely identify each report. The first report defined for an ang_id is assigned sequence 1, the second report 2, etc. |
| 4 | `BEGIN_RANGE` | DOUBLE | NOT NULL |  | This field identifies the beginning time value for the ang report defined. If this is the first report being defined this value will always be 0. |
| 5 | `CODED_RESPONSE_CD` | DOUBLE | NOT NULL |  | This field identifies the coded response to be used for the report task issued for this ang_id. Coded responses are defined on code set 1022, Coded Responses. |
| 6 | `END_RANGE` | DOUBLE | NOT NULL |  | This field identifies the ending time value for the ang report defined. If the first report shouldbe issued after 24 hours this field would be set to 24. |
| 7 | `GROUP_RESPONSE_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value for group response from the mic_group_response table. |
| 8 | `REPORT_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the report task to be issued for this ang_id. Reports are defined on code set 1000, Microbiology Reports. |
| 9 | `UNITS_CD` | DOUBLE | NOT NULL |  | This field identifies the unit of time associated with the beginning and ending range fields. Units are defined on code set 54, Age Units. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERIFY_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the report task should be verified. Valid values include: 0 =Perform the report 1 = Verify the report |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANG_ID` | [MIC_REF_ANG](MIC_REF_ANG.md) | `ANG_ID` |
| `GROUP_RESPONSE_ID` | [MIC_GROUP_RESPONSE](MIC_GROUP_RESPONSE.md) | `GROUP_RESPONSE_ID` |
| `REPORT_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_ANG_AUTOMATED](MIC_ANG_AUTOMATED.md) | `ANG_ID` |
| [MIC_ANG_AUTOMATED](MIC_ANG_AUTOMATED.md) | `ANG_NEG_SEQ` |

