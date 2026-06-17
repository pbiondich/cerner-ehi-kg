# CDI_WORK_ITEM_ATTRIBUTE

> Values for attributes of a CDI Work Item.

**Description:** CDI Work Item Attribute  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_CD` | DOUBLE | NOT NULL |  | Defines the type of attribute. |
| 2 | `ATTR_VALUE_CD` | DOUBLE | NOT NULL |  | Contains the code value for this attribute (codeset is configurable). |
| 3 | `ATTR_VALUE_TXT` | VARCHAR(1024) | NOT NULL |  | Contains the text value for this attribute. |
| 4 | `CDI_WORK_ITEM_ATTRIBUTE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_WORK_ITEM_ATTRIBUTE table. |
| 5 | `CDI_WORK_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The work item that this attribute applies to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_WORK_ITEM_ID` | [CDI_WORK_ITEM](CDI_WORK_ITEM.md) | `CDI_WORK_ITEM_ID` |

