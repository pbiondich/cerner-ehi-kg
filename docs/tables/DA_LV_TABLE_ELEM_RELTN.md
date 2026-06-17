# DA_LV_TABLE_ELEM_RELTN

> Defines relationships between the logical views, tables and elements for Discern Analytics 2.0 metadata.

**Description:** Discern Analytics Logical View Table Element Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this row was created by Cerner. |
| 2 | `DA_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the element that is related to this Table and Logical View. |
| 3 | `DA_LOGICAL_VIEW_ID` | DOUBLE | NOT NULL | FK→ | Identifies the logical view that this Table and Element are related to. |
| 4 | `DA_LV_TABLE_ELEM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_LV_TABLE_ELEM_RELTN table. |
| 5 | `DA_TABLE_INFO_ID` | DOUBLE | NOT NULL | FK→ | Identifies the table that is related to this Logical View and Element. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_ELEMENT_ID` | [DA_ELEMENT](DA_ELEMENT.md) | `DA_ELEMENT_ID` |
| `DA_LOGICAL_VIEW_ID` | [DA_LOGICAL_VIEW](DA_LOGICAL_VIEW.md) | `DA_LOGICAL_VIEW_ID` |
| `DA_TABLE_INFO_ID` | [DA_TABLE_INFO](DA_TABLE_INFO.md) | `DA_TABLE_INFO_ID` |

