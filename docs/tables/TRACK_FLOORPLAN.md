# TRACK_FLOORPLAN

> Floorplan Tracking View Specification

**Description:** Floorplan Tracking View  
**Table type:** REFERENCE  
**Primary key:** `TRACK_FLOORPLAN_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(200) | NOT NULL |  | A place to put a more detailed description of the floorplan view |
| 2 | `DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | Name of the floorplan |
| 3 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | FK From the LONG_BLOB_REFERENCE for the field that contains the floorplay graphic. |
| 4 | `OBJECT_SIZE_FLAG` | DOUBLE | NOT NULL |  | Specifies the size of objects displayed in this view 0 = small, 1 = medium, 2 = large |
| 5 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking group code the floorplan view is associated with |
| 6 | `TRACK_FLOORPLAN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACK_FLOORPLAN_LOCATION](TRACK_FLOORPLAN_LOCATION.md) | `TRACK_FLOORPLAN_ID` |

