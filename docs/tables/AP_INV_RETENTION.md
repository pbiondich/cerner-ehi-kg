# AP_INV_RETENTION

> Describes the retention times of Anatomic Pathology inventory.

**Description:** Aatomic Pathology Inventory Retention  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AP_INV_RETENTION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a given retention time for specific Anatomic Pathology inventory |
| 2 | `INVENTORY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of inventory the retention defines. |
| 3 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | The normalcy code associated with the inventory that the retention defines. |
| 4 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | Contains the prefix associated with the inventory that the retention defines. |
| 5 | `RETENTION_TM_VALUE` | DOUBLE | NOT NULL |  | Contains the retention time. |
| 6 | `RETENTION_UNITS_CD` | DOUBLE | NOT NULL |  | The retention time unit of measure. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |

