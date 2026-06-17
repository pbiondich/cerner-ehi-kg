# AP_PREFIX_AUTO_TASK

> This reference table contains the report order catalog items that will automatically be ordered when a case is initiated. The relationship between the report order catalog items and cases is at the case prefix level.

**Description:** AP Prefix Auto Task  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the order catalog report procedures that are automatically ordered when a case associated with the prefix is accessioned. |
| 2 | `PREFIX_ID` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the prefix value to which the auto order order catalog report procedures are associated. This field contains the foreign key value used to join to the prefix information stored on the AP_PREFIX reference table. |
| 3 | `SPECIMEN_IND` | DOUBLE |  |  | This field is not used at this time. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `PREFIX_ID` | [AP_PREFIX](AP_PREFIX.md) | `PREFIX_ID` |

