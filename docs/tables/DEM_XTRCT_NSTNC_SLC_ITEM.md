# DEM_XTRCT_NSTNC_SLC_ITEM

> Contains the individual IDs for an entity that are to be extracted fro a given extract instance slice.

**Description:** Data Extract Management - Extract Instance Slice Item  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEM_XTRCT_NSTNC_SLC_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a specific extract instance slice related to this item. |
| 2 | `DEM_XTRCT_NSTNC_SLC_ITEM_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an individual id for an entity that is to be extracted for a given extract instance slice. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the id of the entity identifying the type of item that is to be extracted. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the name of the entity identifying the type of item that is to be extracted. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEM_XTRCT_NSTNC_SLC_ID` | [DEM_XTRCT_NSTNC_SLC](DEM_XTRCT_NSTNC_SLC.md) | `DEM_XTRCT_NSTNC_SLC_ID` |

