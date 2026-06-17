# DIFFERENTIAL_REF_ASSAY

> Defines the procedures to be included in a differential count in the result entry application.

**Description:** Differential Reference Assay  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COUNT_KEY` | CHAR(1) |  |  | Defines the keyboard key used to count the defined procedure. |
| 2 | `DIF_REF_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific differential reference row. Creates a relationship to the differential reference table. |
| 3 | `DISPLAY_NAME` | VARCHAR(10) |  |  | Defines the display next to the discrete task assay procedure for the differential result entry application. |
| 4 | `NON_TOTAL_IND` | DOUBLE |  |  | Indicates whether the discrete task assay is to be included in the non-total cell count. A value of 0 defines the procedure to be included in the total cell count. A value of 1 defines the procedure to be included in the non-total cell count. |
| 5 | `NON_TOTAL_TRIGGER_IND` | DOUBLE |  |  | Indicates whether the non-total cell count should be used to determine if the defined calculation should be performed. A value of 0 indicates that this non-total cell count should not be used. A value of 1 indicates that this non-total cell count should be used. Note: Referenced only if the column NON_TOTAL_IND = 1. |
| 6 | `POSITION_SEQ` | DOUBLE |  |  | Defines the position in which the user saved the procedures when building them in the differential build tool. |
| 7 | `PROC_TYPE_FLAG` | DOUBLE |  |  | Defines the area of the screen in which the discrete task assay is to display in the differential result entry application. |
| 8 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies a specific discrete task assay to be used in the differential result entry application. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `ZERO_IND` | DOUBLE |  |  | Indicates whether a result value of zero should be displayed and saved to the database for the discrete task assay. A value of 0 indicates a result value of zero should not be displayed or saved. A value of 1 indicates a result of zero should be displayed and saved. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

