# AP_DC_DISCREPANCY_TERM

> This reference table contains entries representing diagnostic correlation discrepancy categorizations. This option is most often associated with diagnostic correlation evaluation terms that represent disagreement.

**Description:** Diagnostic Correlation Discrepancy Terminology  
**Table type:** REFERENCE  
**Primary key:** `DISCREPANCY_TERM_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(60) |  |  | This field includes the long description, up-to-60 characters, defined for the discrepancy categorization term. |
| 3 | `DISCREPANCY_CD` | DOUBLE | NOT NULL |  | This field includes the internal identification code of the overall classification of the discrepancy categorization term, such as "None", "Major" or "Minor". These classifications are stored on code_set 15451. |
| 4 | `DISCREPANCY_TERM_ID` | DOUBLE | NOT NULL | PK | This field includes the internal identification code assigned to the discrepancy categorization terminology entry. This value would be referenced on other tables, such as the AP_DC_EVENT activity table. |
| 5 | `DISPLAY` | VARCHAR(15) |  |  | This field includes the short description, up-to-15 characters, defined for the discrepancy categorization term. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_DC_EVENT](AP_DC_EVENT.md) | `FINAL_DISCREP_TERM_ID` |
| [AP_DC_EVENT](AP_DC_EVENT.md) | `INIT_DISCREP_TERM_ID` |

