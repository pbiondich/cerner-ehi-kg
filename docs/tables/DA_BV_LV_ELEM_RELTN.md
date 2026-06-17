# DA_BV_LV_ELEM_RELTN

> Contains the relationships between business views, logical views and elements used in Discern Analytics 2.0 metadata.

**Description:** Discern Analytics Business View Logical View Element Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DA_BUS_VIEW_ID` | DOUBLE | NOT NULL | FK→ | The Business View that this logical view and element relate to. |
| 2 | `DA_BV_LV_ELEM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_BV_LV_ELEM_RELTN table. |
| 3 | `DA_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the element that is defined for this business view/logical view combination. |
| 4 | `DA_LOGICAL_VIEW_ID` | DOUBLE | NOT NULL | FK→ | Identifies the logical view that is related to this business view and element. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_BUS_VIEW_ID` | [DA_BUS_VIEW](DA_BUS_VIEW.md) | `DA_BUS_VIEW_ID` |
| `DA_ELEMENT_ID` | [DA_ELEMENT](DA_ELEMENT.md) | `DA_ELEMENT_ID` |
| `DA_LOGICAL_VIEW_ID` | [DA_LOGICAL_VIEW](DA_LOGICAL_VIEW.md) | `DA_LOGICAL_VIEW_ID` |

