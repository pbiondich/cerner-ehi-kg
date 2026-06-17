# ROBOTICS_ITEMS

> Any robotics related unit that transfers information to the robotics server.

**Description:** Robotic components associated with a robotics line.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AV_DEST_CODE_BUILD_IND` | DOUBLE |  |  | Controls building of destination codes for autoverifybuild. |
| 2 | `CALL_ROBOTICS_IND` | DOUBLE |  |  | If set to one call robotics interface. |
| 3 | `DEST_PRIORITY` | DOUBLE |  |  | Priority for this Takeout unit |
| 4 | `LOGIN_LOC_CD` | DOUBLE | NOT NULL | FK→ | Login Location for the robotics item |
| 5 | `LONG_DESC` | CHAR(80) |  |  | Text description of the robotics item. |
| 6 | `MASK_NBR` | DOUBLE | NOT NULL |  | Provides a mask to quickly select a given identifier |
| 7 | `PICT_INDEX_FLG` | DOUBLE |  |  | Index number for a robotics item picture box, based on type |
| 8 | `POST_CONTAINER_EVENT_IND` | DOUBLE |  |  | Allow robotic events from this robotics item to post to the container event table |
| 9 | `RACK_TYPE_CD` | DOUBLE | NOT NULL |  | Code value of rack type corresponding to this robotics item. |
| 10 | `ROBOTICS_DESC1` | CHAR(20) |  |  | Top Row of the Picture Box Descriptor |
| 11 | `ROBOTICS_DESC2` | CHAR(20) |  |  | Bottom Row of the Picture Box Descriptor |
| 12 | `ROBOTICS_DEST` | DOUBLE |  |  | Robotics Destination identifier |
| 13 | `ROBOTICS_ITEM_ID` | DOUBLE | NOT NULL |  | Unique identifier for Robotics Item |
| 14 | `ROBOTICS_ITEM_TYPE_CD` | DOUBLE | NOT NULL |  | Robotics Item Type |
| 15 | `ROBOTICS_NAME` | CHAR(20) |  |  | Name identifier from Robotics Vendor |
| 16 | `ROBOTICS_POS_X` | DOUBLE | NOT NULL |  | X Coordinate Screen Position for Picture Box |
| 17 | `ROBOTICS_POS_Y` | DOUBLE | NOT NULL |  | Y Coordinate Screen Position for Picture Box |
| 18 | `ROBOTICS_ROUTE` | DOUBLE |  |  | Route Code for Robotics Item |
| 19 | `ROBOTICS_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Robotics Line Controller Service Resource Code Value |
| 20 | `ROUTE_ALIAS` | VARCHAR(20) |  |  | This alias when ordered on robotics will cause a container to be routed to this robotics item. |
| 21 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Robotics Item Service Resource |
| 22 | `SHELF_CD` | DOUBLE | NOT NULL |  | Code value of the shelf corresponding to this robotics item. |
| 23 | `TRANSFER_FLG` | CHAR(1) |  |  | Transfer Destination Flag |
| 24 | `TRANSFER_TO_SHELF_CD` | DOUBLE | NOT NULL |  | Code value of the shelf where the rack will be moved when taken off the robotics line.s |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGIN_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `SERVICE_RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

