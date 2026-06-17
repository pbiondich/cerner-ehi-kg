# WORKING_VIEW_PERSONITEM

> Specifies the items for working views that are applicable for a given encounter.

**Description:** WORKING VIEW PERSON ITEM  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INCLUDED_IND` | DOUBLE | NOT NULL |  | Specifies whether the primitive event set is included on the working view. |
| 2 | `LAST_ACTION_DT_TM` | DATETIME |  |  | The date and time of the last action on the item |
| 3 | `PARENT_EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the primitive event set parents associated to a working view section. |
| 4 | `PRIMITIVE_EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the primitive event sets associated to a working view section |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WORKING_VIEW_PERSONITEM_ID` | DOUBLE | NOT NULL |  | Sequence generated primary key. |
| 11 | `WORKING_VIEW_PERSON_SECT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from the Working View Person Sect table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKING_VIEW_PERSON_SECT_ID` | [WORKING_VIEW_PERSON_SECT](WORKING_VIEW_PERSON_SECT.md) | `WORKING_VIEW_PERSON_SECT_ID` |

