# OCS_ATTR_XCPTN

> Used to flex synonym attributes by other entities. For instance, flexing the witness by location indicator by location.

**Description:** Order Catalog Synonym Attribute Exception  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FACILITY_CD` | DOUBLE | NOT NULL |  | This is the facility code that the object is flexed by. |
| 2 | `FLEX_NBR_VALUE` | DOUBLE |  |  | This is the flexed value if the value is numeric. |
| 3 | `FLEX_OBJ_CD` | DOUBLE | NOT NULL |  | This is the code of the object by which the item will flex. |
| 4 | `FLEX_OBJ_TYPE_CD` | DOUBLE | NOT NULL |  | This indicates the data type for the value - whether numeric or string. |
| 5 | `FLEX_STR_VALUE_TXT` | VARCHAR(100) |  |  | This is the string value if the value is alphanumeric. |
| 6 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 7 | `OCS_ATTR_XCPTN_GROUP_ID` | DOUBLE | NOT NULL |  | This is used to group rows into a combination. |
| 8 | `OCS_ATTR_XCPTN_ID` | DOUBLE | NOT NULL |  | This is the generated key for this flex-by object. |
| 9 | `OCS_COL_NAME_CD` | DOUBLE | NOT NULL |  | This is the column name in the ORDER CATALOG SYNONYM table that is being flexed. |
| 10 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | This is the key to the ORDER CATALOG SYNONYM table for the synonym that is being flexed. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

