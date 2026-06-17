# PHYS_COUNT_SHEET

> In the mmPhysicalCount application, the count is created. This sheet is a part of the overal required physical count, assigned to a specific personnel.

**Description:** Physical Count Sheet  
**Table type:** ACTIVITY  
**Primary key:** `PHYS_COUNT_ID`, `SHEET_NBR`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNED_DT_TM` | DATETIME |  |  | The date that this specific sheet was assigned to someone. |
| 2 | `ASSIGNED_TO` | VARCHAR(100) |  |  | The free-text name of the person responsible for counting this sheet. |
| 3 | `ASSIGNED_TO_ID` | DOUBLE | NOT NULL |  | The ID from the prsnl table of the person responsible for counting this sheet. |
| 4 | `COMPLETED_DT_TM` | DATETIME |  |  | The date that the count for this sheet was completed. |
| 5 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 8 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 9 | `DESCRIPTION` | VARCHAR(100) |  |  | A user defined description for this sheet. |
| 10 | `PHYS_COUNT_ID` | DOUBLE | NOT NULL | PK FK→ | Foreign key to phys_count table. |
| 11 | `SHEET_NBR` | DOUBLE | NOT NULL | PK | The sheet number. Also part of the primary key. |
| 12 | `SHEET_STATUS_CD` | DOUBLE | NOT NULL |  | Stores the sheet status. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERIFIED_BY` | VARCHAR(100) |  |  | The free-text name of the person who verified this sheet. |
| 19 | `VERIFIED_BY_ID` | DOUBLE | NOT NULL |  | The ID from the prsnl table of the person who verified this sheet. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PHYS_COUNT_ID` | [PHYS_COUNT](PHYS_COUNT.md) | `PHYS_COUNT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PHYS_COUNT_SHEET_ITEM](PHYS_COUNT_SHEET_ITEM.md) | `PHYS_COUNT_ID` |
| [PHYS_COUNT_SHEET_ITEM](PHYS_COUNT_SHEET_ITEM.md) | `SHEET_NBR` |

