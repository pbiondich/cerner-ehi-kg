# WORKING_VIEW_ITEM

> Specifies the items for working views that are applicable for a given position/location.

**Description:** Working View Item  
**Table type:** REFERENCE  
**Primary key:** `WORKING_VIEW_ITEM_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FALLOFF_VIEW_MINUTES` | DOUBLE | NOT NULL |  | Specifies when to remove the item if it hasn't been documented on within the working view |
| 2 | `INCLUDED_IND` | DOUBLE | NOT NULL |  | Specifies whether the primitive event set is included on the working view. |
| 3 | `PARENT_EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the primitive event set parents associated to a working view section. |
| 4 | `PRIMITIVE_EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the primitive event sets associated to a working view section. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WORKING_VIEW_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique identifier. |
| 11 | `WORKING_VIEW_SECTION_ID` | DOUBLE | NOT NULL | FK→ | FK from the working_view_section table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKING_VIEW_SECTION_ID` | [WORKING_VIEW_SECTION](WORKING_VIEW_SECTION.md) | `WORKING_VIEW_SECTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CNT_WV_ITEM_KEY](CNT_WV_ITEM_KEY.md) | `DCP_WV_ITEM_REF_ID` |

