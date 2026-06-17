# MM_XFI_ITEM_REPL

> This staging table contains item replacement data which is imported from the external ERP system.

**Description:** Interface Item Replacement  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Action to perform on the current row: CreateOrUpdate(1), CreateOnly(2), UpdateOnly(3), Delete(4) |
| 2 | `CONTRIBUTOR` | VARCHAR(40) |  |  | This indicates the Contributor Source to be used for code value aliasing.; |
| 3 | `CONTRIBUTOR_CD` | DOUBLE |  |  | The internal unique contributor cd/id that the item is being replaced in. |
| 4 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted. |
| 6 | `CREATE_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 7 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 8 | `ESTIMATED_END_DT_ISO` | VARCHAR(10) |  |  | Date of the item replacement is expected to be remediated and not the actual date of the remediation in ISO-8601 format (YYYY-MM-DD). |
| 9 | `EXT_TRANSACTION_IDENT` | DOUBLE |  |  | The id tied to the external item replacement transaction. |
| 10 | `FULL_SYNC_IND` | DOUBLE |  |  | This is required to identify when the rows in this table are part of a full sync. In these cases we push this information over to the mm_item_replacement activity table differently |
| 11 | `ITEM_DESC` | VARCHAR(255) |  |  | The unique description of the item being replaced. |
| 12 | `ITEM_ID` | DOUBLE |  | FK→ | The internal unique id of the item being replaced. |
| 13 | `ITEM_NBR` | VARCHAR(255) |  |  | The unique name of the item being replaced. |
| 14 | `LOCATION` | VARCHAR(100) |  |  | The unique location name of the item being replaced. |
| 15 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 16 | `MM_XFI_ITEM_REPL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_XFI_ITEM_REPL table. |
| 17 | `ORG_ID` | DOUBLE |  | FK→ | The group that the item is being replaced in.; |
| 18 | `ORG_NAME` | VARCHAR(100) |  |  | The unique name of the organization the item is being replaced in. |
| 19 | `PROCESS_FLAG` | DOUBLE |  |  | Status of the current row: Default(0), Pending(1), Validation in Process(2), Validation Failed(3), Validation Succeeded / Ready to Import(5), Import in Process(7), Import Succeeded(9), Import Failed(11) |
| 20 | `REPL_ITEM_DESC` | VARCHAR(255) |  |  | The unique description of the replacement item.; |
| 21 | `REPL_ITEM_ID` | DOUBLE |  | FK→ | The internal unique id of the replacement item. |
| 22 | `REPL_ITEM_NBR` | VARCHAR(255) |  |  | The unique name of the replacement item. |
| 23 | `REPL_REASON_TXT` | VARCHAR(255) |  |  | The reason for the replacement in plain text. |
| 24 | `REPL_TYPE_TFLG` | VARCHAR(15) |  |  | The replacement type: PERMANENT or TEMPORARY |
| 25 | `START_DT_ISO` | VARCHAR(10) |  |  | The starting date of the item replacement in ISO-8601 format (YYYY-MM-DD). |
| 26 | `SYNC_DT_TM` | DATETIME |  |  | The sync time of the current run. This date is used to identify which rows have not been touched during a full item replacement sync. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `VENDOR` | VARCHAR(60) |  |  | The unique vendor name of the item being replaced. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `REPL_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

