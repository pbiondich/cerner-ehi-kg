# MM_ITEM_REPL

> This table contains item replacement information.

**Description:** Item Replacement  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted. |
| 3 | `CREATE_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 5 | `ESTIMATED_END_DT_ISO` | VARCHAR(10) |  |  | The date the item replacement is expected to be remediated and not the actual date of the remediation in ISO-8601 format (YYYY-MM-DD). |
| 6 | `EXT_TRANSACTION_IDENT` | DOUBLE |  |  | The id tied to the external item replacement transaction. |
| 7 | `ITEM_ID` | DOUBLE |  | FK→ | The internal unique id of the item being replaced. |
| 8 | `LOCATION` | VARCHAR(100) |  |  | The unique location name of the item being replaced.; |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `MM_ITEM_REPL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_ITEM_REPL table. |
| 11 | `ORG_ID` | DOUBLE |  | FK→ | The unique organization id that the item is being replaced in. |
| 12 | `REPL_ITEM_ID` | DOUBLE |  | FK→ | The id of the replacement item. |
| 13 | `REPL_REASON_TXT` | VARCHAR(255) |  |  | The reason for the replacement in plain text. |
| 14 | `REPL_TYPE_TFLG` | VARCHAR(15) |  |  | The replacement type: PERMANENT or TEMPORARY |
| 15 | `START_DT_ISO` | VARCHAR(10) |  |  | The starting date of the item replacement in ISO-8601 format (YYYY-MM-DD). |
| 16 | `SYNC_DT_TM` | DATETIME |  |  | The sync time of the current run. This date is used to identify which rows have not been touched during a full item replacement sync. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `VENDOR` | VARCHAR(60) |  |  | The unique vendor name of the item being replaced. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `REPL_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

