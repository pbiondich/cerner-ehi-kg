# LH_CNT_IC_NHSN_TEMPLATE

> Lighthouse reference table for Infection Control that stores the Template IDs of CDA components submitted to NHSN>

**Description:** LH_CNT_IC_NHSN_TEMPLATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LH_CNT_IC_NHSN_TEMPLATE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_NHSN_TEMPLATE table. |
| 2 | `TEMPLATE_IDENT` | VARCHAR(200) |  |  | The template ID to be submitted to included in the CDA being sent to NHSN. |
| 3 | `TEMPLATE_MEANING` | VARCHAR(200) | NOT NULL |  | The unique identifier used to identify the correct template row. |
| 4 | `TEMPLATE_NAME` | VARCHAR(200) |  |  | The name of the template being included in the CDA. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

