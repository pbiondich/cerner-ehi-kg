# EXAM_ROOM_LIB_GRP_RELTN

> The Exam_Room_Lib_Grp_Reltn table contains relationships between exam rooms and library groups that will aid in image management loading logic.

**Description:** Exam Room Library Group Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LIB_GROUP_CD` | DOUBLE | NOT NULL | FK→ | The Lib_Group_Cd is a foreign key to the Library Group table. This identifies a specific library group within the image management area. |
| 2 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The Service_Resource_Cd is a foreign key to the Library Group table. This allows library groups to be logically linked to exam rooms for image management loading purposes.F143 |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LIB_GROUP_CD` | [LIBRARY_GROUP](LIBRARY_GROUP.md) | `SERVICE_RESOURCE_CD` |
| `SERVICE_RESOURCE_CD` | [RAD_EXAM_ROOM](RAD_EXAM_ROOM.md) | `SERVICE_RESOURCE_CD` |

