# MED_PACKAGE_TYPE

> Med Package Type

**Description:** Med Package Type  
**Table type:** REFERENCE  
**Primary key:** `MED_PACKAGE_TYPE_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BASE_UOM_CD` | DOUBLE | NOT NULL |  | Base unit of measure |
| 3 | `DESCRIPTION` | VARCHAR(100) |  |  | textual description |
| 4 | `DISPENSE_QTY` | DOUBLE | NOT NULL |  | Quantity amount of the dispensed product. |
| 5 | `MED_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | PK | Med Package Type id |
| 6 | `QTY` | DOUBLE | NOT NULL |  | This column is no longer used. QTY has been replaced by DISPENSE_QTY. |
| 7 | `UOM_CD` | DOUBLE | NOT NULL |  | Unit of Measure |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MED_DEF_FLEX](MED_DEF_FLEX.md) | `MED_PACKAGE_TYPE_ID` |
| [MED_DISPENSE](MED_DISPENSE.md) | `MED_PACKAGE_TYPE_ID` |
| [MED_IDENTIFIER](MED_IDENTIFIER.md) | `MED_PACKAGE_TYPE_ID` |

