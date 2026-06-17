# QC_GROUP_ASSAY

> This table stores the QC Benchmark statistical information for an assay on a given control group.

**Description:** Quality Control Group Assay  
**Table type:** REFERENCE  
**Primary key:** `QC_GROUP_ASSAY_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTROL_GROUP_CD` | DOUBLE | NOT NULL |  | This is the control group to which this control and service resource is related. |
| 4 | `DEVIATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | The method used to represent the degree of deviation.Flag Values:1 = percent2 = absolute |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `GROUP_ASSAY_SEQ_NBR` | DOUBLE | NOT NULL |  | The value that keeps the same task_assay_cd unique for a given control_group_cd. |
| 7 | `MAX_DISPERSION_VALUE` | DOUBLE | NOT NULL |  | This is the maximum permissible impression that is measured by the standard deviation and the coefficient of variation. |
| 8 | `MAX_MEAN_VALUE` | DOUBLE | NOT NULL |  | This is the maximum permissible systematic error value. The difference between the calculated mean and the manufacturer's mean. |
| 9 | `MAX_RESULT_DEVIATION_VALUE` | DOUBLE | NOT NULL |  | This is the maximum permissible qc result deviation. It is the difference between the qc results and the manufacturer's mean. |
| 10 | `PREV_QC_GROUP_ASSAY_ID` | DOUBLE | NOT NULL |  | This column is used to group the modified values for a qc_group_assay_id. |
| 11 | `QC_GROUP_ASSAY_ID` | DOUBLE | NOT NULL | PK | Contains a given control group for an assay and its QC Benchmark statistical information. |
| 12 | `RESULT_RANGE_MAX_VALUE` | DOUBLE | NOT NULL |  | This is the high side of the result value that defines whether this quality control benchmark criteria is used or not. |
| 13 | `RESULT_RANGE_MIN_VALUE` | DOUBLE | NOT NULL |  | This is the low side of the result value that defines whether this quality control benchmark criteria is used or not. |
| 14 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | This is the foreign key to the code_value table that identifies the procedure that is related to this control group. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [QC_RESULT](QC_RESULT.md) | `QC_GROUP_ASSAY_ID` |

