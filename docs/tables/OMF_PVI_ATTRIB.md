# OMF_PVI_ATTRIB

> Component/viewer style attributes.

**Description:** OMF PVI ATTRIB  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIB_ID` | DOUBLE | NOT NULL |  | Unique id for this component/viewer style attribute. |
| 2 | `ATTRIB_TYPE` | VARCHAR(255) |  |  | The 'name' of the attribute you are saving. E.g for a graph this could be 'Chart Style' or 'Title' |
| 3 | `COMPONENT_ID` | DOUBLE |  |  | Parent component or viewer style. |
| 4 | `OMF_PV_ITEM_ID` | DOUBLE |  |  | PowerVision saved view, template, or filter id. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VAL1` | VARCHAR(255) |  |  | Generic column to hold attribute's value. |
| 11 | `VAL2` | VARCHAR(255) |  |  | Generic column to hold attribute's value. |
| 12 | `VAL3` | VARCHAR(255) |  |  | Generic column to hold attribute's value. |
| 13 | `VAL4` | VARCHAR(255) |  |  | Generic column to hold attribute's value. |
| 14 | `VAL5` | VARCHAR(255) |  |  | Generic column to hold attribute's value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

