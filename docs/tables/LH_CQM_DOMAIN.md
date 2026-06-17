# LH_CQM_DOMAIN

> The domains that relate to clinical quality measures. Possible examples; Population/Public Health, Patient Safety

**Description:** Lighthouse Clinical Quality Measures Domain  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOMAIN_MEANING` | VARCHAR(12) | NOT NULL |  | A description of the domain |
| 2 | `LH_CQM_DOMAIN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CQM_DOMAIN table. |
| 3 | `LH_CQM_DOMAIN_NAME` | VARCHAR(100) | NOT NULL |  | The display string for the domain. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

