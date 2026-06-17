# TRACK_FLOORPLAN_LOCATION

> Locations associated to a floorplan and their positions in the floorplan

**Description:** Track Floorplan Location  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANCHOR_PT_X` | DOUBLE | NOT NULL |  | x coordinate, in pixels, relative to the upper left corner of location object |
| 2 | `ANCHOR_PT_Y` | DOUBLE | NOT NULL |  | Y coordinate, in pixels, relative to the upper left corner of location object |
| 3 | `HIDDEN_IND` | DOUBLE | NOT NULL |  | Indicates that the location object should be hidden when vacant |
| 4 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The Location cd |
| 5 | `TRACK_FLOORPLAN_ID` | DOUBLE | NOT NULL | FK→ | Reference to the Parent Floorplan |
| 6 | `TRACK_FLOORPLAN_LOCATION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_FLOORPLAN_ID` | [TRACK_FLOORPLAN](TRACK_FLOORPLAN.md) | `TRACK_FLOORPLAN_ID` |

