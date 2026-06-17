# PRSNL_LOC_RELTN

> Relationship table tying Prsnl to locations

**Description:** PRSNL LOC RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | The internal identifier associated with the bed to which the prsnl is associated. |
| 8 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | The internal identifier associated with the building to which the prsnl is associated. |
| 9 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The internal identifier associated with the facility to which the prsnl is associated. |
| 10 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | The internal identifier associated with the nurse unit to which the prsnl is associated. |
| 11 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | The internal identifier associated with the room to which the prsnl is associated. |
| 12 | `PRSNL_LOC_RELTN_CD` | DOUBLE | NOT NULL |  | Defines the type of relationship between the Prsnl and the location |
| 13 | `PRSNL_LOC_RELTN_ID` | DOUBLE | NOT NULL |  | Primary Key identifier to the PRSNL_LOC_RELTN table. Uses the PERSON_SEQ. |
| 14 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL |  | The person_id of the prsnl who is tied to the location via this reltn table |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

