# PHYS_COUNT

> The header table for physical inventories for a location.

**Description:** Physical Count  
**Table type:** ACTIVITY  
**Primary key:** `PHYS_COUNT_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETED_DT_TM` | DATETIME |  |  | The date that the count was completed. |
| 2 | `COUNT_COMMIT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that committed the count. |
| 3 | `COUNT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the count was created by the sheet level or by locator level. |
| 4 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 7 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 8 | `DESCRIPTION` | VARCHAR(100) |  |  | The user defined description associated with this count. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location that the physical count is taking place. |
| 10 | `MANUAL_COUNT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the manual count is for Perpetual items, Non-Perpetual items, or both. |
| 11 | `PHYS_COUNT_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 12 | `SORT_FIELD1` | VARCHAR(12) |  |  | Used to store the sort sequence for the count sheets. |
| 13 | `SORT_FIELD2` | VARCHAR(12) |  |  | Used to store the sort sequence for the count sheets. |
| 14 | `SORT_FIELD3` | VARCHAR(12) |  |  | Used to store the sort sequence for the count sheets. |
| 15 | `SORT_FIELD4` | VARCHAR(12) |  |  | Used to store the sort sequence for the count sheets. |
| 16 | `SORT_FIELD5` | VARCHAR(12) |  |  | Used to store the sort sequence for the count sheets. |
| 17 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the count. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VERIFIED_BY` | VARCHAR(100) |  |  | The free-text name of the person responsible for verification. |
| 24 | `VERIFIED_BY_ID` | DOUBLE | NOT NULL |  | The internal ID of the person responsible for verification. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COUNT_COMMIT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PHYS_COUNT_SHEET](PHYS_COUNT_SHEET.md) | `PHYS_COUNT_ID` |

