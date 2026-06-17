# MIC_STAT_SUS_DC_RESULT

> This statistical reference table contains susceptibility duplicate checking(DC) values information defined for each valid results based on criteria and antibiotic. This is a child table of mic_stat_sus_dc_ab.

**Description:** Micro Susceptibility Duplicate Checking Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code_value of the antibiotic used to define sus DC value criteria. |
| 2 | `RESULT_CD` | DOUBLE | NOT NULL |  | This field contains the code_value of the alpha results and interp results used to define sus DC value. |
| 3 | `SUS_DC_VALUE_ID` | DOUBLE | NOT NULL | FK→ | This field contains a foreign key value used to join sus DC value information stored on mic_stat_sus_dc_value and mic_stat_sus_dc_ab tables. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE` | DOUBLE | NOT NULL |  | This field indicates the DC value assigned to the particular result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANTIBIOTIC_CD` | [MIC_STAT_SUS_DC_AB](MIC_STAT_SUS_DC_AB.md) | `ANTIBIOTIC_CD` |
| `SUS_DC_VALUE_ID` | [MIC_STAT_SUS_DC_AB](MIC_STAT_SUS_DC_AB.md) | `SUS_DC_VALUE_ID` |

