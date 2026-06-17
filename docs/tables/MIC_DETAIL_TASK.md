# MIC_DETAIL_TASK

> This table contains the detail components of group level tasks defined within the database. Detailcomponents of groups are also located on the mic_task table.

**Description:** Microbiology Detail Tasks  
**Table type:** REFERENCE  
**Primary key:** `TASK_COMPONENT_CD`  
**Columns:** 15  
**Referenced by:** 19 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_BY_TRADE_IND` | DOUBLE |  |  | This field is not used at this time. |
| 2 | `CODED_RSLT_IND` | DOUBLE |  |  | This field indicates if the detail biochemical will utilize coded results or be a free-text biochemical. Valid values include: 0 = Free-text result 1 = Coded result |
| 3 | `MAX_VALUE` | DOUBLE |  |  | This field defines the maximum numeric value that can be entered for a task type 6 - Numeric Sensi Detail procedure. The maximum value is defined in the Susceptibility Tool. |
| 4 | `MED_TYPE` | DOUBLE |  |  | This field identifies the type of medication defined. Valid values include: 0 = Antibiotic 1 = Antifungal 2 = Antiviral |
| 5 | `NBR_DECIMALS` | DOUBLE |  |  | This field defines the number of decimal positions to be included in the result of a task type 6 - Numeric Sensi Detail procedure. |
| 6 | `NBR_DIGITS` | DOUBLE |  |  | This field defines the maximum number of digits that can be entered for the result of a task type 6 - Numeric Sensi Detail procedure. |
| 7 | `SUPPRESS_IND` | DOUBLE |  |  | This field indicates whether or not the susceptibility detail or antibiotic will be suppressed fromdisplaying in inquiry applications or included on patient reports. Valid values include: 0 = Chart 1 = Do not chart |
| 8 | `TASK_COMPONENT_CD` | DOUBLE | NOT NULL | PK | This field identifies the code_value of the detail task. Valid detail tasks include biochemicals, susceptibility detail procedures and antibiotics. |
| 9 | `TASK_TYPE_FLAG` | DOUBLE |  |  | This field identifies a value that determines the task type associated with the task entered. The task type further categorizes similar tasks within each task class. For example the task class biochemicals has two task type associated: (3)Group Biochemicals and (4)Detail Biochemicals. |
| 10 | `UNITS_CD` | DOUBLE | NOT NULL |  | This field defines the units of measure associated with the task type 6 - Numeric Sensi Detail procedure. Units of measure are defined on code set 54 Units of Measure. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (19)

| From table | Column |
|------------|--------|
| [MIC_ABN_SUS_RESULT](MIC_ABN_SUS_RESULT.md) | `SUS_DETAIL_CD` |
| [MIC_BIOCHEMICAL_TEST_RESULT](MIC_BIOCHEMICAL_TEST_RESULT.md) | `DETAIL_BIO_CD` |
| [MIC_EVENT_DETAIL](MIC_EVENT_DETAIL.md) | `DETAIL_SUS_CD` |
| [MIC_INTERP](MIC_INTERP.md) | `INTERP_TEST_CD` |
| [MIC_MEDICATION_RANGE](MIC_MEDICATION_RANGE.md) | `MEDICATION_CD` |
| [MIC_MEDS_ACTIVITY](MIC_MEDS_ACTIVITY.md) | `MEDICATION_CD` |
| [MIC_MED_TRADE_NAME](MIC_MED_TRADE_NAME.md) | `TASK_COMPONENT_CD` |
| [MIC_REF_BILLING_AB](MIC_REF_BILLING_AB.md) | `ANTIBIOTIC_CD` |
| [MIC_REQUIRED_TASK](MIC_REQUIRED_TASK.md) | `ANTIBIOTIC_CD` |
| [MIC_REQUIRED_TASK](MIC_REQUIRED_TASK.md) | `DETAIL_CD` |
| [MIC_RESULT_FOOTNOTE_R](MIC_RESULT_FOOTNOTE_R.md) | `ANTIBIOTIC_CD` |
| [MIC_SUS_FIRST_LEVEL_INTERP](MIC_SUS_FIRST_LEVEL_INTERP.md) | `MEDICATION_CD` |
| [MIC_SUS_FIRST_LEVEL_INTERP](MIC_SUS_FIRST_LEVEL_INTERP.md) | `SUS_DETAIL_CD` |
| [MIC_SUS_MED_RESULT](MIC_SUS_MED_RESULT.md) | `PANEL_MEDICATION_CD` |
| [MIC_SUS_ORDER_DETAIL](MIC_SUS_ORDER_DETAIL.md) | `DETAIL_SUS_CD` |
| [MIC_TASK_DETAIL_R](MIC_TASK_DETAIL_R.md) | `TASK_COMPONENT_CD` |
| [MIC_VALID_BIOCHEM_RESULT](MIC_VALID_BIOCHEM_RESULT.md) | `TASK_COMPONENT_CD` |
| [MIC_VALID_SUS_RESULT](MIC_VALID_SUS_RESULT.md) | `SUS_TYPE_CD` |
| [MIC_VALID_SUS_RESULT](MIC_VALID_SUS_RESULT.md) | `TASK_COMPONENT_CD` |

