# OMF_CALC_INDICATOR

> List of indicators needed by PowerVision to calculate a given indicator. This ensures that a formula indicator will be able to be calculated regardless of whether the user chooses the indicators it is dependent on to be viewed.

**Description:** List of indicators needed by PowerVision to calculate a given indicator.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALC_INDICATOR_CD` | DOUBLE | NOT NULL |  | Indicator which is needed by another indicator to be calculated. (cdf_meaning = 'INDICATOR'). Other codesets can be used besides 14265 depending on the team defining the value. |
| 2 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | Indicator which needs other indicators to calculate it. (cdf_meaning = 'INDICATOR'). Other codesets can be used besides 14265 depending on the team defining the value. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

