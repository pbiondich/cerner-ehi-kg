# DEM_XTRCT_NSTNC

> Contains an instance of an entity type to be extracted fro reporting purposes. an extract instance is type of an entity (Revuenue, ATB, etc.) for a given day.

**Description:** Data Extract Management - Extract Instance  
**Table type:** ACTIVITY  
**Primary key:** `DEM_XTRCT_NSTNC_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME |  |  | The data and time the extract represents. |
| 2 | `ACTIVITY_TZ` | DOUBLE |  |  | TIME ZONE FOR THE ACTIVITY_DT_TM FIELD |
| 3 | `DEM_XTRCT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the extract related to this instance. |
| 4 | `DEM_XTRCT_NSTNC_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies an instance of an entity type to be extracted for reporting purposes. an extract instance is the type of an entity (revenue, ATB, etc.) for a given day. |
| 5 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the logical domain to which the row data belongs. |
| 6 | `QLFCTN_CMPLTN_DT_TM` | DATETIME |  |  | Contains the date and time the qualification was completed. |
| 7 | `SLICE_CNT` | DOUBLE | NOT NULL |  | The number of slices for this extract instance. |
| 8 | `SLICE_ITEM_CNT` | DOUBLE | NOT NULL |  | Contains the number of slice items for this extract instance. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEM_XTRCT_ID` | [DEM_XTRCT](DEM_XTRCT.md) | `DEM_XTRCT_ID` |
| `MILL_LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEM_XTRCT_NSTNC_SLC](DEM_XTRCT_NSTNC_SLC.md) | `DEM_XTRCT_NSTNC_ID` |

