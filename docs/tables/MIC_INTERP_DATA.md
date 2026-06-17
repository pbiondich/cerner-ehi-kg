# MIC_INTERP_DATA

> This table associates the susceptibility interpretation results with the organism/source/antibiotic/susceptibility detail combination defined on the mic_sus_first_level_interp table.

**Description:** Microbiology Interpretations Data  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HIGH_VALUE` | DOUBLE |  |  | This field identifies the highest numeric susceptibility result for the interpretation range defined. This field displays the results according to the numeric sensi detail procedure's nbr_digits andnbr_decimals from the mic_detail_task table. This field is only valid for numeric sensi detail procedures, task_type_flag = 6. |
| 2 | `INTERP_RANGE_ID` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each combination of interp_id and susceptibility interpretation detail procedure. This allows users to have multiple interpretations for each dilution result. |
| 3 | `INTERP_RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the interpretation result for which susceptibility interpretations are defined.. Susceptibility interpretation results are defined on code set 64, Susceptibility Interp Results. |
| 4 | `LOW_VALUE` | DOUBLE | NOT NULL |  | This field identifies the lowest numeric susceptibility result for the interpretation range defined. This field displays the results according to the numeric sensi detail procedure's nbr_digits and nbr_decimals from the mic_detail_task table. This field is only valid for numeric sensi detail procedures, task_type_flag = 6. |
| 5 | `SUS_RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the susceptiblity result for which susceptibility interpretations are defined.. Susceptibility alpha results are defined on code set 1025, Alpha SusceptibilityResults. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERP_RANGE_ID` | [MIC_INTERP](MIC_INTERP.md) | `INTERP_RANGE_ID` |

