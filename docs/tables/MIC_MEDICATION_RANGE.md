# MIC_MEDICATION_RANGE

> This table associates the abnormal susceptibility results with the procedure/source/organism/susceptibility type and service resource combination defined on the mic_abn_sus_result table.

**Description:** Microbiology Medication Range  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_SUS_ID` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each set of abnormal susceptibility results defined for a procedure/source/organism/susceptibility type and service resource combination. |
| 2 | `DEFAULT_RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the susceptibility alpha or interpretation result for which abnormals susceptibility results are defined.. Susceptibility interpretation results are defined on code set 64, Susceptibility Interp Results and alpha susceptibility results are defined on code set 1025, Alpha Susceptibility Results. |
| 3 | `HIGH_VALUE` | DOUBLE |  |  | This field identifies the highest numeric susceptibility result for the abnormal susceptibility result range defined. This field displays the results according to the numeric sensi detail procedure's nbr_digits and nbr_decimals from the mic_detail_task table. This field is only valid for numeric sensi detail procedures, task_type_flag = 6. |
| 4 | `LOW_VALUE` | DOUBLE | NOT NULL |  | This field identifies the lowest numeric susceptibility result for the abnormal susceptibility result range defined. This field displays the results according to the numeric sensi detail procedure'snbr_digits and nbr_decimals from the mic_detail_task table. This field is only valid for numeric sensi detail procedures, task_type_flag = 6. |
| 5 | `MEDICATION_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the antibiotic for which susceptibility interpretations are defined.. Antibiotics are defined on code set 1011 Antibiotics(Medications) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ABN_SUS_ID` | [MIC_ABN_SUS_RESULT](MIC_ABN_SUS_RESULT.md) | `ABN_SUS_ID` |
| `MEDICATION_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |

