# DEM_XTRCT_NSTNC_SLC

> Contains the slices for an extract instance. The slice size is based on the slice size from the extract table.

**Description:** Data Extract Management - Extract Instance Slice  
**Table type:** ACTIVITY  
**Primary key:** `DEM_XTRCT_NSTNC_SLC_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEM_XTRCT_NSTNC_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the extract instance related to this slice. |
| 2 | `DEM_XTRCT_NSTNC_SLC_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a slice for an extract instance. The slice size is based on the slice size from the extract table. |
| 3 | `NSTNCE_SLC_STATUS_FLAG` | DOUBLE | NOT NULL |  | Contains the status of the extract instance slice.1 = Qualification in Process2 = Ready for Extraction |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEM_XTRCT_NSTNC_ID` | [DEM_XTRCT_NSTNC](DEM_XTRCT_NSTNC.md) | `DEM_XTRCT_NSTNC_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEM_XTRCT_NSTNC_SLC_ITEM](DEM_XTRCT_NSTNC_SLC_ITEM.md) | `DEM_XTRCT_NSTNC_SLC_ID` |

