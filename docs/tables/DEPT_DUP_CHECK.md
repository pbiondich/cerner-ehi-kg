# DEPT_DUP_CHECK

> Used to store duplicate checking information that the department would want to store (dup checking across order catalog items)

**Description:** Departmental Duplicate Checking  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Used to store the code for the catalog item for which duplicate checking is being specified |
| 7 | `DUP_CATALOG_CD` | DOUBLE | NOT NULL |  | Used to store the code for the catalog item that will cause cancellation of the order catalog item in the catalog_cd field if orders for this item already exist on the system |
| 8 | `DUP_QUANTITY` | DOUBLE |  |  | Used to store quantity information for duplicate checking. This field is used to allow multiples of duplicate orders to be processed but will cancel duplicates beyond the value in this field. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `MINUTES_AHEAD` | DOUBLE |  |  | Used to store the number of minutes ahead to look for other orders scheduled on the system to perform duplicate checking. |
| 11 | `MINUTES_BEHIND` | DOUBLE |  |  | Used to store the number of minutes behind to look for other orders scheduled on the system to perform duplicate checking. |
| 12 | `MNEMONIC_TYPE_CD` | DOUBLE | NOT NULL |  | Used to store the mnemonic type for the catalog item for display purposes |
| 13 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | Used to store the code value for the priority to validate when performing duplicate checking |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `CATALOG_CD` |

