# RAD_STG_EXT_IDENTIFIER

> This table holds the external identifiers for the document sent from external sources.

**Description:** Radiology Staging External Identifier  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EVENT_ID` | DOUBLE |  |  | The clinical event identifier of the document when it is added to patient chart. |
| 3 | `ORG_ID` | DOUBLE |  | FK→ | Identifier of the organization that issued/managed the external identifier. |
| 4 | `RAD_STG_DATA_ID` | DOUBLE |  | FK→ | The unique id of the external document this external identifier is linked to. |
| 5 | `RAD_STG_EXT_IDENTIFIER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_STG_EXT_IDENTIFIER table. |
| 6 | `SYSTEM_URI` | VARCHAR(100) |  |  | Namespace for the identifier value. |
| 7 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VALUE_TXT` | VARCHAR(100) |  |  | External identifier used for the Diagnostic report. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `RAD_STG_DATA_ID` | [RAD_STG_DATA](RAD_STG_DATA.md) | `RAD_STG_DATA_ID` |

