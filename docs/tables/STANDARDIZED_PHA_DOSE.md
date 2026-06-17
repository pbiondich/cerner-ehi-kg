# STANDARDIZED_PHA_DOSE

> Standardized dose ranges for ordering pharmaceuticals

**Description:** Standardized Pharmacy Dose  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMPARE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for comparison. |
| 3 | `COMPARE_VALUE1` | DOUBLE | NOT NULL |  | First value to use in comparison |
| 4 | `COMPARE_VALUE2` | DOUBLE | NOT NULL |  | Second value to use in comparison |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the corresponding item definition for the standardized dose range |
| 6 | `RELATIONAL_OPERATOR_FLAG` | DOUBLE | NOT NULL |  | Identifies the relational operator for comparison with compare_value1 and compare_value2. |
| 7 | `ROUTE_CD` | DOUBLE | NOT NULL |  | Identifies a specific route of administration for medication. |
| 8 | `STANDARDIZED_PHA_DOSE_ID` | DOUBLE | NOT NULL |  | Standardized dose ranges for ordering pharmaceuticals |
| 9 | `STD_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for standard dose |
| 10 | `STD_DOSE_VALUE` | DOUBLE | NOT NULL |  | The standard dose value |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

