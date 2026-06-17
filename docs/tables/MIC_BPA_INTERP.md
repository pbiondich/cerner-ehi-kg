# MIC_BPA_INTERP

> This reference table contains a combination of an organism, susceptibility panel, antibiotic, and susceptibility detail for which breakpoint interpretive data is defined.

**Description:** Microbiology Breakpoint Interpretation  
**Table type:** REFERENCE  
**Primary key:** `INTERP_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the antibiotic. |
| 2 | `INTERP_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the 'breakpoint interpretive' data for an organism/susceptibility panel/antibiotic/susceptibility detail combination. This value is used to join to the MIC_BPA_INTERP_RESULT and MIC_BPA_INTERP_PLATE_RESULT table. |
| 3 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the organism. |
| 4 | `SUSC_DETAIL_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the susceptibility detail. |
| 5 | `SUSC_PANEL_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the susceptibility panel. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_BPA_INTERP_RESULT](MIC_BPA_INTERP_RESULT.md) | `INTERP_ID` |

