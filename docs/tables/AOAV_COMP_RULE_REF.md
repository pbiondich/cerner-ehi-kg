# AOAV_COMP_RULE_REF

> This table stores the AOAV component rules

**Description:** AOAV_COMPONENT_RULE_REFERENCE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AOAV_COMP_CD` | DOUBLE | NOT NULL |  | Code value for a component |
| 3 | `AOAV_COMP_RULE_REF_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `RULE_CONTEXT` | VARCHAR(12) | NOT NULL |  | The contextof the rule |
| 5 | `RULE_NBR` | DOUBLE | NOT NULL |  | Number that identifies the rule |
| 6 | `RULE_TXT` | VARCHAR(4000) |  |  | The rule |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

