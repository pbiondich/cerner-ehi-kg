# CNT_DATA_MAP

> DATA MAP

**Description:** CNT DATA MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNT_DATA_MAP_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `CNT_DTA_KEY_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY VALUE FROM CNT_DTA_KEY2 |
| 4 | `DATA_MAP_TYPE_FLAG` | DOUBLE | NOT NULL |  | 0.00 Standard data map 1.00 QC data map |
| 5 | `MAX_DIGITS` | DOUBLE |  |  | Defines the maximum number of digits allowed in the result. |
| 6 | `MIN_DECIMAL_PLACES` | DOUBLE |  |  | Defines the minimum number of decimal places required in the result. |
| 7 | `MIN_DIGITS` | DOUBLE |  |  | Defines the minimum number of digits required in the result. |
| 8 | `RESULT_ENTRY_FORMAT` | VARCHAR(40) |  |  | (Currently not implemented) |
| 9 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the service resource (such as instrument, bench, or sub section) for which the data map is specified. A value of zero indicates that the data map is defined for any service resource associated with the discrete task assay. |
| 10 | `SERVICE_RESOURCE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 11 | `SERVICE_RESOURCE_DISP` | VARCHAR(40) |  |  | DISPLAY |
| 12 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_DTA_KEY_ID` | [CNT_DTA_KEY2](CNT_DTA_KEY2.md) | `CNT_DTA_KEY_ID` |

