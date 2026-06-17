# HLA_SCREEN_ANALYSIS_DETAIL

> Detail information related to a saved modified antibody screen analysis.

**Description:** HLA Antibody Screen Analysis Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIGEN_CD` | DOUBLE | NOT NULL |  | Antigen that is to be removed from the antibody screen analysis. |
| 2 | `BCELL_LOCI_CD` | DOUBLE | NOT NULL |  | Contains the b-cell loci that is to be included in the antibody screen analysis. |
| 3 | `CREG_ID` | DOUBLE | NOT NULL | FK→ | CREG identifier that relates to the information to be removed from the antibody screen analysis. |
| 4 | `CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | Relates information to the activity data of the modified antibody screen analysis. |
| 5 | `SCREEN_ANALYSIS_DETAIL_ID` | DOUBLE | NOT NULL |  | An identifier used to keep each row on the HLA_SCREEN_ANALYSIS_DETAIL table unique. |
| 6 | `TCELL_LOCI_CD` | DOUBLE | NOT NULL |  | The t-cell loci that is to be included in the antibody screen analysis. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREG_ID` | [CREG](CREG.md) | `CREG_ID` |
| `CRITERIA_ID` | [HLA_SCREEN_ANALYSIS](HLA_SCREEN_ANALYSIS.md) | `CRITERIA_ID` |

