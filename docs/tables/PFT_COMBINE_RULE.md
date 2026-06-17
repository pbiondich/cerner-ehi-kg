# PFT_COMBINE_RULE

> This table is used to store rule information that triggered the combine operation.

**Description:** PFT Combine Rule  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PFT_COMBINE_LOG_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the PFT_COMBINE_LOG table. |
| 3 | `PFT_COMBINE_RULE_ID` | DOUBLE | NOT NULL |  | A system generated identifier used to uniquely identify a row on the PFT_COMBINE_RULE table. |
| 4 | `RULE_DESC` | VARCHAR(350) |  |  | Rule description of the external system that triggered the combine operation |
| 5 | `RULE_IDENT` | VARCHAR(200) |  |  | Rule Identifier of the external system that triggered the combine operation. Rule Identifier and Rule Version properties uniquely identifies the financial combine rule of the external system. |
| 6 | `RULE_VERSION_TXT` | VARCHAR(200) |  |  | Rule version of the external system that triggered the combine operation. Rule Identifier and Rule Version properties uniquely identifies the financial combine rule of the external system. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_COMBINE_LOG_ID` | [PFT_COMBINE_LOG](PFT_COMBINE_LOG.md) | `PFT_COMBINE_LOG_ID` |

