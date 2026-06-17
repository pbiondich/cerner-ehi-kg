# LH_CNT_IRFPAI_CHANGE

> This table will hold user selected values for the IRF-PAI report. This is necessary to allow users to select values other than the default selected values when exporting a report.

**Description:** Lighthouse Content IRF-PAI Change  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter ID this specific row is related to. |
| 2 | `FORM_QUESTION_IDENTIFIER` | VARCHAR(20) | NOT NULL |  | The section of the IRF-PAI report this saved change is for. |
| 3 | `FORM_QUESTION_VALUE` | VARCHAR(20) | NOT NULL |  | The actual value selected in the IRF-PAI report for this section. |
| 4 | `LH_CNT_IRFPAI_CHANGE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IRFPAI_CHANGE table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

