# DRC_UNIT

> Reference data that defines the simple units of measure for dose range checking.

**Description:** Dose Range Checking Unit  
**Table type:** REFERENCE  
**Primary key:** `DRC_UNIT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITION_ADDEND_AMT` | DOUBLE | NOT NULL |  | This is the addend used to convert units within the same base class. |
| 2 | `BASE_NBR` | DOUBLE | NOT NULL |  | This identifies the base class for the unit. |
| 3 | `BRANCH_NBR` | DOUBLE | NOT NULL |  | This identifies the branch unit within a base class. The base unit will have a branch number of 1. |
| 4 | `DRC_UNIT_CKI` | VARCHAR(255) | NOT NULL |  | This is the CKI defined for the unit as assigned in code set 54 with the cs_54_utility tool. |
| 5 | `DRC_UNIT_DESC` | VARCHAR(100) |  |  | Description of the drc unit. |
| 6 | `DRC_UNIT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for unit. |
| 7 | `MULTIPLY_FACTOR_AMT` | DOUBLE | NOT NULL |  | This is the factor used to convert units within the same base class. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DRC_UNIT_EXPRSN_RELTN](DRC_UNIT_EXPRSN_RELTN.md) | `DRC_UNIT_ID` |

