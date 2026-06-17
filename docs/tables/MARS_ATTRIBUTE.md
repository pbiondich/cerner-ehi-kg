# MARS_ATTRIBUTE

> Identifies an attribute of a unique MARS_NODE row

**Description:** MARS_ATTRIBUTE  
**Table type:** REFERENCE  
**Primary key:** `MARS_ATTRIBUTE_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_NAME` | VARCHAR(100) | NOT NULL |  | The attribute name is unique to the MARS_NODE.MARS_NODE_ID and contains attribute names such as name, required etc |
| 2 | `ATTRIBUTE_TEXT` | VARCHAR(4000) |  |  | Text contained within the attribute tag itself, this is usually the result of a documentation node |
| 3 | `ATTRIBUTE_VALUE` | VARCHAR(255) | NOT NULL |  | The attribute value is the data within the attribute name. |
| 4 | `MARS_ATTRIBUTE_ID` | DOUBLE | NOT NULL | PK | PRIMAY KEY |
| 5 | `MARS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Parent MARS_NODE.MARS_NODE_ID identifying the parent for this attribute. |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MARS_NODE_ID` | [MARS_NODE](MARS_NODE.md) | `MARS_NODE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MARS_MAPPING](MARS_MAPPING.md) | `MARS_ATTRIBUTE_ID` |

