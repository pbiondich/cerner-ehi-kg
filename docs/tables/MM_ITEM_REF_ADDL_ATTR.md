# MM_ITEM_REF_ADDL_ATTR

> Contains the reference database information of item that contains more than one value

**Description:** Item Reference Additional Attribute  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTR_NAME_TXT` | VARCHAR(255) | NOT NULL |  | The attribute name that has more than one value from the Reference Database. |
| 2 | `ATTR_VALUE_TXT` | LONGTEXT |  |  | The value of the attribute from the Reference Database. |
| 3 | `MM_ITEM_REF_ADDL_ATTR_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_ITEM_REF_ADDL_ATTR table. |
| 4 | `MM_ITEM_REF_DATA_ID` | DOUBLE | NOT NULL | FK→ | The item that these attributes apply to. |
| 5 | `SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence of the values of the attribute. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MM_ITEM_REF_DATA_ID` | [MM_ITEM_REF_DATA](MM_ITEM_REF_DATA.md) | `MM_ITEM_REF_DATA_ID` |

